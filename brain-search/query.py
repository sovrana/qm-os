#!/usr/bin/env python3
"""
QM Vault Query Interface
Semantic search over indexed vault content using sentence-transformers + numpy.
No ChromaDB required.
"""

import argparse
import json
import os
from pathlib import Path
import numpy as np
from sentence_transformers import SentenceTransformer

# Configuration - override with environment variables
VAULT_PATH = Path(os.environ.get("QM_VAULT_PATH", os.getcwd()))
INDEX_PATH = Path(os.environ.get(
    "QM_INDEX_PATH",
    str(VAULT_PATH / "99_System" / "brain-search" / "vector-index")
))
MODEL_NAME = os.environ.get("QM_MODEL_NAME", "all-MiniLM-L6-v2")

# Global cache (lazy loaded)
_model = None
_embeddings = None
_metadata = None


def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model


def load_index():
    global _embeddings, _metadata
    if _embeddings is None:
        _embeddings = np.load(INDEX_PATH / "embeddings.npy")
        with open(INDEX_PATH / "metadata.json") as f:
            _metadata = json.load(f)
    return _embeddings, _metadata


def search(query: str, n_results: int = 10, theme_filter: str = None) -> list[dict]:
    """
    Search the vault for semantically similar content.

    Args:
        query: Search query (natural language)
        n_results: Number of results to return
        theme_filter: Optional theme to filter by

    Returns:
        List of results with file_path, heading, text snippet, and score
    """
    model = get_model()
    embeddings, metadata = load_index()

    # Generate query embedding
    query_embedding = model.encode([query])[0]
    query_embedding = query_embedding / np.linalg.norm(query_embedding)

    # Compute cosine similarities (embeddings already normalised)
    similarities = embeddings @ query_embedding

    # Get indices sorted by similarity
    sorted_indices = np.argsort(similarities)[::-1]

    # Filter and format results
    results = []
    for idx in sorted_indices:
        if len(results) >= n_results:
            break

        meta = metadata[idx]

        if theme_filter and meta['theme'].lower() != theme_filter.lower():
            continue

        score = float(similarities[idx])

        results.append({
            'file_path': meta['file_path'],
            'heading': meta['heading_path'],
            'theme': meta['theme'],
            'line': meta['line_start'],
            'score': round(score, 3),
            'snippet': meta['text'][:300] + "..." if len(meta['text']) > 300 else meta['text'],
            'full_text': meta['text'],
        })

    return results


def print_results(results: list[dict], show_snippets: bool = True):
    """Pretty print search results."""
    if not results:
        print("No results found.")
        return

    print(f"\n{'='*60}")
    print(f"Found {len(results)} results")
    print(f"{'='*60}\n")

    for i, r in enumerate(results, 1):
        print(f"[{i}] {r['file_path']}:{r['line']}")
        print(f"    Heading: {r['heading']}")
        print(f"    Theme: {r['theme']} | Score: {r['score']}")
        if show_snippets:
            snippet = r['snippet'].replace('\n', ' ').strip()
            snippet = ' '.join(snippet.split())
            print(f"    > {snippet[:200]}...")
        print()


def main():
    parser = argparse.ArgumentParser(description="Semantic search over markdown vault")
    parser.add_argument("query", nargs="?", help="Search query")
    parser.add_argument("-n", "--num", type=int, default=10, help="Number of results")
    parser.add_argument("-t", "--theme", help="Filter by theme")
    parser.add_argument("--no-snippets", action="store_true", help="Hide snippets")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if not args.query:
        print("QM Vault Semantic Search")
        print("Type a query, or 'quit' to exit\n")
        while True:
            try:
                query = input("Search: ").strip()
                if query.lower() in ('quit', 'exit', 'q'):
                    break
                if query:
                    results = search(query, n_results=args.num, theme_filter=args.theme)
                    print_results(results, show_snippets=not args.no_snippets)
            except KeyboardInterrupt:
                break
        return

    results = search(args.query, n_results=args.num, theme_filter=args.theme)

    if args.json:
        for r in results:
            del r['full_text']
        print(json.dumps(results, indent=2))
    else:
        print_results(results, show_snippets=not args.no_snippets)


if __name__ == "__main__":
    main()
