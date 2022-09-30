CREATE TABLE IF NOT EXISTS "CommunityUsers"
(
    "id" SERIAL PRIMARY KEY NOT NULL,
    "username" VARCHAR NOT NULL,
    "fullname" VARCHAR NOT NULL,
    "email" VARCHAR NOT NULL,
    "registration_timestamp" TIMESTAMP NOT NULL    
);

