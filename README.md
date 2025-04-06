# 📝 Content Rewriter

A Streamlit-powered web app that rewrites input content based on configurable tone, style, and formatting settings—powered by Writer’s domain-specific **Palmyra** LLMs.

## 🔍 Overview

This app helps users rephrase and enhance content in a way that aligns with domain-specific expectations (Creative, Medical, Finance, or General-purpose), making it especially useful for professional writing, compliance, and communication scenarios.

### 💡 Models Used

- **`palmyra-creative`** – Creative and brand-focused rewriting.
- **`palmyra-med`** – Simplifies medical content for readability (informational only).
- **`palmyra-fin`** – Restructures financial documents for clarity.
- **`palmyra-x-004`** – General-purpose rewriting assistant.

> ⚠️ **Disclaimer**  
> Medical and Financial outputs must not be used for diagnostic, therapeutic, or investment purposes without review by licensed professionals.

---

## 🚀 Features

- Upload JSON config to customize rewriting:
  - Tone
  - Required or banned words
  - Sentence length
  - Output formatting
- Paste or generate domain-specific content.
- Select from four domain-specific models.
- Get live-streamed markdown-formatted output.

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/content-rewriter.git
cd content-rewriter
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a .env file in the root of your project:

```
WRITER_API_KEY=your_writer_api_key_here
```

### 4. Run the App

Start the Streamlit app:

```
streamlit run app.py
```

---

## 📁 JSON Config Format

To control how your content is rewritten, upload a JSON file like this:

```
{
  "tone": "professional",
  "banned_words": ["very", "really"],
  "required_terms": ["efficiency", "growth"],
  "max_sentence_length": 25,
  "formatting": "bullet_points"
}
```

---

## 🧪 How It Works

1. **Upload your config file** – Define tone, formatting, and other style rules.
2. **Paste or generate example content** – Use the sidebar to input or auto-generate realistic content.
3. **Choose your domain** – Select from:
   - Creative
   - Medical
   - Finance
   - Omni
4. **Submit** – The app rewrites your content and displays both original and transformed versions side by side.

---

## ✨ Powered By

- **`palmyra-creative`** – For creative and brand-focused rewriting
- **`palmyra-med`** – For interpreting medical shorthand into readable summaries (non-diagnostic)
- **`palmyra-fin`** – For analyzing and rewriting financial documents
- **`palmyra-x-004`** – General-purpose, all-domain content rewriting
