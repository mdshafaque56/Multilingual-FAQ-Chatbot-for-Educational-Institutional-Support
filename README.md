# Multilingual FAQ Chatbot for Educational & Institutional Support – README

## Domain
Artificial Intelligence, Natural Language Processing, Conversational Agents, Educational Technology

---

## Overview

This project is a multilingual FAQ chatbot designed to assist users with queries related to any Educational Institute(for demo, I have taken my institute NITC). Built with Python and Streamlit, the chatbot leverages advanced NLP techniques to semantically match user questions (in English, Hindi, or Malayalam) to a curated FAQ dataset. The system features semantic search using sentence embeddings, automatic translation, user authentication, chat history, and an integrated accuracy evaluation tool.

---

## Features

- **Multilingual Input:** Accepts questions in English, Hindi, or Malayalam and translates them to English for processing.
- **Semantic Search:** Uses Sentence Transformers to match user queries to the most relevant FAQ entry, even for paraphrased questions.
- **User Authentication:** Simple login system for access control.
- **Chat History:** Displays previous user and bot interactions in the session.
- **Contextual Follow-ups:** Handles follow-up queries like "why?" or "how?" by referencing the last question.
- **Accuracy Evaluation:** Upload a test set and evaluate chatbot accuracy directly from the UI.
- **Sample Questions:** Displays example questions to help users get started.

---

## Tech Stack

| Component           | Technology/Library                 |
|---------------------|------------------------------------|
| UI                  | Streamlit                          |
| Data Handling       | pandas                             |
| NLP/Embeddings      | sentence-transformers (MiniLM-L6)  |
| Translation         | googletrans                        |
| Accuracy Metrics    | scikit-learn (accuracy_score)      |
| Authentication      | Streamlit session state            |
| Language            | Python                             |

---

## Dataset

- **FAQ Dataset:** `faq_data.csv`  
  - Columns: `Question`, `Answer`
  - Place this file in the project root directory.

- **Test Dataset (Optional):** `faq_test.csv`  
  - Columns: `Input`, `Expected`
  - Used for accuracy evaluation.

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/nitc-faq-chatbot.git
   cd nitc-faq-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit pandas sentence-transformers googletrans==4.0.0-rc1 scikit-learn
   ```

3. **Download the model (if needed)**
   - If you encounter authentication issues, download the `all-MiniLM-L6-v2` model manually from Hugging Face and place it in the project directory.
   - Update the model path in the code if using a local copy.

4. **Place your datasets**
   - Ensure `faq_data.csv` (and optionally `faq_test.csv`) are in the project root.

---

## Usage

1. **Run the chatbot**
   ```bash
   streamlit run faq_chatbot.py
   ```

2. **Login**
   - Username: `admin`
   - Password: `1234`

3. **Ask Questions**
   - Enter your question in English, Hindi, or Malayalam.
   - The bot will respond with the most relevant answer and a confidence score.

4. **Evaluate Accuracy**
   - Expand the "📈 Evaluate Chatbot Accuracy" section.
   - Upload `faq_test.csv` and click "Run Evaluation" to view accuracy metrics.

---

## Code Structure

- `faq_chatbot.py`: Main application script (see [attached file][1])
- `faq_data.csv`: FAQ question-answer pairs
- `faq_test.csv`: (Optional) Test set for evaluation

---

## How It Works

1. **Authentication:** Users must log in to access the chatbot.
2. **Data & Model Loading:** Loads FAQ data and encodes questions using a transformer model.
3. **Translation:** User input is translated to English if needed.
4. **Semantic Search:** The user query is embedded and compared to FAQ embeddings to find the closest match.
5. **Response:** The bot returns the best-matched answer with a confidence score.
6. **Follow-up Handling:** Recognizes follow-up prompts and provides context-aware responses.
7. **Accuracy Evaluation:** Compares model predictions to expected answers in a test set and reports accuracy.

---

## Customization

- **Expand the FAQ:** Add more question-answer pairs to `faq_data.csv`.
- **Change Authentication:** Modify the login logic as needed.
- **UI Enhancements:** Adjust Streamlit components for a richer interface.
- **Model Tuning:** Experiment with different transformer models for improved matching.

---

## Troubleshooting

- **Model Download Errors:**  
  If you see an "Unauthorized" or connection error when loading the model, try:
  - Adding `token=False` to the model loader.
  - Downloading the model manually and loading from a local path.

- **File Not Found:**  
  Ensure `faq_data.csv` is present in the project directory.

- **Translation Issues:**  
  If translation fails, the bot will process the original input as a fallback.

---

## License

MIT License

---

## Acknowledgements

- [Hugging Face Sentence Transformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io/)
- [Googletrans](https://py-googletrans.readthedocs.io/)

---

**Developed by MD Shafaque as a Project**

---
