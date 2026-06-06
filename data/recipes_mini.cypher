// Module 9 Week B — Core Skills Drill — Recipe warm-up subgraph
// Tiny W9B-vocabulary fixture: 5 recipes, 3 cuisines (with a 1-level
// SUBCLASS_OF chain Sichuan -> Chinese), 2 ingredients.
// Lets learners practice the canonical M9B schema vocabulary before the
// Translation Task; the full ~200-node recipe graph appears in the Lab.
//
// Identity Discipline: every node carries :Entity + id. Idempotent MERGE.

// ---------- Cuisines (3) ----------
MERGE (:Cuisine:Entity {id: 'cuisine:italian',  name: 'Italian'});
MERGE (:Cuisine:Entity {id: 'cuisine:sichuan',  name: 'Sichuan'});
MERGE (:Cuisine:Entity {id: 'cuisine:chinese',  name: 'Chinese'});

// ---------- Ingredients (2) ----------
MERGE (:Ingredient:Entity {id: 'ingredient:ginger', name: 'ginger', category: 'spice'});
MERGE (:Ingredient:Entity {id: 'ingredient:basil',  name: 'basil',  category: 'herb'});

// ---------- Recipes (5) ----------
MERGE (r1:Recipe:Entity {id: 'recipe:1'}) SET r1.name = 'Margherita Pizza',     r1.prepMinutes = 25;
MERGE (r2:Recipe:Entity {id: 'recipe:2'}) SET r2.name = 'Pesto Pasta',          r2.prepMinutes = 20;
MERGE (r3:Recipe:Entity {id: 'recipe:3'}) SET r3.name = 'Mapo Tofu',            r3.prepMinutes = 30;
MERGE (r4:Recipe:Entity {id: 'recipe:4'}) SET r4.name = 'Kung Pao Chicken',     r4.prepMinutes = 35;
MERGE (r5:Recipe:Entity {id: 'recipe:5'}) SET r5.name = 'Ginger Scallion Noodles', r5.prepMinutes = 15;

// ---------- OF_CUISINE edges (5) ----------
MATCH (r:Recipe {id: 'recipe:1'}), (c:Cuisine {id: 'cuisine:italian'}) MERGE (r)-[:OF_CUISINE]->(c);
MATCH (r:Recipe {id: 'recipe:2'}), (c:Cuisine {id: 'cuisine:italian'}) MERGE (r)-[:OF_CUISINE]->(c);
MATCH (r:Recipe {id: 'recipe:3'}), (c:Cuisine {id: 'cuisine:sichuan'}) MERGE (r)-[:OF_CUISINE]->(c);
MATCH (r:Recipe {id: 'recipe:4'}), (c:Cuisine {id: 'cuisine:sichuan'}) MERGE (r)-[:OF_CUISINE]->(c);
MATCH (r:Recipe {id: 'recipe:5'}), (c:Cuisine {id: 'cuisine:chinese'}) MERGE (r)-[:OF_CUISINE]->(c);

// ---------- USES_INGREDIENT edges (4) ----------
MATCH (r:Recipe {id: 'recipe:1'}), (i:Ingredient {id: 'ingredient:basil'})  MERGE (r)-[:USES_INGREDIENT]->(i);
MATCH (r:Recipe {id: 'recipe:2'}), (i:Ingredient {id: 'ingredient:basil'})  MERGE (r)-[:USES_INGREDIENT]->(i);
MATCH (r:Recipe {id: 'recipe:3'}), (i:Ingredient {id: 'ingredient:ginger'}) MERGE (r)-[:USES_INGREDIENT]->(i);
MATCH (r:Recipe {id: 'recipe:5'}), (i:Ingredient {id: 'ingredient:ginger'}) MERGE (r)-[:USES_INGREDIENT]->(i);

// ---------- SUBCLASS_OF edges (1) — Sichuan -> Chinese ----------
MATCH (c1:Cuisine {id: 'cuisine:sichuan'}), (c2:Cuisine {id: 'cuisine:chinese'})
  MERGE (c1)-[:SUBCLASS_OF]->(c2);
