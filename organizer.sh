#!/bin/bash

# Check if archive directory exists
if [ ! -d "archive" ]; then
    mkdir archive
fi

# Check if grades.csv exists
if [ ! -f "grades.csv" ]; then
    echo "Error: grades.csv not found."
    exit 1
fi

# Generate timestamp
timestamp=$(date +"%Y%m%d-%H%M%S")

# Create new archived filename
archived_file="grades_${timestamp}.csv"

# Move and rename grades.csv
mv grades.csv archive/$archived_file

# Create a new empty grades.csv
touch grades.csv

# Log the operation
echo "Timestamp: $timestamp | Original: grades.csv | Archived: $archived_file" >> organizer.log

echo "Grades file archived successfully."
