# Food Safety Inspection Dashboard

A simple dashboard for visualizing food safety inspection data.

## Overview

This project provides:
- Data processing functions for food safety metrics
- A web dashboard to visualize the data
- Mock data generation (no database required)

## Quick Start

### Installation

```bash
# Install dependencies
pip install flask flask-cors
```

### Running the Application

```bash
# From the backend/myproject directory
python3 api.py
```

Then open your browser to: http://localhost:5000

## Features

### Task 1: Failed Food Safety Inspections
- Shows restaurants that failed inspections over the last 6 months
- Filter by region or view all regions

### Task 2: Restaurant Inspection Percentages
- Shows percentage of restaurants visited by inspectors
- Displays change vs previous month
- Breaks down data by region

## API Endpoints

- `/api/failed-inspections` - Get failed inspection data
- `/api/inspection-percentages` - Get inspection percentage data
- `/api-docs` - View API documentation

## Project Structure

```
backend/myproject/
├── api.py                 # Flask API server
├── task_models_2.py       # Data processing functions
└── static/                # Web dashboard files
    └── index.html         # Dashboard interface
```

## Notes

- All data is generated using mock functions
- No real database connection required
- Charts are created using Chart.js