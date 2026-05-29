# Customer Churn Prediction

## Overview
A machine learning model that predicts whether a telecom customer will churn or stay, built using real world customer data from Kaggle.

---

## Approach
- Cleaned and prepared real customer data from Kaggle
- Encoded text columns to numbers and scaled numeric values
- Trained four models and compared them based on Recall
- Applied feature selection to keep only the top 5 important features
- Retrained the model with selected features for better performance

---

## Model Comparison

| Model | Accuracy | Recall |
|-------|----------|--------|
| Logistic Regression | 80% | 0.57 |
| Decision Tree | 71% | 0.47 |
| Random Forest | 78% | 0.49 |
| **XGBoost** | **75%** | **0.68** ✅ |

> Recall was prioritized over accuracy — catching actual churners matters more than overall correctness.

---

## Final Output
The model takes 5 customer details as input and predicts whether that customer will Churn or Stay.

| | Recall |
|--|--------|
| Before feature selection | 0.68 |
| After feature selection | 0.82 |

---

## Tools and Libraries Used

| | |
|--|--|
| Language | Python |
| Libraries | Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, XGBoost |
| Platform | Jupyter Notebook |
| Dataset | [Kaggle — Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) |
| Package Manager | [`uv`](https://github.com/astral-sh/uv) |

---

## Installation

```bash
uv add pandas numpy matplotlib seaborn scikit-learn xgboost
```

---

## Author
**Mitra Sreekandan**  
BE CSE, 2nd Year — Sri Krishna College of Technology (SKCT)

