import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# TensorFlow Model Prediction
def model_prediction(image_file):
    model = tf.keras.models.load_model("train_model.h5")
    image = Image.open(image_file).resize((128, 128))
    image = image.convert("RGB")
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  
    predictions = model.predict(input_arr)
    return predictions  


class_labels = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
    'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
    'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
    'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
    'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
    'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
    'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
    'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
    'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
    'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
    'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
    'Tomato___healthy'
]


st.set_page_config(page_title="Plant Disease Recognition System", page_icon="🌿")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page:", ["Home", "Predictive"])


if page == "Home":
    st.title("🌿 Welcome to Plant Disease Recognition System")
    st.markdown("""
        This system detects plant diseases through image analysis.
        Upload an image of a plant leaf, and the model will predict the disease.
    """)
    st.image("Background.jpg", use_column_width=True)


elif page == "Predictive":
    st.title("🌿 Plant Disease Recognition System")
    test_image = st.file_uploader("Upload an Image of a Plant Leaf:", type=["jpg", "png", "jpeg"])

    if test_image:
        st.image(test_image, caption="Uploaded Image")
        if st.button("Predict"):
            with st.spinner("Analyzing..."):
                predictions = model_prediction(test_image)
                result_index = np.argmax(predictions)
                prediction = class_labels[result_index]
                st.success(f"**Predicted Class:** {prediction}")

