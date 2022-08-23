\connect atm_track;
DROP TABLE IF EXISTS "TERMINAL_DATA";


CREATE TABLE "TERMINAL_DATA" (
  "id" serial PRIMARY KEY,
  "createdAt" timestamp not null default CURRENT_DATE,
  "terminalID" varchar not null default 'NHFRKS50',
  "cashBalance" integer not null default 0000,
  "daysUntilLoad" integer not null default 31,
  "lastTransaction" varchar UNIQUE
);

SELECT * FROM "TERMINAL_DATA";
