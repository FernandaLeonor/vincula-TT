#!/bin/bash

bash wait.sh db:5432

# Check if wait.sh executed successfully
if [ $? -ne 0 ]; then
  echo "wait.sh failed"
  exit 1
fi

# Execute the passed command
exec "$@"