# Drill 9B — SKOS Lookup & Resolve

Complete the two functions in `linker/lookup.py`:

- `candidates(graph, surface_form)` — return URIs whose `skos:prefLabel` or `skos:altLabel` matches `surface_form` (case-insensitive). Must use a parameterized SPARQL query (no string interpolation).
- `resolve(graph, surface_form, expected_type)` — call `candidates`, filter by `rdf:type`, return the single matching URI or `None` (NIL) if zero or more than one remain.

Full task description, expected behavior, and worked examples are in the drill guide:
<https://LevelUp-Applied-AI.github.io/aispire-14005-pages/modules/module-9/b99fbce7>

Run locally:

```bash
pip install -r requirements.txt
pytest tests/ -v
```

No Docker or Fuseki needed — everything runs in-memory against `rdflib`.

---

## License

This repository is provided for educational use only. See [LICENSE](LICENSE) for terms.

You may clone and modify this repository for personal learning and practice, and reference code you wrote here in your professional portfolio. Redistribution outside this course is not permitted.
