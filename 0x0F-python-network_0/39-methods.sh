#!/bin/bash
# displays all HTTP methods the server will accept for a given url
curl -si -X OPTIONS $1 | grep Allow | cut -d ':' -f 2- | awk '$1=$1'
