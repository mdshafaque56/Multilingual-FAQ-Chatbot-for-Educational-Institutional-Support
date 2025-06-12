import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util
from googletrans import Translator
from sklearn.metrics import accuracy_score
import os
import time

# ------------------------- Authentication ------------------------- #
def login():
    st.title("Login to FAQ Chatbot")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.session_state.logged_in = True
        else:
            st.error("Invalid credentials")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
    st.stop()

# ------------------------- Load Data & Model ------------------------- #

@st.cache_data
def load_data():
    try:
        df = pd.read_csv('faq_data.csv')
        df = df.dropna(subset=['Question', 'Answer'])
        return df
    except FileNotFoundError:
        st.error("❌ FAQ file not found. Please upload 'faq_data.csv'.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading FAQ data: {e}")
        st.stop()

try:
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', token=False)
except Exception as e:
    st.error("❌ Failed to load the transformer model.")
    st.stop()

translator = Translator()

faq_df = load_data()
faq_questions = faq_df['Question'].tolist()

@st.cache_data
def encode_questions(questions):
    return model.encode(questions, convert_to_tensor=True)

faq_embeddings = encode_questions(faq_questions)

# ------------------------- Semantic Search ------------------------- #
def translate_to_english(query):
    try:
        translated = translator.translate(query, dest='en')
        return translated.text
    except Exception:
        return query  # fallback if translation fails

def get_best_answer(user_question, threshold=0.65):
    try:
        user_embedding = model.encode([user_question], convert_to_tensor=True)
        scores = util.cos_sim(user_embedding, faq_embeddings)[0]
        best_idx = int(scores.argmax())
        best_score = float(scores[best_idx])
        if best_score >= threshold:
            return faq_df['Answer'].iloc[best_idx], best_score
        else:
            return "Sorry, I don't know the answer to that yet.", best_score
    except Exception as e:
        return f"Error occurred: {e}", 0.0

# ------------------------- UI ------------------------- #
st.title("🧠Welcome")
st.write("Ask your question in English, Hindi, or Malayalam.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "last_question" not in st.session_state:
    st.session_state.last_question = ""

# Display previous messages
for msg in st.session_state.chat_history:
    st.markdown(msg)

user_input = st.text_input("Your question:")

if user_input:
    if user_input.lower() in ["why?", "how?", "tell me more"]:
        user_input = st.session_state.last_question + " " + user_input

    translated_input = translate_to_english(user_input)
    st.session_state.last_question = translated_input

    with st.spinner("🤖 Typing..."):
        time.sleep(1)
        answer, score = get_best_answer(translated_input)

    user_msg = f"**👤 You:** {user_input}"
    bot_msg = f"**🤖 Bot:** Hi, I'm your friendly FAQ Assistant from NIT Calicut. 😊\n\n{answer}\n\n*Confidence: {score:.2f}*"

    st.session_state.chat_history.append(user_msg)
    st.session_state.chat_history.append(bot_msg)

    st.markdown(bot_msg)

# ------------------------- Accuracy Evaluation ------------------------- #
def evaluate_model():
    if os.path.exists("faq_test.csv"):
        test_df = pd.read_csv("faq_test.csv")
        correct = 0
        total = len(test_df)

        for i, row in test_df.iterrows():
            user_query = translate_to_english(row['Input'])
            expected_answer = row['Expected']
            predicted_answer, _ = get_best_answer(user_query)

            if expected_answer.strip().lower() == predicted_answer.strip().lower():
                correct += 1

        accuracy = correct / total if total > 0 else 0
        st.success(f"📊 Evaluation Accuracy: {accuracy * 100:.2f}% ({correct}/{total})")
    else:
        st.info("📁 'faq_test.csv' not found. Upload it to evaluate accuracy.")

with st.expander("📈 Evaluate Chatbot Accuracy"):
    if st.button("Run Evaluation"):
        evaluate_model()

# ------------------------- Examples ------------------------- #
st.markdown("---")
st.write("💡 Example questions you can try:")
for q in faq_questions[:5]:
    st.write(f"- {q}")