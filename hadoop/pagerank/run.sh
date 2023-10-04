#!/bin/bash

if [ $# -ne 3 ]; then
    echo 1>&2 Usage: ./run.sh Inputs-File-Directory Number-of-Urls Number-Of-Iterations
    echo "e.g. ./run.sh input.pagerank 5000 1"
    exit -1
fi
hdfs dfs -rm -r -f output.pagerank

for i in $(seq 0 $3); do
    hdfs dfs -rm -r -f $i
done

hadoop jar PageRank.jar cloud.hadoop.pagerank.HadoopPageRank $1 output.pagerank $2 $3
