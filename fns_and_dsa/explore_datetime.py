from datetime import datetime
from datetime import timedelta


    
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)


def calculate_future_date():
    try:
        days = int(input("Enter number of days to add: "))
        future_date = datetime.now() + timedelta(days=days)
        print("Future Date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Please enter a valid integer.")

# Run Part 2
calculate_future_date()
 