## 🔐 Real-Time Unauthorized Network Access Detection
## CyberSec-PBL | SOC-Style Security Monitoring Platform
## 📌 Project Overview

This project implements a SOC (Security Operations Center)–style monitoring platform to detect unauthorized or malicious network access in near real time.
It integrates Intrusion Detection Systems (IDS), Machine Learning–based anomaly detection, and Behavioral Analytics (UEBA) into a single automated dashboard with real-time alerts.

The system is designed to detect:
Known attacks using signature-based IDS
Unknown / zero-day attacks using ML
Insider threats using behavioral analysis
This project was developed as part of Project-Based Learning (PBL) under the domain of Cyber Security.

## 🎯 Objectives

Monitor and analyze network and user activity
Detect known attacks using IDS (Suricata)
Detect unknown or anomalous traffic using ML
Detect insider threats using behavioral analytics
Generate real-time WhatsApp alerts
Visualize security events on a centralized dashboard
Automate detection without manual script execution

## 🧠 Detection Techniques Implemented
1️⃣ Intrusion Detection System (IDS)
Tool used: Suricata
Signature-based detection
Detects known attack patterns from live or captured traffic
Live detection from network interface
Generates real-time alerts and logs

2️⃣ Anomaly Detection (Machine Learning)
Algorithm: Isolation Forest
Dataset: UNSW-NB15
Trained only on normal traffic
Detects deviations as anomalous activity
Capable of identifying unknown / zero-day attacks

3️⃣ Behavioral Analytics (UEBA)
Rule-based user behavior analysis
Detects:
Abnormal login times
Excessive connection attempts
High data transfer
Sensitive port access
Effective for detecting insider threats and misuse

## 🚨 Real-Time Alerting
Alerts are sent automatically via WhatsApp (Twilio Sandbox),TelegramBot
Triggered when:
ML detects anomalous traffic
UEBA detects suspicious user behavior
Simulates enterprise SOC alerting workflows

## 📊 Security Dashboard
Built using Flask
Auto-refreshes every 10 seconds
Displays:
ML anomaly counts
UEBA suspicious user counts
Visualized using Chart.js
Fully automated (no manual execution required)

## 🏗️ System Architecture (High-Level)
Network Traffic / Dataset
        │
        ▼
 ┌─────────────┬──────────────────┬──────────────────┐
 │   IDS       │  Anomaly ML       │   UEBA           │
 │ (Suricata)  │ (IsolationForest) │ (Behavior Rules) │
 └─────────────┴──────────────────┴──────────────────┘
        │
        ▼
 Real-Time Alerts (WhatsApp) + Logs
        │
        ▼
   Flask SOC Dashboard (Charts)

## 📂 Project Structure

```
realtime_ids/
├── alerts/
│   ├── telegram_alert.py                    # Telegram alert integration
│   └── whatsapp_alert.py                    # WhatsApp alert integration
├── anomaly_detection/
│   ├── detect_anomaly.py                    # ML anomaly detection logic
│   ├── train_model.py                       # Model training
│   ├── test_model.py                        # Model testing
│   ├── preprocess.py                        # Data preprocessing
│   └── data/
│       ├── UNSW_NB15_training-set.csv      # Training dataset
│       ├── UNSW_NB15_testing-set.csv       # Testing dataset
│       ├── train_normal.csv                # Processed training data
│       └── anomaly_results.csv             # ML output
├── behavioral_analytics/
│   ├── behavior_model.py                    # UEBA logic
│   ├── behavior_results.csv                # UEBA output
│   └── user_logs.csv                       # User behavior data
├── dashboard/
│   ├── app.py                              # Flask backend
│   └── templates/
│       └── index.html                      # Dashboard UI with charts
├── ids/
│   ├── suricata_reader.py                  # Live Suricata detection
│   ├── custom.rules                        # Custom IDS rules
│   └── [app-layer, dns, http, ssh, etc.]   # IDS rule files
├── data/
│   ├── UNSW_NB15_training-set.csv
│   ├── UNSW_NB15_testing-set.csv
│   ├── train_normal.csv
│   ├── anomaly_results.csv
│   └── behavior_results.csv
├── __init__.py
└── README.md
```

## 🛠️ Technologies Used
Operating System: Kali Linux / Ubuntu
IDS: Suricata
Programming Language: Python
Machine Learning: Scikit-learn, Pandas, NumPy
Visualization: Flask, Chart.js
Alerts: Twilio WhatsApp Sandbox
Dataset: UNSW-NB15

## ▶️ How to Run the Project
1️⃣ Train the ML model (one-time)
python3 anomaly_detection/train_model.py

2️⃣ Start the dashboard (auto-runs everything)
python3 dashboard/app.py

3️⃣ Open in browser
http://127.0.0.1:5000

## 🧪 Real-Time Testing
Near real-time testing via dashboard auto-refresh
Live traffic detection using Suricata:
sudo suricata -i eth0
Live detection automatically monitors network interface
Generate traffic using ping, nmap, etc.
Alerts and dashboard update automatically

## 📈 Evaluation Metrics
Detection accuracy
Anomaly detection count
Behavioral anomaly detection
Alert responsiveness
System automation effectiveness

## 🚀 Future Enhancements
SIEM / ELK stack integration
Kafka-based streaming detection
Deep learning–based models
Cloud deployment
Role-based SOC dashboards
Advanced threat hunting capabilities

## 👨‍💻 Author
Vikram (Trishula)
B.Tech – Data Science
Cyber Security & IOT Enthusiast

## 📜 Disclaimer
This project is developed strictly for educational and academic purposes.
