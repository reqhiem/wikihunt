#!/bin/bash

hdfs dfs -copyToLocal output.invertedindex/part-r-00000 invertedindex.out.txt
