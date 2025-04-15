# predictor/views.py
from django.shortcuts import render
import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'model.pkl')
model = joblib.load(model_path)


feature_names = [
    "mean_radius", "mean_texture", "mean_perimeter", "mean_area", "mean_smoothness",
    "mean_compactness", "mean_concavity", "mean_concave_points", "mean_symmetry", "mean_fractal_dimension",
    "se_radius", "se_texture", "se_perimeter", "se_area", "se_smoothness",
    "se_compactness", "se_concavity", "se_concave_points", "se_symmetry", "se_fractal_dimension",
    "worst_radius", "worst_texture", "worst_perimeter", "worst_area", "worst_smoothness",
    "worst_compactness", "worst_concavity", "worst_concave_points", "worst_symmetry"
]

def index(request):
    if request.method == "POST":
        inputs = [float(request.POST.get(f)) for f in feature_names]
        prediction = model.predict([inputs])[0]

        if prediction == 1:
            message = {
                "label": "Malignant (Cancerous)",
                "color": "danger",
                "advice": "⚠️ Please contact a healthcare provider immediately."
            }
        else:
            message = {
                "label": "Benign (Non-cancerous)",
                "color": "success",
                "advice": "✅ Good news! But please follow up with your doctor for confirmation."
            }

        return render(request, "predictor/result.html", {"message": message})

    return render(request, "predictor/form.html", {"features": feature_names})
