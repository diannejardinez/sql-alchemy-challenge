# SQLAlchemy - Surfs Up! Analysis

Was treated to a vacation to Honolulu, Hawaii between September 1 to September 7 of 2011. Will be doing some climate analysis on the area during that time period.

**Objectives of the Climate Analysis is to illustrate:**
- SQLAlchemy ORM queries
- Pandas
- Matplotlib
- Flask API

## Climate Analysis and Exploration

### Part 1: Precipitation Analysis
Precipitation Analysis shows the following below:
- SQLAlchemy ORM queries retrieving precipitation data for the last 12 months of the dataset
- Loading queries into a Pandas DataFrame
- Using DataFrame line plot method to plot precipitation data for the dates between 08/23/2016 to 08/23/2017

![](https://github.com/diannejardinez/sql-alchemy-challenge/blob/master/Output_data/Precipitation_Analysis.png)

### Part 2: Station Analysis
Station Analysis shows the following below:
- SQLAlchemy ORM queries retrieving station data of the most active station(Station USC00519281 located in Waihee, HI) and its temperature observation data(TOBS) in the last 12 months of the dataset
- Loading queries into a Pandas DataFrame
- Using DataFrame plot method to plot a histogram for the temperature observations for dates between 08/23/2016 to 08/23/2017 

![](https://github.com/diannejardinez/sql-alchemy-challenge/blob/master/Output_data/Station_Analysis_USC00519281.png)


### Part 3: Climate App
Climate App shows a Flask API based on the queries below:
- Homepage route:
	- Listing all available routes

- `/api/v1.0/precipitation` route:
	- Returning a JSON representation of a dictionary of dates and precipitation values for all stations from precipitation data for the dates between 08/23/2016 to 08/23/2017

- `/api/v1.0/stations` route:
	- Returning a JSON list of stations with station and station name from the dataset

- `/api/v1.0/tobs` route:
	- Returning a JSON list of temperature observations(TOBS) for the previous year of the most active station last year
	(Date range: 08/23/2016 to 08/23/2017 for active station USC00519281 located in Waihee, HI)
	
- `/api/v1.0/<start>` route:
	- User is able to specify a date and is returned a JSON list of the minimum temperature, the average temperature, and the max temperature for all dates greater than and equal to the start date from active station USC00519281

- `/api/v1.0/<start>/<end>` route:
	- User is able to specify a start and end date and is returned a JSON list of the minimum temperature, the average temperature, and the max temperature for that specific date range from active station USC00519281


## Bonus: Other Recommended Analyses

### Temperature Analysis I
Temperature Analysis I shows the following below:
- Identifies the average temperature in June and December at all stations across all available years in the dataset

- Conduct an unpaired independent t-test for two independent datasets to determine if there is a statistical difference between temperature means between June and December. 
![](https://github.com/diannejardinez/sql-alchemy-challenge/blob/master/Output_data/Bonus_TempAnI_tobs_JunDec_sctrplt.png)


*After completing test, and assuming a 5% significant level, we received a p value of 4.193529835915755e-187 so the Null Hypothesis is rejected and the Alternative Hypothesis is accepted. This means that there is a meaningful and statistically significant difference in temperatures between June and December.*



### Temperature Analysis II
Temperature Analysis II shows the following below:
- SQLAlchemy ORM queries to calculate the minimum, average, and maximum temperatures for the previous year of trip dates (previous year range: 09/01/2010 to 09/07/2010)
- Loading queries into a Pandas DataFrame
- Using DataFrame bar plot method with an error bar for the average temperature observations for dates between 09/01/2010 to 09/07/2010

![](https://github.com/diannejardinez/sql-alchemy-challenge/blob/master/Output_data/Bonus_TempAnII_avetemp.png)


### Daily Rainfall Average
- SQLAlchemy ORM queries to calculate precipitation for all stations in the dataset for the previous year of trip dates (previous year range: 09/01/2010 to 09/07/2010)
- SQLAlchemy ORM queries to calculate the the daily minimum, average, and maximum temperatures for the trip dates between 09/01/2011 to 09/07/2011
- Loading 09/01/2011 to 09/07/2011 queries into a Pandas DataFrame
- Using DataFrame area plot method for the minimum, average, and maximum temperatures for the trip dates between 09/01/2011 to 09/07/2011

![](https://github.com/diannejardinez/sql-alchemy-challenge/blob/master/Output_data/Bonus_RainfallAve_dailytemp_areaplt.png)


---
# SQLAlchemy - Surfs Up! Instructions

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.

## Step 1 - Climate Analysis and Exploration

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.


* Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.

* Use SQLAlchemy `create_engine` to connect to your sqlite database.

* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

### Precipitation Analysis

* Design a query to retrieve the last 12 months of precipitation data.

* Select only the `date` and `prcp` values.

* Load the query results into a Pandas DataFrame and set the index to the date column.

* Sort the DataFrame values by `date`.

* Plot the results using the DataFrame `plot` method.


* Use Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Design a query to calculate the total number of stations.

* Design a query to find the most active stations.

  * List the stations and observation counts in descending order.

  * Which station has the highest number of observations?

  * Hint: You may need to use functions such as `func.min`, `func.max`, `func.avg`, and `func.count` in your queries.

* Design a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filter by the station with the highest number of observations.

  * Plot the results as a histogram with `bins=12`.



- - -

## Step 2 - Climate App

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

* Use Flask to create your routes.

### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Return the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the most active station for the last year of data.
  
  * Return a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

## Hints

* You will need to join the station and measurement tables for some of the queries.

* Use Flask `jsonify` to convert your API data into a valid JSON response object.

- - -

## Bonus: Other Recommended Analyses

* The following are optional challenge queries. These are highly recommended to attempt, but not required for the homework.

### Temperature Analysis I

* Hawaii is reputed to enjoy mild weather all year. Is there a meaningful difference between the temperature in, for example, June and December?

* You may either use SQLAlchemy or pandas's `read_csv()` to perform this portion.

* Identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature.

* Use the t-test to determine whether the difference in the means, if any, is statistically significant. Will you use a paired t-test, or an unpaired t-test? Why?

### Temperature Analysis II

* The starter notebook contains a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.

* Use the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year (i.e., use "2017-01-01" if your trip start date was "2018-01-01").

* Plot the min, avg, and max temperature from your previous query as a bar chart.

  * Use the average temperature as the bar height.

  * Use the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).



### Daily Rainfall Average

* Calculate the rainfall per weather station using the previous year's matching dates.

* Calculate the daily normals. Normals are the averages for the min, avg, and max temperatures.

* You are provided with a function called `daily_normals` that will calculate the daily normals for a specific date. This date string will be in the format `%m-%d`. Be sure to use all historic TOBS that match that date string.

* Create a list of dates for your trip in the format `%m-%d`. Use the `daily_normals` function to calculate the normals for each date string and append the results to a list.

* Load the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Use Pandas to plot an area plot (`stacked=False`) for the daily normals.


### Copyright

Trilogy Education Services © 2019. All Rights Reserved.

	