# 🏠 PropVal-AI  
### Enterprise-Grade Real Estate Valuation Engine (AVM)

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/216656971-9b47a2e2-6f7c-4b2f-b9cf-3c96b5e3f5a5.gif" width="500"/>
</p>

<p align="center">
  <b>An Automated Valuation Model (AVM) that estimates real estate prices using advanced Ensemble Machine Learning with interpretability.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Model-Gradient%20Boosting-success"/>
  <img src="https://img.shields.io/badge/Python-3.9-blue"/>
  <img src="https://img.shields.io/badge/ML-Scikit--Learn-orange"/>
  <img src="https://img.shields.io/badge/License-MIT-green"/>
</p>

---

## 🚀 Project Motivation

Real estate valuation is a **high-stakes financial problem** where inaccurate pricing leads to poor investment decisions. Traditional models struggle with **non-linear relationships** between structural, locational, and qualitative features.

**PropVal-AI** is engineered to:
- Accurately estimate property values  
- Handle real-world data imperfections  
- Provide **transparent, interpretable predictions**  

This project reflects **production-grade ML practices**, not a notebook-only experiment.

---

## 🧠 Core Features

- Handles **79+ heterogeneous features**
- Robust missing-value strategy
- Log-transformed target for statistical stability
- Ensemble-based regression (Gradient Boosting)
- Feature importance for explainability
- Modular & scalable architecture

---

## ⚙️ System Architecture

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/216656963-6c6b5c4a-f39d-4b8b-8d0e-9f6b10b53b6b.gif" width="500"/>
</p>

### 1️⃣ Target Transformation
- Applied **Log(1 + SalePrice)** to reduce skewness and stabilize variance

### 2️⃣ Intelligent Missing Value Handling
- **Numerical (Missing Randomly):** Median Imputation  
- **Categorical (Feature Absent):** Explicit `None` category  

### 3️⃣ Feature Engineering
- One-Hot Encoding for zoning, structure, and quality features  
- Expanded to **200+ machine-readable variables**

### 4️⃣ Model Training
- **Gradient Boosting Regressor**
- Ensemble of decision trees minimizing RMSE
- Captures complex non-linear interactions

---

## 📊 Model Performance

| Metric | Result |
|------|-------|
| **R² Score** | **0.89+** |
| **Error Metric** | RMSE |
| **Validation** | Train / Validation Split |

### 🔍 Key Value Drivers
- `OverallQual` – Construction quality  
- `GrLivArea` – Above-grade living area  
- `TotalBsmtSF` – Basement size  

---

## 🛠️ Technology Stack

| Layer | Tool | Purpose |
|-----|------|--------|
| Language | Python | Core pipeline |
| ML | Scikit-Learn | Gradient Boosting |
| Data | Pandas, NumPy | Processing |
| Visualization | Seaborn, Matplotlib | Diagnostics |
| Environment | Jupyter / VS Code | Development |

---

## 📁 Project Structure

```text
PropVal-AI/
│
├── src/
│   └── train_model.py
│
├── notebooks/
│   └── eda_and_modeling.ipynb
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── outputs/
│   └── model_metrics.txt
│
├── requirements.txt
└── README.md
