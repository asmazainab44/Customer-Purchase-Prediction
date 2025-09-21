# Customer Purchase Prediction  

## Overview  
In today’s digital learning platforms, understanding user behavior is crucial for predicting customer decisions. This project builds a **machine learning model** that predicts whether a customer will make a purchase based on their engagement patterns — such as time spent on the platform, courses started, exams attempted, and geographical location. By analyzing these factors, the project helps uncover insights into customer behavior and identifies key drivers of purchase decisions, which can be valuable for targeted marketing and retention strategies.  

---

## How It Works  

### Exploratory Data Analysis (EDA)  
In the Exploratory Data Analysis (EDA) phase, I visualized the distribution of the target variable purchased, generated KDE plots to observe feature distributions both before and after outlier removal, examined correlations between numerical features using a heatmap, and assessed multicollinearity through the Variance Inflation Factor (VIF).

### Data Preprocessing  
During data preprocessing, I removed extreme outliers to ensure cleaner and more reliable training data, handled missing values in the student_country column by replacing them with "Unknown", encoded categorical features using an OrdinalEncoder, and applied MinMaxScaler to scale all features uniformly.

### Model Development  
Trained and fine-tuned multiple machine learning models—including Logistic Regression, KNN, SVM, Decision Tree, and Random Forest—using GridSearchCV for optimal hyperparameters.

### Model Evaluation  
Evaluated each model using Confusion Matrix, Classification Report (Precision, Recall, F1-score), ROC Curve & AUC Score, and Feature Importance (coefficients or permutation importance). 

---

## Model Optimization  
After hyperparameter tuning and cross-validation, Random Forest was identified as the best-performing model and saved as model.pkl for deployment or future use. 

---

## Deployment  
Although still in prototype stage, the project is ready for deployment using **Flask** , making it possible to build a user-friendly interface where customer data can be input, and predictions can be generated instantly.  

---

## How to Use  
1. **Visit the Application**: https://customer-purchase-prediction-kx9p.onrender.com/
2. **Input Data**: Enter details such as days on platform, minutes watched, courses started, practice exams, and country.  
3. **Submit**: Send your data for analysis.  
4. **Get Prediction**: Instantly receive whether the customer is likely to **Purchase** or **Not Purchase**.  

---
## Features  
- **Comprehensive EDA**: Detailed exploration of dataset structure, patterns, and outliers.  
- **Multiple Models Compared**: Logistic Regression, KNN, SVM, Decision Tree, Random Forest.  
- **Best Model Selection**: Identified Random Forest as the most accurate predictor.  
- **Reusable Model**: Final model is stored as a pickle file (`model.pkl`).  
- **Scalable Approach**: Can easily integrate additional features or larger datasets.  

---

## Example Output  
After entering customer details, the model predicts whether a customer will make a purchase (Will Purchase or Will Not Purchase), helping you identify potential buyers and plan targeted marketing strategies.

---
