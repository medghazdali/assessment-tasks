"""
Simple Flask API to serve the task_models_2 data
"""
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from datetime import datetime
import os
from task_models_2 import task_1, task_2

app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    """Serve the dashboard HTML"""
    return send_from_directory('static', 'index.html')

@app.route('/api-docs')
def api_docs():
    """API documentation endpoint"""
    return """
    <html>
        <head>
            <title>Food Safety API</title>
            <style>
                body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
                h1 { color: #333; }
                h2 { color: #555; margin-top: 30px; }
                pre { background: #f5f5f5; padding: 10px; border-radius: 5px; }
                .endpoint { background: #e9f7fe; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
            </style>
        </head>
        <body>
            <h1>Food Safety Inspection API</h1>
            <p>This API provides data about restaurant food safety inspections.</p>
            
            <h2>Available Endpoints:</h2>
            
            <div class="endpoint">
                <h3>1. Failed Food Safety Inspections</h3>
                <p>Get data about restaurants that failed food safety inspections over the last 6 months.</p>
                <p><strong>URL:</strong> /api/failed-inspections</p>
                <p><strong>Method:</strong> GET</p>
                <p><strong>Query Parameters:</strong></p>
                <ul>
                    <li><code>region_id</code> (optional): Filter by region ID</li>
                </ul>
                <p><strong>Example:</strong></p>
                <pre>/api/failed-inspections?region_id=1</pre>
            </div>
            
            <div class="endpoint">
                <h3>2. Restaurant Inspection Percentages</h3>
                <p>Get percentage of restaurants visited by inspectors by region.</p>
                <p><strong>URL:</strong> /api/inspection-percentages</p>
                <p><strong>Method:</strong> GET</p>
                <p><strong>Example:</strong></p>
                <pre>/api/inspection-percentages</pre>
            </div>
        </body>
    </html>
    """

@app.route('/api/failed-inspections')
def failed_inspections():
    """Get failed food safety inspections data"""
    # Get current date
    now = datetime.now()
    current_month = now.month
    current_year = now.year
    
    # Get region_id from query parameters if provided
    region_id = request.args.get('region_id')
    if region_id:
        try:
            region_id = int(region_id)
        except ValueError:
            return jsonify({"error": "Invalid region_id. Must be an integer."}), 400
    else:
        region_id = None
    
    # Get data from task_1
    data = task_1(current_month, current_year, region_id)
    
    return jsonify({
        "data": data,
        "region_id": region_id,
        "description": "Failed food safety inspections over the last 6 months"
    })

@app.route('/api/inspection-percentages')
def inspection_percentages():
    """Get restaurant inspection percentages by region"""
    # Get current date
    now = datetime.now()
    current_month = now.month
    current_year = now.year
    
    # Get data from task_2
    data = task_2(current_month, current_year)
    
    return jsonify({
        "data": data,
        "description": "Restaurant inspection percentages by region"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)