#!/usr/bin/env python3
"""
QM Semantic Search MCP Server
Exposes semantic search over a markdown vault as an MCP tool for Claude Code.
"""

import sys
import json
import os
import logging
from pathlib import Path

# Resolve paths from environment
VAULT_PATH = Path(os.environ.get("QM_VAULT_PATH", os.getcwd()))
SEARCH_DIR = Path(__file__).parent

sys.path.insert(0, str(SEARCH_DIR))

from query import search, load_index, get_model

# Setup logging to stderr (stdout is for MCP protocol)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)


def handle_initialize(params):
    """Handle MCP initialize request."""
    return {
        "protocolVersion": "2024-11-05",
        "capabilities": {
            "tools": {}
        },
        "serverInfo": {
            "name": "qm-search",
            "version": "1.0.0"
        }
    }


def handle_tools_list(params):
    """Return list of available tools."""
    return {
        "tools": [
            {
                "name": "semantic_search",
                "description": "Search the vault using semantic similarity. Use this when you need to find conceptually related content without knowing exact keywords. Returns ranked chunks with file paths, headings, and relevance scores.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Natural language search query (e.g., 'organizational resistance to change', 'pricing strategy discussions')"
                        },
                        "n_results": {
                            "type": "integer",
                            "description": "Number of results to return (default: 10, max: 20)",
                            "default": 10
                        },
                        "theme_filter": {
                            "type": "string",
                            "description": "Optional: Filter results to a specific theme folder name"
                        }
                    },
                    "required": ["query"]
                }
            }
        ]
    }


def handle_tools_call(params):
    """Execute a tool call."""
    tool_name = params.get("name")
    arguments = params.get("arguments", {})

    if tool_name != "semantic_search":
        return {
            "content": [{"type": "text", "text": f"Unknown tool: {tool_name}"}],
            "isError": True
        }

    try:
        query = arguments.get("query", "")
        n_results = min(arguments.get("n_results", 10), 20)
        theme_filter = arguments.get("theme_filter")

        if not query:
            return {
                "content": [{"type": "text", "text": "Error: query is required"}],
                "isError": True
            }

        logger.info(f"Searching: {query[:50]}... (n={n_results}, theme={theme_filter})")

        results = search(query, n_results=n_results, theme_filter=theme_filter)

        # Format results for Claude
        output_lines = [f"Found {len(results)} results for: \"{query}\"", ""]

        for i, r in enumerate(results, 1):
            output_lines.append(f"[{i}] {r['file_path']}:{r['line']}")
            output_lines.append(f"    Heading: {r['heading']}")
            output_lines.append(f"    Theme: {r['theme']} | Score: {r['score']}")
            snippet = r['snippet'].replace('\n', ' ').strip()
            snippet = ' '.join(snippet.split())[:200]
            output_lines.append(f"    > {snippet}...")
            output_lines.append("")

        return {
            "content": [{"type": "text", "text": "\n".join(output_lines)}]
        }

    except Exception as e:
        logger.error(f"Search error: {e}")
        return {
            "content": [{"type": "text", "text": f"Search error: {str(e)}"}],
            "isError": True
        }


def main():
    """Main MCP server loop."""
    logger.info("QM Search MCP server starting...")
    logger.info(f"Vault path: {VAULT_PATH}")

    # Pre-load model and index for faster first query
    logger.info("Pre-loading model and index...")
    try:
        get_model()
        load_index()
        logger.info("Model and index loaded successfully")
    except Exception as e:
        logger.error(f"Failed to load model/index: {e}")

    # Process JSON-RPC messages from stdin
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            request = json.loads(line)
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {e}")
            continue

        request_id = request.get("id")
        method = request.get("method")
        params = request.get("params", {})

        logger.info(f"Received: {method}")

        result = None
        error = None

        try:
            if method == "initialize":
                result = handle_initialize(params)
            elif method == "notifications/initialized":
                continue
            elif method == "tools/list":
                result = handle_tools_list(params)
            elif method == "tools/call":
                result = handle_tools_call(params)
            else:
                error = {"code": -32601, "message": f"Method not found: {method}"}
        except Exception as e:
            logger.error(f"Error handling {method}: {e}")
            error = {"code": -32603, "message": str(e)}

        response = {"jsonrpc": "2.0", "id": request_id}
        if error:
            response["error"] = error
        else:
            response["result"] = result

        print(json.dumps(response), flush=True)


if __name__ == "__main__":
    main()
