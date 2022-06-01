-- DROP TABLE IF EXISTS "TERMINAL_DATA";
-- DROP DATABASE IF EXISTS atm_track;
CREATE DATABASE IF NOT EXISTS atm_track;
\connect atm_track;

CREATE TABLE "TERMINAL_DATA" (
  "id" serial PRIMARY KEY,
  "createdAt" timestamp not null default CURRENT_DATE,
  "terminalID" varchar,
  "cashBalance" integer,
  "daysUntilLoad" integer,
  "lastTransaction" date not null default CURRENT_DATE
);

SELECT * FROM "TERMINAL_DATA";
-- INSERT INTO "TERMINAL_DATA" ("createdAt", "terminalID", "cashBalance", "daysUntilLoad", "lastTransaction") VALUES (Now(), 'NH097675', 740.00, 3, Now());
-- SELECT * FROM "TERMINAL_DATA";