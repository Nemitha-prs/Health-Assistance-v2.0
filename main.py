import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import json
import time
import threading
import os
import webbrowser

# --------------------------
# CONFIGURATION AND SETUP
# --------------------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


diseases_db = {

    "fever": ["Flu", "Malaria", "Typhoid", "COVID-19", "Common Cold", "Pneumonia"],
    "cough": ["Bronchitis", "Asthma", "Flu", "Tuberculosis", "COVID-19", "Common Cold"],
    "coughing": ["Bronchitis", "Asthma", "Flu", "Tuberculosis", "COVID-19", "Common Cold"],
    "sneezing": ["Common Cold", "Allergic Rhinitis", "Sinusitis", "Flu"],
    "headache": ["Migraine", "Tension Headache", "Dehydration", "Flu", "Stress"],
    "stomach pain": ["Gastritis", "Ulcer", "Food Poisoning", "Appendicitis", "IBS"],
    "nausea": ["Food Poisoning", "Pregnancy", "Gastritis", "Migraine", "Motion Sickness"],
    "vomiting": ["Food Poisoning", "Stomach Flu", "Pregnancy", "Migraine"],
    "diarrhea": ["Food Poisoning", "Stomach Flu", "Cholera", "IBS"],
    "fatigue": ["Anemia", "Depression", "Hypothyroidism", "Diabetes", "Flu"],
    "depression": ["Major Depression", "Bipolar Disorder", "Thyroid Imbalance", "Anxiety Disorder"],
    "sore throat": ["Strep Throat", "Flu", "Common Cold", "COVID-19"],
    "runny nose": ["Common Cold", "Allergic Rhinitis", "Flu", "Sinusitis"],

    "stomach pain": ["Gastritis", "Food Poisoning", "Stomach Flu", "Appendicitis", "Ulcer"],
    "back pain": ["Muscle Strain", "Herniated Disc", "Kidney Stones", "Osteoarthritis"],
    "headache": ["Migraine", "Tension Headache", "Sinusitis", "Brain Tumor (rare)"],
    "fever": ["Flu", "Common Cold", "COVID-19", "Malaria", "Dengue"],
    "joint pain": ["Arthritis", "Lupus", "Rheumatoid Arthritis", "Gout"],
    "cough": ["Bronchitis", "Common Cold", "Pneumonia", "Asthma"],
    "skin rash": ["Eczema", "Allergy", "Psoriasis", "Chickenpox"],
    "stomach": ["Gastritis", "Food Poisoning", "Stomach Flu", "Indigestion", "Ulcer", "Irritable Bowl Syndrome"],
    "tummy": ["Gastritis", "Indigestion", "Food Poisoning"],
    "headache": ["Migraine", "Tension Headache", "Sinus Infection", "Stress", "Dehydration"],
    "fever": ["Flu", "COVID-19", "Malaria", "Infection", "Dengue"],
    "cough": ["Common Cold", "Bronchitis", "Pneumonia", "Asthma"],
    "back": ["Muscle Strain", "Kidney Stone", "Poor Posture", "Herniated Disc"],
    "joint": ["Arthritis", "Gout", "Inflammation", "Rheumatoid Arthritis"],
    "fatigue": ["Anemia", "Hypothyroidism", "Diabetes", "Sleep Apnea", "Stress"],
    "chest": ["Heart Attack", "Angina", "Acid Reflux", "Pneumonia"],
    "rash": ["Allergy", "Eczema", "Chickenpox", "Measles", "Hives"],
    "vomit": ["Food Poisoning", "Gastroenteritis", "Pregnancy", "Migraine"],
    "diarrhea": ["Food Poisoning", "Gastroenteritis", "IBS", "Lactose Intolerance"],
    "shortness of breath": ["Asthma", "COPD", "Pneumonia", "Heart Failure"],
    "nausea": ["Pregnancy", "Food Poisoning", "Gastritis", "Migraine"],
    "dizzy": ["Dehydration", "Low Blood Pressure", "Anemia", "Vertigo"],
    "cold": ["Common Cold", "Flu", "Sinus Infection"],
    "sore throat": ["Tonsillitis", "Flu", "Common Cold", "Strep Throat"],
    "abdominal pain": ["Appendicitis", "Gallstones", "Gastritis", "IBS"],
    "bloody stool": ["Hemorrhoids", "Colon Cancer", "IBD", "Infection"],
    "heartburn": ["Acid Reflux", "GERD", "Ulcer"],
    "chills": ["Flu", "Malaria", "Infection"],
    "weight loss": ["Diabetes", "Thyroid Disorder", "Cancer", "TB"],
    "weight gain": ["Hypothyroidism", "PCOS", "Cushing's Syndrome"],
    "frequent urination": ["Diabetes", "UTI", "Prostate Problem"],
    "burning urination": ["UTI", "Kidney Infection", "STI"],
    "abnormal bleeding": ["Hemophilia", "Vitamin K Deficiency", "Hormonal Imbalance"],
    "swelling": ["Edema", "Heart Failure", "Kidney Disease"],
    "itching": ["Allergy", "Eczema", "Liver Disease"],
    "hair loss": ["Alopecia", "Thyroid Disorder", "Nutritional Deficiency"],
    "dry skin": ["Hypothyroidism", "Eczema", "Psoriasis"],
    "red eyes": ["Conjunctivitis", "Allergy", "Infection"],
    "blurred vision": ["Glaucoma", "Diabetes", "Cataract", "Migraine"],
    "hearing loss": ["Ear Infection", "Age-Related Hearing Loss", "Noise Exposure"],
    "ringing in ears": ["Tinnitus", "Ear Infection", "Hearing Loss"],
    "chest pain": ["Heart Attack", "Angina", "GERD", "Pulmonary Embolism"],
    "palpitations": ["Arrhythmia", "Anxiety", "Hyperthyroidism"],
    "anxiety": ["Generalized Anxiety Disorder", "Panic Disorder", "Stress"],
    "depression": ["Major Depression", "Bipolar Disorder", "Thyroid Imbalance"],
    "confusion": ["Dementia", "Stroke", "Hypoglycemia", "Infection"],
    "memory loss": ["Alzheimer's", "Vitamin B12 Deficiency", "Stroke"],
    "insomnia": ["Stress", "Sleep Apnea", "Depression"],
    "excessive sleep": ["Hypothyroidism", "Sleep Apnea", "Depression"],
    "excessive thirst": ["Diabetes", "Dehydration", "Kidney Disease"],
    "muscle pain": ["Fibromyalgia", "Vitamin D Deficiency", "Infection", "Injury"],
    "muscle weakness": ["Myopathy", "Neuropathy", "Stroke"],
    "tremors": ["Parkinson's", "Hyperthyroidism", "Stress"],
    "numbness": ["Neuropathy", "Stroke", "Vitamin B12 Deficiency"],
    "tingling": ["Neuropathy", "Vitamin B12 Deficiency", "Circulatory Problems"],
    "swollen lymph nodes": ["Infection", "Cancer", "Immune Disorders"],
    "nosebleed": ["Dryness", "High Blood Pressure", "Bleeding Disorder"],
    "frequent infections": ["Immune Deficiency", "Diabetes", "HIV"],
    "easy bruising": ["Blood Disorders", "Vitamin Deficiency", "Medication Side Effect"],
    "chronic cough": ["Tuberculosis", "Asthma", "COPD", "Lung Cancer"],
    "wheezing": ["Asthma", "COPD", "Allergy"],
    "difficulty swallowing": ["Throat Cancer", "Esophageal Disorder", "Neurological Problem"],
    "hoarseness": ["Laryngitis", "Throat Cancer", "Vocal Strain"],
    "chronic diarrhea": ["IBD", "IBS", "Infection", "Celiac Disease"],
    "constipation": ["IBS", "Hypothyroidism", "Low Fiber Diet"],
    "blood in urine": ["Kidney Stone", "UTI", "Bladder Cancer"],
    "abdominal bloating": ["IBS", "Food Intolerance", "Celiac Disease"],
    "excessive sweating": ["Hyperthyroidism", "Menopause", "Infection"],
    "cold hands/feet": ["Hypothyroidism", "Poor Circulation", "Anemia"],
    "leg cramps": ["Dehydration", "Electrolyte Imbalance", "Peripheral Artery Disease"],
    "joint stiffness": ["Arthritis", "Injury", "Fibromyalgia"],
    "morning stiffness": ["Rheumatoid Arthritis", "Osteoarthritis", "Fibromyalgia"],
    "chronic fatigue": ["Anemia", "Hypothyroidism", "Chronic Fatigue Syndrome", "Diabetes"],
    "hair thinning": ["Alopecia", "Thyroid Imbalance", "Stress"],
    "pale skin": ["Anemia", "Vitamin Deficiency", "Blood Loss"],
    "yellow skin/eyes": ["Jaundice", "Liver Disease", "Hepatitis"],
    "dark urine": ["Dehydration", "Liver Disease", "Hematuria"],
    "frequent headaches": ["Migraine", "Tension Headache", "Sinus Infection"],
    "facial pain": ["Sinus Infection", "Dental Infection", "Trigeminal Neuralgia"],
    "sensitivity to light": ["Migraine", "Meningitis", "Eye Disorders"],
    "sensitivity to sound": ["Migraine", "Meniere's Disease", "Stress"],
    "vomiting blood": ["Ulcer", "Gastritis", "Esophageal Varices"],
    "persistent vomiting": ["Gastroenteritis", "Pregnancy", "Gastrointestinal Obstruction"],
    "bad breath": ["Dental Infection", "Gastroesophageal Reflux", "Sinus Infection"],
    "chest tightness": ["Asthma", "Heart Attack", "Anxiety"],
    "abnormal heart rhythm": ["Arrhythmia", "Heart Disease", "Electrolyte Imbalance"],
    "bloated abdomen": ["Ascites", "IBS", "Constipation"],
    "joint redness": ["Arthritis", "Gout", "Infection"],
    "knee pain": ["Arthritis", "Injury", "Bursitis"],
    "ankle swelling": ["Heart Failure", "Kidney Disease", "Injury"],
    "foot pain": ["Plantar Fasciitis", "Gout", "Injury"],
    "heel pain": ["Plantar Fasciitis", "Achilles Tendonitis", "Heel Spur"],
    "toothache": ["Dental Infection", "Cavity", "Gum Disease"],
    "gum bleeding": ["Gingivitis", "Vitamin K Deficiency", "Blood Disorders"],
    "frequent nose congestion": ["Allergy", "Sinus Infection", "Deviated Septum"],
    "runny nose": ["Common Cold", "Allergy", "Sinus Infection"],
    "facial swelling": ["Allergy", "Infection", "Kidney Disease"],
    "stiff neck": ["Meningitis", "Muscle Strain", "Cervical Spondylosis"],
    "neck pain": ["Muscle Strain", "Cervical Spondylosis", "Injury"],
    "shoulder pain": ["Rotator Cuff Injury", "Arthritis", "Frozen Shoulder"],
    "elbow pain": ["Tennis Elbow", "Arthritis", "Injury"],
    "wrist pain": ["Carpal Tunnel", "Arthritis", "Injury"],
    "hand numbness": ["Carpal Tunnel", "Neuropathy", "Cervical Radiculopathy"],
    "finger tingling": ["Carpal Tunnel", "Neuropathy", "Vitamin Deficiency"],
    "abdominal cramps": ["IBS", "Gastroenteritis", "Food Poisoning"],
    "acid reflux": ["GERD", "Ulcer", "Hiatal Hernia"],
    "acne": ["Hormonal Imbalance", "PCOS", "Skin Infection"],
    "agitation": ["Anxiety", "Hyperthyroidism", "Sleep Deprivation"],
    "aggression": ["Brain Injury", "Dementia", "Mental Disorder"],
    "anorexia": ["Depression", "Eating Disorder", "Cancer"],
    "ankle swelling": ["Heart Failure", "Kidney Disease", "Venous Insufficiency"],
    "anxiety": ["Generalized Anxiety Disorder", "Panic Disorder", "Hyperthyroidism"],
    "arm pain": ["Heart Attack", "Muscle Strain", "Nerve Compression"],
    "arm numbness": ["Stroke", "Neuropathy", "Cervical Radiculopathy"],
    "bleeding gums": ["Gingivitis", "Vitamin C Deficiency", "Blood Disorder"],
    "bloating": ["IBS", "Celiac Disease", "Constipation"],
    "blood in stool": ["Hemorrhoids", "Colon Cancer", "IBD"],
    "blurred vision": ["Glaucoma", "Diabetes", "Migraine"],
    "body aches": ["Flu", "Dengue", "Fibromyalgia"],
    "bone pain": ["Osteoporosis", "Cancer", "Fracture"],
    "breathlessness": ["Asthma", "Heart Failure", "COPD"],
    "bruising easily": ["Vitamin K Deficiency", "Blood Disorder", "Medication Side Effect"],
    "chest tightness": ["Asthma", "Heart Attack", "Anxiety"],
    "chills": ["Malaria", "Flu", "Sepsis"],
    "cold sweats": ["Heart Attack", "Hypoglycemia", "Shock"],
    "confusion": ["Stroke", "Dementia", "Hypoglycemia"],
    "constipation": ["IBS", "Hypothyroidism", "Low Fiber Diet"],
    "coughing blood": ["TB", "Lung Cancer", "Bronchitis"],
    "cramps": ["Menstrual Pain", "Dehydration", "Electrolyte Imbalance"],
    "dehydration": ["Heat Stroke", "Diarrhea", "Vomiting"],
    "delirium": ["Infection", "Drug Reaction", "Sepsis"],
    "depression": ["Major Depression", "Bipolar Disorder", "Thyroid Imbalance"],
    "diarrhea": ["Gastroenteritis", "IBS", "Lactose Intolerance"],
    "difficulty breathing": ["Asthma", "COPD", "Pneumonia"],
    "difficulty concentrating": ["ADHD", "Stress", "Thyroid Disorder"],
    "dizziness": ["Vertigo", "Low Blood Pressure", "Anemia"],
    "dry mouth": ["Diabetes", "Medication Side Effect", "Dehydration"],
    "dry skin": ["Eczema", "Hypothyroidism", "Psoriasis"],
    "ear pain": ["Ear Infection", "TMJ Disorder", "Tooth Infection"],
    "ear ringing": ["Tinnitus", "Hearing Loss", "Ear Infection"],
    "fatigue": ["Anemia", "Hypothyroidism", "Sleep Apnea"],
    "fainting": ["Heart Disease", "Low Blood Pressure", "Hypoglycemia"],
    "facial swelling": ["Allergy", "Kidney Disease", "Infection"],
    "fever": ["Flu", "COVID-19", "Malaria"],
    "frequent urination": ["Diabetes", "UTI", "Prostate Disease"],
    "frequent infections": ["Immune Deficiency", "Diabetes", "HIV"],
    "gastrointestinal bleeding": ["Ulcer", "Cancer", "Esophageal Varices"],
    "giddiness": ["Vertigo", "Dehydration", "Low Blood Sugar"],
    "hair loss": ["Alopecia", "Thyroid Disease", "Nutritional Deficiency"],
    "headache": ["Migraine", "Tension Headache", "Sinus Infection"],
    "heart palpitations": ["Arrhythmia", "Anxiety", "Hyperthyroidism"],
    "heartburn": ["GERD", "Ulcer", "Hiatal Hernia"],
    "hoarseness": ["Laryngitis", "Throat Cancer", "Vocal Strain"],
    "hot flashes": ["Menopause", "Hyperthyroidism", "Hormonal Imbalance"],
    "hunger pangs": ["Hypoglycemia", "Gastritis", "Stomach Ulcer"],
    "hypotension": ["Dehydration", "Heart Disease", "Endocrine Disorder"],
    "impaired coordination": ["Stroke", "Neuropathy", "Cerebellar Disease"],
    "indigestion": ["Gastritis", "GERD", "Ulcer"],
    "insomnia": ["Stress", "Sleep Apnea", "Depression"],
    "joint pain": ["Arthritis", "Gout", "Lupus"],
    "joint swelling": ["Arthritis", "Infection", "Gout"],
    "leg cramps": ["Dehydration", "Electrolyte Imbalance", "Peripheral Artery Disease"],
    "leg weakness": ["Neuropathy", "Stroke", "Muscle Disorder"],
    "lightheadedness": ["Anemia", "Dehydration", "Low Blood Pressure"],
    "loss of appetite": ["Cancer", "Depression", "Infection"],
    "loss of balance": ["Vertigo", "Neuropathy", "Cerebellar Disease"],
    "lumps": ["Cancer", "Cyst", "Lipoma"],
    "memory loss": ["Alzheimer's", "Vitamin B12 Deficiency", "Stroke"],
    "menstrual irregularities": ["PCOS", "Thyroid Disorder", "Hormonal Imbalance"],
    "muscle cramps": ["Electrolyte Imbalance", "Dehydration", "Peripheral Artery Disease"],
    "muscle weakness": ["Myopathy", "Neuropathy", "Stroke"],
    "nausea": ["Food Poisoning", "Pregnancy", "Migraine"],
    "neck pain": ["Muscle Strain", "Cervical Spondylosis", "Injury"],
    "numbness": ["Neuropathy", "Stroke", "Vitamin B12 Deficiency"],
    "night sweats": ["Tuberculosis", "Cancer", "Menopause"],
    "nosebleeds": ["Hypertension", "Dryness", "Bleeding Disorders"],
    "pale skin": ["Anemia", "Vitamin Deficiency", "Blood Loss"],
    "panic attacks": ["Anxiety Disorder", "PTSD", "Hyperthyroidism"],
    "palpitations": ["Arrhythmia", "Anxiety", "Thyroid Disease"],
    "persistent cough": ["TB", "Lung Cancer", "Chronic Bronchitis"],
    "persistent vomiting": ["Gastroenteritis", "Pregnancy", "Gastric Obstruction"],
    "poor concentration": ["ADHD", "Stress", "Thyroid Imbalance"],
    "rash": ["Allergy", "Eczema", "Chickenpox", "Measles"],
    "red eyes": ["Conjunctivitis", "Allergy", "Infection"],
    "restlessness": ["Anxiety", "Hyperthyroidism", "Stress"],
    "seizures": ["Epilepsy", "Brain Tumor", "Infection"],
    "shortness of breath": ["Asthma", "COPD", "Heart Failure"],
    "shoulder pain": ["Rotator Cuff Injury", "Arthritis", "Frozen Shoulder"],
    "skin discoloration": ["Liver Disease", "Vitiligo", "Bruising"],
    "sore throat": ["Tonsillitis", "Flu", "Common Cold", "Strep Throat"],
    "stiff neck": ["Meningitis", "Muscle Strain", "Cervical Spondylosis"],
    "stomach pain": ["Gastritis", "Food Poisoning", "Ulcer"],
    "sweating": ["Hyperthyroidism", "Infection", "Menopause"],
    "swollen lymph nodes": ["Infection", "Cancer", "Immune Disorders"],
    "tremors": ["Parkinson's", "Hyperthyroidism", "Stress"],
    "trouble swallowing": ["Throat Cancer", "Esophageal Disorder", "Neurological Problem"],
    "unexplained bruises": ["Blood Disorders", "Vitamin Deficiency", "Medication Side Effect"],
    "urinary frequency": ["Diabetes", "UTI", "Prostate Disease"],
    "urinary urgency": ["UTI", "Prostate Problem", "Overactive Bladder"],
    "vomiting blood": ["Ulcer", "Gastritis", "Esophageal Varices"],
    "weakness": ["Anemia", "Hypothyroidism", "Chronic Disease"],
    "weight gain": ["Hypothyroidism", "PCOS", "Cushing's Syndrome"],
    "weight loss": ["Diabetes", "Cancer", "Hyperthyroidism"],
    "yellowing of skin/eyes": ["Jaundice", "Hepatitis", "Liver Disease"]
}

