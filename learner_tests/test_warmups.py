import pytest

from queries.warmups import (
    q1_list_recipes,
    q2_filter_by_cuisine,
    q3_subclass_traversal,
)


def test_q1_list_recipes_returns_all_five(driver):
    cypher = q1_list_recipes()

    with driver.session() as session:
        rows = [record["name"] for record in session.run(cypher)]

    assert len(rows) == 5

    expected = {
        "Margherita Pizza",
        "Pesto Pasta",
        "Mapo Tofu",
        "Kung Pao Chicken",
        "Ginger Scallion Noodles",
    }

    assert set(rows) == expected


def test_q3_traversal_picks_up_subclasses(driver):
    cypher, params = q3_subclass_traversal("Chinese")

    with driver.session() as session:
        rows = [record["name"] for record in session.run(cypher, params)]

    assert "Mapo Tofu" in rows
    assert "Kung Pao Chicken" in rows
    assert "Ginger Scallion Noodles" in rows
    assert len(rows) == 3