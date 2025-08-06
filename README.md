# Food Safety Inspection Dashboard

A simple dashboard for visualizing restaurant food safety inspection data.

## Project Structure

```
assessment-tasks/
├── backend/               # Python backend code
│   ├── myproject/         # Main project directory
│   │   ├── api.py         # Flask API server
│   │   ├── task_models_2.py  # Data processing functions
│   │   └── static/        # Web dashboard files
│   │       └── index.html # Dashboard interface
│   └── run_api.sh         # Script to run the API
│
└── front/                 # React frontend (not used in this solution)
```

## Quick Start

### Backend

1. Install dependencies:
```bash
cd backend
pip install flask flask-cors
```

2. Run the API server:
```bash
cd myproject
python3 api.py
```

3. Access the dashboard:
   - Open your browser to: http://localhost:5000

### Key Implementation Details

#### Backend (Python/Flask)

- **Mock Data Generation**: Created functions that simulate database queries with realistic mock data
- **API Endpoints**: 
  - `/api/failed-inspections` - Failed inspection data over 6 months
  - `/api/inspection-percentages` - Restaurant visit percentages by region

#### Frontend (HTML/JavaScript)

- **Interactive Charts**: Used Chart.js for data visualization
- **Responsive Design**: Works on different screen sizes
- **Dynamic Filtering**: Can filter data by region

## Features

1. **Failed Food Safety Inspections**
   - Shows restaurants that failed inspections over the last 6 months
   - Displays trends over time
   - Allows filtering by region

2. **Restaurant Inspection Percentages**
   - Shows percentage of restaurants visited by inspectors
   - Displays change vs previous month
   - Breaks down data by region

## Implementation Notes

- Used mock data instead of database queries for simplicity
- Created a single-page application for easy deployment
- Implemented responsive charts that adapt to different data
- Added region filtering to demonstrate interactive features
- Used Flask's built-in server for simplicity