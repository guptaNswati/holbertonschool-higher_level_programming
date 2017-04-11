#!/bin/bash
# displays only the status code of the curl request response
curl -LI $1 -s -o /dev/null -w %{http_code}
