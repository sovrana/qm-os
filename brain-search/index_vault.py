#!/usr/bin/env python3
"""
QM Vault Indexer
Indexes markdown files with heading-based chunking for semantic search.
Uses numpy-based storage - no ChromaDB dependency.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime
import numpy as np
from sentence_transformers import SentenceTransformer

# Configuration - override with environment variables
VAULT_PATH = Path(os.environ.get("QM_VAULT_PATH", os.getcwd()))
INDEX_PATH = Path(os.environ.get(
    "QM_INDEX_PATH",
    str(VAULT_PATH / "99_System" / "brain-search" / "vector-index")
))
MODEL_NAME = os.environ.get("QM_MODEL_NAME", "all-MiniLM-L6-v2")

# Folders to skip (noisy or irrelevant)
SKIP_FOLDERS = {
    ".git",
    ".obsidian",
    "node_modules",
    "brain-search-env",
    "vector-index",
}

# File patterns to skip
SKIP_PATTERNS = [
    r".*-raw-transcript\.md$",  # Raw transcripts are noisy
]


def should_skip_file(file_path: Path) -> bool:
    """Check if file should be skipped."""
    rel_path = str(file_path.relative_to(VAULT_PATH))

    for folder in SKIP_FOLDERS:
        if folder in rel_path.split(os.sep):
            return True

    for pattern in SKIP_PATTERNS:
        if re.match(pattern, file_path.name):
            return True

    return False


def chunk_by_headings(content: str, file_path: Path) -> list[dict]:
    """
    Split markdown content into chunks based on headings.
    Each chunk includes the heading hierarchy for context.
    """
    chunks = []
    lines = content.split('\n')

    current_chunk = []
    heading_stack = []  # [(level, text), ...]
    chunk_start_line = 0

    for i, line in enumerate(lines):
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)

        if heading_match:
            # Save previous chunk if it has content
            if current_chunk:
                chunk_text = '\n'.join(current_chunk).strip()
                if len(chunk_text) > 50:
                    heading_path = ' > '.join(h[1] for h in heading_stack) if heading_stack else "Document Root"
                    chunks.append({
                        'text': chunk_text,
                        'heading_path': heading_path,
                        'file_path': str(file_path.relative_to(VAULT_PATH)),
                        'line_start': chunk_start_line,
                    })

            # Update heading stack
            level = len(heading_match.group(1))
            heading_text = heading_match.group(2).strip()

            while heading_stack and heading_stack[-1][0] >= level:
                heading_stack.pop()

            heading_stack.append((level, heading_text))
            current_chunk = [line]
            chunk_start_line = i + 1
        else:
            current_chunk.append(line)

    # Last chunk
    if current_chunk:
        chunk_text = '\n'.join(current_chunk).strip()
        if len(chunk_text) > 50:
            heading_path = ' > '.join(h[1] for h in heading_stack) if heading_stack else "Document Root"
            chunks.append({
                'text': chunk_text,
                'heading_path': heading_path,
                'file_path': str(file_path.relative_to(VAULT_PATH)),
                'line_start': chunk_start_line,
            })

    # Whole file as one chunk if no headings found
    if not chunks and len(content.strip()) > 50:
        chunks.append({
            'text': content.strip()[:5000],
            'heading_path': "Document Root",
            'file_path': str(file_path.relative_to(VAULT_PATH)),
            'line_start': 1,
        })

    return chunks


def extract_theme(file_path: str) -> str:
    """Extract theme from file path based on 02_Themes/ convention."""
    parts = file_path.split(os.sep)
    if len(parts) >= 2 and parts[0] == "02_Themes":
        return parts[1]
    return parts[0] if parts else "Unknown"


def index_vault():
    """Main indexing function."""
    print(f"Starting vault indexing...")
    print(f"Vault path: {VAULT_PATH}")
    print(f"Index path: {INDEX_PATH}")

    print(f"\nLoading embedding model: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)

    md_files = list(VAULT_PATH.glob("**/*.md"))
    print(f"\nFound {len(md_files)} markdown files")

    all_chunks = []
    files_processed = 0
    files_skipped = 0

    for file_path in md_files:
        if should_skip_file(file_path):
            files_skipped += 1
            continue

        try:
            content = file_path.read_text(encoding='utf-8')
            chunks = chunk_by_headings(content, file_path)

            for chunk in chunks:
                chunk['theme'] = extract_theme(chunk['file_path'])
                chunk['modified'] = datetime.fromtimestamp(
                    file_path.stat().st_mtime
                ).isoformat()

            all_chunks.extend(chunks)
            files_processed += 1

            if files_processed % 50 == 0:
                print(f"  Processed {files_processed} files, {len(all_chunks)} chunks...")

        except Exception as e:
            print(f"  Error processing {file_path}: {e}")

    print(f"\nProcessed {files_processed} files, skipped {files_skipped}")
    print(f"Total chunks: {len(all_chunks)}")

    if not all_chunks:
        print("No chunks to index!")
        return

    print(f"\nGenerating embeddings...")
    texts = [c['text'][:2000] for c in all_chunks]

    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings)

    # Normalise for cosine similarity
    norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
    embeddings = embeddings / norms

    INDEX_PATH.mkdir(parents=True, exist_ok=True)

    np.save(INDEX_PATH / "embeddings.npy", embeddings)

    metadata = []
    for i, chunk in enumerate(all_chunks):
        metadata.append({
            'id': i,
            'file_path': chunk['file_path'],
            'heading_path': chunk['heading_path'],
            'theme': chunk['theme'],
            'modified': chunk['modified'],
            'line_start': chunk['line_start'],
            'text': chunk['text'][:2000],
        })

    with open(INDEX_PATH / "metadata.json", 'w') as f:
        json.dump(metadata, f)

    print(f"\nIndexing complete!")
    print(f"  - embeddings.npy: {embeddings.shape}")
    print(f"  - metadata.json: {len(metadata)} chunks")

    # Summary
    themes = {}
    for chunk in all_chunks:
        theme = chunk['theme']
        themes[theme] = themes.get(theme, 0) + 1

    print(f"\nChunks by theme:")
    for theme, count in sorted(themes.items(), key=lambda x: -x[1])[:10]:
        print(f"  {theme}: {count}")


if __name__ == "__main__":
    index_vault()
