CREATE TABLE IF NOT EXISTS SitesUsers
(
    "id" SERIAL NOT NULL,
    "username" TEXT NOT NULL,
    "fullname" TEXT NOT NULL,
    "admin_email" TEXT NOT NULL,
    "registration_timestamp" FLOAT DEFAULT NULL,
    PRIMARY KEY ("id")
    
);
