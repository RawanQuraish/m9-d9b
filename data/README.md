# Drill 9B fixtures

Two fixture files load at autograder start (and any `python load_fixture.py` run):

## `books_kg.cypher` — Translation Task target graph

Mirrors the W9A SPARQL drill's `fixtures/mini_kg.ttl` as a Neo4j property graph
with the same conceptual content. Used by the SPARQL → Cypher Translation Task
tests to check **result-set equivalence** between your Cypher (in
`queries/translations.py`) and the W9A SPARQL queries.

| Label    | Count |
|----------|-------|
| Author   | 6     |
| Book     | 5     |
| Topic    | 2     |

| Relationship  | Count |
|---------------|-------|
| AUTHORED_BY   | 7     |
| ON_TOPIC      | 4     |

`Book.topic` is also stored as a string property on `:Book` (mirroring the
W9A literal triple) so that translations can reach topics either by property
access or via the `(:Book)-[:ON_TOPIC]->(:Topic)` edge.

## `recipes_mini.cypher` — M9B vocabulary warm-up subgraph

A tiny slice of the M9B recipe schema you'll see in full in the Lab (~200
nodes). The drill warm-ups in `queries/warmups.py` run against this graph
so you practice the canonical `:Recipe / :Cuisine / :Ingredient /
[:OF_CUISINE] / [:USES_INGREDIENT] / [:SUBCLASS_OF]` vocabulary before
attempting the Translation Task.

| Label      | Count |
|------------|-------|
| Recipe     | 5     |
| Cuisine    | 3     |
| Ingredient | 2     |

| Relationship      | Count |
|-------------------|-------|
| OF_CUISINE        | 5     |
| USES_INGREDIENT   | 4     |
| SUBCLASS_OF       | 1     |

`Sichuan -[:SUBCLASS_OF]-> Chinese` is the load-bearing edge that lets
"Chinese recipes" reach Sichuan recipes via `[:SUBCLASS_OF*0..]` traversal.

## Combined totals (asserted by `load_fixture.py`)

- **23 nodes** (6 + 5 + 2 + 5 + 3 + 2)
- **21 relationships** (7 + 4 + 5 + 4 + 1)

Every node carries `:Entity` + an `id` property per the M9B Identity
Discipline. The `entity_id_unique` constraint is asserted at load time.
