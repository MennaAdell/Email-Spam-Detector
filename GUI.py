import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import joblib
import re
import warnings
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import os

ctk.set_appearance_mode("Light")  
ctk.set_default_color_theme("blue")  

warnings.filterwarnings("ignore", category=UserWarning)

try:
    stop_words = set(stopwords.words('english'))
except:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

try:
    tfidf = joblib.load('tfidf_vectorizer.pkl')
    ensemble_model = joblib.load('ensemble_voting_model.pkl')
    print("Ensemble System Loaded Successfully!")
except Exception as e:
    print(f"Error loading files: {e}")

def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', str(text).lower())
    words = text.split()
    clean_words = [ps.stem(w) for w in words if w not in stop_words]
    return ' '.join(clean_words)

PLACEHOLDER_TEXT = "Enter email content here..."
is_placeholder_active = True

def on_key_press(event):
    global is_placeholder_active
    if is_placeholder_active:
        text_area.delete("1.0", tk.END)
        text_area.configure(text_color="#1F2937")  
        is_placeholder_active = False

def on_focus_out(event):
    global is_placeholder_active
    current_text = text_area.get("1.0", "end-1c").strip()
    if not current_text:
        text_area.delete("1.0", tk.END)
        text_area.insert("1.0", PLACEHOLDER_TEXT)
        text_area.configure(text_color="#9CA3AF")  
        is_placeholder_active = True

def reset_gui():
    global is_placeholder_active
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", PLACEHOLDER_TEXT)
    text_area.configure(text_color="#9CA3AF")
    is_placeholder_active = True
    result_label.configure(text="Awaiting Analysis...", fg_color="#F3F4F6", text_color="#4B5563")

def handle_paste(event=None):
    global is_placeholder_active
    try:
        if is_placeholder_active:
            text_area.delete("1.0", tk.END)
            text_area.configure(text_color="#1F2937")
            is_placeholder_active = False
            
        text = root.clipboard_get()
        text_area.insert(tk.INSERT, text)
    except tk.TclError:
        pass
    return "break"

def classify_email():
    global is_placeholder_active
    email_input = text_area.get("1.0", "end-1c").strip()
    
    if not email_input or is_placeholder_active:
        messagebox.showwarning("Warning", "Please provide email content to analyze.")
        return

    try:
        clean_input = clean_text(email_input)
        vectorized_text = tfidf.transform([clean_input])
        prediction = ensemble_model.predict(vectorized_text)[0]
        
        status = "SPAM" if str(prediction).lower() in ['1', 'spam'] else "HAM"
        
        if status == "SPAM":
            result_label.configure(text="🚨 HIGH RISK: SPAM DETECTED", fg_color="#FEE2E2", text_color="#991B1B")
        else:
            result_label.configure(text="✅ SAFE: LEGITIMATE EMAIL (HAM)", fg_color="#D1FAE5", text_color="#065F46")

    except Exception as e:
        messagebox.showerror("Error", f"Classification failed: {e}")

root = ctk.CTk()
root.title("Email Spam Detector")
root.geometry("850x670")
root.configure(fg_color="#FAFAFA")  

if os.path.exists('app_icon.ico'):
    root.iconbitmap('app_icon.ico')

root.bind_all("<Control-v>", handle_paste)
root.bind_all("<Control-V>", handle_paste)

title_label = ctk.CTkLabel(root, text="Email Spam Detector", font=("Century Gothic", 34, "bold"), text_color="#7C19BE") 
title_label.pack(pady=(50, 6))

subtitle_label = ctk.CTkLabel(root, text="A multi-model ensemble system designed for rigorous email text verification.", font=("Segoe UI", 13), text_color="#6B7280")
subtitle_label.pack(pady=(0, 35))

text_area = ctk.CTkTextbox(root, width=700, height=250, font=("Segoe UI", 13), border_width=1, border_color="#E5E7EB", fg_color="#FFFFFF", corner_radius=14)
text_area.pack(pady=10)

text_area.insert("1.0", PLACEHOLDER_TEXT)
text_area.configure(text_color="#9CA3AF")

text_area.bind("<Key>", on_key_press)
text_area.bind("<FocusOut>", on_focus_out)

btn_frame = ctk.CTkFrame(root, fg_color="transparent")
btn_frame.pack(pady=25)

classify_btn = ctk.CTkButton(
    btn_frame, 
    text="Verify Email", 
    font=("Segoe UI", 14, "bold"), 
    fg_color="#7C19BE",       
    hover_color="#4F1277",    
    width=160, 
    height=44, 
    corner_radius=22, 
    command=classify_email
)
classify_btn.pack(side="left", padx=12)

clear_btn = ctk.CTkButton(
    btn_frame, 
    text="Clear", 
    font=("Segoe UI", 14, "bold"), 
    fg_color="#F3F4F6",       
    hover_color="#E5E7EB",    
    text_color="#374151",     
    width=110, 
    height=44, 
    corner_radius=22, 
    command=reset_gui
)
clear_btn.pack(side="left", padx=12)

result_label = ctk.CTkLabel(
    root, 
    text="Awaiting Analysis...", 
    font=("Segoe UI", 15, "bold"), 
    width=700, 
    height=60, 
    corner_radius=14, 
    fg_color="#F3F4F6", 
    text_color="#4B5563"
)
result_label.pack(pady=(20, 50))

root.mainloop()