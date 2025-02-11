# 🌿 Automated Plant Disease Recognition Using Machine Learning

## 🔍 Overview
This project detects plant diseases using a **Convolutional Neural Network (CNN)**. The model is trained on labeled plant images and can classify them as healthy or diseased. A **Streamlit-based GUI** provides an interactive interface for users.

## 🚀 Features
- **Deep Learning Model:** A CNN for image classification.
- **Image Preprocessing:** Normalization, augmentation, and resizing.
- **User-friendly Interface:** Built with Streamlit.
- **Real-time Diagnosis:** Upload an image and get predictions.

## 💁️ Dataset
The dataset consists of healthy and diseased plant images. Data augmentation and normalization techniques are applied.

## 🛠️ Technologies Used
- **Python** - For scripting and modeling.
- **TensorFlow/Keras** - For building the CNN.
- **OpenCV & PIL** - For image processing.
- **NumPy & Pandas** - For data handling.
- **Jupyter Notebook** - For running the model.
- **Streamlit** - For the graphical interface.

## 🎯 Installation Guide
### 🔹 Prerequisites
Install required dependencies:
```bash
pip install tensorflow streamlit opencv-python numpy pandas pillow matplotlib
```

### 🔹 Clone the Repository
```bash
git clone https://github.com/anshikarawat07/plant-disease-detection.git
cd plant-disease-detection
```

## 🚦 Usage
### 1️⃣ Open and Run the Model in Jupyter Notebook
Open the `Train_plant_disease.ipynb` file in Jupyter Notebook and run the cells sequentially to train the model.

### 2️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## 📊 Model Performance
The CNN model is trained with a target accuracy of **90%+**. Evaluation metrics include accuracy, precision, recall, and loss.

