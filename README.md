# Storyteller
AI Storyteller
# 🧠 AI Storyteller – Generative Story App

**AI Storyteller** is a simple and powerful application that allows users to generate full-length, coherent stories from a single sentence or a short prompt using a large language model (LLM).

## 🚀 Features

* ✍️ Generate creative and engaging stories from just a few words.
* 🌍 Supports multiple languages (French, English, Arabic, etc.).
* 🎨 Automatically adds structure: introduction, development, and conclusion.
* 🔁 Optionally regenerate or continue stories for longer narratives.
* 📱 Simple and intuitive Streamlit interface.

## 🧩 Use Case

* **Input Prompt**: `"Un enfant trouve une clé mystérieuse dans la forêt."`
* **Generated Story**: A multi-paragraph story introducing characters, setting, conflict, and resolution — all invented dynamically.

## 🛠️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/ai-storyteller.git
   cd ai-storyteller
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your LLM API key** in a `.env` file:

   ```
   API_KEY=your_openai_or_groq_key
   ```

## ▶️ Run the app

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`

## 🧠 Model & Prompting Strategy

The model uses **instruction tuning** and carefully crafted prompts to guide the LLM to generate consistent and engaging stories. Prompts may include:

* Clear roles (e.g. *"You are a creative storyteller..."*)
* Tone/genre hints (e.g. *mystery, fantasy, science fiction*)
* Output formatting instructions

## 📂 Project Structure

```
.
├── app.py               # Streamlit app
├── prompts.py           # Prompt templates
├── utils.py             # Helper functions
├── requirements.txt     # Dependencies
└── README.md            # You're here!
```

## 📌 Examples

| Input Prompt                              | Genre    | Output Length    |
| ----------------------------------------- | -------- | ---------------- |
| "Une fille découvre un miroir magique"    | Fantasy  | \~3-4 paragraphs |
| "Il pleuvait quand le téléphone sonna..." | Suspense | \~2-3 paragraphs |
| "A robot falls in love with a human"      | Sci-Fi   | \~3-5 paragraphs |

## 💡 Ideas for Extensions

* Add **voice narration** using TTS
* Save stories as **PDF or EPUB**
* Introduce **character control or story branching**
* Use **images** to enhance story visualization


