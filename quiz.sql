BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "quiz" (
	"que"	TEXT,
	"a"	TEXT,
	"b"	TEXT,
	"c"	TEXT,
	"d"	TEXT
);
INSERT INTO "quiz" VALUES ('Фамилия создателя OS Windows','Андресон','Джобс','Безос','Маск');
COMMIT;
