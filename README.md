# 🚨 Intelligent Email Spam Detector

A high-performance, End-to-End NLP and Machine Learning system designed for rigorous email text verification. This project leverages a **Consensus-Based Voting Ensemble Architecture** combined with advanced class balancing techniques to achieve top-tier classification metrics.

---

## 🎬 Project Overview & UI

The project features a modern, clean, and user-friendly desktop application interface built with **CustomTkinter** (Light Mode), ensuring a seamless user experience for real-time text analysis.

### 💻 Desktop Application Interface (Live Previews)

| 🚨 Spam Detection Preview | ✅ Ham Verification Preview |
|---|---|
| ![Email Spam Detector (Spam)](Email%20Spam%20Detector%20%28Spam%29.png) | ![Email Spam Detector (Ham)](Email%20Spam%20Detector%20%28Ham%29.png) |

---

## 🧠 Technical Architecture & Pipeline

Instead of relying on a single classifier, this system utilizes a **Soft-Voting Ensemble Layer** that combines the probability distributions of three foundational machine learning algorithms:

1. **Logistic Regression:** Optimized with balanced class weights for strong text classification baselines.
2. **Multinomial Naive Bayes:** Highly efficient for handling frequency-based text probabilities.
3. **Support Vector Machine (SVC):** Tuned with probability outputs for drawing optimal hyperplanes in high-dimensional text space.

### 📈 Model Development & Kaggle Success
The complete pipeline—from Exploratory Data Analysis (EDA) to hyperparameter tuning—is fully documented and has already gained active engagement on Kaggle.

⭐ **Check out the live development workspace:** [Spam Vs Ham on Kaggle](https://www.kaggle.com/code/mennaadel111/spam-vs-ham)

### Key NLP & Data Science Pipeline:
* **Text Cleansing:** Regex pattern matching to extract alphabetic characters and lowercasing.
* **Stopwords Filter & Stemming:** Filtering common English stopwords and applying word normalization using NLTK's **PorterStemmer**.
* **Feature Extraction:** Advanced text vectorization using **TF-IDF Vectorizer**.
* **Class Balancing:** Applied **SMOTE** (Synthetic Minority Over-sampling Technique) to address the text label imbalance before training, significantly boosting recall for the minority class.

---

## 📁 Repository Structure

* `GUI.py`: Complete desktop app implementation using CustomTkinter with integrated text placeholders and clipboard handlers.
* `Spam Vs Ham.ipynb`: Complete Jupyter Notebook containing EDA, data handling, and evaluation code.
* `ensemble_voting_model.pkl`: The trained, serialized soft-voting ensemble classifier.
* `tfidf_vectorizer.pkl`: The fitted TF-IDF vocabulary state.
* `app_icon.ico`: Custom branding identity icon for the application window.

---
