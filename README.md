# Customer Purchase Prediction  

## Overview  
Understanding customer behavior is essential for businesses to improve engagement and conversion rates. This project leverages **Machine Learning classification models** to predict whether a customer is likely to purchase a product or not, based on their platform activity and demographics. With a simple and interactive **Flask web application**, users can input customer details and receive instant predictions.  

---

## How It Works  

### Model Development  
- Built a classification model using **Logistic Regression / Random Forest / Gradient Boosting**.  
- Trained on customer data including **Days on Platform, Minutes Watched, Courses Started, Exams Passed, Steps, and Student Country**.  
- Encoded categorical variables using **OrdinalEncoder** and standardized numerical features using **StandardScaler**.  

### Exploratory Data Analysis (EDA)  
- Performed analysis with **histograms, correlation heatmaps, and boxplots**.  
- Identified patterns in user activity and purchase behavior.  

### Data Preprocessing  
- Handled categorical data with **encoding techniques**.  
- Normalized numerical features to improve model performance.  

### Model Optimization  
- Tuned hyperparameters and compared models using **accuracy, precision, recall, and F1-score**.  
- Final model achieved **high accuracy in predicting purchase behavior**.  

### Deployment  
- Deployed the model using **Flask**.  
- Integrated with an **HTML form** where users can enter customer details.  
- Hosted on **Render / Azure / Localhost**.  

---

## How to Use  

1. **Visit the Application**: Open the deployed app in your browser.  
2. **Input Data**: Fill out the form with customer details.  
3. **Submit**: Click *Predict* to send data to the model.  
4. **Get Prediction**: The app will return either:  
   - ✅ **Will Purchase**  
   - ❌ **Will Not Purchase**  

---

## Features  

- **Machine Learning Powered**: Predicts customer purchase intent using ML models.  
- **Preprocessing Pipeline**: Encodes categorical data and scales features.  
- **User-Friendly Interface**: HTML form connected to Flask for easy interaction.  
- **Actionable Insights**: Helps businesses identify potential buyers.  

---

## Example Output  

After submitting customer details, the model may return:  

- **Prediction**: *Will Purchase* ✅  
- or  
- **Prediction**: *Will Not Purchase* ❌  
