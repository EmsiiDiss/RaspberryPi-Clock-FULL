# Raspberry Pi Temperature Measurement Application

## Description

This Python-based application is designed to measure temperature using the DS18B20 sensor, store it in an SQLite database, and display it on an LCD screen connected to a Raspberry Pi 4 using the I2C interface. Additionally, the application retrieves temperature and weather information from the location of the Raspberry Pi using extreme-ip-lookup.com and api.openweathermap.org.

## Features

1. Temperature measurement using the DS18B20 sensor.
2. Storing the measured temperature in an SQLite database.
3. Fetching location data from extreme-ip-lookup.com.
4. Utilizing api.openweathermap.org to retrieve information about the current temperature and weather in the given location.
5. Displaying data on an LCD screen connected to Raspberry Pi 4 via the I2C interface.

## Requirements

1. Raspberry Pi 4.
2. DS18B20 temperature sensor.
3. LCD screen compatible with Raspberry Pi and I2C interface.
4. Internet access to retrieve weather data.
5. Python packages: sqlite3, smbus (for I2C support), requests (for API data retrieval).

## Installation

1. Connect the DS18B20 sensor and LCD screen to the appropriate ports on Raspberry Pi 4.
2. Install the required Python packages:

   ```bash
   pip install sqlite3 smbus requests
Download the application files.
Run the program by executing the main file main.py.
## Configuration
Configure the I2C interface on Raspberry Pi.
Obtain an API key from api.openweathermap.org.
Ensure the DS18B20 sensor is correctly connected and configured.
Check if the LCD screen is properly connected to the I2C interface.
## Usage
Run the main program file (main.py).
The application will automatically fetch the device location and weather data.
Measure the temperature using the DS18B20 sensor and save it to the database.
Display temperature and weather information on the LCD screen.
## Author
Emsii
5.12.2023





