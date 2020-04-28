#Importing Dependecies

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt

from flask import Flask, jsonify

###########################################################

# Database Setup
engine = create_engine("sqlite:////Users/diannejardinez/Desktop/sql-alchemy-challenge/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

###########################################################

# Flask Setup
app = Flask(__name__)

###########################################################

# Flask Routes

@app.route("/")
def welcome():
    return (
        #Listing all available API routes without instructions
        "<h2>Welcome to Surfs Up! Hawaii Climate App</h2>"
        "<p><em>All available api routes without instructions:</em><br>"
        "/api/v1.0/precipitation<br>"
        "/api/v1.0/stations<br>"
        "/api/v1.0/tobs<br>"
        "/api/v1.0/&lt;start&gt;<br>"
        "/api/v1.0/&lt;start&gt;/&lt;end&gt;"
        "<hr>"

        #Listing all available API routes with instructions
         "<p><em>All available api routes with instructions:</em>"
        "<p>Below are a list of all the available API Routes to find: <br> "
        "precipitation recordings, stations, temperature observations<br>(also minimum, average, and maximum temperature observations of specific dates of user's choosing)</li></ul><br>"
        "<p><strong>Instructions:</strong><br>"
        "Add the below endpoint (after each colon ':') to the end of this webpage's url</p>"
        "<strong>Precipitation recordings API Route:</strong> &nbsp;/api/v1.0/precipitation<br>"
        "<strong>Stations API Route:</strong> &nbsp;/api/v1.0/stations<br>"
        "<strong>Temperature observations:</strong> &nbsp;/api/v1.0/tobs<br>"
        "<strong>One date with minimum, average, and maximum temperature observations</strong><br> (replace &lt;start&gt; with a date in the format of yyyy-mm-dd): &nbsp;/api/v1.0/&lt;start&gt;<br>"
        "<strong>Start and end date with minimum, average, and maximum temperature observations</strong><br> (replace &lt;start&gt; and &lt;end&gt; with dates in the format of yyyy-mm-dd): &nbsp;/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

#Return the JSON representation of a dictionary for dates 
#as the key and precipitation as the value from the Precipitation Analysis query
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Query for the last date and the last 12 months for precipitation
    #year ago date: 2016-08-23
    year_ago = dt.date(2017,8, 23) - dt.timedelta(days=365)

    #Query for 2016-2017 dates in measurement table
    #Date range: 08/23/2016 to 08/23/2017 
    precipitation_results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= year_ago).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all precipitation measurements
    all_precipitation_results = []
    for date, prcp in precipitation_results:
        precipitation_results_dict = {}
        precipitation_results_dict["date"] = date
        precipitation_results_dict["prcp"] = prcp
        all_precipitation_results.append(precipitation_results_dict)

    #Return a list of all dates and precipitation
    return jsonify(all_precipitation_results)


#Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query station and station name 
    station_info = session.query(Station.station, Station.name).all()

    session.close()

    # Convert list of tuples into normal list
    station_info_list = list(np.ravel(station_info))

    #Return a list of all information about each station
    return jsonify(station_info_list)


# Return a JSON list of temperature observations (TOBS) for the previous year
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Query for the last date and the last 12 months for temperature observations 
    #(year ago date: 2016-08-23)
    year_ago = dt.date(2017,8, 23) - dt.timedelta(days=365)

    #Query the dates of the most active station from last year for the previous year temperature observations 
    #(date range: 08/23/2016 to 08/23/2017 for station USC00519281)
    tobs_results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= year_ago).all()

    session.close()

    # Convert list of tuples into normal list
    all_tobs_results = list(np.ravel(tobs_results))

    #Return a list of all dates and temperature observations from previous year(08/23/2016 to 08/23/2017) for station USC00519281
    return jsonify(all_tobs_results)


#Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start
@app.route("/api/v1.0/<start>")
def start_date(start):
    #Fetch the minimum temperature, the average temperature, and 
    #the max temperature whose start date matches
    #the path variable supplied by the user

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query to calculate the min, avg, and max Temperatures for a given date in the format %Y-%m-%d
    # When given the start only, calculate TMIN, TAVG, and TMAX for all dates EQUAL to the start date
    # From active station USC00519281
    results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.station == 'USC00519281').\
        filter(func.strftime("%Y-%m-%d", Measurement.date) == start).all()
    
    #For loop and if statement for results query where if user api route date equals query date
    for result in results:
        search_date = start

        if search_date == start:
            #Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start
            return jsonify(result)


#Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    """Fetch the minimum temperature, the average temperature, and 
       the max temperature whose start date and end date matches
       the path variable supplied by the user"""

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query to calculate the min, avg, and max Temperatures for given dates in the format %Y-%m-%d
    # When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive
    # From active station USC00519281
    results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.station == 'USC00519281').\
        filter(func.strftime("%Y-%m-%d", Measurement.date) >= start).\
        filter(Measurement.date <= end).all()
    
    #For loop and if statement for results query where if user api route dates equals query dates
    for result in results:
        search_date1= start
        search_date2 = end

        if search_date1 == start and search_date2 == end:
            #Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range
            return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)



