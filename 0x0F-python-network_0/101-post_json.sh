#!/bin/bash
# sends a JSON POST request and displays the body of the response.
curl -X POST -H "Content-Type: application/json" -T $2 $1
