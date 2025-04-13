
# Breast Cancer Prediction System (Django + Machine Learning)
This web-based application predicts whether a tumor is malignant or benign based on 30 medical features. The project utilizes Django for the web interface and Machine Learning models trained in a Jupyter Notebook. The most accurate model, Random Forest, achieved a prediction accuracy of 97.36%.

-------------------------------------------------------------------------------------------
🚀 Features

Web Interface: Simple and interactive UI where users can input medical features and get predictions.

Prediction Models: Three models are trained to predict breast cancer:

Logistic Regression

Decision Tree

Random Forest (🌟 Best Model with 97.36% Accuracy)

Clear, Color-coded Results: The prediction result is displayed with an easy-to-understand color-coded message and basic advice.

Model Serialization: The trained model is serialized using joblib and loaded in Django views for making predictions.

-------------------------------------------------------------------------------------------

🧠 Models Used

Logistic Regression: Achieved ~96.49% accuracy.

Decision Tree: Achieved ~93.86% accuracy.

Random Forest: 🌟 Best model with ~97.36% accuracy.

All models are trained and evaluated in breast_cancer_prediction.ipynb, and the best model (Random Forest) is saved as model.pkl using joblib.

-------------------------------------------------------------------------------------------
🗂️ Project Structure

breast_cancer_predictor/
│
├── predictor/
│   ├── templates/predictor/
│   │   ├── form.html          # Input form for medical feature inputs
│   │   └── result.html        # Displays the prediction result
        └── base.html   
│   ├── views.py               # Logic to load the model and make predictions
│   └── ...
│
├── model.pkl                  # Trained Random Forest model (saved using joblib)
├── data.csv                   # Breast Cancer Wisconsin Dataset used for training
├── breast_cancer_prediction.ipynb  # Jupyter notebook for model training and evaluation
├── manage.py
└── requirements.txt

-------------------------------------------------------------------------------------------
🛠️ Setup Instructions

1.Clone the Repository:
-git clone https://github.com/your-username/breast_cancer_predictor.git
-cd breast_cancer_predictor

2.Install Dependencies:
-pip install -r requirements.txt

3.Train the Model (if needed):
-Open breast_cancer_prediction.ipynb in Jupyter Notebook.
-Run all cells to train the models.
-Save the best model as model.pkl using joblib.

4.Run the Django Server:
python manage.py runserver


✅ Example Inputs
Each input corresponds to various tumor characteristics such as:
Radius, texture, perimeter, area, smoothness, etc.
These are calculated as the mean, standard error, or worst-case for each feature.

-------------------------------------------------------------------------------------------

📈 Model Evaluation (on Test Set)

Model                  	Accuracy	   Precision (avg)	    Recall (avg)	     F1-score (avg)
Logistic Regression    	96.49%	        0.97	                0.96              0.96
Decision Tree	          93.86%	        0.94	                0.94              0.94
Random Forest 🏆	      97.36%	        0.98	                0.97	            0.97

✅ Best Model: Random Forest Classifier — chosen for deployment due to its highest overall performance.
-------------------------------------------------------------------------------------------
📌 Future Improvements

-Add user authentication for a personalized experience.
-Deploymet.
-Improve UI/UX for better user interaction.
-Add a model comparison dashboard to evaluate model performance.
-------------------------------------------------------------------------------------------
