# 🎓 Student Performance Predictor  

An interactive **Machine Learning web app** built with **Streamlit** that predicts a student’s final grade (G3) based on academic and personal attributes.  

---

## 🚀 Features  

-   Predicts **final student grade (G3)** on a 0–20 scale  
-   Displays **Pass / Fail** status dynamically  
-   Custom modern **Streamlit UI** with CSS styling  
-   **Interactive Plotly graphs** for results visualization  
-   Offers **improvement tips** based on the predicted score  
-   **Model saved as a Pickle file** for quick loading  

---


## 📸 Screenshots

Here is a look at the application's interface.

**Main Prediction Page:**
<br>
<br>
<img width="2554" height="1389" alt="Studentpredictor1" src="https://github.com/user-attachments/assets/5d5fcc30-2e48-41fb-8af6-f09f31d05965" />


---

**Prediction Result (Pass):**
<br>
<br>
<img width="2560" height="1383" alt="Studentpredictor2" src="https://github.com/user-attachments/assets/c3c6c38b-e432-4511-8ae3-60e146207e78" />

<br>
<br>

<img width="2523" height="1372" alt="Studentpredictor3" src="https://github.com/user-attachments/assets/ca8e460f-df3f-446a-a18e-f3a5bf956fe2" />

---

**Prediction Result (Fail with Tips):**
<br>
<br>
<img width="2534" height="1376" alt="Studentpredictor5" src="https://github.com/user-attachments/assets/b71236dd-3591-4879-a820-62e515b26025" />

<br>
<br>

<img width="2536" height="1374" alt="Studentpredictor6" src="https://github.com/user-attachments/assets/ef958cce-39d5-42c4-8e28-297920499311" />

<br>
<br>

<img width="2555" height="1377" alt="Studentpredictor7" src="https://github.com/user-attachments/assets/2037843e-5522-46dd-b439-ed3bc401055c" />

---


## 📊 Dataset  

The dataset used for model training was taken from Kaggle: https://www.kaggle.com/datasets/alejandraalvarado/student-mat  

It includes features such as study time, absences, health, and previous grades (G1, G2), which are used to predict the final grade (G3).

---

## 🧰 Tech Stack
  
- **Python 3.10+**: Core programming language used for the project
- **Streamlit**: For building the interactive web interface to deploy the model
- **Scikit-learn (sklearn)**: Used for building and training the LinearRegression model
- **Pandas**: For loading, cleaning, and managing the dataset
- **NumPy**: For creating and handling numerical arrays
- **Matplotlib**: For visualizing the model performance using “Actual vs Predicted” graphs
- **Pickle**: For saving and loading the trained machine learning model

---

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### 1. Prerequisites

* Python 3.10+
* pip (Python package installer)

### 2. Installation

1.  **Clone the repository** (or download the files `app.py`, `studentgrade.pkl`, and `student-mat.csv` to a local directory):
    ```bash
    git clone [https://github.com/your-username/student-performance-predictor.git](https://github.com/your-username/student-performance-predictor.git)
    cd student-performance-predictor
    ```

2.  **Create and activate a virtual environment** (recommended):
    * *On macOS/Linux:*
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * *On Windows:*
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the required dependencies:**
    (You can create a `requirements.txt` file with the contents below for easy installation)
    ```bash
    pip install streamlit pandas numpy scikit-learn plotly matplotlib
    ```

### 3. Run the App

With your virtual environment active and dependencies installed, run the Streamlit app from your terminal:

```bash
streamlit run app.py
---


