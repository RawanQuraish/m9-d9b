# Module 9 Week B — Core Skills Drill

Cypher fundamentals + a SPARQL → Cypher Translation Task.

This drill exercises the M9B knowledge-graph vocabulary on Neo4j and then
asks you to **translate the five SPARQL queries from the M9 Week A drill
into Cypher** against an equivalent property graph. Same questions, same
data, different query language — the translation makes the W9A → W9B
shift in graph paradigm concrete.

## What you'll build

**Warm-ups (`queries/warmups.py`).** Three Cypher queries against a tiny
recipe sub-graph (5 recipes, 3 cuisines, 2 ingredients) so you practice
the canonical M9B vocabulary — `:Recipe`, `:Cuisine`, `:Ingredient`,
`[:OF_CUISINE]`, `[:USES_INGREDIENT]`, `[:SUBCLASS_OF]`. One of the
warm-ups uses `[:SUBCLASS_OF*0..]` so a search for "Chinese recipes"
picks up Sichuan recipes through the hierarchy.

**Translation Task (`queries/translations.py`).** Five Cypher queries
against a books mini-graph that mirrors the W9A SPARQL drill's
`fixtures/mini_kg.ttl`. For each `q1()…q5()`, your Cypher must return
the **same result set** as the W9A SPARQL query of the same number. The
autograder runs both — the W9A SPARQL against an rdflib parse of the
books data, your Cypher against Neo4j — and asserts set-of-tuples
equality on the named result columns.

**Learner-written tests (`learner_tests/test_warmups.py`).** Two test
stubs. Replace each `pytest.fail("Not implemented…")` body with real
assertions against your warm-up queries. The autograder verifies you
wrote real assertions, not silent passes.

## Repo layout

```
.
├── README.md
├── FORK-SUBMIT.md            # how to submit (fork-and-submit flow)
├── LICENSE
├── requirements.txt
├── docker-compose.yml         # Neo4j 5 Community for local runs
├── conftest.py                # pytest `driver` fixture
├── load_fixture.py            # ingests both .cypher files + asserts counts
├── data/
│   ├── books_kg.cypher        # 6 authors, 5 books, 2 topics (Translation Task target)
│   ├── recipes_mini.cypher    # 5 recipes, 3 cuisines, 2 ingredients (warm-up target)
│   └── README.md
├── queries/
│   ├── warmups.py             # YOU WRITE — 3 functions
│   └── translations.py        # YOU WRITE — 5 functions (q1..q5)
├── learner_tests/
│   └── test_warmups.py        # YOU WRITE — 2 tests, replace placeholders
└── tests/
    └── test_drill_9b.py       # autograder — do not modify
```

## Setup

You should already have run the Module 9 Week B reading's install
section. If not, install dependencies now:

```bash
pip install -r requirements.txt
```

## Run Neo4j locally

```bash
docker compose up -d
# wait for "Started." in the log:
docker compose logs -f neo4j | head
```

Default credentials: `neo4j` / `testtest` (set in `docker-compose.yml`).

## Load the fixtures

```bash
python load_fixture.py
```

This applies the `entity_id_unique` constraint, executes the two
`.cypher` files, and asserts the expected node and relationship counts.
A successful load prints `Fixture loaded: 23 nodes, 21 relationships …`.

## Run the autograder locally

```bash
pytest tests/ -v
```

The same suite runs in CI on every push to a non-`main` branch (see
`.github/workflows/m9-d9b-autograder.yml`).

## Implementation guidance

- **Parameterized Cypher.** Whenever a value comes from outside the
  query (a function argument, anything the caller controls), use
  `$param` syntax — never f-strings. The autograder rejects f-string
  Cypher in `queries/`.
- **Identity Discipline.** Every fixture node carries `:Entity` and an
  `id` property like `'recipe:1'` or `'book:1'`. You won't need to
  modify the constraint, but you'll see the `id` field in result rows.
- **Hierarchy traversal.** `(:Cuisine)-[:SUBCLASS_OF]->(:Cuisine)`
  forms a small chain (Sichuan → Chinese). A Cypher search that should
  cover descendants uses `[:SUBCLASS_OF*0..]` so the cuisine itself
  and any sub-cuisine match in a single pattern.
- **Translation Task result-set columns.** Each `q1()…q5()` docstring
  names the exact column names the autograder expects. Use `AS` to
  alias your returned values to those names.

## Submitting

See [FORK-SUBMIT.md](FORK-SUBMIT.md). Branch name:
`drill-9b-cypher-translation`.

---

## License

This repository is provided for educational use only. See [LICENSE](LICENSE) for terms.

You may clone and modify this repository for personal learning and practice, and reference code you wrote here in your professional portfolio. Redistribution outside this course is not permitted.
