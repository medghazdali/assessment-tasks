#!/bin/bash

# Navigate to the myproject directory
cd "$(dirname "$0")/myproject"

# Activate virtual environment if it exists
if [ -d "../env/bin" ]; then
    source ../env/bin/activate
fi

# Run the Flask API
python3 api.py