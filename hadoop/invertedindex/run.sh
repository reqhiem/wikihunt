#!/bin/bash

if [ $# -ne 2 ]; then
    echo 1>&2 Usage: ./run.sh Inputs-File-Directory
    echo "e.g. ./run.sh input.invertedindex"
    exit -1
fi
hdfs dfs -rm -r -f output.invertedindex

hadoop jar InvertedIndex.jar cloud.hadoop.invertedindex.HadoopInvertedIndex $1 output.invertedindex
