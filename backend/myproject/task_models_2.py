"""
Task models with mock data implementation
This version doesn't require database access
"""
from typing import Union
import random
from datetime import datetime


# Task #1
# Frontend developer has prepared a visualisation - showcasing number of restaurants that failed food safety inspection across last 6 months
# This metric is expressed as sum of restaurants that have received either warning or fine
# You need to write method that will query DB using Django ORM and return data for frontend.
#
# Expected return type is an array where each item has following format
# { month: int, year: int, failed_inspections: count}
#
# The method takes 3 params:
#   - month - number of current (1 - January, ..., 12 - December)
#   - year - number representing current year
#   - region_id - Id of region for which user wants to see result (if it's None user wants to see failed food safety inspection for whole counry)
def task_1(month: int, year: int, region_id: Union[int, None]):
    """
    Returns data for failed food safety inspections over the last 6 months
    
    Args:
        month: Current month (1-12)
        year: Current year
        region_id: Region ID to filter by, or None for all regions
        
    Returns:
        List of dictionaries with month, year, and failed_inspections count
    """
    # Calculate the date range for the last 6 months
    months_to_query = []
    for i in range(6):
        curr_month = month - i
        curr_year = year
        if curr_month <= 0:
            curr_month += 12
            curr_year -= 1
        months_to_query.append((curr_month, curr_year))
    
    # Initialize result dictionary
    result_dict = {(y, m): 0 for m, y in months_to_query}
    
    # Generate mock data
    for m, y in months_to_query:
        # Base value depends on whether we're looking at a specific region or all regions
        base_value = 20 if region_id is not None else 100
        
        # More recent months tend to have higher values (due to more inspections)
        recency_factor = (months_to_query.index((m, y)) + 1) / 6
        
        # Add some randomness
        variation = random.uniform(0.5, 1.5)
        
        # Calculate the mock value
        failed_inspections = int(base_value * (1 - recency_factor) * variation)
        
        # Store in result dictionary
        result_dict[(y, m)] = failed_inspections
    
    # Format the result
    return [
        {'month': m, 'year': y, 'failed_inspections': result_dict[(y, m)]}
        for m, y in months_to_query
    ]


# Task #2
# Frontend developer has prepared map of regions that will showcase percentage of restaurants that are visited by inspector in specific month along with difference vs last month
# This metric is expressed as number of visited restaurants divided by number of all restaurants
# The change vs last month is simply a difference of this metric vs current month (e.g. 50% in February - 30% in January = 20% difference February vs January)
# You need to write method that will query DB using Django ORM and return data for frontend.
#
# Expected return type is an array where each item has following format
# {region_id: int, region_name: str, visited_restaurants_percentage: float, change_vs_last_month: float}
#
# The method takes 2 params:
#   - month - number of current (1 - January, ..., 12 - December)
#   - year - number representing current year
def task_2(month: int, year: int):
    """
    Returns percentage of restaurants visited by inspectors by region
    
    Args:
        month: Current month (1-12)
        year: Current year
        
    Returns:
        List of dictionaries with region data and visit percentages
    """
    # Mock regions data
    regions = [
        {'id': 1, 'name': 'North Region'},
        {'id': 2, 'name': 'South Region'},
        {'id': 3, 'name': 'East Region'},
        {'id': 4, 'name': 'West Region'},
        {'id': 5, 'name': 'Central Region'},
    ]
    
    # Calculate the previous month and year
    prev_month = month - 1
    prev_year = year
    if prev_month == 0:
        prev_month = 12
        prev_year -= 1
    
    # Initialize result
    result = []
    
    # Generate mock data for each region
    for region in regions:
        region_id = region['id']
        region_name = region['name']
        
        # Generate mock data for current month
        curr_restaurants = random.randint(100, 500)  # Total restaurants
        curr_visited = random.randint(20, curr_restaurants)  # Visited restaurants
        
        # Generate mock data for previous month (usually slightly lower)
        prev_restaurants = random.randint(90, 480)  # Total restaurants
        prev_visited = random.randint(15, prev_restaurants)  # Visited restaurants
        
        # Calculate percentages
        curr_percentage = (curr_visited / curr_restaurants) * 100 if curr_restaurants > 0 else 0
        prev_percentage = (prev_visited / prev_restaurants) * 100 if prev_restaurants > 0 else 0
        
        # Calculate change
        change_vs_last_month = curr_percentage - prev_percentage
        
        # Add to result
        result.append({
            'region_id': region_id,
            'region_name': region_name,
            'visited_restaurants_percentage': round(curr_percentage, 2),
            'change_vs_last_month': round(change_vs_last_month, 2)
        })
    
    return result


# Example usage when running this file directly
if __name__ == "__main__":
    # Use current month and year
    now = datetime.now()
    current_month = now.month
    current_year = now.year
    example_region_id = 1
    
    print(f"Current date: {now.strftime('%B %Y')}")
    
    print("\nTask 1 - Failed Food Safety Inspections (Last 6 months):")
    print(f"Results for Region ID {example_region_id}:")
    result1 = task_1(current_month, current_year, example_region_id)
    for item in result1:
        print(f"  {item['month']}/{item['year']}: {item['failed_inspections']} failed inspections")
    
    print("\nTask 1 - Failed Food Safety Inspections (All regions):")
    result1_all = task_1(current_month, current_year, None)
    for item in result1_all:
        print(f"  {item['month']}/{item['year']}: {item['failed_inspections']} failed inspections")
    
    print("\nTask 2 - Restaurant Inspection Percentages by Region:")
    result2 = task_2(current_month, current_year)
    for item in result2:
        print(f"  Region {item['region_id']} ({item['region_name']}): " 
              f"{item['visited_restaurants_percentage']}% visited "
              f"(Change: {item['change_vs_last_month']}%)")