#!/bin/bash
# script that do a put request using header origin with curl
curl -Ls -H "Origin: HolbertonSchool" -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