symptom_keywords = {
    "nausea": "Stomach Pain", "vomiting": "Stomach Pain", "stomach": "Stomach Pain", "headache": "Headache", "dizzy": "Headache", "fever": "Fever", "chills": "Fever", "abdominal cramps": "Stomach Pain", "acid reflux": "Stomach Pain", "indigestion": "Stomach Pain", "bloating": "Stomach Pain", "constipation": "Stomach Pain", "diarrhea": "Stomach Pain", "vomiting": "Stomach Pain", "stomach pain": "Stomach Pain", "food intolerance": "Stomach Pain", "gastrointestinal bleeding": "Stomach Pain", "acidic burps": "Stomach Pain", "headache": "Headache", "dizzy": "Headache", "confusion": "Headache", "memory loss": "Headache", "fainting": "Headache", "lightheadedness": "Headache", "seizures": "Headache", "difficulty concentrating": "Headache", "poor concentration": "Headache", "agitation": "Headache", "aggression": "Headache", "fever": "Fever", "chills": "Fever", "cold sweats": "Fever", "night sweats": "Fever", "persistent cough": "Fever", "coughing blood": "Fever", "sore throat": "Fever", "runny nose": "Fever", "frequent infections": "Fever", "shortness of breath": "Breathing Problem", "difficulty breathing": "Breathing Problem", "breathlessness": "Breathing Problem", "wheezing": "Breathing Problem", "chest tightness": "Breathing Problem", "palpitations": "Heart Problem", "heart palpitations": "Heart Problem", "chest pain": "Heart Problem", "chest tightness": "Heart Problem", "cold hands/feet": "Heart Problem", "swelling": "Heart Problem", "ankle swelling": "Heart Problem", "joint pain": "Muscle/Joint Pain", "joint swelling": "Muscle/Joint Pain", "joint stiffness": "Muscle/Joint Pain", "morning stiffness": "Muscle/Joint Pain", "muscle cramps": "Muscle/Joint Pain", "muscle weakness": "Muscle/Joint Pain", "muscle pain": "Muscle/Joint Pain", "leg cramps": "Muscle/Joint Pain", "leg weakness": "Muscle/Joint Pain", "back pain": "Muscle/Joint Pain", "shoulder pain": "Muscle/Joint Pain", "neck pain": "Muscle/Joint Pain", "elbow pain": "Muscle/Joint Pain", "wrist pain": "Muscle/Joint Pain", "foot pain": "Muscle/Joint Pain", "heel pain": "Muscle/Joint Pain", "rash": "Skin Problem", "acne": "Skin Problem", "dry skin": "Skin Problem", "skin discoloration": "Skin Problem", "hair loss": "Skin Problem", "hair thinning": "Skin Problem", "pale skin": "Skin Problem", "yellowing of skin/eyes": "Skin Problem", "red eyes": "Skin Problem", "facial swelling": "Skin Problem", "frequent urination": "Urinary Problem", "urinary frequency": "Urinary Problem", "urinary urgency": "Urinary Problem", "blood in urine": "Urinary Problem", "burning urination": "Urinary Problem", "anxiety": "Mental Health", "panic attacks": "Mental Health", "depression": "Mental Health", "restlessness": "Mental Health", "insomnia": "Mental Health", "excessive sleep": "Mental Health", "blurred vision": "Eye Problem", "sensitivity to light": "Eye Problem", "ear pain": "Ear Problem", "ear ringing": "Ear Problem", "hearing loss": "Ear Problem", "nosebleeds": "ENT Problem", "frequent nose congestion": "ENT Problem", "fatigue": "General Weakness", "chronic fatigue": "General Weakness", "weakness": "General Weakness", "weight loss": "General Weakness", "weight gain": "General Weakness", "loss of appetite": "General Weakness", "hunger pangs": "General Weakness", "excessive sweating": "General Weakness", "hot flashes": "General Weakness", "pale skin": "General Weakness", "delirium": "General Weakness", "agitation": "General Weakness", "giddiness": "General Weakness", "abnormal bleeding": "General Weakness", "unexplained bruises": "General Weakness", "lumps": "General Weakness"
}

