#!/bin/bash
# sends a JSON POST request and displays the body of the response.
echo curl $1 -X POST -H "Content-Type: application/json" -d $2
