#!/bin/bash
# sends a POST request to the URL with key-values, and displays the body of the response
echo curl $1 -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"

