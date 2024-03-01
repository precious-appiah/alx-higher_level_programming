#!/bin/bash
# make a get request using curl and response body with status of 200
status = curl -sI "$2" | grep -i "status"
