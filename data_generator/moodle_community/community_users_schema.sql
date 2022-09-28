CREATE TABLE IF NOT EXISTS CommunityUsers
(
    "id" SERIAL NOT NULL,
    "username" TEXT NOT NULL,
    "fullname" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "registration_timestamp" FLOAT DEFAULT NULL,
    PRIMARY KEY ("id")
    
);
