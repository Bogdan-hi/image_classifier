from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(255), nullable=False)
    label = db.Column(db.String(50), nullable=False)
    confidence = db.Column(db.Float, nullable=False)

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

def add_prediction(image_path, label, confidence):
    """Добавление предсказания в базу данных"""
    new_pred = Prediction(image_path=image_path, label=label, confidence=confidence)
    db.session.add(new_pred)
    db.session.commit()

def get_predictions():
    """Получение всех предсказаний из базы данных"""
    return Prediction.query.all()
