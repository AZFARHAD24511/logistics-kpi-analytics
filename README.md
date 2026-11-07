# 🚚 Logistics & Supply Chain KPI Analytics

### Interactive Management Dashboard | Root Cause Analysis | Data-Driven Operations

[![Live Dashboard](https://img.shields.io/badge/🔴_Live_Dashboard-Click_Here-red?style=for-the-badge)](https://logistics-kpi-analytics.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🔗 Live Interactive Dashboard

**👉 [Open the Live KPI Dashboard](https://logistics-kpi-analytics.streamlit.app/)**

The dashboard includes:
- Real-time KPI cards (Delay Rate, Asset Utilization, Waiting Time, ...)
- Interactive filters (Asset, Traffic Status, Shipment Status)
- Root Cause Analysis of delays
- Asset performance comparison
- Inventory vs Demand Forecast view
- Export filtered data

> Designed to support daily stand-ups, operational reviews, and data-driven decision making.

---

## 📌 Project Overview

This project demonstrates professional **KPI tracking**, **root cause analysis**, and **operational reporting** skills for logistics and supply chain environments.

It is particularly relevant for roles such as:

- **RAD Process Assistant** (Rapid Asset Deployment)
- Logistics / Transportation Coordinator
- Fulfillment Center Process Support
- Global Transportation Logistics (GTL) operations

**Key capabilities shown:**
- Monitoring critical logistics KPIs
- Systematic root cause analysis of delays
- Creating clear, stakeholder-ready visualizations
- Supporting data-driven process improvement

---

## 🎯 Key Performance Indicators

| KPI | Description | Business Impact |
|-----|-------------|-----------------|
| **Logistics Delay Rate** | % of shipments with delays | Direct impact on OTIF & customer experience |
| **Asset Utilization** | How efficiently trucks/assets are used | Cost efficiency & capacity planning |
| **Average Waiting Time** | Time assets spend waiting | Process bottleneck identification |
| **Inventory vs Demand Forecast** | Alignment between stock and predicted demand | Inventory optimization |
| **Shipment Status Distribution** | In Transit / Delivered / Delayed ratios | Operational health overview |
| **Delay Root Causes** | Traffic, Weather, Mechanical Failure, etc. | Targeted process improvement |

---

## 🛠️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/AZFARHAD24511/logistics-kpi-analytics.git
cd logistics-kpi-analytics

# Install dependencies
pip install -r requirements.txt

# Run the interactive dashboard
streamlit run app.py
```

---

## 📂 Repository Structure

```
logistics-kpi-analytics/
├── app.py                          # Interactive Streamlit Dashboard
├── notebooks/
│   └── 01_logistics_kpi_analysis.ipynb
├── src/
│   └── kpi_calculator.py           # Reusable KPI functions
├── data/
│   └── README.md                   # Dataset documentation
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

The dataset is dedicated to the public domain under **CC0 1.0 Universal**. You can copy, modify, distribute, and use it even for commercial purposes without asking permission.

> When using this dataset, you should not imply endorsement by the original author.

Full column descriptions are available in [`data/README.md`](data/README.md).

---

## 👤 Author

**Azizallah Farhadi**

- GitHub: [AZFARHAD24511](https://github.com/AZFARHAD24511)
- LinkedIn: [Azizallah Farhadi](https://www.linkedin.com/in/azizallah-farhadi-19bb3438/)

---

## 📄 License

This project code is licensed under the MIT License.  
The dataset used in this project is licensed under [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/).
