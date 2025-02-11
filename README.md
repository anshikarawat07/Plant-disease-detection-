<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Plant Disease Detection</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code {
            background: #eee;
            padding: 2px 5px;
            border-radius: 5px;
        }
        pre {
            background: #333;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>🌿 Automated Plant Disease Recognition Using Machine Learning</h1>
    
    <h2>🔍 Overview</h2>
    <p>This project detects plant diseases using a <strong>Convolutional Neural Network (CNN)</strong>. The model is trained on labeled plant images and can classify them as healthy or diseased. A <strong>Streamlit-based GUI</strong> provides an interactive interface for users.</p>
    
    <h2>🚀 Features</h2>
    <ul>
        <li><strong>Deep Learning Model:</strong> A CNN for image classification.</li>
        <li><strong>Image Preprocessing:</strong> Normalization, augmentation, and resizing.</li>
        <li><strong>User-friendly Interface:</strong> Built with Streamlit.</li>
        <li><strong>Real-time Diagnosis:</strong> Upload an image and get predictions.</li>
        <li><strong>Deployable:</strong> Can be hosted on web or mobile platforms.</li>
    </ul>
    
    <h2>📁 Dataset</h2>
    <p>The dataset consists of healthy and diseased plant images. Data augmentation and normalization techniques are applied.</p>
    
    <h2>🛠️ Technologies Used</h2>
    <ul>
        <li><strong>Python</strong> - For scripting and modeling.</li>
        <li><strong>TensorFlow/Keras</strong> - For building the CNN.</li>
        <li><strong>OpenCV & PIL</strong> - For image processing.</li>
        <li><strong>NumPy & Pandas</strong> - For data handling.</li>
        <li><strong>Streamlit</strong> - For the graphical interface.</li>
    </ul>
    
    <h2>🎯 Installation Guide</h2>
    <h3>🔹 Prerequisites</h3>
    <p>Install required dependencies:</p>
    <pre><code>pip install tensorflow streamlit opencv-python numpy pandas pillow matplotlib</code></pre>
    
    <h3>🔹 Clone the Repository</h3>
    <pre><code>git clone https://github.com/YourGitHubUsername/plant-disease-detection.git
cd plant-disease-detection</code></pre>
    
    <h2>🚦 Usage</h2>
    <h3>1️⃣ Train the Model</h3>
    <pre><code>python train.py</code></pre>
    
    <h3>2️⃣ Run the Streamlit App</h3>
    <pre><code>streamlit run app.py</code></pre>
    
    <h2>📊 Model Performance</h2>
    <p>The CNN model is trained with a target accuracy of <strong>90%+</strong>. Evaluation metrics include accuracy, precision, recall, and loss.</p>
    
    <h2>🚀 Future Enhancements</h2>
    <ul>
        <li>🌱 Mobile App Integration</li>
        <li>🔬 Explainable AI for Model Interpretability</li>
        <li>🛰️ Satellite Image Processing for Large-Scale Monitoring</li>
    </ul>
    
    <h2>👩‍💻 Contributing</h2>
    <p>Contributions are welcome! Fork the repo, make changes, and submit a pull request.</p>
    
    <h2>📜 License</h2>
    <p>This project is open-source under the <strong>MIT License</strong>.</p>
</body>
</html>
