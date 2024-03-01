#!/bin/bash
# make a get request using curl and get response body when status is  200
status = curl -sI "$2" | grep -i "status"
