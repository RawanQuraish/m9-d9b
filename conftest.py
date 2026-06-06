"""Shared pytest fixtures for the Drill 9B repo.

Provides a `driver` fixture wired to NEO4J_URI/NEO4J_USER/NEO4J_PASSWORD
with sensible local defaults (matching docker-compose.yml).
"""

from __future__ import annotations

import os

import pytest
from neo4j import GraphDatabase


@pytest.fixture(scope="session")
def driver():
    uri = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
    user = os.environ.get("NEO4J_USER", "neo4j")
    password = os.environ.get("NEO4J_PASSWORD", "testtest")
    drv = GraphDatabase.driver(uri, auth=(user, password))
    yield drv
    drv.close()
