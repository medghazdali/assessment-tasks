"""
Demonstration of the task models with mock data
This version doesn't require database access
"""
from typing import Union
from datetime import datetime, timedelta


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
    
    # Mock data - generate random values
    # In real implementation, this would query the database
    result = []
    import random
    
    for month_val, year_val in months_to_query:
        # Generate random data - higher for recent months
        base_value = 100 if region_id is None else 20
        recency_factor = 1 + (0.2 * i)  # More recent months have higher values
        
        failed_inspections = int(random.randint(
            int(base_value / recency_factor / 2),
            int(base_value / recency_factor * 2)
        ))
        
        result.append({
            'month': month_val,
            'year': year_val,
            'failed_inspections': failed_inspections
        })
    
    return result


def task_2(month: int, year: int):
    """
    Returns percentage of restaurants visited by inspectors by region
    
    Args:
        month: Current month (1-12)
        year: Current year
        
    Returns:
        List of dictionaries with region data and visit percentages
    """
    # Mock data - generate regions with random values
    import random
    
    # Create mock regions
    regions = [
        {'id': 1, 'name': 'North Region'},
        {'id': 2, 'name': 'South Region'},
        {'id': 3, 'name': 'East Region'},
        {'id': 4, 'name': 'West Region'},
        {'id': 5, 'name': 'Central Region'},
    ]
    
    result = []
    
    for region in regions:
        # Generate random percentages for current and previous month
        curr_percentage = random.uniform(20, 80)
        # Previous month usually lower by 0-20%
        prev_percentage = max(0, curr_percentage - random.uniform(0, 20))
        
        result.append({
            'region_id': region['id'],
            'region_name': region['name'],
            'visited_restaurants_percentage': round(curr_percentage, 2),
            'change_vs_last_month': round(curr_percentage - prev_percentage, 2)
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