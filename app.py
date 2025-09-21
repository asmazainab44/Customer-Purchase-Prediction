from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

# Load trained model, encoder, and scaler
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

app = Flask(__name__)

# Prediction mapping
purchase_mapping = {
    0: "Will Not Purchase",
    1: "Will Purchase"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        days_on_platform = float(request.form['days_on_platform'])
        minutes_watched = float(request.form['minutes_watched'])
        courses_started = float(request.form['courses_started'])
        practice_exams_passed = float(request.form['practice_exams_passed'])
        minutes_spent_on_exams = float(request.form['minutes_spent_on_exams'])
        student_country = request.form['student_country']

        # Encode student_country safely using a new variable
        try:
            student_country_enc = encoder.transform(pd.DataFrame({'student_country':[student_country]}))[0][0]
        except:
            # If unknown country, use the most common country from training
            student_country_enc = encoder.transform(pd.DataFrame({'student_country':['USA']}))[0][0]

        # Prepare feature array
        features = np.array([[days_on_platform, minutes_watched, courses_started,
                              practice_exams_passed, minutes_spent_on_exams,
                              student_country_enc]], dtype='float')

        # Scale features
        features_scaled = scaler.transform(features)

        # Make prediction
        prediction = model.predict(features_scaled)
        output = int(prediction[0])
        purchase_label = purchase_mapping.get(output, "Unknown")

        return render_template('index.html', prediction_text=f'Purchase Prediction: {purchase_label}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
