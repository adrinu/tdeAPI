from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.support.ui import Select




app = Flask(__name__)

@app.route("/api", methods = ['GET'])
def API():
    request_goal_info =  str(request.args['findCalories'])

    data = request_goal_info.split(" ")

    isBulk = data[0]
    gender_input = data[1]
    age_input = int(data[2])
    weight_input = int(data[3])
    height_input = data[4]
    activity_input = data[5]
    calories_needed = fillIn(isBulk, gender_input, age_input, weight_input, height_input, activity_input)
    return jsonify(calories_needed)

@app.route("/")
def homescreen():
    info =  '''
        Welcome to tdeAPI, to get started:
        <br/> add /api?findCalories= at then end of the URl
        <br/>
        <br/>

        The API takes in six agruments: <br/>
        <br/>- isBulk, bool -> USE "True" or "False" CASE SENSITIVE
        <br/>- gender_input, string -> USE "male" or "female"; CASE SENSITIVE
        <br/>- age_input, int
        <br/>- weight_input, int -> LBS
        <br/>- height input, int -> INCHES
        <br/>- activity_input, float -> Pick one of these numbers: 1.2, 1.375, 1.55 , 1.725, 1.9

        <br/><br/> Now, to get the data from the API, input these agruments into the url with a space between
        <br/> EXAMPLE: http://127.0.0.1:5000/api?findCalories=TRUE male 19 160 70 1.55
        
        <br/> The API will return a JSON of the caloric goal.
    '''

    return info
def fillIn(isBulk, gender_input, age_input, weight_input, height_input, activity_input):
    browser = webdriver.Chrome()
    browser.get("https://tdeecalculator.net")

    if gender_input == "male":
        whichGender = browser.find_element_by_xpath('//*[@id="male"]')
    else:
        whichGender = browser.find_element_by_xpath('//*[@id="female"]')

    whichGender.click()
    
    
    age = browser.find_element_by_xpath('//*[@id="age"]')
    age.send_keys(age_input)
    
    weight = browser.find_element_by_xpath('//*[@id="weight"]')
    weight.send_keys(weight_input)
  
    height = Select(browser.find_element_by_xpath('//*[@id="height"]'))
    height.select_by_value(height_input)
    

    activity = Select(browser.find_element_by_xpath('//*[@id="form"]/form/table/tbody/tr[5]/td[2]/select'))
    activity.select_by_value(activity_input)
    
    sumbit_button = browser.find_element_by_id('submit')
    sumbit_button.click()
    
    cal = browser.find_element_by_xpath('//*[@id="tdee-cals"]/div[1]/span[1]')
    temp = cal.text
    temp = temp.replace(',','')
    temp = int(temp)
    
    if isBulk is 'False':
        temp -= 500
        return str(temp)
    else:
        temp += 500
        return str(temp)


        
if __name__ == "__main__":
    app.run()
