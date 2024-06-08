from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

model_path = "C:/Users/Hasbi/Desktop/skripsi_gpu/skripsi/Skripsi_UI/Hasbi-Coffee-Bean-99.37.keras"
model = load_model(model_path, compile=False)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    img_file = request.files.get("image")
    if img_file:
        img_path = os.path.join("images", img_file.filename)
        img_file.save(img_path)
        img = load_img(img_path, target_size=(224, 224))
        x = img_to_array(img)
        x = np.expand_dims(x, axis=0)
        predictions = model.predict(x)
        predicted_class_index = np.argmax(predictions, axis=1)[0]
        class_names = ["Dark", "Green", "Light", "Medium"]
        prediction = class_names[predicted_class_index]
        return render_template("index.html", prediction=prediction)
    return render_template("index.html", prediction="Tidak ada file yang diunggah")


if __name__ == "__main__":
    app.run(debug=True)
