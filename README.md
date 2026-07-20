# Individual Coding Lab - Grade Evaluator & Archiver

## Overview

This project contains a Python grade evaluation system and a Bash script for archiving grade files.

The Python program reads `grades.csv`, validates scores and weights, calculates the final grade and GPA, determines the student's pass/fail status, and identifies eligible assignments for resubmission.

The Bash script automates the archiving of processed grade files by adding timestamps, moving files into an archive folder, creating a new grades file, and logging the operation.

## Files

- `grade-evaluator.py` - Python application for grade processing and evaluation.
- `organizer.sh` - Bash script for grade file archiving.
- `grades.csv` - Sample grade dataset used for testing.
## grade-evaluator.py

Python program that:

- Reads grade information from a CSV file
- Validates scores are between 0 and 100
- Checks that assignment weights total:
  - Formative: 60%
  - Summative: 40%
  - Overall: 100%
- Calculates final grade
- Calculates GPA
- Determines whether the student has passd or failed
- Finds failed formative assignments with the highest weight for resubmission.
## organizer.sh

Bash script that:

- Creates an archive directory if it does not exist
- Generates a timestamp
- Renames and moves the existing grades.csv file into the archive folder
- Creates a new empty grades.csv file
- Records archive actions in organizer.log

## How to Run

### Run Python Program
Enter the bash command "python3 grade-evaluator.py", then enter "grades.csv" when prompted.Give permission to the archive script by entering "chmod +x organizer.sh" and run it by entering "./organizer.sh".

