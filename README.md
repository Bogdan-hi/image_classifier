# Веб-приложение для классификации изображений

Это веб-приложение, построенное с использованием Flask и TensorFlow, для классификации изображений с использованием предобученной модели CIFAR-10. Приложение позволяет пользователям загружать изображение, и оно предсказывает класс изображения из набора данных CIFAR-10.

## Возможности

- Загрузка изображения через веб-интерфейс
- Классификация изображения на основе модели CIFAR-10
- Отображение предсказанного класса и уверенности
- Сохранение истории предсказаний в базе данных SQLite

## Требования

- Python 3.x
- TensorFlow (для машинного обучения)
- Flask (для веб-сервера)
- h5py (для загрузки модели)
- SQLite (для хранения данных)

## Настройка

### Шаг 1: Клонируйте репозиторий

```bash
https://github.com/Bogdan-hi/image_classifier.git
```
### Шаг 2: Создайте и активируйте виртуальное окружение
```bash
python -m venv venv
venv\Scripts\activate
```
### Шаг 3: Установите зависимости
```bash
pip install -r requirements.txt
```
### Шаг 4: Подготовьте модель CIFAR-10
Убедитесь, что предобученная модель CIFAR-10 cifar10_model.h5 находится в директории проекта. Если модели нет, вы можете создать её заново, используя следующий скрипт:
```bash
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import cifar10

# Загрузка данных CIFAR-10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Нормализация данных
x_train, x_test = x_train / 255.0, x_test / 255.0

# Создание модели
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10)
])

# Компиляция модели
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Обучение модели
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# Сохранение модели
model.save('cifar10_model.h5')
```
### Шаг 5: Запустите приложение
```bash
python app.py
```
### Шаг 6: Откройте приложение
Откройте браузер и перейдите по адресу http://127.0.0.1:5000/. Вы можете загрузить изображение, и приложение отобразит предсказанный класс на основе модели CIFAR-10.
### Структура проекта
```bash
image-classifier/
│
├── app.py                  # Главный файл приложения Flask
├── cifar10_model.h5        # Предобученная модель CIFAR-10
├── requirements.txt        # Зависимости Python
├── static/                 # Статические файлы (например, CSS, JS)
│   └── style.css
└── templates/              # HTML-шаблоны
    └── index.html
```
Используемые технологии
Flask: Для создания веб-приложения.
TensorFlow: Для машинного обучения и работы с моделью.
SQLite: Для хранения истории предсказаний.
HTML/CSS/JavaScript: Для фронтенда приложения.
