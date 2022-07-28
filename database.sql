DROP TABLE IF EXISTS "trainer";
DROP SEQUENCE IF EXISTS trainer_id_seq;
CREATE SEQUENCE trainer_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."trainer" (
    "id" integer DEFAULT nextval('trainer_id_seq') NOT NULL,
    "nickname" character(100),
    "first_name" character(100),
    "last_name" character(100),
    "email" character(100),
    "password" character(100),
    "team" character(100),
    CONSTRAINT "trainer_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "trainer_pokemon";
CREATE TABLE "public"."trainer_pokemon" (
    "trainer_id" integer NOT NULL,
    "name" character(50) NOT NULL,
    "level" integer NOT NULL,
    "pokemon_id" integer NOT NULL
) WITH (oids = false);