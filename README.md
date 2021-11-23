# WeatherCheck

This web app is used to take in a city and give the weather detalis of that city and add it to the city searched till now. Using flask Backend, API- [OpenWeatherAPI](https://openweathermap.org/api) and deployed it on Heroku cloud platform.

Checkout- [Website](https://dp-weathercheck.herokuapp.com/)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python --version 3.9.2(tested on)
* Flask --version 2.0.2(tested on)
* SQLAlchemy
To check your version use below command in the command line
```
flask --version
```
* Requests - Getting the data from the API in json format and parsing it to text format

Note: If any errors faced while hosting just follow the installation guide properly

### Installing

Clone this repository. 
```
git clone git@github.com:dhananjaypai08/WeatherCheck.git
```

Change your directory by locating the WeatherCheck directory and changing it.

Create virtual environment and activate it.
```
virtualenv yourenvironment
yourenvironment/Scripts/activate
```

Install all the necessary packages
```
pip install -r requirements.txt
```

### Documentation
Very simple to use . You just have to type in the city name of which you want to get the weather information about and click add city.

### How to Run
Just type in the below command in the command line
```
python main.py
```
  or 
```
flask run
```
Note: Make sure you are in the WeatherCheck directory in the command line while entering the above command

You will be then provided with a localhost website link for your local build and clicking on that link will redirect you to the web app.
