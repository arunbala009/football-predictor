#  European Football Match Predictor

A Machine Learning-powered web application that predicts football match outcomes for top European clubs across the Top 5 leagues.

Live App:(https://football-predictor-78febfwlzfvarjvweizi6m.streamlit.app/)

Model Link: https://colab.research.google.com/drive/1laRz3C6jhbJsCuuhky6kIqTYkKJHa7T6?usp=sharing

## Overview

This project predicts the outcome of football matches using historical match statistics and machine learning techniques. Users can select teams and input match details through an interactive Streamlit interface.

The model predicts:

- Home Win
- Draw
- Away Win

The project is inspired by sports prediction platforms and adapted for European football.

---

## Supported Leagues

- Premier League
- La Liga
- Bundesliga
- Serie A
- Ligue 1

### Featured Clubs
Includes top teams such as:

- Real Madrid
- Barcelona
- Manchester City
- Arsenal
- Liverpool
- Bayern Munich
- Inter Milan
- Paris Saint-Germain
- and more

---

## Features

 Match outcome prediction  
 Interactive Streamlit UI  
 Team selection dropdowns  
 Machine learning model integration  
 Deployment on Streamlit Cloud  
 Trained on historical football data  

---

## Dataset

Historical football datasets were collected and merged from multiple seasons.

Data sources:

- Football-Data.co.uk
- Kaggle football datasets

Features used include:

- Home Team
- Away Team
- Goals scored
- Shots
- Shots on target
- Match results

---

## Machine Learning Workflow

1. Collect historical datasets
2. Merge league data
3. Clean and preprocess
4. Encode team names
5. Train prediction model
6. Save trained model
7. Deploy using Streamlit

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- XGBoost
- Pickle
- Git
- GitHub

---

## Project Structure

```text
football-predictor/
│
├── app.py
├── model.pkl
├── encoder.pkl
├── requirements.txt
├── README.md
```

## Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/football-predictor.git
```

Open folder:

```bash
cd football-predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```

---
Screenshots:
<img width="1915" height="1079" alt="image" src="https://github.com/user-attachments/assets/71be9e22-6b00-4ff5-aae9-2d73bc8ad7fa" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/532a3597-336c-477b-b0f4-f757dd809b6b" />

---



## Further Improvements Possible

- Team logos
- Head-to-head statistics
- Last 5 match form
- Live API integration
- Match probability charts
- Player statistics
- Dark themed dashboard

---

## Author

Arun Bala

Built using Machine Learning and Streamlit.
