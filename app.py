# app.py
from flask import Flask, render_template, request, send_file
import os
from ml import predictor, preprocessor
import pandas as pd


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

from statistics import mean, median, stdev
import numpy as np

from statistics import mean, median, stdev
import numpy as np

@app.route('/upload', methods=['POST'])
def upload():
    if 'excel_file' not in request.files:
        return 'No file part'

    file = request.files['excel_file']

    # Assuming 'file' is the Excel file object
    # Load the Excel file into a Pandas DataFrame

    if file.filename == '':
        return 'No selected file'

    if file:
        filename = file.filename
        file.save(os.path.join('uploads', filename)) 
        preprocessor.run(filename) 
        performances = predictor.predict()
        performances_list = performances.tolist()    
        df = pd.read_excel(file)

    # Assuming 'targeted_productivity' is the column name
    # Extract the data from the 'targeted_productivity' column
        targeted_productivity_data = df['targeted_productivity']
        print(targeted_productivity_data)

        # Round performance values to two significant figures
        performances_list_rounded = [round(performance, 2) for performance in performances_list]
        targeted_performance_rounded = [round(performance, 2) for performance in targeted_productivity_data]
        # Calculate statistics
        avg_performance = round(mean(performances_list_rounded), 2)
        median_performance = round(median(performances_list_rounded), 2)
        std_deviation = round(stdev(performances_list_rounded), 2)
        best_teams_indices = np.argsort(performances_list)[-5:][::-1]  # Get indices of top 5 teams in descending order
        worst_teams_indices = np.argsort(performances_list)[:5][::-1]  # Get indices of bottom 5 teams in descending order

        # Pass calculated values to the template
        return render_template('performances.html', excel_data=df.to_html(), performances=performances_list_rounded, targeted_performances= targeted_performance_rounded,
                               avg_performance=avg_performance, median_performance=median_performance,
                               std_deviation=std_deviation, best_teams=best_teams_indices, worst_teams=worst_teams_indices)

@app.route('/download_template')
def download_template():
    template_path = './downloads/template.xlsx'  # Adjust the path to your template file
    return send_file(template_path, as_attachment=True)

@app.route('/tables')
def tables():
    return render_template('tables.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
