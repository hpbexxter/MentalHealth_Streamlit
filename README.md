# 🧠 Mental Health in the Tech Industry

An interactive Streamlit dashboard for exploring mental health and burnout indicators among employees in the tech industry.

The application provides insights into a large synthetic dataset containing information about mental health, job roles, seniority levels, and workplace-related factors. The primary focus is the analysis and prediction of depressive symptoms using the **PHQ-9 (Patient Health Questionnaire-9)** score.

## 📖 Project Overview

Mental health has become an increasingly important topic in modern workplaces, especially within the tech sector. This project aims to analyze factors that may influence depressive symptoms among tech employees and identify workplace characteristics associated with mental well-being.

The dashboard includes:

* 🏠 **Overview Dashboard**

  * General project information
  * Dataset summary statistics
  * Gender and seniority distributions
  * PHQ-9 score explanation and severity scale

* 📊 **Data Analysis**

  * Statistical evaluation of the dataset
  * Investigation of relationships between professional factors and mental health indicators

* 📈 **Data Visualization**

  * Exploratory data analysis (EDA)
  * Interactive charts and visual insights

* 🆘 **Mental Health Resources**

  * Links to professional support services and mental health organizations

* ⬇️ **Resources & Downloads**

  * Access to the project repository
  * Original dataset source
  * Download cleaned dataset as CSV

## 📊 Dataset

The application uses a synthetic dataset focused on mental health and burnout among employees.

Dataset characteristics include:

* ~90,000 employees
* 10 industries
* 12 different professions
* International data coverage
* Mental health indicators based on established clinical assessment methods

The analysis primarily focuses on the **PHQ-9 score**, a clinically validated screening tool used to assess depressive symptoms.

> **Note:** The dataset is synthetic. It is not known whether the data is based on real-world surveys or entirely generated.

## 🔎 What is the PHQ-9 Score?

The **Patient Health Questionnaire-9 (PHQ-9)** is a widely used clinical instrument for assessing depression severity.

It consists of 9 questions covering symptoms such as:

* Loss of interest or pleasure
* Depressed mood
* Sleep disturbances
* Fatigue
* Appetite changes
* Feelings of guilt or worthlessness
* Difficulty concentrating
* Psychomotor agitation or slowing
* Suicidal thoughts

Each question is rated from **0 (not at all)** to **3 (nearly every day)**, resulting in a total score between **0 and 27**.

Higher scores indicate more severe depressive symptoms.

## 🛠️ Technology Stack

* Python
* Streamlit
* Plotly
* Pandas
* NumPy

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/hpbexxter/MentalHealth_Streamlit.git
cd MentalHealth_Streamlit
```

Create a virtual environment and install all dependencies:

```bash
make install
```

This command will:

1. Create a Python virtual environment (`.venv`)
2. Upgrade `pip`
3. Install all required dependencies from `requirements.txt`

## ▶️ Running the Application

Start the Streamlit application:

```bash
make run
```

Alternatively:

```bash
streamlit run app.py
```

The application will be available in your browser at:

```text
http://localhost:8501
```

## 🧹 Cleaning Temporary Files

To remove Python cache files and `__pycache__` directories:

```bash
make clean
```

## 📁 Project Structure

```text
.
├── app.py
├── pages/
├── utils/
│   ├── utils.py
├── assets/
│   ├── github.png
│   ├── kaggle.png
│   └── ...
├── requirements.txt
├── Makefile
└── README.md
```

## 📚 Data Source

The dataset used in this project originates from a Kaggle dataset on mental health and burnout among tech workers.

## ⚠️ Disclaimer

This project is intended for educational and analytical purposes only.

The presented analyses do not constitute medical advice, diagnosis, or treatment recommendations. Mental health assessments should always be performed by qualified healthcare professionals.
