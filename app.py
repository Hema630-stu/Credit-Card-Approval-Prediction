from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Ensure model pickle file exists before boot
MODEL_PATH = 'credit_model.pkl'

def load_model_assets():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Missing 'credit_model.pkl' matrix file. Run model_builder.py script to compile training stages first.")
    with open(MODEL_PATH, 'rb') as f:
        return pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
        
    if request.method == 'POST':
        # Load precompiled artifact parameters safely during state handling
        assets = load_model_assets()
        model = assets['model']
        encoders = assets['encoders']
        
        # Capture raw user values via request payload objects
        income = float(request.form['AMT_INCOME_TOTAL'])
        income_type = request.form['NAME_INCOME_TYPE']
        education_type = request.form['NAME_EDUCATION_TYPE']
        family_status = request.form['NAME_FAMILY_STATUS']
        housing_type = request.form['NAME_HOUSING_TYPE']
        employment_years = float(request.form['Employment_Years'])
        age = float(request.form['Age'])
        
        # Fallback safe category encoding matching fit steps to prevent missing key index issues
        def safe_encode(encoder_name, value):
            encoder = encoders[encoder_name]
            if value in encoder.classes_:
                return encoder.transform([value])[0]
            else:
                # Assign default baseline structural fallback class if unmapped edge variables appear
                return encoder.transform([encoder.classes_[0]])[0]

        enc_income_type = safe_encode('NAME_INCOME_TYPE', income_type)
        enc_education_type = safe_encode('NAME_EDUCATION_TYPE', education_type)
        enc_family_status = safe_encode('NAME_FAMILY_STATUS', family_status)
        enc_housing_type = safe_encode('NAME_HOUSING_TYPE', housing_type)
        
        # Build strict numerical arrays matching the trained feature mapping
        # Order: ['AMT_INCOME_TOTAL', 'NAME_INCOME_TYPE', 'NAME_EDUCATION_TYPE', 'NAME_FAMILY_STATUS', 'NAME_HOUSING_TYPE', 'Employment_Years', 'Age']
        input_data = np.array([[
            income, 
            enc_income_type, 
            enc_education_type, 
            enc_family_status, 
            enc_housing_type, 
            employment_years, 
            age
        ]])
        
        # Generate classification inference
        prediction_output = int(model.predict(input_data)[0])
        
        return render_template('result.html', prediction=prediction_output)

if __name__ == '__main__':
    print("Initializing Credit Approval Assessment Engine local runtime environment...")
    app.run(debug=True, port=5000)