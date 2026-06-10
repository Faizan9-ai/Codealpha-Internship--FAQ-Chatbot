
import streamlit as st
import pandas as pd
import nltk
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("punkt")

# Load FAQs
df = pd.read_csv("faqs.csv")

# Text preprocessing
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text

df["clean_question"] = df["question"].apply(clean_text)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(df["clean_question"])

# Get best answer
def get_answer(user_question):
    user_question_clean = clean_text(user_question)
    user_vector = vectorizer.transform([user_question_clean])

    similarity = cosine_similarity(user_vector, faq_vectors)
    best_match_index = similarity.argmax()
    best_score = similarity[0][best_match_index]

    if best_score < 0.2:
        return "Sorry, I could not find a proper answer. Please ask another question."

    return df.iloc[best_match_index]["answer"]

# Streamlit UI
st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")

st.title("🤖 FAQ Chatbot")
st.write("Ask any question from the FAQ database.")

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = get_answer(user_input)
        st.success(response)

st.sidebar.title("Available FAQs")
for q in df["question"]:
    st.sidebar.write("•", q)