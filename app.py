# Import Required Modules
from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

wdf = pd.read_csv("CSVFiles/issue_hw_day_07_2023.csv", encoding = "cp949")
#flask --app app run
# Create Home Page Route
app = Flask(__name__)


@app.route('/')
def bar_with_plotly():
    # Students data available in a list of list
    students = [['First', 34, 'Sydney', 'Australia'],
                ['Rithika', 30, 'Coimbatore', 'India'],
                ['Priya', 31, 'Coimbatore', 'India'],
                ['Sandy', 32, 'Tokyo', 'Japan'],
                ['Praneeth', 16, 'New York', 'US'],
                ['Praveen', 17, 'Toronto', 'Canada']]

    # Convert list to dataframe and assign column values
    df = pd.DataFrame(students,
                      columns=['Name', 'Age', 'City', 'Country'],
                      index=['a', 'b', 'c', 'd', 'e', 'f'])

    # Create Bar chart
    fig = px.bar(wdf, x='location', y='average_temp(°C)', color='date')
    print(wdf)
    # Create graphJSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # Use render_template to pass graphJSON to html
    return render_template('bar.html', graphJSON=graphJSON)

print(wdf)
