# moodle_test_challenge

## Challenge Description

Propose a detailed solution for the given scenario (sinks, producers, consumers, etc).

Please list the technologies involving the Kafka cluster, languages used and the final data pipeline from end to end (preferred in a flow chart):

### Scenario  

* Moodle has 2 public sites, Moodle Community & Moodle Sites. They are not connected and don't share users  
* Moodle Community has open forums for registered users (using their email)  
* Moodle Sites has registration data of customers using/installing Moodle (part of the data sent for registration is the administrator email)  
* Both sites have all data in different databases and their logs are sent to a central repository  

### We want to know

* Number of sites being registered weekly and its time evolution  
* Number of users from Moodle Community administrating registered sites and its time evolution  

Please add a coded solution to solve the connection between the producer, the data source and the cluster. We have some solutions coded in bash and others in python, feel free to choose any of them or another language.

## My Assumptions

* Moodle Community --> MC
* Moodle Sites --> MS
* The first statement saying that MC and MS don't share users is not strict. It is meant to say that they don't necessarily share users but they could have some users incommon.
* *MC* Registration data:
  * user_handle
  * **email**
  * password
  * **registration_timestamp**
* *MS* registration data:
  * Organization
  * Site URI
  * Sector / Content type
  * **admin email**
  * **registration_timestamp**
* I will Ignore the log data since I am assuming it is for recovery only.

## Components

* Will be using Apache Kafka instead of Confluent Kafka because of the free and open sources nature of Apache Kafka
* A Kafka Connect component that reads data from the source databases and makes light transformations.
