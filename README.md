# SQLAlchemy - Surfs Up!

Being treated to a vacation to Honolulu, Hawaii between September 1 to September 7. Will be doing some climate analysis on the area.

**Objectives of the Research Project is to illustrate**
- SQLAlchemy ORM queries
- Pandas
- Matplotlib
- Flask API

Climate Analysis and Exploration
**Part 1: Precipitation Analysis**
Precipitation Analysis shows the following below:
- SQLAlchemy ORM queries retrieving precipitation data for the last 12 months
- Loading queries into a Pandas DataFrame
- Using DataFrame line plot method to plot precipitation data for the dates between  08/23/2016 to 08/23/2017

![](https://github.com/diannejardinez/sql-alchemy-challenge/blob/master/Output_data/Precipitation_Analysis.png)

**Part 2: Station Analysis**
Station Analysis shows the following below:
- SQLAlchemy ORM queries retrieving station data of the most active station(Station USC00519281 located in Waihee, HI) and its temperature observation data(TOBS) in the last 12 months
- Loading queries into a Pandas DataFrame
- Using DataFrame plot method to plot a histogram for the temperature observations for dates between 08/23/2016 to 08/23/2017 
![](https://github.com/diannejardinez/sql-alchemy-challenge/blob/master/Output_data/Station_Analysis_USC00519281.png)


**Part 3: Climate App**
Climate App shows a Flask API based on the queries below:
- Homepage route:
	-Listing all available routes

- `/api/v1.0/precipitation` route:
	- Returning a JSON representation of a dictionary of dates and precipitation values for all stations from the dataset

- `/api/v1.0/stations` route:
	- Returning a JSON list of stations from the dataset

- `/api/v1.0/tobs` route:
	- Returning a JSON list of temperature observations(TOBS) for the previous year of the most active station last year(Date range: 2015-08-24 to 2016-08-23 for active station USC00519397 located in Waikiki, HI)
	
- `/api/v1.0/<start>` route:
	- User is able to specify a date and is returned a JSON list of the minimum temperature, the average temperature, and the max temperature for that specific date

- `/api/v1.0/<start>/<end>` route:
	- User is able to specify a start and end date and is returned a JSON list of the minimum temperature, the average temperature, and the max temperature for that specific date range

	