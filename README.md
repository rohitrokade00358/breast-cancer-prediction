# 🧬 Breast Cancer Prediction System (Django + Machine Learning)

This web-based application predicts whether a tumor is **malignant** or **benign** using 30 medical features. It integrates **Django** for the web interface and **machine learning** models trained in a Jupyter Notebook. The top-performing model, **Random Forest**, reached **97.36%** accuracy and is deployed in the system.

🌐 **Live Demo**: [https://breast-cancer-prediction-kxqc.onrender.com](https://breast-cancer-prediction-kxqc.onrender.com)

---

## 🚀 Features

- **Web Interface**  
  Simple and user-friendly interface where users input tumor-related metrics to receive real-time predictions.

- **Multiple ML Models**  
  Trains and compares three models:
  - Logistic Regression  
  - Decision Tree  
  - 🌟 Random Forest (best performing model)

- **Color-coded Results**  
  Predictions are visually highlighted with clear messages and basic medical advice.

- **Serialized ML Model**  
  Uses `joblib` to save and load the best model (`model.pkl`) inside Django views.

---

## 🧠 Model Evaluation (on Test Set)

| Model                | Accuracy   | Precision (avg) | Recall (avg) | F1-score (avg) |
|---------------------|------------|-----------------|--------------|----------------|
| Logistic Regression | 96.49%     | 0.97            | 0.96         | 0.96           |
| Decision Tree       | 93.86%     | 0.94            | 0.94         | 0.94           |
| 🏆 Random Forest     | **97.36%** | 0.98            | 0.97         | 0.97           |

✅ **Best Model:** Random Forest Classifier — selected for deployment due to its top performance across all metrics.

---

## 🗂️ Project Structure

```bash
breast_cancer_predictor/
├── predictor/                  # Django app folder
│   ├── templates/predictor/    # HTML templates for the web app
│   │   ├── form.html           # Input form
│   │   └── result.html         # Display result
│   ├── views.py                # Django views (Python code)
│   ├── models.py               # Django models (Python code)
│   ├── urls.py                 # URL routing (Python code)
│   └── static/                 # Static files (CSS, JS, etc.)
│
├── model.pkl                   # Serialized machine learning model (from joblib)
├── breast_cancer_prediction.ipynb  # Jupyter notebook (model training)
├── manage.py                   # Django manage script (Python code)
├── requirements.txt            # Python dependencies
├── .gitignore                  # Ignore unnecessary files
└── README.md                   # Project description
```

---
## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/rohitrokade00358/breast-cancer-prediction.git
cd breast_cancer_predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train Model (Optional)

- Open `breast_cancer_prediction.ipynb`
- Run all cells to retrain models
- Save the best model using:

```python
import joblib
joblib.dump(model, 'model.pkl')
```

### 4. Run Django Server (Locally)

```bash
python manage.py runserver
```

Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to use the application.

---

## ☁️ Deployment on Render

### 1. Add a `Procfile`

In the root directory of your project, create a file named `Procfile` with the following content:

```
web: gunicorn breast_cancer_predictor.wsgi:application
```

This tells Render to use Gunicorn as the WSGI server to run your Django application.

### 2. Create a `build.sh` Script

Also, in the root directory, create a file named `build.sh` with the following content:

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# Create a superuser (optional)
# python manage.py createsuperuser --no-input
```

Make sure to give execute permissions to this script:

```bash
chmod +x build.sh
```

This script ensures that every time you deploy, Render will install your dependencies, collect static files, and apply any database migrations.

### 3. Deploy on Render

Once you've added these files:

1. Push your changes to your GitHub repository.
2. In the Render dashboard, create a new web service and link it to your repository.
3. Set the **Build Command** to `./build.sh`.
4. Set the **Start Command** to `gunicorn breast_cancer_predictor.wsgi:application`.

Render will automatically detect these configurations and deploy our application accordingly.

---

## ✅ Example Input Features

Each of the 30 input features represents tumor characteristics such as:

- **Radius**, **Texture**, **Perimeter**, **Area**, **Smoothness**, etc.
- Calculated as **mean**, **standard error**, or **worst-case (max)** values.

These features come from the Breast Cancer Wisconsin dataset.

---

## 📌 Future Improvements

- Add user authentication
- Improve UI/UX design
- Deploy on cloud platforms 
- Add a model comparison dashboard
- Containerize the project using Docker

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) — free to use, modify, and distribute with attribution.

---


## 🙌 Acknowledgments

- Scikit-learn team for machine learning utilities
- Django community for the robust web framework
- UCI for the Breast Cancer dataset

---

