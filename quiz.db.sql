BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "quiz_name" (
	"id"	INTEGER,
	"name"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS " question" (
	"quiz_id"	INTEGER,
	"que"	TEXT,
	"a"	TEXT,
	"b"	TEXT,
	"c"	TEXT,
	"d"	TEXT,
	PRIMARY KEY("quiz_id")
);
INSERT INTO "quiz_name" VALUES (1,'cinema');
INSERT INTO "quiz_name" VALUES (2,'other');
INSERT INTO " question" VALUES (1,'Фамилия создателя OS Windows','Гейтс','Джобс','Безос','Маск');
INSERT INTO " question" VALUES (2,'2+2','3','1','5','4');
COMMIT;
