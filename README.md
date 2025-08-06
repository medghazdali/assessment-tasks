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




## Screens 

<img width="1687" height="932" alt="monthly chart" src="https://github.com/user-attachments/assets/0eeb89e2-df50-456b-b154-8b47486973ca" />
<img width="1696" height="940" alt="sales charts" src="https://github.com/user-attachments/assets/f4158217-7225-45b2-bff9-f6bf3baa5384" />
<img width="788" height="676" alt="api2" src="https://github.com/user-attachments/assets/ddbdd237-30cb-4cb0-9839-62aa03a5ab08" />
<img width="724" height="669" alt="api1" src="https://github.com/user-attachments/assets/75058508-48d4-4ada-bc86-bc73ead211b1" />
<img width="929" height="876" alt="apis" src="https://github.com/user-attachments/assets/322009b3-e975-4d6c-88c5-683d02ef2a5b" />
