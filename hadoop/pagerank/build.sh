#!/bin/bash

mvn clean
mvn install
mv target/PageRank-1.0-SNAPSHOT.jar ./PageRank.jar
rm -rf target/
