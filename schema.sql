-- DROP TABLE IF EXISTS "TERMINAL_DATA";
DROP DATABASE IF EXISTS atm_track;
CREATE DATABASE atm_track;
\connect atm_track;

CREATE TABLE "TERMINAL_DATA" (
  "id" serial PRIMARY KEY,
  "createdAt" timestamp not null default CURRENT_DATE,
  "terminalID" varchar,
  "cashBalance" integer,
  "daysUntilLoad" integer,
  "lastTransaction" varchar
);

SELECT * FROM "TERMINAL_DATA";
