#!/bin/bash

pid=`ps -ef | grep server_start | grep -v grep | awk '{print $2}'`
kill -9 $pid
