import streamlit as st
import tensorflow as tf
import numpy as np

#Tensor Model Prediction

def model_prediction(test_image):
    model = tf.keras.models.load_model('trained_model.keras')
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to a batch
    predictions = model.predict(input_arr)
    result_index = np.argmax(predictions) #Maximam index of best probable result
    return result_index

#Sidebar
st.sidebar.title('Dashboard')
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Classifier"])

#Home Page
if (app_mode=="Home"):
    st.header("Plamt disease recognition app")
    st.markdown("""
                Welcome to this cool app     
                ###How it works
                """)
elif(app_mode=="About"):
    st.header("About")
    st.markdown(""" ###Tell me more""")


elif(app_mode=="Disease Classifier"):
    st.header("Predictor")
    test_image = st.file_uploader("Choose an Image")
    if (st.button("Show Image")):
        st.image(test_image, use_container_width=True)
    #Predict button
    if(st.button("Predict")):
        #with st.spinner("In progress..."): 
        st.balloons()
        st.write("Out prediction is that ")
        result_index = model_prediction(test_image)  
        #Define Class
        class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
    
        st.success("Model is predicting that it is a {}".format(class_name[result_index]) )
        st.snow()