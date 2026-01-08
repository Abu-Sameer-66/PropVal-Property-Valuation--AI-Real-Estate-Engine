# 🏠 PropVal-AI: Real Estate Valuation Engine

> **An Enterprise-grade Automated Valuation Model (AVM) designed to estimate real estate asset prices with high precision using Ensemble Machine Learning.**

[![Status](https://img.shields.io/badge/Model-Gradient_Boosting-success)]()
[![Python](https://img.shields.io/badge/Python-3.9-blue)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()

---

### 🚀 Overview
Predicting housing prices requires more than just square footage. **PropVal-AI** leverages advanced regression techniques to analyze **79+ variables**, including zoning classification, basement quality, and proximity to arterial roads, to generate a fair market value estimate.

This engine solves the **"Black Box"** problem by providing interpretable feature importance—showing exactly *why* a property is valued at a specific price.

---

### ⚙️ Technical Architecture
I engineered this system using a 4-stage pipeline:

1.  **Data Normalization:** Applied `Log(1+x)` transformation to the target variable (`SalePrice`) to correct skewness and improve statistical stability.
2.  **Smart Imputation:** Handled missing data by distinguishing between "Missing Randomly" (imputed with Median) vs "Feature Not Present" (imputed with None).
3.  **One-Hot Encoding:** Converted categorical zoning and structural data into a machine-readable format (expanding to 200+ features).
4.  **Gradient Boosting Regressor:** Utilized an ensemble of weak prediction models (Decision Trees) to minimize the Loss Function (RMSE).

---

### 📊 Performance & Insights
The model achieves high accuracy by focusing on key value drivers.
* **Accuracy (R²):** **0.89+** on validation data.
* **Key Drivers Identified:**
    * `OverallQual`: Material and finish quality.
    * `GrLivArea`: Above-grade living area.
    * `TotalBsmtSF`: Total basement area.

---

### 🛠️ Tech Stack
| Component | Library | Usage |
| :--- | :--- | :--- |
| **Core Logic** | `Python` | Scripting and logic control. |
| **ML Engine** | `Scikit-Learn` | Gradient Boosting, Train/Test Split. |
| **Data Ops** | `Pandas / NumPy` | Vectorized operations and cleaning. |
| **Visualization** | `Seaborn` | Residual plots and Feature Importance charts. |

---

### 💻 How to Run
1. **Clone the repository**
   ```bash
   git clone [https://github.com/Abu-Sameer-66/PropVal-AI-Real-Estate-Engine.git](https://github.com/Abu-Sameer-66/PropVal-AI-Real-Estate-Engine.git)
