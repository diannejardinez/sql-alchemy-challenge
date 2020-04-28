# SQLAlchemy - Surfs Up!

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
	- User is able to specify a date and is returned a JSON list of the minimum temperature, the average temperature, and the max temperature for that specific date from active station USC00519281

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




	