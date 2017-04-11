#!/bin/bash
# displays only the status code of the curl request response
curl -Ls -w %{http_code} $1
