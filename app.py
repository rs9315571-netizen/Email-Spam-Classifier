import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

# Load your saved files
tfidf = pickle.load(open('tf.pkl', 'rb'))
model = pickle.load(open('MNB.pkl', 'rb'))

# Download NLTK requirements (only runs once)
nltk.download('punkt')
nltk.download('stopwords')

# Your same transform function
def text_transform(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    Y = []
    for i in text:
        if i.isalnum():
            Y.append(i)

    text = Y[:]
    Y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            Y.append(i)

    text = Y[:]
    Y.clear()

    ps_stemmer = PorterStemmer()
    for i in text:
        Y.append(ps_stemmer.stem(i))

    return " ".join(Y)


# ------------- Streamlit UI -----------------

st.set_page_config(page_title="Email Spam Classifier", page_icon="📩")
st.title("📧 Email Spam Detector")
st.write("Type an email or message below to check if it's **Spam or Not Spam**")

input_sms = st.text_area("Enter the message here:")

if st.button('Predict'):
    if input_sms.strip() == "":
        st.warning("Please type a message first!")
    else:
        # 1. Preprocess
        transformed_sms = text_transform(input_sms)
        # 2. Vectorize
        vector_input = tfidf.transform([transformed_sms])
        # 3. Predict
        result = model.predict(vector_input)[0]
        # 4. Display result
        if result == 1:
            st.error("🚨 Spam Message Detected!")
        else:
            st.success("✅ This message is Not Spam.")
