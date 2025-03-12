import os
import uuid
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from classifier import classify_image
from database import db, init_db, add_prediction, get_predictions 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///predictions.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

if not os.path.exists("uploads"):
    os.makedirs("uploads")

app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "gif"}  # Разрешенные форматы
# Инициализируем базу данных с привязкой к Flask-приложению
UPLOAD_FOLDER = "static/uploads"  # Папка для загрузки изображений
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Создаём папку, если её нет
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER  #  Добавляем в конфиг
init_db(app)

@app.route("/history")
def history():
    predictions = get_predictions()  #  Используем функцию
    return render_template("history.html", predictions=predictions)
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

@app.route("/")
def index():
    return render_template("index.html", history=get_predictions())

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        unique_filename = str(uuid.uuid4()) + "_" + filename
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], unique_filename)
        file.save(file_path)

        label, confidence = classify_image(file_path)
        add_prediction(file_path, label, confidence)

        return jsonify({"filename": unique_filename, "label": label, "confidence": confidence})

    return jsonify({"error": "Invalid file type"})

if __name__ == "__main__":
    app.run(debug=True)
