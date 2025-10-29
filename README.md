# 🎓 Student Performance Predictor  

An interactive **Machine Learning web app** built with **Streamlit** that predicts a student’s final grade (G3) based on academic and personal attributes.  


---

## 📊 Dataset  

The dataset used for model training was taken from Kaggle: https://www.kaggle.com/datasets/alejandraalvarado/student-mat 

It includes features such as study time, absences, health, and previous grades (G1, G2), which are used to predict the final grade (G3).

---

## 🚀 Features  

-  Predicts **final student grade (G3)** on a 0–20 scale  
-  Displays **Pass / Fail** status dynamically  
-  Custom modern **Streamlit UI** with CSS styling  
-  **Interactive Plotly graphs** for results visualization  
-  Offers **improvement tips** based on the predicted score  
-  **Model saved as a Pickle file** for quick loading  


---

## 🧰 Tech Stack
  
- Python 3.10+: Core programming language used for the project

- Pandas: For loading, cleaning, and managing the dataset

- NumPy: For creating and handling numerical arrays

- Scikit-learn (sklearn): Used for building and training the LinearRegression model, and for data splitting (train_test_split)

- Matplotlib: For visualizing the model performance using “Actual vs Predicted” graphs

- Streamlit: For building the interactive web interface to deploy the model

- Pickle: For saving and loading the trained machine learning model

---

## 🧩 How It Works  

1. **Data Preprocessing**  
   - Loaded the Kaggle dataset and handled missing values.  
   - Encoded categorical features and normalized numeric ones.  

2. **Model Training**  
   - Implemented a Linear Regression model using Scikit-learn.  
   - Split the dataset using `train_test_split`.  
   - Saved the trained model as `model.pkl` using Pickle.  

3. **Frontend Integration**  
   - Built an interactive web app (`app.py`) using Streamlit.  
   - Loaded the model and generated predictions dynamically.  

4. **Prediction Output**  
   - Displays predicted grade (G3).  
   - Shows actual vs predicted graph using Matplotlib.  
   - Provides performance feedback. 

---
 

