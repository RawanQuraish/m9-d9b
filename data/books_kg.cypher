// Module 9 Week B — Core Skills Drill — Books mini-graph
// Mirrors the W9A SPARQL drill's fixtures/mini_kg.ttl conceptually (6 authors,
// 5 books, optional topic, multi-author edges). Used by the SPARQL->Cypher
// Translation Task autograder for result-set equivalence checks.
//
// Identity Discipline: every node carries :Entity + id. Idempotent MERGE.

// ---------- Authors (6) ----------
MERGE (:Author:Entity {id: 'author:hunt',       name: 'Andrew Hunt'});
MERGE (:Author:Entity {id: 'author:thomas',     name: 'David Thomas'});
MERGE (:Author:Entity {id: 'author:hofstadter', name: 'Douglas Hofstadter'});
MERGE (:Author:Entity {id: 'author:knuth',      name: 'Donald Knuth'});
MERGE (:Author:Entity {id: 'author:martin',     name: 'Robert C. Martin'});
MERGE (:Author:Entity {id: 'author:fowler',     name: 'Martin Fowler'});

// ---------- Books (5) ----------
// book1: The Pragmatic Programmer, 1999, topic = Software Engineering, authors = Hunt + Thomas
MERGE (b1:Book:Entity {id: 'book:1'})
  SET b1.title = 'The Pragmatic Programmer',
      b1.year  = 1999,
      b1.topic = 'Software Engineering';

// book2: Godel, Escher, Bach, 1979, NO topic, author = Hofstadter
MERGE (b2:Book:Entity {id: 'book:2'})
  SET b2.title = 'Godel, Escher, Bach',
      b2.year  = 1979;
// Note: no topic property on b2 — exercises the OPTIONAL MATCH in Q4.

// book3: The Art of Computer Programming, Volume 1, 1968, topic = Algorithms, author = Knuth
MERGE (b3:Book:Entity {id: 'book:3'})
  SET b3.title = 'The Art of Computer Programming, Volume 1',
      b3.year  = 1968,
      b3.topic = 'Algorithms';

// book4: Clean Code, 2008, topic = Software Engineering, author = Martin
MERGE (b4:Book:Entity {id: 'book:4'})
  SET b4.title = 'Clean Code',
      b4.year  = 2008,
      b4.topic = 'Software Engineering';

// book5: Refactoring, 2018, topic = Software Engineering, authors = Fowler + Martin
MERGE (b5:Book:Entity {id: 'book:5'})
  SET b5.title = 'Refactoring',
      b5.year  = 2018,
      b5.topic = 'Software Engineering';

// ---------- (:Topic) nodes — promoted from string literals to nodes ----------
// Two distinct topics across the corpus: Software Engineering, Algorithms.
MERGE (:Topic:Entity {id: 'topic:software-engineering', name: 'Software Engineering'});
MERGE (:Topic:Entity {id: 'topic:algorithms',           name: 'Algorithms'});

// ---------- AUTHORED_BY edges ----------
MATCH (b:Book {id: 'book:1'}), (a:Author {id: 'author:hunt'})       MERGE (b)-[:AUTHORED_BY]->(a);
MATCH (b:Book {id: 'book:1'}), (a:Author {id: 'author:thomas'})     MERGE (b)-[:AUTHORED_BY]->(a);
MATCH (b:Book {id: 'book:2'}), (a:Author {id: 'author:hofstadter'}) MERGE (b)-[:AUTHORED_BY]->(a);
MATCH (b:Book {id: 'book:3'}), (a:Author {id: 'author:knuth'})      MERGE (b)-[:AUTHORED_BY]->(a);
MATCH (b:Book {id: 'book:4'}), (a:Author {id: 'author:martin'})     MERGE (b)-[:AUTHORED_BY]->(a);
MATCH (b:Book {id: 'book:5'}), (a:Author {id: 'author:fowler'})     MERGE (b)-[:AUTHORED_BY]->(a);
MATCH (b:Book {id: 'book:5'}), (a:Author {id: 'author:martin'})     MERGE (b)-[:AUTHORED_BY]->(a);

// ---------- ON_TOPIC edges (mirrors :topic literal triples; book2 has none) ----------
MATCH (b:Book {id: 'book:1'}), (t:Topic {id: 'topic:software-engineering'}) MERGE (b)-[:ON_TOPIC]->(t);
MATCH (b:Book {id: 'book:3'}), (t:Topic {id: 'topic:algorithms'})           MERGE (b)-[:ON_TOPIC]->(t);
MATCH (b:Book {id: 'book:4'}), (t:Topic {id: 'topic:software-engineering'}) MERGE (b)-[:ON_TOPIC]->(t);
MATCH (b:Book {id: 'book:5'}), (t:Topic {id: 'topic:software-engineering'}) MERGE (b)-[:ON_TOPIC]->(t);
