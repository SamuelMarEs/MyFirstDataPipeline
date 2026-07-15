#!\bin\bash
# This bash script downoalds two data sets directly from kaggle.

# Confirms if a Data folder exists. If not, it creates one.
if [ -d "Data/" ]; then
	echo "Data exists"
	cd Data
else
	echo "Data doesn't exists. Creating Data/"
	mkdir Data
	cd Data
fi

# Checks if the data sets are already in the Data folder.
# If not, it downloads them.

# NYC weather data set
if [ -f "NYC_Weather_2016_2022.csv" ]; then
	echo ".csv is already unziped"
elif [ -f "nyc-weather-2016-to-2022.zip" ]; then
	echo ".zip already exists, but not extracted. Extracting .csv"
	unzip nyc-weather-2016-to-2022.zip
else
	echo "Downloading raw .zip file"
	kaggle datasets download aadimator/nyc-weather-2016-to-2022
	echo "Extracting .csv"
	unzip nyc-weather-2016-to-2022.zip
fi

# NYC taxi duration data set
if [ -f "NYC.csv" ]; then
        echo ".csv is already unziped"
elif [ -f "nyc-taxi-trip-duration.zip" ]; then
        echo ".zip already exists, but not extracted. Extracting .csv"
        unzip nyc-taxi-trip-duration.zip
else
        echo "Downloading raw .zip file"
        kaggle datasets download yasserh/nyc-taxi-trip-duration
        echo "Extracting .csv"
        unzip nyc-taxi-trip-duration.zip
fi
