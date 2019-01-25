#!/bin/bash

let item=0
item=`ps -ef | grep server_start | grep -v grep | wc -l`

cd ../src
if [ $item -eq 1 ]; then
	echo "The server is running, please shut it down..."
else
	echo "Start server now ..."
	python server_start.py
fi

