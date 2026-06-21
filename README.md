# 🚨 Intelligent Email Spam Detector

A high-performance, End-to-End NLP and Machine Learning system designed for rigorous email text verification. This project moves away from single-model approaches to leverage a **Voting Ensemble Architecture**, achieving top-tier accuracy and robust generalization.

---

## 🎬 Project Overview & UI

The project features a modern, clean, and user-friendly desktop application interface built with **CustomTkinter**, ensuring a seamless user experience for real-time text analysis.

### 💻 Desktop Application Interface (Live Previews)

| 🚨 Spam Detection Preview | ✅ Ham Verification Preview |
|---|---|
| ![Email Spam Detector (Spam)](Email%20Spam%20Detector%20%28Spam%29.png) | ![Email Spam Detector (Ham)](Email%20Spam%20Detector%20%28Ham%29.png) |

---

## 🧠 Core Architecture & Technical Depth

Instead of relying on a single classifier, this system utilizes a **Consensus-Based Voting Ensemble Layer** combining multiple optimized models:
* **Logistic Regression** (Baseline text classification)
* **Naive Bayes** (Highly efficient for text frequency probabilities)
* **XGBoost** (Advanced gradient boosting for fine-grained feature splitting)

### 📊 Model Development & Kaggle Notebook
The complete development pipeline from Exploratory Data Analysis (EDA) to hyperparameter tuning and ensemble evaluation is fully documented. 

⭐ **Check out the live development workspace and show support here:** [Spam Vs Ham on Kaggle](https://www.kaggle.com/code/mennaadel111/spam-vs-ham)

### Key NLP Preprocessing Steps:
1. **Text Cleansing:** Regex pattern matching to remove non-alphabetic characters and lowercasing.
2. **Tokenization & Stopwords Removal:** Filtering out common English stopwords using **NLTK**.
3. **Stemming:** Reducing words to their base form using the **PorterStemmer** algorithm.
4. **Vectorization:** Transforming cleaned text into numerical features using **TF-IDF Vectorizer**.

---

## 📁 Repository Structure

* `GUI.py`: The core desktop application script with zero clutter.
* `Spam Vs Ham.ipynb`: The complete development pipeline notebook.
* `ensemble_voting_model.pkl`: The trained, ready-to-use Voting Classifier.
* `tfidf_vectorizer.pkl`: The fitted TF-IDF vocabulary extractor.
* `app_icon.ico`: Custom purple identity icon for the application window.

---

## 🛠️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/MennaAdell/Email-Spam-Detector.git](https://github.com/MennaAdell/Email-Spam-Detector.git)
