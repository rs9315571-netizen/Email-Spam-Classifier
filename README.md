# **Email Spam Detector**

A simple AI-powered web app that predicts whether a message is **Spam** or **Not Spam** using **Naive Bayes** and **TF-IDF**.  
Built with **Python** and **Streamlit**, it analyzes text in real time with a clean, modern interface.

*(Note: The model is trained on a small sample dataset and may not represent real-world data.)*

---

## Features
- Real-time spam detection
- Simple Streamlit UI
- Lightweight machine learning model (Naive Bayes + TF-IDF)
---

## Prerequisites
Before running this project, make sure you have the following installed:
- Python  
- Streamlit  
- Scikit-learn  
- NLTK  
- Pandas & NumPy  

---

## How It Works
1. The input text is preprocessed using NLTK (tokenization, stopword removal, etc.)  
2. TF-IDF converts the text into numerical features.  
3. A trained Naive Bayes model predicts if the message is spam or not.  
4. The result is displayed instantly in the app.

---

## If Want To Run the App Locally
```bash
pip install -r requirements.txt
streamlit run app.py
