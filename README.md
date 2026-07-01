# 🍽️ AI Zomato Chatbot

An AI-powered restaurant recommendation chatbot that understands natural language queries and provides personalized restaurant suggestions using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 🤖 Natural language conversation
- 🍴 Restaurant recommendations based on user preferences
- 🔍 Semantic search using vector embeddings
- 🧠 Retrieval-Augmented Generation (RAG)
- 💬 Context-aware responses
- 🌐 Interactive Streamlit web application

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- OpenAI / Gemini LLM
- FAISS / ChromaDB (Vector Store)
- Sentence Transformers / HuggingFace Embeddings
- Pandas
- NumPy

---

## 📂 Project Structure

```
AI-Zomato-Chatbot/
│
├── app.py
├── chatbot.py
├── requirements.txt
├── restaurant_data.csv
├── embeddings/
├── vector_store/
├── utils.py
├── README.md
└── assets/
```

---

## ⚙️ How It Works

1. User enters a restaurant-related query.
2. The query is converted into vector embeddings.
3. Relevant restaurant information is retrieved from the vector database.
4. The retrieved context is passed to the LLM.
5. The chatbot generates a personalized response.

---

## 💡 Example Questions

- Recommend the best biryani restaurants.
- Suggest restaurants under ₹500.
- Find vegetarian restaurants nearby.
- Recommend family-friendly restaurants.
- Which restaurants have the highest ratings?
- Suggest cafes for remote work.

---

## 📸 Demo

### Live Application

> https://huggingface.co/spaces/Yash-14/AI-Zomato-Chatbot

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Zomato-Chatbot.git
```

Move into the project directory

```bash
cd AI-Zomato-Chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Future Improvements

- Restaurant booking integration
- Google Maps integration
- Voice-based chatbot
- Multi-language support
- Personalized recommendations
- Real-time restaurant data
- Agentic AI with tool calling

---

## Author

**Yashwanth Reddy**

GitHub: https://github.com/Yash14-prog

LinkedIn: https://www.linkedin.com/in/vakiti-yashwanth-reddy/

---

## License

This project is licensed under the MIT License.
