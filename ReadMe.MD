# Purchase Requisition System

## About the Project
A purchase requisition system written in Python for BACT7501 Assessment 2. Staff submit requisitions, small ones are approved automatically, and larger ones wait for a manager's decision.

## Project Features
- Staff information input
- Multiple item entries
- Automatic total calculation
- Manager approval system
- Requisition statistics

## Features
- Generates a requisition ID automatically, starting at 10001.
- Stores the staff details (date, staff ID and staff name) and one or more items with their prices.
- Calculates the total cost.
- Approves requisitions under $500 automatically.
- Keeps requisitions of $500 or more Pending until a manager approves or rejects them (or leaves them Pending).
- Creates an approval reference for approved requisitions (staff ID + last 3 digits of the requisition ID, e.g. FN19001).
- Displays all requisitions and statistics.
- Checks input, so blank entries, invalid prices and invalid choices are asked again.

## How to Start
Run this in the terminal (use `python3` if `python` doesn't work):

```
python requisition_system.py
```

## Example Output
```
Requisition Summary
Date: 03-04-2024
Requisition ID: 10001
Staff ID: FN19
Staff Name: John Paul
Items:
  - Cutter: $450.0
Total: $450.0
Status: Approved
Approval Reference Number: FN19001
```

## Language Used
Python (Object-oriented Programming)