"""Autograder for Drill 9B — SKOS lookup & resolve."""

import ast
import csv
import os
import sys

import pytest
from rdflib import Graph, URIRef

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from linker.lookup import candidates, resolve  # noqa: E402


@pytest.fixture(scope="module")
def kg():
    g = Graph()
    g.parse("fixtures/recipes_kg.ttl", format="turtle")
    return g


@pytest.fixture(scope="module")
def cases():
    with open("fixtures/lookups.csv") as f:
        return list(csv.DictReader(f))


def test_candidates_returns_correct_set(kg, cases):
    for row in cases:
        if row["check"] != "candidates":
            continue
        result = set(str(u) for u in candidates(kg, row["surface_form"]))
        expected = set(row["expected_uris"].split("|"))
        assert result == expected, row


def test_resolve_handles_disambiguation_and_nil(kg, cases):
    for row in cases:
        if row["check"] != "resolve":
            continue
        result = resolve(kg, row["surface_form"], URIRef(row["expected_type"]))
        expected = None if row["expected_uri"] == "NIL" else URIRef(row["expected_uri"])
        assert result == expected, row


# Static AST meta-test — drill autograder is course-provided so the Learner-Written Test
# Rule does not apply here. The meta-test instead ensures `candidates` uses initBindings
# (parameterized query, not string-interpolation — preempts SPARQL injection lessons).
def test_candidates_uses_init_bindings():
    src = open("linker/lookup.py").read()
    tree = ast.parse(src)
    found = any(
        isinstance(n, ast.keyword) and n.arg == "initBindings"
        for n in ast.walk(tree)
    )
    assert found, "candidates() must use initBindings to parameterize the SPARQL query (not string interpolation)"
