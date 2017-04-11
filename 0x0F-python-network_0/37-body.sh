#!/bin/bash
# sends a GET request to an URL, and displays the body of the response
response=$(curl -LI $1 -s -o /dev/null -w %{http_code})
if (($response == 200)) ; then
    curl -L $1
fi
