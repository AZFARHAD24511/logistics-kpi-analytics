"""
Reusable KPI calculation functions for Logistics / Supply Chain analysis.
Designed for easy extension into automated reporting.
"""

import pandas as pd
import numpy as np


def calculate_delay_rate(df: pd.DataFrame, delay_col: str = "Logistics_Delay") -> float:
    """Calculate overall logistics delay rate (%)."""
    return df[delay_col].mean() * 100


def calculate_avg_utilization(df: pd.DataFrame, util_col: str = "Asset_Utilization") -> float:
    """Average asset utilization percentage."""
    return df[util_col].mean()


def calculate_avg_waiting_time(df: pd.DataFrame, wait_col: str = "Waiting_Time") -> float:
    """Average waiting time in minutes."""
    return df[wait_col].mean()


def delay_reason_breakdown(df: pd.DataFrame, reason_col: str = "Logistics_Delay_Reason") -> pd.Series:
    """Count of delay reasons (for root cause analysis)."""
    return df[reason_col].value_counts(dropna=False)


def shipment_status_distribution(df: pd.DataFrame, status_col: str = "Shipment_Status") -> pd.Series:
    """Distribution of shipment statuses."""
    return df[status_col].value_counts(normalize=True) * 100


def generate_kpi_summary(df: pd.DataFrame) -> dict:
    """
    Generate a dictionary of core KPIs ready for reporting or dashboard.
    """
    summary = {
        "delay_rate_pct": round(calculate_delay_rate(df), 1),
        "avg_asset_utilization_pct": round(calculate_avg_utilization(df), 1),
        "avg_waiting_time_min": round(calculate_avg_waiting_time(df), 1),
        "total_records": len(df),
        "delayed_shipments": int(df["Logistics_Delay"].sum()),
    }
    return summary


if __name__ == "__main__":
    # Example usage (requires data file)
    print("KPI Calculator module loaded successfully.")
    print("Import and use with your logistics dataframe.")
