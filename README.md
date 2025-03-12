# Image Classifier Web Application

This is a web application built using Flask and TensorFlow to classify images using a pre-trained CIFAR-10 model. The application allows users to upload an image, and it predicts the class of the image from the CIFAR-10 dataset.

## Features

- Upload an image through the web interface
- Image classification based on the CIFAR-10 model
- Displays the predicted class along with the confidence
- Stores prediction history in an SQLite database

## Requirements

- Python 3.x
- TensorFlow (for the machine learning model)
- Flask (for the web server)
- h5py (for loading the model)
- SQLite (for database storage)

## Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/image-classifier.git
cd image-classifier
