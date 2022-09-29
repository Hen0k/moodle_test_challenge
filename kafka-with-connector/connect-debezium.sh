#/bin/bash

curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" 127.0.0.1:8083/connectors --data "@debezium-sites.json";
echo "\n\nDone with sites source connector\n\n";

curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" 127.0.0.1:8084/connectors --data "@debezium-community.json";
echo "\n\nDone with community source connector\n\n";

curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" 127.0.0.1:8085/connectors --data "@jdbc-sink-connector.json";
echo "\n\nDone with jdbc sink connector\n\n";

