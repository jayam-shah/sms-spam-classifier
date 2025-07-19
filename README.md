# 📩 SMS Spam Classifier

This is a simple yet effective machine learning web application built with **Streamlit** that classifies SMS messages as **Spam** or **Not Spam (Ham)**. It uses a trained **TF-IDF Vectorizer** and a **Multinomial Naive Bayes model** for accurate classification.

---

## 🛠️ Features

- Classify SMS messages instantly.
- Clean and simple UI using Streamlit.
- Built-in text preprocessing.
- Model trained using scikit-learn's `TfidfVectorizer` + `MultinomialNB`.

---

## 🧠 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **ML Libraries:** scikit-learn, pandas, nltk

---

## 📁 Project Structure

```

├── app.py               # Main Streamlit application
├── model.pkl            # Trained classification model
├── vectorizer.pkl       # Trained TF-IDF vectorizer
├── requirements.txt     # Python dependencies

````

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/sms-spam-classifier.git
cd sms-spam-classifier
````

### 2. Install Dependencies

Create a virtual environment (optional but recommended), then:

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 📦 Deployment

You can deploy this app easily using [Streamlit Cloud](https://streamlit.io/cloud):

1. Push all files to a public GitHub repo.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and click "New App".
3. Connect your GitHub repo.
4. Set the main file path to `app.py`.
5. Click "Deploy".

✅ Make sure `vectorizer.pkl` and `model.pkl` are also committed to the repo.

---

## 📌 Notes

* Make sure to import `TfidfVectorizer` before loading the `.pkl` files to avoid `ModuleNotFoundError`:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
```

* When loading `.pkl` files, use absolute paths:

```python
import os
path = os.path.join(os.path.dirname(__file__), 'vectorizer.pkl')
pickle.load(open(path, 'rb'))
```

---

## 🙋‍♂️ Author

**JD Shah**
📫 Feel free to connect on [LinkedIn](www.linkedin.com/in/jayamshah2278)
