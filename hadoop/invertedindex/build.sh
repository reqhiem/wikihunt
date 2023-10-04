#!/bin/bash

mvn clean
mvn install
mv target/InvertedIndex-1.0-SNAPSHOT.jar ./InvertedIndex.jar
rm -rf target/
