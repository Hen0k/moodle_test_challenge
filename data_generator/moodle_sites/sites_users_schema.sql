CREATE TABLE IF NOT EXISTS "SitesUsers"
(
    "id" SERIAL PRIMARY KEY NOT NULL,
    "username" VARCHAR NOT NULL,
    "fullname" VARCHAR NOT NULL,
    "admin_email" VARCHAR NOT NULL,
    "registration_timestamp" TIMESTAMP NOT NULL    
);
