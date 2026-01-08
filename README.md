# 🏠 PropVal-AI

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Inter&size=22&pause=1000&color=2F81F7&center=true&vCenter=true&width=750&lines=Enterprise+Real+Estate+Valuation+Engine;Automated+Valuation+Model+(AVM);Interpretable+Machine+Learning+Pipeline" />
</p>

<div align="center">
  <br>
  <b>🚀 LATEST STATUS: </b> 
  <samp>Model v2.0 Deployed • RMSE Reduced by 15% • Production Ready</samp>
  <br><br>
</div>

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/216656971-9b47a2e2-6f7c-4b2f-b9cf-3c96b5e3f5a5.gif" width="100%"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Model-Gradient%20Boosting-success"/>
  <img src="https://img.shields.io/badge/Python-3.9-blue"/>
  <img src="https://img.shields.io/badge/License-MIT-green"/>
</p>

---

### 🚀 Motivation
**PropVal-AI** solves the challenge of accurate real estate pricing. Unlike traditional linear models, this engine handles **non-linear relationships** and real-world data imperfections to provide transparent, interpretable valuations.

---

### 🧠 Features & Architecture

| Core Capabilities | Technical Pipeline |
| :--- | :--- |
| ✅ **79+ Features:** Handles heterogeneous data | **1️⃣ Target Transform:** `Log(1 + SalePrice)` for stability |
| 🧩 **Smart Imputation:** Median (Num) & `None` (Cat) | **2️⃣ Processing:** One-Hot Encoding & Feature Expansion |
| 📈 **Ensemble ML:** Gradient Boosting Regressor | **3️⃣ Training:** RMSE minimization with Decision Trees |
| 🔍 **Explainable:** Feature importance ranking | **4️⃣ Deployment:** Modular & scalable architecture |

---

### ⚡️ Usage
<p align="center">
  <img src="https://i.imgur.com/QbLoGC8.gif" width="600" alt="Terminal execution animation"/>
</p>

```bash
# 1. Install Dependencies
pip install -r requirements.txt

# 2. Run Pipeline
python src/train_model.py
