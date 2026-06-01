"""SKOS-mediated lookup and resolution against a fixture KG.

Both functions operate on an in-memory ``rdflib.Graph`` populated from
``fixtures/recipes_kg.ttl``.
"""

from rdflib import Graph, URIRef


def candidates(graph: Graph, surface_form: str) -> list[URIRef]:
    """Return URIs whose SKOS label matches ``surface_form`` (case-insensitive).

    A match is any entity carrying a ``skos:prefLabel`` or ``skos:altLabel``
    whose lowercased lexical form equals ``surface_form.lower()``.

    Must use a parameterized SPARQL query (no string interpolation of the
    surface form into the query text).

    Returns the matching URIs; the order is not significant — callers compare
    as a set.
    """
    # TODO: write a parameterized SPARQL query using initBindings (no string
    # interpolation) that returns URIs matching prefLabel OR altLabel,
    # case-insensitive.
    # TODO: execute the query against `graph` and collect the resulting URIs.
    raise NotImplementedError("Implement candidates() — see the drill guide for the task description.")


def resolve(graph: Graph, surface_form: str, expected_type: URIRef) -> URIRef | None:
    """Resolve ``surface_form`` to a single URI of type ``expected_type``, or NIL.

    Call ``candidates`` to get the lexical matches, then keep only those
    whose ``rdf:type`` is ``expected_type``. Return the URI if exactly one
    survives the filter; otherwise return ``None`` (the NIL outcome — used
    when zero candidates match the type, and also when more than one
    candidate would survive with no further signal to disambiguate).
    """
    # TODO: get the lexical candidates from candidates().
    # TODO: filter the candidates by rdf:type == expected_type.
    # TODO: return the single survivor, or None when zero or more than one remain.
    raise NotImplementedError("Implement resolve() — see the drill guide for the task description.")
