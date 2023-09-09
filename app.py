
from flask import Flask, render_template
import pandas as pd
import csv

app = Flask(__name__)

# Function to calculate the percentage for churn values
def calculate_percentage(churn_0_count, churn_1_count):
    total = churn_0_count + churn_1_count
    percentage_0 = (churn_0_count / total) * 100
    percentage_1 = (churn_1_count / total) * 100
    return percentage_0, percentage_1

# Route to generate dynamic HTML
@app.route('/')
def dynamic_html():
    # Initialize variables to count churn values
    churn_0_count = 0
    churn_1_count = 0

    # Open the CSV file
    with open('data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Iterate through rows and count churn values
        for row in reader:
            churn_value = int(row['Churn'])
            if churn_value == 0:
                churn_0_count += 1
            elif churn_value == 1:
                churn_1_count += 1

    # Calculate percentages
    percentage_0, percentage_1 = calculate_percentage(churn_0_count, churn_1_count)

    # Render the HTML template with embedded Python variables
    return render_template('index.html', percentage_0=percentage_0, percentage_1=percentage_1)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
