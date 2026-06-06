"""Load the Drill 9B fixtures into Neo4j and assert acceptance counts.

Run order:
    1. Apply the entity_id_unique constraint (M9B Identity Discipline).
    2. Execute data/books_kg.cypher (Translation Task target graph).
    3. Execute data/recipes_mini.cypher (M9B vocabulary warm-up subgraph).
    4. Assert per-label node counts, total node count, and total edge count.
    5. Exit non-zero on any mismatch.

Env vars (with defaults for local docker-compose):
    NEO4J_URI       bolt://localhost:7687
    NEO4J_USER      neo4j
    NEO4J_PASSWORD  testtest
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

from neo4j import GraphDatabase

NEO4J_URI = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.environ.get("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "testtest")

DATA_DIR = Path(__file__).parent / "data"
BOOKS_CYPHER = DATA_DIR / "books_kg.cypher"
RECIPES_CYPHER = DATA_DIR / "recipes_mini.cypher"

# Acceptance expectations (kept in lockstep with the fixture .cypher files).
EXPECTED_LABEL_COUNTS = {
    "Author": 6,
    "Book": 5,
    "Topic": 2,
    "Recipe": 5,
    "Cuisine": 3,
    "Ingredient": 2,
}
EXPECTED_TOTAL_NODES = sum(EXPECTED_LABEL_COUNTS.values())   # 23
EXPECTED_TOTAL_RELS = 7 + 4 + 5 + 4 + 1                       # 21

CONSTRAINT_CYPHER = (
    "CREATE CONSTRAINT entity_id_unique IF NOT EXISTS "
    "FOR (n:Entity) REQUIRE n.id IS UNIQUE"
)

# Strip /* ... */ block comments, // line comments, and split on semicolons.
_BLOCK_COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)
_LINE_COMMENT_RE = re.compile(r"//[^\n]*")


def _split_statements(text: str) -> list[str]:
    text = _BLOCK_COMMENT_RE.sub("", text)
    text = _LINE_COMMENT_RE.sub("", text)
    return [s.strip() for s in text.split(";") if s.strip()]


def _run_cypher_file(session, path: Path) -> None:
    statements = _split_statements(path.read_text())
    for stmt in statements:
        session.run(stmt).consume()


def _assert(condition: bool, message: str) -> None:
    if not condition:
        print(f"ACCEPTANCE FAILURE: {message}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    try:
        with driver.session() as session:
            session.run(CONSTRAINT_CYPHER).consume()
            _run_cypher_file(session, BOOKS_CYPHER)
            _run_cypher_file(session, RECIPES_CYPHER)

            for label, expected in EXPECTED_LABEL_COUNTS.items():
                actual = session.run(
                    f"MATCH (n:`{label}`) RETURN count(n) AS c"
                ).single()["c"]
                _assert(
                    actual == expected,
                    f"label :{label} expected {expected} nodes, got {actual}",
                )

            total_nodes = session.run(
                "MATCH (n) RETURN count(n) AS c"
            ).single()["c"]
            _assert(
                total_nodes == EXPECTED_TOTAL_NODES,
                f"total nodes expected {EXPECTED_TOTAL_NODES}, got {total_nodes}",
            )

            total_rels = session.run(
                "MATCH ()-[r]->() RETURN count(r) AS c"
            ).single()["c"]
            _assert(
                total_rels == EXPECTED_TOTAL_RELS,
                f"total relationships expected {EXPECTED_TOTAL_RELS}, got {total_rels}",
            )

            print(
                f"Fixture loaded: {total_nodes} nodes, {total_rels} relationships. "
                f"Per-label counts: {EXPECTED_LABEL_COUNTS}"
            )
    finally:
        driver.close()


if __name__ == "__main__":
    main()
