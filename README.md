# Laptop Price Prediction

This project predicts the price of a laptop based on its specifications using Machine Learning models.  
It involves data preprocessing, model training, and deployment through a simple local user interface.

---

## Project Structure

| File Name | Description |
|------------|--------------|
| **App.py** | Contains the user interface for the laptop price prediction model. This file allows users to input laptop specifications and get the predicted price on their local machine. |
| **Laptop_price_predictor.ipynb** | Jupyter Notebook containing the complete workflow for preprocessing, training, and testing the dataset. |
| **df.pkl** | Serialized (pickled) file containing the refined and cleaned dataset used for model training. |
| **laptop_data.csv** | Original dataset containing laptop specifications and prices. |
| **pipe.pkl** | Contains the saved pipeline which includes the encoder and trained model used for making predictions. |

---

## 🧠 Model Information

- The model was trained using multiple machine learning techniques for regression.  
- It includes preprocessing steps such as encoding categorical variables and feature scaling through a pipeline.  
- The final model achieved an **accuracy of 88%** on the test dataset.

---

## ⚙️ How to Run Locally

   # 1. Clone the repository
        git clone https://github.com/sbhattacherjee98-ops/Laptop-Price-Prediction.git
        cd Laptop-Price-Prediction

   # 2. Install dependencies
        pip install -r requirements.txt

   # 3. Run the Streamlit app
        streamlit run App.py
  
