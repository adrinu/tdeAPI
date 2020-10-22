# tdeAPI
A Python API to fill in the info in https://tdeecalculator.net/ and return the value of a user's caloric goal.

## Purpose
Get a user's calories needed to achieve their goal for fitME application: https://github.com/adrinu/FitME


## Get Started
* Import Flask & Selenium
* Download Chromedriver and place it either in System32 or include the PATH in Environmental Variables


## Using the API
* Run the application.py file
* In your perferable browser, type in http://127.0.0.1:5000 in the URL
* Add /api?findCalories= at then end of the URl


<br />The API takes in 6 parameters:
<br />string isBulk : Use "True" or "False" ( Case Sensitive )
<br />string gender : Use "male" or "female" ( Case Sensitive )
<br />int age
<br />int weight : Use pounds (lbs)
<br />int height: Use inches (in)
<br />int activity : Use these values -> 1.2, 1.375, 1.55 , 1.725, 1.9 (From Least Active to Very Active)

* To get the data from the API, add these parameters into the URL with a space between
* The return data is jsonified.

## Example
http://127.0.0.1:5000/api?findCalories=TRUE male 19 160 70 1.55
RETURN: 3208


## Upcoming Features 
* Scrape https://www.eatthismuch.com/ to get recipes based on how much calories the user needs to achieve their goal
