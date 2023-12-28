import numpy as np
from flask import Flask,request,render_template
import pickle

app = Flask(__name__)

# Mapping for Employment Type values
employment_type_mapping = {
    "Full Time": 0,
    "Part Time": 1,
    "Contract": 2,
}

# company_type_mapping = {
#     "Small Scale": 1,
#     "Medium Scale": 0,
#     "Large Scale": 2,
# }

job_title_type_mapping = {
    "Data Scientist": 0,
    "Data Engineer": 1,
    "Data Analyst": 2,
    "Machine Learning Engineer": 3,
    "Software Developer": 4,
}

company_location_type_mapping = {
    "USA": 0,
    "Non USA": 1,
}

employee_residence_type_mapping = {
    "USA": 0,
    "Non USA": 1,
}

#model = pickle.load(open('linear_regression_model.pickle','rb'))
model = pickle.load(open('new_linear_regression_model.pickle','rb'))

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)
    # #output = round(prediction[0])
    # return render_template('index.html',prediction_text = 'Salary Should be  $ {}'.format(prediction))
    
    # Extracting values from the form
    experience_level = int(request.form['experience_level'])
    employment_type = int(request.form['employment_type'])
    job_title = int(request.form['job_title'])
    employee_residence = int(request.form['employee_residence'])
    company_location = int(request.form['company_location'])
    #company_size = int(request.form['company_size'])

    # Mapping dropdown value to numeric value
    numeric_employment_type = employment_type_mapping.get(str(employment_type), -1)

    #numeric_company_type = company_type_mapping.get(str(employment_type), -1)

    numeric_job_title_type = job_title_type_mapping.get(str(employment_type), -1)

    numeric_company_location_type = company_location_type_mapping.get(str(company_location), -1)

    numeric_employee_residence_type = employee_residence_type_mapping.get(str(company_location), -1)

    # Combine all features into a list
    features = [experience_level, numeric_employment_type,numeric_company_location_type,numeric_employee_residence_type, numeric_job_title_type]

    # Convert the features list to a numpy array for prediction
    final_features = np.array(features).reshape(1, -1)

    # Assuming 'model' is your trained machine learning model
    prediction = model.predict(final_features)
    formatted_prediction = "${:,.2f}".format(prediction[0])

    return render_template('index.html', prediction_text='Salary Should be $ {}'.format(formatted_prediction))

if __name__ == "__main__":
    app.run(port = 5000, debug = True)