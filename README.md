# 🍅 Tomato Disease Prediction System

## 1. Title of the Application Based Mini Project

**Tomato Disease Prediction System**

---

## 2. Student Name and Roll Number

**Student Name:** Rupali Nagesh Akkewar

**Branch:** Electronics and Telecommunication Engineering (ETC)

**Semester:** V Semester

**Roll Number:** BT240003ET__________

**Course:** Natural Language Processing (ET5M004)

---

## 3. Problem Statement / Objective

### Problem Statement

Tomato crops can be affected by different diseases due to environmental and soil conditions such as temperature, humidity, rainfall, soil pH, and season.

Identifying the possible disease at an early stage can help farmers take preventive measures and reduce crop losses.

### Objective

The objective of this project is to develop a Machine Learning based system that:

- Accepts location from the user.
- Accepts crop name from the user.
- Accepts soil pH value.
- Accepts season from the user.
- Uses environmental parameters such as temperature, humidity, and rainfall.
- Predicts the possible tomato disease.
- Displays prediction confidence.
- Determines the risk level.
- Provides preventive recommendations.
- Saves the prediction result in an output file.

---

## 4. Introduction

Tomato is an important agricultural crop that can be affected by various diseases.

Environmental conditions such as temperature, humidity, rainfall, and soil conditions can influence the occurrence of diseases.

This project uses Machine Learning to predict possible tomato diseases based on environmental and soil parameters.

A Random Forest Classifier is used to train the model and predict the disease.

The system provides the predicted disease, confidence percentage, risk level, and recommendation to the user.

---

## 5. Machine Learning Technique / Method Used

### Random Forest Classifier

Random Forest is a Machine Learning classification algorithm that combines multiple decision trees to make a prediction.

In this project, Random Forest is used to classify the tomato crop condition based on:

- Temperature
- Humidity
- Rainfall
- Soil pH
- Season

### Input Parameters

The system takes the following information:

| Parameter | Description |
|---|---|
| Location | Location of the crop |
| Crop Name | Name of the crop |
| Soil pH | pH value of the soil |
| Season | Current growing season |
| Temperature | Environmental temperature |
| Humidity | Environmental humidity |
| Rainfall | Rainfall measurement |

### Output

The system predicts:

- Disease
- Confidence
- Risk Level
- Recommendation

---

## 6. Dataset / Source of Data

The dataset is stored inside the `dataset` folder.

The dataset contains environmental and soil parameters related to tomato disease prediction.

### Dataset Features

- Temperature
- Humidity
- Rainfall
- Soil_pH
- Season
- Disease

The dataset is loaded using the **Pandas** library.

---

## 7. Software / Tools / Libraries Used

### Software

- Python
- Visual Studio Code
- Git
- GitHub

### Libraries

- Pandas
- NumPy
- Scikit-learn

### Machine Learning Algorithm

**Random Forest Classifier**

---

## 8. Methodology / Workflow

The workflow of the project is:

```text
Start
  ↓
Load Dataset
  ↓
Data Preprocessing
  ↓
Encode Season
  ↓
Select Features
  ↓
Train Random Forest Model
  ↓
Take User Input
  ↓
Get Weather Information
  ↓
Prepare Input Data
  ↓
Predict Tomato Disease
  ↓
Calculate Confidence
  ↓
Determine Risk Level
  ↓
Generate Recommendation
  ↓
Display Prediction Result
  ↓
Save Output
  ↓
End

## 9.Project Structure
Tomato_Disease_Prediction
│
├── dataset
│   └── tomato_disease_dataset.csv
│
├── source_code
│   └── main.py
│
├── output
│   └── prediction_output.txt
│
├── screenshots
│   ├── project_folder.png
│   ├── code.png
│   └── final_output.png
│
├── README.md
├── requirements.txt
└── .gitignore