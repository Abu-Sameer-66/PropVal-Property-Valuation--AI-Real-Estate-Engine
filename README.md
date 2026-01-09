# 🏠 PropVal-AI: Real Estate Valuation Engine

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=25&pause=1000&color=2E86C1&center=false&vCenter=true&width=600&lines=Enterprise-grade+Automated+Valuation+Model;Predicting+Prices+with+Gradient+Boosting;Unlocking+Feature+Interpretability;Precision+Real+Estate+Analytics)](https://git.io/typing-svg)
> **An Enterprise-grade Automated Valuation Model (AVM) designed to estimate real estate asset prices with high precision using Ensemble Machine Learning.**

<p align="left">
  <img src="https://img.shields.io/badge/Model-Gradient_Boosting-success?style=for-the-badge&logo=scikit-learn" />
  <img src="https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Accuracy-89%25-orange?style=for-the-badge" />
</p>

---

## 🚀 Overview

Predicting housing prices requires more than just square footage. **PropVal-AI** leverages advanced regression techniques to analyze **79+ variables**, including zoning classification, basement quality, and proximity to arterial roads, to generate a fair market value estimate.

This engine solves the **"Black Box"** problem by providing interpretable feature importance—showing exactly *why* a property is valued at a specific price.

---

## ⚙️ Technical Architecture

I engineered this system using a robust 4-stage pipeline designed to handle the noise and sparsity typical of real estate data.



### 1. Data Normalization & Mathematics
Real estate prices often follow a right-skewed distribution. To correct this and stabilize variance, I applied a Logarithmic Transformation to the target variable $SalePrice$:

$$y' = \log(1 + y)$$

This ensures that the model minimizes relative error rather than absolute error, preventing expensive properties from biasing the model.

### 2. Smart Imputation Strategy
Handling missing data is critical. I implemented a split-logic imputer:
* **Missing Randomly:** Numerical features (e.g., `LotFrontage`) imputed using the **Median** to resist outliers.
* **Feature Not Present:** Categorical features (e.g., `PoolQC`) where "NaN" actually means "No Pool," imputed with **None/0**.

### 3. Dimensionality Management (One-Hot Encoding)
Converted categorical zoning and structural data into a machine-readable format, expanding the dataset to **200+ features** while managing sparsity.

### 4. The Model: Gradient Boosting Regressor
Utilized an ensemble of weak prediction models (Decision Trees). The model builds trees sequentially, where each new tree helps to correct errors made by the previously trained tree.

---

## 📊 Performance & Insights

The model achieves high accuracy by focusing on key value drivers, validated against a hold-out test set.

| Metric | Score | Note |
| :--- | :--- | :--- |
| **R² (Validation)** | **0.89** | Explains 89% of the variance in price. |
| **RMSE** | **0.13** | Low Log-Root-Mean-Squared-Error. |

### 🔑 Key Value Drivers Identified
The model identified these features as the strongest predictors of property value:
1.  **`OverallQual`**: Material and finish quality (Rating 1-10).
2.  **`GrLivArea`**: Above-grade (ground) living area square footage.
3.  **`TotalBsmtSF`**: Total square footage of the basement area.

---

## 🛠️ Tech Stack

| Component | Library | Role & Usage |
| :--- | :--- | :--- |
| **Core Logic** | `Python 3.9` | Scripting and logic control. |
| **ML Engine** | `Scikit-Learn` | Gradient Boosting Regressor, GridSearchCV, Pipelines. |
| **Data Ops** | `Pandas` / `NumPy` | Vectorized operations, dataframe slicing, and cleaning. |
| **Visualization** | `Seaborn` / `Matplotlib` | Residual plots, Heatmaps, and Feature Importance charts. |

---

## 📂 Repository Structure

```text
PropVal-AI/
├── data/
│   ├── train.csv          # Historical training data
│   └── test.csv           # Unseen data for validation
├── notebooks/
│   └── EDA_and_Model.ipynb # Jupyter notebook for experimentation
├── src/
│   ├── preprocessing.py   # Imputation and encoding logic
│   └── train.py           # Model training script
├── README.md              # Project Documentation
└── requirements.txt       # Dependencies
