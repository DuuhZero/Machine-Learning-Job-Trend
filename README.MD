# 📊 ML Job Trends Visualizer

Welcome to the **ML Job Trends Visualizer** — a project for analyzing and visualizing the most in-demand Machine Learning job roles over time, based on real-world job posting data from the United States.

---

## 🎯 Purpose

This repository aims to:

### - Identify which ML job titles are most frequently posted over time.
### - Visualize hiring trends using clear, interactive line charts.
### - Provide a practical example of using **Python**, **Pandas**, and **Matplotlib** for real data analysis.

---

## 📁 Project Structure

Machine-Learning-Job-Trend/

├── 1000_ml_jobs_us.csv  - `Dataset containing 1000 ML job listings (US)`

├── ML-Job-trend-plot.py - `Script for trend visualization`

├── ML-Job-AlongTime-trend-plot.py - `Script for trend visualization along the time`

├── requirements.txt -  `List of required Python packages`

├── README.md - `Project description and usage guide`

└── .gitignore - `Files/folders to be ignored by Git`


---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/DuuhZero/Machine-Learning-Job-Trend.git

cd ml-job-trends-visualizer
```

### 2. (Optional) Create a virtual environment

```bash
python3 -m venv venv

source venv/bin/activate          # On Windows: venv\Scripts\activate
```

### 3. Install the required packages
```bash
pip install -r requirements.txt
```

### 4. Run the script
```bash
python ML-Job-trend-plot.py
```
#### And

```bash
python ML-Job-AlongTime-trend-plot.py
```



## 🛠️ Technologies Used

    Python 3

    Pandas

    Matplotlib

    Numpy

## 📌 Notes

### - The dataset must include a column with job posting dates (job_posted_date) and job titles (job_title).

### - You can modify the number of job titles visualized by editing the head(10) line in the script.

## 📬 Contact

### Feel free to fork this repo or open issues!

### Created by DuuhZero
