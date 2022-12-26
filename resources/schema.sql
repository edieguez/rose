BEGIN TRANSACTION;
DROP TABLE IF EXISTS "definitions";
CREATE TABLE IF NOT EXISTS "definitions" (
  "id" INTEGER,
  "words_id" INTEGER NOT NULL,
  "part_of_speech" TEXT NOT NULL,
  "description" TEXT NOT NULL,
  "example" TEXT UNIQUE,
  FOREIGN KEY("words_id") REFERENCES "words"("id"),
  PRIMARY KEY("id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "words";
CREATE TABLE IF NOT EXISTS "words" (
  "id" INTEGER NOT NULL,
  "text" TEXT NOT NULL UNIQUE,
  "image_url" TEXT,
  PRIMARY KEY("id" AUTOINCREMENT)
);
COMMIT;
