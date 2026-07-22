# My first data pipeline project
The project consists on a data pipeline, starting from the downloading of the raw data sets from [Kaggle](https://www.kaggle.com/), until the data is ready for use.


### Data sets
The first data set used is the [NYC Taxi Trip Duration](https://www.kaggle.com/datasets/yasserh/nyc-taxi-trip-duration), which contains yellow cab trip records from 2016 in New York City.

The second data set used is [NYC Weather - 2016 to 2022](https://www.kaggle.com/datasets/aadimator/nyc-weather-2016-to-2022), containing hourly weather information in New York City, starting from 2016 to 2022.

The zipped data sets are already available in the [Data](Data/) folder, but the project is made so that it downlads them if they don´t exist already.

### Setup
The project uses *Python 3.14.4* and *Bash*, and is runed in Windows 11 using a bash terminal.
#### Enviornment
In order to set up the enviornment, use the following commands. The commands may differ based on the operating system. First, we create the enviornment as follows:
```bash
python -m venv env
```
After creating the enviornment, we need to activate it with the following command
```bash
source env/Scripts/activate
```
Lastly, we need to install the required librarys directly from the [requirements.txt](requirements.txt) file:
```bash
pip install -r requirements.txt
```
And we can use the following command to determine if the librarys were installed correctly. The required ones are Pandas and SQLalchemy.
```bash
pip list
```

### Execution
In order to execute the full pipeline, the only command needed is
```bash
bash Execute-Pipeline.sh
``` 
This will download and unzip the data sets from [Kaggle](https://www.kaggle.com/) into the [Data](Data/) folder, load them into Pandas DataFrames via the [LoadData.py](LoadData.py) script, which also creates a data base and uploads them as tables. Lastly, the code joins the tables based on **date-time** and exports the result as *taxi_trips.csv*, containing all the data from the [NYC Taxi Trip Duration](https://www.kaggle.com/datasets/yasserh/nyc-taxi-trip-duration) data set, plus the weather conditions at the time.