tly
LOGO_PATH = r"C:\Users\Nemitha\OneDrive\Desktop\istockphoto-1578253407-612x612.jpg"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Health Assistant")
        self.geometry("500x600")
        self.resizable(False, False)

        self.logo_photo = None
        self.logo_label = None


        try:
            icon_image = Image.open(LOGO_PATH)
            icon_image = icon_image.resize((64, 64), Image.Resampling.LANCZOS)
            self.wm_iconphoto(True, ImageTk.PhotoImage(icon_image))
        except Exception as e:
            print(f"Error loading icon: {e}")


        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True)

        self.display_logo_and_start()

    def display_logo_and_start(self):

        for widget in self.content_frame.winfo_children():
            widget.destroy()


        try:
            logo_image = Image.open(LOGO_PATH)
            logo_image = logo_image.resize((300, 300), Image.Resampling.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            self.logo_label = ctk.CTkLabel(self.content_frame, image=self.logo_photo, text="")
            self.logo_label.pack(expand=True, padx=20, pady=20)
        except Exception as e:
            print(f"Error loading logo for splash screen: {e}")
            self.logo_label = ctk.CTkLabel(self.content_frame, text="Health Assistant", font=("Arial", 24, "bold"))
            self.logo_label.pack(expand=True, padx=20, pady=20)


        threading.Thread(target=self.delayed_start).start()

    def delayed_start(self):
        time.sleep(3)  # Wait fos
        self.after(0, self.setup_main_ui)

    def setup_main_ui(self):

        if self.logo_label:
            self.logo_label.destroy()
        

        self.main_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        

        self.heading_label = ctk.CTkLabel(
            self.main_frame,
            text="",
            font=("Roboto", 24, "bold"),
            wraplength=450
        )
        self.heading_label.pack(pady=(20, 10))
        

        self.scrollable_frame = ctk.CTkScrollableFrame(self.main_frame, fg_color=("#3a4f61", "#2c3e50"))
        self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.start_screen()
        
    def type_text(self, label, text, index=0):
        if index < len(text):
            label.configure(text=label.cget("text") + text[index])
            self.after(15, lambda: self.type_text(label, text, index + 1))
            
    def clear_content(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

    def start_screen(self):
        self.clear_content()
        self.heading_label.configure(text="")
        self.type_text(self.heading_label, "Welcome! Choose an option:")


        button_width = 300
        button_height = 60
        button_font = ("Roboto", 18, "bold")

        symptom_btn = ctk.CTkButton(
            self.scrollable_frame,
            text="Symptom Checker",
            command=self.symptom_checker_screen,
            width=button_width,
            height=button_height,
            font=button_font,
            corner_radius=10 
        )
        symptom_btn.pack(pady=20, ipadx=20, ipady=10)

        bmi_btn = ctk.CTkButton(
            self.scrollable_frame,
            text="BMI Calculator",
            command=self.bmi_screen,
            width=button_width,
            height=button_height,
            font=button_font,
            corner_radius=10
        )
        bmi_btn.pack(pady=20, ipadx=20, ipady=10)

        calorie_btn = ctk.CTkButton(
            self.scrollable_frame,
            text="Calorie Counter",
            command=self.calorie_counter_screen,
            width=button_width,
            height=button_height,
            font=button_font,
            corner_radius=10
        )
        calorie_btn.pack(pady=20, ipadx=20, ipady=10)
        
        about_btn = ctk.CTkButton(
            self.scrollable_frame,
            text="About",
            command=self.about_screen,
            width=button_width,
            height=button_height,
            font=button_font,
            corner_radius=10
        )
        about_btn.pack(pady=20, ipadx=20, ipady=10)
        
        developed_by_label = ctk.CTkLabel(
            self.scrollable_frame,
            text="Developed by Nemitha Prabashwara",
            font=("Roboto", 12),
            text_color="#888888"
        )
        developed_by_label.pack(pady=(20, 5))



    def symptom_checker_screen(self):
        self.clear_content()
        self.heading_label.configure(text="")
        self.type_text(self.heading_label, "Describe your symptoms in detail:")

        self.text_widget = ctk.CTkTextbox(self.scrollable_frame, height=200, width=400, corner_radius=10)
        self.text_widget.pack(pady=20)

        check_btn = ctk.CTkButton(
            self.scrollable_frame,
            text="Check Symptoms",
            command=lambda: self.analyze_symptoms(self.text_widget.get("1.0", "end")),
            corner_radius=10
        )
        check_btn.pack(pady=10)
        
        back_btn = ctk.CTkButton(
            self.scrollable_frame,
            text="Back",
            command=self.start_screen,
            fg_color="transparent",
            border_color="gray",
            border_width=2,
            text_color="white",
            corner_radius=10
        )
        back_btn.pack(pady=5)

    def analyze_symptoms(self, symptoms_text):
        import re
        from difflib import get_close_matches


        symptoms_text = symptoms_text.lower()
        symptoms = [s.strip() for s in re.split(r"[,\sand]+", symptoms_text) if s.strip()]

        if not symptoms:
            self.heading_label.configure(text="Please enter at least one symptom.")
            return

        matched_symptoms = set()
        db_keys = [k.lower() for k in diseases_db.keys()]

        for user_symptom in symptoms:
            matched = False

            for keyword, standardized_symptom in symptom_keywords.items():
                if keyword.lower() in user_symptom:
                    matched_symptoms.add(standardized_symptom.lower())
                    matched = True

            if not matched:
                close = get_close_matches(user_symptom, db_keys, n=1, cutoff=0.6)
                if close:
                    matched_symptoms.add(close[0])
                    matched = True

            if not matched:
                for db_key in db_keys:
                    if user_symptom in db_key or db_key in user_symptom:
                        matched_symptoms.add(db_key)
                        matched = True

            if not matched:
                matched_symptoms.add(user_symptom)


        all_conditions = []
        for s in matched_symptoms:
            matched_conditions = set()
            for db_key, diseases in diseases_db.items():
                if s == db_key.lower() or s in db_key.lower() or db_key.lower() in s:
                    matched_conditions.update(diseases)
            if matched_conditions:
                all_conditions.append(matched_conditions)


        if len(all_conditions) > 1:
            common_conditions = set.intersection(*all_conditions)
            if common_conditions:
                results = list(common_conditions)
            else:
                results = ["No exact common disease found. Possible conditions include:"] + list(set.union(*all_conditions))
        elif len(all_conditions) == 1:
            results = list(all_conditions[0])
        else:
            results = ["No common diseases found for the given symptoms. Please consult a doctor."]

        self.show_symptom_results(results)



    def show_symptom_results(self, conditions):
        self.clear_content()
        self.heading_label.configure(text="")
        self.type_text(self.heading_label, "Possible Conditions:")

        for i, cond in enumerate(conditions):
            lbl = ctk.CTkLabel(
                self.scrollable_frame,
                text=f"• {cond}",
                font=("Roboto", 14),
                wraplength=400,
                anchor="w",
                justify="left"
            )
            lbl.pack(pady=5, fill="x", padx=10)
            
        back_btn = ctk.CTkButton(
            self.scrollable_frame,
            text="Back",
            command=self.symptom_checker_screen,
            fg_color="transparent",
            border_color="gray",
            border_width=2,
            text_color="white",
            corner_radius=10
        )
        back_btn.pack(pady=(20,5))
        
        home_btn = ctk.CTkButton(
            self.scrollable_frame,
            text="Home",
            command=self.start_screen,
            corner_radius=10
        )
        home_btn.pack(pady=5)

    def bmi_screen(self):
        self.clear_content()
        self.heading_label.configure(text="")
        self.type_text(self.heading_label, "Enter your details to calculate BMI:")
        
        entries = {}
        fields = ["Weight (kg)", "Height (cm)"]
        for f in fields:
            lbl = ctk.CTkLabel(self.scrollable_frame, text=f)
            lbl.pack(pady=(10, 0))
            ent = ctk.CTkEntry(self.scrollable_frame, corner_radius=10)
            ent.pack(pady=5)
            entries[f] = ent

        result_lbl = ctk.CTkLabel(self.scrollable_frame, text="", font=("Roboto", 16, "bold"))
        result_lbl.pack(pady=10)
        
        def calculate_bmi():
            try:
                weight = float(entries["Weight (kg)"].get())
                height = float(entries["Height (cm)"].get()) / 100
                bmi = weight / (height ** 2)
                bmi = round(bmi, 2)
                result_lbl.configure(text=f"Your BMI is: {bmi}", text_color="green")
            except ValueError:
                result_lbl.configure(text="Invalid input. Please enter numbers only.", text_color="red")
        
        calc_btn = ctk.CTkButton(self.scrollable_frame, text="Calculate BMI", command=calculate_bmi, corner_radius=10)
        calc_btn.pack(pady=10)
        
        back_btn = ctk.CTkButton(
            self.scrollable_frame,
            text="Back",
            command=self.start_screen,
            fg_color="transparent",
            border_color="gray",
            border_width=2,
            text_color="white",
            corner_radius=10
        )
        back_btn.pack(pady=5)

    def calorie_counter_screen(self):
        self.clear_content()
        self.heading_label.configure(text="")
        self.type_text(self.heading_label, "Enter details to calculate daily calorie goal:")
        
        entries = {}
        fields = ["Gender (M/F)", "Age", "Current Weight (kg)", "Target Weight (kg)", "Height (cm)", "Activity Level (1-4)", "Days to achieve target"]
        for f in fields:
            lbl = ctk.CTkLabel(self.scrollable_frame, text=f)
            lbl.pack(pady=(10, 0))
            ent = ctk.CTkEntry(self.scrollable_frame, corner_radius=10)
            ent.pack(pady=5)
            entries[f] = ent

        result_lbl = ctk.CTkLabel(self.scrollable_frame, text="", font=("Roboto", 16, "bold"))
        result_lbl.pack(pady=10)
        
        def calculate_calories():
            try:
                gender = entries["Gender (M/F)"].get().upper()
                if gender not in ["M", "F"]:
                    raise ValueError("Gender must be 'M' or 'F'")
                age = int(entries["Age"].get())
                weight = float(entries["Current Weight (kg)"].get())
                target = float(entries["Target Weight (kg)"].get())
                height = float(entries["Height (cm)"].get())
                activity = int(entries["Activity Level (1-4)"].get())
                if activity not in [1, 2, 3, 4]:
                    raise ValueError("Activity level must be 1, 2, 3, or 4")
                days = int(entries["Days to achieve target"].get())

                if gender == "M":
                    BMR = 10 * weight + 6.25 * height - 5 * age + 5
                else:
                    BMR = 10 * weight + 6.25 * height - 5 * age - 161

                act_mult = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725}.get(activity)
                TDEE = BMR * act_mult

                if target < weight:
                    total_cal_deficit = (weight - target) * 7700
                    daily_cal_goal = TDEE - total_cal_deficit / days
                else:
                    total_cal_surplus = (target - weight) * 7700
                    daily_cal_goal = TDEE + total_cal_surplus / days

                result_lbl.configure(text=f"Daily Calorie Goal: {round(daily_cal_goal, 2)} kcal", text_color="green")
            except ValueError as e:
                result_lbl.configure(text=f"Invalid input: {e}", text_color="red")
            except Exception as e:
                result_lbl.configure(text="An error occurred. Please check all fields.", text_color="red")

        calc_btn = ctk.CTkButton(self.scrollable_frame, text="Calculate Calories", command=calculate_calories, corner_radius=10)
        calc_btn.pack(pady=10)
        
        back_btn = ctk.CTkButton(
            self.scrollable_frame,
            text="Back",
            command=self.start_screen,
            fg_color="transparent",
            border_color="gray",
            border_width=2,
            text_color="white",
            corner_radius=10
        )
        back_btn.pack(pady=5)


    def about_screen(self):
        self.clear_content()
        self.heading_label.configure(text="")
        self.type_text(self.heading_label, "About")


        try:
            logo_image = Image.open(LOGO_PATH)
            logo_image = logo_image.resize((150, 150), Image.Resampling.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
            logo_label = ctk.CTkLabel(self.scrollable_frame, image=self.logo_photo, text="")
            logo_label.pack(pady=(20, 10))
        except Exception as e:
            print(f"Error loading logo for about screen: {e}")
            logo_label = ctk.CTkLabel(self.scrollable_frame, text="Health Assistant", font=("Arial", 20, "bold"))
            logo_label.pack(pady=(20, 10))


        about_text = (
            "This Health Assistant application is designed to provide quick and accessible "
            "health information. It features a Symptom Checker to identify potential "
            "conditions based on user-input symptoms, a BMI Calculator to assess body mass, "
            "and a Calorie Counter to help set daily nutritional goals.\n\n"
            "This tool is intended for informational purposes and should not replace "
            "professional medical advice. Always consult a qualified healthcare provider "
            "for diagnosis, treatment, and medical guidance."
        )
        
        ctk.CTkLabel(
            self.scrollable_frame, 
            text=about_text, 
            wraplength=400, 
            justify="center", 
            font=("Roboto", 14)
        ).pack(pady=(0, 20), padx=10)


        ctk.CTkLabel(
            self.scrollable_frame,
            text="Developer",
            font=("Roboto", 18, "bold")
        ).pack(pady=(10, 5))
        
        ctk.CTkLabel(
            self.scrollable_frame,
            text="Nemitha Prabashwara",
            font=("Roboto", 14)
        ).pack(pady=5)

        # Contact heading
        ctk.CTkLabel(
            self.scrollable_frame,
            text="Contact",
            font=("Roboto", 18, "bold")
        ).pack(pady=(10, 5))

        ctk.CTkLabel(
            self.scrollable_frame,
            text=f"Email: nemithaprs@gmail.com",
            font=("Roboto", 14)
        ).pack(pady=5)

        ctk.CTkLabel(
            self.scrollable_frame,
            text=f"Instagram: nemitha_prs",
            font=("Roboto", 14)
        ).pack(pady=5)
        
 n
        back_btn = ctk.CTkButton(
            self.scrollable_frame,
            text="Back",
            command=self.start_screen,
            fg_color="transparent",
            border_color="gray",
            border_width=2,
            text_color="white",
            corner_radius=10
        )
        back_btn.pack(pady=(20, 5))


if __name__ == "__main__":
    app = App()
    app.mainloop()
