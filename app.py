
from flask import render_template, request, json, jsonify,Flask
# from sklearn import preprocessing
# from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd

#create flask instance
app = Flask(__name__)

#decorator to access the app
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

#decorator to access the service
@app.route("/customerchurn", methods=['GET', 'POST'])
def customerchurn():

    #extract form inputs
    Call_Failure = request.form.get("Call_Failure")
    Complaint = request.form.get("Complaint")
    Tenure = request.form.get("Tenure")
    Charge_Amount = request.form.get("Charge_Amount")
    Seconds_of_Use = request.form.get("Seconds_of_Use")
    Frequency_of_use = request.form.get("Frequency_of_use")
    Frequency_of_SMS = request.form.get("Frequency_of_SMS")
    Distinct_Called_Numbers = request.form.get("Distinct_Called_Numbers")
    Age_Group = request.form.get("Age_Group")
    Tariff_Plan = request.form.get("Tariff_Plan")
    Status = request.form.get("Status")
    Age = request.form.get("Age")
    Customer_Value = request.form.get("Customer_Value")




   #convert data to json
    input_data = json.dumps({"Call_Failure": Call_Failure, "Complaint": Complaint, "Tenure": Tenure, "Charge_Amount": Charge_Amount, "Seconds_of_Use": Seconds_of_Use, 
                             "Frequency_of_use": Frequency_of_use, "Frequency_of_SMS": Frequency_of_SMS, "Distinct_Called_Numbers": Distinct_Called_Numbers,
                              "Age_Group": Age_Group, "Tariff_Plan": Tariff_Plan, "Status": Status,"Age": Age,"Customer_Value": Customer_Value})

    #url for bank marketing model
    # url = "http://localhost:8020/api"
    url = "https://customer-churn-mm7i.onrender.com/api"
  
    #post data to url
    results =  requests.post(url, input_data)

    #send input values and prediction result to index.html for display
    return render_template("index.html",  results=results.content.decode('UTF-8'))
  
if __name__ == '__main__':
    app.run(port=4000, debug=True)