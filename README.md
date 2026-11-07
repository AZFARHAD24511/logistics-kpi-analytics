# 🚚 Logistics & Supply Chain KPI Analytics

### Interactive Management Dashboard | Root Cause Analysis | Predictive Insights

[![Live Dashboard](https://img.shields.io/badge/🔴_Live_Dashboard-Click_Here-red?style=for-the-badge)](https://logistics-kpi-analytics.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Predictive-F7931E)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🔗 Live Interactive Dashboard

**👉 [Open the Live KPI Dashboard](https://logistics-kpi-analytics.streamlit.app/)**

The dashboard includes:
- Real-time KPI cards (Delay Rate, Asset Utilization, Waiting Time)
- Interactive filters (Asset, Traffic Status, Shipment Status)
- Root Cause Analysis of delays
- Asset performance comparison
- Inventory vs Demand Forecast view
- Export filtered data

---

## 📌 Project Overview

This project demonstrates professional **KPI tracking**, **root cause analysis**, and **predictive thinking** for logistics and supply chain environments.

It is particularly relevant for roles such as:

- **RAD Process Assistant** (Rapid Asset Deployment)
- Logistics / Transportation Coordinator
- Fulfillment Center Process Support
- Global Transportation Logistics (GTL) operations

**Core idea behind this project:**  
A strong analyst should not only report what already went wrong. The real value is to **anticipate problems before they fully materialize** and enable the team to act early.  
In other words: *prevention is better than reaction*. Accurate prediction and timely action can significantly reduce operational disruptions.

---

## 📊 Key Insights from the Analysis

### 1. Delay Root Causes

| Rank | Delay Reason              | Observation |
|------|---------------------------|-----------|
| 1    | Weather                   | Highest driver of delays |
| 2    | Unknown / Not Specified   | Data quality gap – needs better reason capturing |
| 3    | Traffic                   | Significant controllable factor |
| 4    | Mechanical Failure        | Indicates potential maintenance opportunities |

**Insight:** Weather and Traffic together account for a large share of delays. Improving contingency planning for weather and route optimization can have high impact.

### 2. Asset Utilization
- Utilization across trucks is relatively balanced (mostly between **76% – 80.7%**).
- There is limited variation between assets → fleet is used quite evenly.
- Still room for improvement toward higher utilization targets (e.g. 85%+).

### 3. Waiting Time
- Delayed shipments show a wider and higher distribution of waiting time compared to on-time shipments.
- Waiting time is both a symptom and a **leading indicator** of delays.
- Reducing waiting time should be treated as a priority process improvement lever.

### 4. Recommended Actions

| Priority | Action | Expected Impact |
|----------|--------|-----------------|
| High | Set Delay Rate threshold (e.g. 45%) and escalate when breached | Faster reaction to performance drops |
| High | Improve capture of delay reasons (reduce "Unknown") | Better root cause analysis |
| High | Focus weekly reviews on Weather & Traffic delays | Targeted process improvement |
| Medium | Track Waiting Time as a leading indicator | Earlier detection of bottlenecks |
| Medium | Review asset utilization and reallocate where needed | Higher fleet efficiency |

---

## 🔮 Predictive View & Leading Indicators

In addition to descriptive and diagnostic analysis, this project includes a **predictive component**.

A simple machine learning model (Random Forest) was trained to estimate the probability of a logistics delay and to rank the most influential factors.

### Why prediction matters
Reporting historical delays is useful, but the higher value lies in **anticipating risk**.  
A strong analyst helps the organization act *before* the problem becomes expensive or customer-facing.

### Leading Indicators defined in this project

| Leading Indicator | Example Threshold | Suggested Action |
|-------------------|-------------------|------------------|
| Waiting Time | ≥ 45 minutes | Escalate / investigate bottleneck |
| Traffic Status | Heavy or Detour | Review routing options |
| Asset Utilization | < 70% | Check load planning |
| Inventory Gap | Large negative gap | Align with planning team |

These signals can be reviewed in daily stand-ups as early warning indicators.

**Notebook:** `notebooks/02_predictive_delay_model.ipynb`

---

## 🖼️ Analysis Charts

### Root Cause of Delays
![Root Cause of Delays](visualizations/02_delay_reasons.png)

### Asset Utilization & Waiting Time
![Utilization and Waiting Time](visualizations/03_utilization_and_waiting.png)

### Shipment Status & Traffic Impact
![Status and Traffic](visualizations/01_status_and_traffic.png)

### Inventory vs Demand Forecast
![Inventory vs Demand](visualizations/04_inventory_vs_demand.png)

### Feature Importance (Predictive Model)
![Feature Importance](visualizations/05_feature_importance.png)

---

## 🛠️ How to Run Locally

```bash
git clone https://github.com/AZFARHAD24511/logistics-kpi-analytics.git
cd logistics-kpi-analytics
pip install -r requirements.txt
streamlit run app.py
```

---

## 📂 Repository Structure

```
logistics-kpi-analytics/
├── app.py                              # Interactive Streamlit Dashboard
├── notebooks/
│   ├── 01_logistics_kpi_analysis.ipynb # Descriptive + Diagnostic analysis
│   └── 02_predictive_delay_model.ipynb # Predictive model & leading indicators
├── src/
│   └── kpi_calculator.py
├── data/
│   └── README.md
├── visualizations/                     # Generated charts
├── reports/
│   └── executive_summary.md
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

**Smart Logistics Supply Chain Dataset**

- **Source:** [Kaggle – Smart Logistics Supply Chain Dataset](https://www.kaggle.com/datasets/smart-logistics-supply-chain-dataset)
- **License:** [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
- **Records:** 1,000 rows of simulated 2024 logistics operations
- **Content:** Asset tracking, inventory levels, shipment status, traffic conditions, waiting times, delay reasons, IoT sensor data (temperature, humidity), and demand forecast

The dataset is dedicated to the public domain under **CC0 1.0 Universal**.

---

## 👤 Author

**Azizallah Farhadi**

- GitHub: [AZFARHAD24511](https://github.com/AZFARHAD24511)
- LinkedIn: [Azizallah Farhadi](https://www.linkedin.com/in/azizallah-farhadi-19bb3438/)

---

## 📄 License

- **Project code:** MIT License  
- **Dataset:** [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
