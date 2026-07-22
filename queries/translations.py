"""SPARQL -> Cypher Translation Task.

Each function returns a Cypher **string** whose executed result is
equivalent to the corresponding W9A SPARQL query (see the W9A drill at
`drill-9a-sparql/starter/queries/drill.py`). Equivalence is asserted by
the autograder as set-of-tuples equality on the named result columns,
ignoring row order (except where ORDER BY is part of the contract).

Run against the books mini-graph in `data/books_kg.cypher`.
"""


def q1() -> str:
    """Q1 — Return all (book, title) pairs."""
    return """
MATCH (b:Book)
RETURN b.id AS book, b.title AS title
"""


def q2() -> str:
    """Q2 — Return (book, year) pairs filtered to books published after 2010."""
    return """
MATCH (b:Book)
WHERE b.year > 2010
RETURN b.id AS book, b.year AS year
"""


def q3() -> str:
    """Q3 — Return all (book, author_name) pairs."""
    return """
MATCH (b:Book)-[:AUTHORED_BY]->(a:Author)
RETURN b.id AS book, a.name AS author_name
"""


def q4() -> str:
    """Q4 — Return (book, topic) pairs with topic OPTIONAL."""
    return """
MATCH (b:Book)
OPTIONAL MATCH (b)-[:ON_TOPIC]->(t:Topic)
RETURN b.id AS book, t.name AS topic
"""


def q5() -> str:
    """Q5 — Return TRUE iff any book has more than one author."""
    return """
MATCH (b:Book)-[:AUTHORED_BY]->(a:Author)
WITH b, COUNT(DISTINCT a) AS author_count
RETURN ANY(x IN COLLECT(author_count) WHERE x >= 2) AS result
"""