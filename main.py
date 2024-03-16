import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from flask import Flask, render_template, request
from matplotlib.lines import Line2D
from sklearn.cluster import KMeans

//TO DISPLAY GRAPH//
def display_graph():
    # Retrieve the selected state, district, and year from the form data
    selected_state = request.form['state']
    selected_district = request.form['district']
    selected_year = request.form['year']

    # Generate the crime graph and get the base64-encoded image data
    graph_data = generate_crime_graph(selected_state, selected_district, selected_year)

    return render_template('index_2.html', selected_state=selected_state,
                           selected_district=selected_district, selected_year=selected_year,
                           graph_data=graph_data)
//YEARLY CRIME RATE//
def yearly_crime_rates():
    # Group the dataset by year and calculate the total crime rates for each year
    yearly_crime_data = dataset.groupby('Year').sum()

    # Create a bar plot of the yearly crime rates
    yearly_crime_data.plot(kind='line', y=['Rape', 'Kidnapping and Abduction'], rot=0)
    plt.xlabel('Year')
    plt.ylabel('Total Crime Rate')
    plt.title('Yearly Crime Rates')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    graph_data = base64.b64encode(img.read()).decode('utf-8')
    plt.close()
    return render_template('index_2.html', graph_data=graph_data)
