# 🤖 FAQ Chatbot using NLP and Streamlit

## 📌 Project Overview

The FAQ Chatbot is an NLP-based chatbot that automatically answers user questions by matching them with the most relevant Frequently Asked Questions (FAQs) stored in a dataset. The chatbot uses Natural Language Processing (NLP), TF-IDF vectorization, and Cosine Similarity to identify the closest matching question and return the appropriate answer.

This project demonstrates the practical application of NLP techniques for building intelligent question-answering systems.

---

## 🚀 Features

* Interactive chatbot interface built with Streamlit
* FAQ dataset stored in CSV format
* Text preprocessing and cleaning
* TF-IDF vectorization for text representation
* Cosine Similarity for question matching
* Displays the most relevant answer instantly
* User-friendly web interface
* Lightweight and easy to customize

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NLTK
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

---

## 📂 Project Structure

```text
faq-chatbot/
│
├── app.py
├── faqs.csv
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

1. Load FAQ questions and answers from a CSV file.
2. Clean and preprocess the text data.
3. Convert questions into TF-IDF vectors.
4. Accept a user's query through the Streamlit interface.
5. Calculate cosine similarity between the user query and stored FAQs.
6. Identify the most similar FAQ.
7. Display the corresponding answer.


---

## 📸 Sample Questions

* What is Python?
* What is AI?
* What is Machine Learning?
* What is NLP?
* What is Streamlit?
* How can I learn AI?

---

## 📈 Future Enhancements

* Voice-based chatbot
* PDF FAQ support
* FAQ upload functionality
* Multi-language support
* Sentence Transformers embeddings
* FAISS Vector Database integration
* Gemini/OpenAI/Groq API integration
* Chat history and analytics dashboard

---

## 🎯 Learning Outcomes

Through this project, I learned:

* Natural Language Processing fundamentals
* Text preprocessing techniques
* TF-IDF vectorization
* Cosine similarity calculations
* Building web applications with Streamlit
* Working with datasets using Pandas
* Deploying Python applications




