# 🚚 Logistics & Supply Chain KPI Analytics

### From Reporting to Prevention — KPI Monitoring, Root Cause Analysis, Predictive Signals & Temporal Patterns

[![Live Dashboard](https://img.shields.io/badge/🔴_Live_Dashboard-Click_Here-red?style=for-the-badge)](https://logistics-kpi-analytics.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Predictive-F7931E)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🔗 Live Interactive Dashboard

**👉 [Launch the Live KPI Dashboard](https://logistics-kpi-analytics.streamlit.app/)**

Interactive filters • KPI cards • Root cause views • Asset performance • Exportable data

---

## 📌 Why This Project Exists

In logistics operations, reporting what already went wrong is not enough.

A strong analyst helps the organization **see risk early** and act before performance deteriorates.  
This project is built around that mindset:

> **Prevention is better than reaction.**  
> Accurate monitoring, clear root cause analysis, and timely prediction reduce disruptions, protect customer experience, and support better daily decisions.

The work is designed to reflect the type of thinking expected in roles such as:

- **RAD Process Assistant** (Rapid Asset Deployment)
- Logistics / Transportation Coordinator
- Fulfillment Center Process Support
- Global Transportation Logistics (GTL) operations

---

## 🧠 Analytical Framework

| Layer | Question | What This Project Delivers |
|-------|----------|----------------------------|
| **Descriptive** | What happened? | Core KPI summary, status distribution, utilization |
| **Diagnostic** | Why did it happen? | Root cause breakdown of delays |
| **Predictive** | What is likely to happen? | Delay probability model + leading indicators |
| **Temporal** | When does it happen? | Hour, day-of-week, month and season patterns |

---

## 📊 Key Findings

### 1. Delay Root Causes
| Rank | Reason | Observation |
|------|--------|-------------|
| 1 | Weather | Strongest single driver of delays |
| 2 | Unknown / Not Specified | Important data quality gap |
| 3 | Traffic | Controllable operational factor |
| 4 | Mechanical Failure | Points to maintenance & asset reliability |

Weather and Traffic together represent a large share of delays. Improving reason capture (reducing “Unknown”) would make root cause analysis significantly more actionable.

### 2. Asset Utilization
- Fleet utilization is relatively balanced (mostly **76–81%**).
- Variation between trucks is limited → usage is even, but there is still headroom toward higher targets (e.g. 85%+).

### 3. Waiting Time as a Leading Signal
- Delayed shipments show clearly higher and more variable waiting times.
- Waiting time is both a symptom and an early warning indicator.
- It should be monitored daily, not only after delays are confirmed.

### 4. Temporal Patterns (When problems concentrate)

**Season**
| Season | Delay Rate | Insight |
|--------|------------|---------|
| Winter | 55.4% | Stable |
| Spring | 55.5% | Stable |
| **Summer** | **62.5%** | Highest risk season |
| Autumn | 53.2% | Best performance |

**Day of Week**
| Day | Delay Rate | Insight |
|-----|------------|---------|
| Monday | 52.3% | Relatively strong |
| **Tuesday** | **65.0%** | Weakest day — needs extra attention |
| Wednesday | 56.3% | Average |
| Thursday | 55.6% | Average |
| Friday | 53.7% | Relatively strong |
| Saturday | 59.7% | Elevated |
| Sunday | 53.9% | Relatively strong |

**Highest-risk hours**
- 17:00 → 69.4% delay rate  
- 14:00 → 67.4% delay rate  
- 04:00 → 65.1% delay rate  
- 08:00 → 64.0% delay rate  

Late afternoon and selected early-morning / late-night windows show elevated risk and can be used for staffing and dispatch planning.

---

## 🎯 Recommended Operational Actions

| Priority | Action | Why it matters |
|----------|--------|----------------|
| High | Define a Delay Rate threshold and escalate when breached | Creates clear trigger for action |
| High | Improve delay reason capture (reduce “Unknown”) | Makes root cause analysis reliable |
| High | Give extra focus to **Tuesdays** and **Summer** | Highest risk periods in the data |
| High | Monitor peak hours (especially 14:00–17:00) | Enables proactive capacity allocation |
| Medium | Track Waiting Time as a leading indicator | Earlier detection of bottlenecks |
| Medium | Review low-utilization assets | Improves fleet efficiency |

---

## 🔮 Predictive Layer & Leading Indicators

A Random Forest model was trained to estimate delay probability and rank influential factors.

**Leading indicators defined for daily use:**

| Leading Indicator | Example Threshold | Suggested Action |
|-------------------|-------------------|------------------|
| Waiting Time | ≥ 45 minutes | Escalate / investigate |
| Traffic Status | Heavy or Detour | Review routing |
| Asset Utilization | < 70% | Check load planning |
| Inventory Gap | Large negative gap | Align with planning |

These signals are intended to support stand-ups and shift handovers so that teams can act **before** delays fully materialize.

---

## 🖼️ Selected Charts

### Root Cause of Delays
![Root Cause](visualizations/02_delay_reasons.png)

### Utilization & Waiting Time
![Utilization & Waiting](visualizations/03_utilization_and_waiting.png)

### Status & Traffic Impact
![Status & Traffic](visualizations/01_status_and_traffic.png)

### Inventory vs Demand
![Inventory vs Demand](visualizations/04_inventory_vs_demand.png)

### Feature Importance (Predictive Model)
![Feature Importance](visualizations/05_feature_importance.png)

### Temporal Patterns
![Hourly](visualizations/06_hourly_patterns.png)
![Day of Week](visualizations/07_day_of_week_patterns.png)
![Monthly](visualizations/08_monthly_patterns.png)
![Seasonal](visualizations/09_seasonal_delay.png)
![Daily Trend](visualizations/10_daily_trend.png)

---

## 🛠️ How to Run

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
├── app.py                              # Interactive Streamlit dashboard
├── notebooks/
│   ├── 01_logistics_kpi_analysis.ipynb # Descriptive + Diagnostic
│   ├── 02_predictive_delay_model.ipynb # Predictive model & leading indicators
│   └── 03_temporal_analysis.ipynb      # Hour / Day / Month / Season patterns
├── src/kpi_calculator.py
├── data/README.md
├── visualizations/
├── reports/executive_summary.md
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

**Smart Logistics Supply Chain Dataset**

- **Source:** [Kaggle – Smart Logistics Supply Chain Dataset](https://www.kaggle.com/datasets/smart-logistics-supply-chain-dataset)
- **License:** [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
- **Size:** 1,000 records covering 2024 logistics operations
- **Content:** Asset tracking, inventory, shipment status, traffic, waiting time, delay reasons, IoT sensor data, demand forecast

---

## 👤 Author

**Azizallah Farhadi**

- GitHub: [AZFARHAD24511](https://github.com/AZFARHAD24511)
- LinkedIn: [Azizallah Farhadi](https://www.linkedin.com/in/azizallah-farhadi-19bb3438/)

---

## 📄 License

- **Code:** MIT License  
- **Dataset:** [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
