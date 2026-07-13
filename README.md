Credit Card Approval Predictor

📌 Project Overview

The Credit Card Approval Predictor is a Machine Learning project that predicts whether a credit card application should be Approved or Rejected based on an applicant's financial and personal details. The goal of this project is to automate the approval process, reduce manual effort, and improve decision-making accuracy for banks and financial institutions.

🎯 Problem Statement

Banks receive thousands of credit card applications every day. Manually reviewing each application is time-consuming and can lead to inconsistent decisions. This project uses Machine Learning to analyze applicant information and predict whether a customer is eligible for a credit card.

✨ Features
Predicts credit card approval status.

User-friendly web interface.

Fast and accurate predictions.

REST API support using Flask.

Easy to deploy and use.

🛠️ Technologies Used

Python

Flask

Scikit-learn

Pandas

NumPy

HTML

CSS

Bootstrap (Optional)

📂 Project Structure

Credit-Card-Approval-Predictor/
│
├── app.py                  # Flask application

├── model.pkl               # Trained ML model

├── scaler.pkl              # Saved scaler

├── requirements.txt

├── README.md
│
├── templates/

│   └── index.html
│
├── static/

│   └── style.css

│
├── dataset/

│   └── credit_card.csv
│
└── notebooks/

    └── model_training.ipynb
📊 Dataset

The dataset contains applicant details such as:

Age

Gender

Annual Income

Employment Status

Credit Score

Existing Loan Amount

Number of Credit Inquiries

Loan-to-Income Ratio

Debt-to-Income Ratio

Other financial attributes

Target Variable

Approved (1)


Rejected (0)

⚙️ Machine Learning Workflow

Collect the dataset.

Clean and preprocess the data.

Handle missing values.

Encode categorical variables.

Scale numerical features.

Split data into training and testing sets.

Train the Machine Learning model.

Evaluate model performance.

Save the trained model using Pickle.

Deploy using Flask.

🤖 Model Used

The project can use one of the following algorithms:

Logistic Regression

Decision Tree

Random Forest

XGBoost (Optional)

Selected Model: Random Forest Classifier (recommended for better accuracy).

🚀 Installation

Clone the repository:

git clone https://github.com/yourusername/Credit-Card-Approval-Predictor.git

Move into the project folder:

cd Credit-Card-Approval-Predictor

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open your browser and visit:

http://127.0.0.1:5000/

💻 How to Use

Open the web application.

Enter applicant details.

Click the Predict button.

The system displays whether the application is Approved or Rejected.

📈 Model Evaluation

Common evaluation metrics include:

Accuracy

Precision

Recall

F1-Score

Confusion Matrix

ROC-AUC Score

📸 Output

Input:

Age: 30

Income: ₹8,00,000

Credit Score: 760

Existing Loan: ₹50,000

Credit Inquiries: 1

Prediction:

✅ Credit Card Approved

🔮 Future Enhancements

Improve prediction accuracy with advanced algorithms.

Deploy on Render, Railway, or Heroku.

Add user authentication.

Store prediction history in a database.

Integrate explainable AI (SHAP/LIME) to show why a prediction was made.

Build a responsive dashboard with charts and analytics.

🤝 Contributing

Contributions are welcome.

Fork the repository.

Create a new branch.

Commit your changes.

Push to your branch.

Open a Pull Request.

⭐ Acknowledgements

Scikit-learn

Flask

Pandas

NumPy

Open Source Machine Learning Community

Sample Requirements (requirements.txt)

Flask

numpy

pandas

scikit-learn

joblib

gunicorn

