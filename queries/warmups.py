"""Cypher warm-ups against the M9B recipe vocabulary."""


def q1_list_recipes() -> str:
    return """
MATCH (r:Recipe)
RETURN r.name AS name
"""


def q2_filter_by_cuisine(cuisine_name: str) -> tuple[str, dict]:
    query = """
MATCH (r:Recipe)-[:OF_CUISINE]->(c:Cuisine {name: $cuisine})
RETURN r.name AS name
"""
    return query, {"cuisine": cuisine_name}


def q3_subclass_traversal(cuisine_name: str) -> tuple[str, dict]:
    query = """
MATCH (r:Recipe)-[:OF_CUISINE]->(:Cuisine)-[:SUBCLASS_OF*0..]->(:Cuisine {name: $cuisine})
RETURN r.name AS name
"""
    return query, {"cuisine": cuisine_name}