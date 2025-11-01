# PROJECT TITLE:  🎧 Spotify Data Analysis Project

## 📘 Overview
This project explores the characteristics that make songs popular on Spotify.  
Using a dataset of 114,000 tracks, I analyzed how musical features such as danceability, energy, valence, and tempo relate to song popularity.

The project was completed as part of my **Data Analytics Portfolio**, demonstrating skills in Python, data visualization, and analytical storytelling.

---

## 🎯 Objectives
- Run an **end-to-end data analysis** project.
- Explore relationships between song features and popularity.
- Practice **data cleaning, wrangling, and visualization**.
- Communicate findings effectively using **Jupyter Notebook** and GitHub.

---

## 🧩 Dataset
- **Source:** [Kaggle – Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
- **Description:** Contains track-level information including artist, album, popularity, and 10+ audio features.
- **Size:** 114,000 records × 21 columns.

---

## 🧠 Key Skills Demonstrated
- Python (pandas, numpy, matplotlib, seaborn)
- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Correlation and comparative analysis
- Data visualization and storytelling
- Git & GitHub version control
- Jupyter Notebook documentation

---

## 📊 Key Insights
1. Most songs have **moderate popularity**; very few reach top levels.
2. **Danceability**, **energy**, and **valence** show the strongest relationships with popularity.
3. **Pop**, **Dance**, and **Hip-Hop** genres dominate among high-popularity tracks.
4. **Explicit songs** are slightly more popular on average, but not by much.

---

## 🧰 Project Structure

dsa_final_project/
│
├── data/
│ ├── raw/ # Original dataset
│ └── processed/ # Cleaned data (if applicable)
│
├── notebooks/
│ └── spotify_analysis.ipynb # Main analysis notebook
│
├── src/ # Helper scripts (data loading, etc.)
│
├── figures/ # Plots and visualizations
│
├── reports/ # Summary or PDF exports (optional)
│
├── README.md # Project documentation (this file)
└── .gitignore


## FIRST STUDY:
# Project Title 
Data analytics portfolio Project

## Overview 

Data analytics portfolio is your secret weapon when applying for potential positions. It should not only show off your skills and experience but give your interviewers insight into how you tackle data analytics problems. Your portfolio should highlight to hiring managers how you thought about, worked through, and visualized your results. In this final portfolio project, you’ll use your understanding of data analytics and visualization to answer a question about a topic of your choosing.

## Goals  
What question are you trying to answer?
Why does it matter (business/research/personal interest)?

🔹 Project Scope (Spotify Popularity Analysis)
1. My Project Goal

- Analyze Spotify tracks to understand what audio features (danceability, energy, tempo, etc.) are associated with song popularity.

2. Dataset
- Source: Spotify Tracks Dataset (Kaggle)
- Size/Format: CSV file with ~100,000+ tracks, includes features like:
danceability, energy, tempo, loudness, speechiness, acousticness, instrumentalness, valence, duration_ms
popularity (target variable)
artist_name, track_name, release_date, genre


🔹 Task 4: Load and Check Data (Jupyter Notebook)


3. Methods / Analysis Plan
⦁	Data Acquisition & Cleaning
⦁	Load dataset (CSV) into Pandas.
⦁	Handle missing values, duplicates.
⦁	Convert time-related variables (release_date → year).
⦁	
⦁	Exploratory Data Analysis (EDA)
⦁	Summary statistics (mean, median, std of features).
⦁	Visualizations:
⦁	Histogram of popularity distribution.
⦁	Correlation heatmap of features.
⦁	Scatterplots (e.g., energy vs. popularity).
⦁	Genre-level averages.

4. Deliverables

⦁	Jupyter Notebook (notebooks/spotify_analysis.ipynb) with code + commentary.
⦁	Visualizations (figures/).
⦁	Short report in README.md summarizing findings.

# plan
- Complete a project to add to a portfolio
- Use Git version control
- Use Jupyter Notebook to communicate findings
- Run an end-to-end data analytics project
- Become familiar with data analytics workflows

## Prerequisites:
- Python Fundamentals
- Data Acquisition
- Data Manipulation with Pandas
- Data Wrangling and Tidying
- Summary Statistics
- Hypothesis Testing
- Data Visualization
- Communicating Data Analysis Findings

## Data 

Dataset(s)
What data will you use?
Is it publicly available?
Rough size/format (CSV, API, etc.).

- Source: [link or citation] 
Check out these helpful resources:
⦁	Matplotlib tutorial
⦁	seaborn examples
⦁	NumPy tutorial
⦁	pandas user guide
- Files included: `data/raw/...` 

## Methods / Analysis Plan
- What kind of analysis will you run? (e.g., summary stats, correlations, hypothesis tests, predictive modeling).
- What visualizations might be useful?

## Deliverables

- Jupyter Notebook with code + explanations.
- Visualizations/plots.
- Short report/summary in README.md or a report/ folder.

## How to run 

1. Create virtualenv and install dependencies: 
   `pip install -r requirements.txt` 
2. Open `notebooks/01-exploratory.ipynb` in Jupyter. 

## Repository structure 
(briefly explain folders) 

## License 
MIT (or your choice) 

## Contact 
Altan Kayabasi — altankayabasi3@gmail.com