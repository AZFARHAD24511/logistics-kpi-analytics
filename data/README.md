# Dataset Information

## Smart Logistics Supply Chain Dataset

**Source:** Kaggle – Smart Logistics Supply Chain Dataset  
**Size:** 1,000 records  
**Time Period:** 2024 simulated operational data

### Key Columns

| Column | Description | Relevance to KPIs |
|--------|-------------|-------------------|
| Timestamp | Event date & time | Trend analysis over time |
| Asset_ID | Truck / Asset identifier | Asset-level performance |
| Inventory_Level | Current inventory | Inventory health KPI |
| Shipment_Status | Delayed / In Transit / Delivered | Core operational status |
| Waiting_Time | Minutes waiting | Process efficiency KPI |
| Asset_Utilization | % utilization (60–100) | Capacity & cost KPI |
| Demand_Forecast | Predicted demand | Forecast accuracy |
| Logistics_Delay | Binary (0/1) | Primary Delay Rate KPI |
| Logistics_Delay_Reason | Traffic / Weather / etc. | Root Cause Analysis |
| Traffic_Status | Clear / Heavy / Detour | Contributing factor |
| Temperature / Humidity | Environmental conditions | Potential quality & delay drivers |

### How to Obtain the Data

1. Download from Kaggle:  
   https://www.kaggle.com/datasets/smart-logistics-supply-chain-dataset

2. Place the CSV file in this `data/` folder as:
   ```
   smart_logistics_dataset.csv
   ```

> **Important:** Large data files are intentionally excluded from this repository (see `.gitignore`) to keep the repo clean and professional.

### Sample Usage in Analysis

The notebook expects the file at:
```python
df = pd.read_csv('../data/smart_logistics_dataset.csv')
```
