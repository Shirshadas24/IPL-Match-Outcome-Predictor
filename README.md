# 🏏 IPL Match Outcome Predictor

An interactive web app built with **Streamlit** that predicts the chances of winning an IPL match based on live match inputs like score, target, overs, wickets, etc.

## 🔍 Features
- Predict match-winning chances using ML classification
- Choose batting and bowling teams, venue, and live stats
- Built with scikit-learn, pandas, and Streamlit
- Trained on IPL 2008–2022 ball-by-ball data

## 🛠️ Tech Stack
- Python, Pandas, Scikit-learn
- Streamlit (for UI)
- Pickle (for model persistence)
- Jupyter Notebook (for training)

## 📂 Files
- `app.py` – Streamlit frontend
- `ra_pipe.pkl` – Trained model pipeline
- `data/` – Contains IPL datasets

## 🚀 Run Locally

```bash
git clone https://github.com/Shirshadas24/IPL-Match-Outcome-Predictor.git
cd ipl-match-predictor
pip install -r requirements.txt
streamlit run app.py

![App Screenshot](assets/screenshot.png)
