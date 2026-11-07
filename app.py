"""
Logistics KPI Management Dashboard
Interactive dashboard for monitoring operational KPIs, 
delay root causes, and asset performance.
Designed for Process Assistant / RAD / GTL style stand-ups.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# -------------------------------------------------
# Page Config
# -------------------------------------------------
st.set_page_config(
    page_title="Logistics KPI Dashboard",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# Custom CSS for a cleaner management look
# -------------------------------------------------
st.markdown("""
<style>
    .main-header {
        font-size: 2.1rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #64748b;
        margin-bottom: 1.5rem;
    }
    .stMetric {
        background: #f8fafc;
        padding: 10px 15px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Data Loading
# -------------------------------------------------
@st.cache_data
def load_data():
    possible_paths = [
        Path("data/smart_logistics_dataset.csv"),
        Path("../data/smart_logistics_dataset.csv"),
        Path("smart_logistics_dataset.csv"),
    ]
    
    for path in possible_paths:
        if path.exists():
            df = pd.read_csv(path)
            df["Timestamp"] = pd.to_datetime(df["Timestamp"])
            df["Date"] = df["Timestamp"].dt.date
            df["Is_Delayed"] = df["Logistics_Delay"].astype(bool)
            return df
    
    st.error("""
    **Dataset not found.**  
    Please place the file `smart_logistics_dataset.csv` in the `data/` folder.
    """)
    st.stop()

df = load_data()

# -------------------------------------------------
# Sidebar Filters
# -------------------------------------------------
st.sidebar.title("Filters")
st.sidebar.markdown("Use filters to focus on specific segments for stand-up discussions.")

assets = ["All"] + sorted(df["Asset_ID"].unique().tolist())
selected_asset = st.sidebar.selectbox("Asset (Truck)", assets)

traffic_options = ["All"] + sorted(df["Traffic_Status"].unique().tolist())
selected_traffic = st.sidebar.selectbox("Traffic Status", traffic_options)

status_options = ["All"] + sorted(df["Shipment_Status"].unique().tolist())
selected_status = st.sidebar.selectbox("Shipment Status", status_options)

only_delayed = st.sidebar.checkbox("Show only Delayed shipments", value=False)

# Apply filters
filtered = df.copy()
if selected_asset != "All":
    filtered = filtered[filtered["Asset_ID"] == selected_asset]
if selected_traffic != "All":
    filtered = filtered[filtered["Traffic_Status"] == selected_traffic]
if selected_status != "All":
    filtered = filtered[filtered["Shipment_Status"] == selected_status]
if only_delayed:
    filtered = filtered[filtered["Logistics_Delay"] == 1]

# -------------------------------------------------
# Header
# -------------------------------------------------
st.markdown('<p class="main-header">🚚 Logistics KPI Management Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Real-time view of operational performance • Root cause insights • Decision support for Process & RAD teams</p>', unsafe_allow_html=True)

# -------------------------------------------------
# KPI Cards
# -------------------------------------------------
total_records = len(filtered)
delay_rate = filtered["Logistics_Delay"].mean() * 100 if total_records > 0 else 0
avg_util = filtered["Asset_Utilization"].mean() if total_records > 0 else 0
avg_wait = filtered["Waiting_Time"].mean() if total_records > 0 else 0
delayed_count = int(filtered["Logistics_Delay"].sum()) if total_records > 0 else 0

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Records", f"{total_records:,}")
with col2:
    st.metric("Delay Rate", f"{delay_rate:.1f}%",
              delta=f"{delay_rate - 45:.1f}% vs target 45%" if delay_rate else None,
              delta_color="inverse")
with col3:
    st.metric("Delayed Shipments", f"{delayed_count:,}")
with col4:
    st.metric("Avg Utilization", f"{avg_util:.1f}%")
with col5:
    st.metric("Avg Waiting Time", f"{avg_wait:.1f} min")

st.divider()

# -------------------------------------------------
# Charts - Row 1
# -------------------------------------------------
left, right = st.columns(2)

with left:
    st.subheader("Shipment Status Distribution")
    status_counts = filtered["Shipment_Status"].value_counts().reset_index()
    status_counts.columns = ["Status", "Count"]
    fig_status = px.pie(status_counts, names="Status", values="Count",
                        color_discrete_sequence=px.colors.qualitative.Set2, hole=0.45)
    fig_status.update_layout(margin=dict(t=20, b=20, l=20, r=20), height=340)
    st.plotly_chart(fig_status, use_container_width=True)

with right:
    st.subheader("Delay Rate by Traffic Status")
    traffic_delay = (filtered.groupby("Traffic_Status")["Logistics_Delay"]
                     .mean().mul(100).sort_values(ascending=False).reset_index())
    traffic_delay.columns = ["Traffic Status", "Delay Rate (%)"]
    
    fig_traffic = px.bar(traffic_delay, x="Traffic Status", y="Delay Rate (%)",
                         color="Delay Rate (%)", color_continuous_scale="Reds", text_auto=".1f")
    fig_traffic.update_layout(margin=dict(t=20, b=20, l=20, r=20), height=340, showlegend=False)
    st.plotly_chart(fig_traffic, use_container_width=True)

# -------------------------------------------------
# Root Cause
# -------------------------------------------------
st.subheader("Root Cause Analysis – Delay Reasons")

delayed_df = filtered[filtered["Logistics_Delay"] == 1]

if len(delayed_df) > 0:
    reason_counts = delayed_df["Logistics_Delay_Reason"].value_counts(dropna=False).reset_index()
    reason_counts.columns = ["Reason", "Count"]
    reason_counts["Reason"] = reason_counts["Reason"].fillna("Unknown / Not Specified")

    fig_reason = px.bar(reason_counts, x="Count", y="Reason", orientation="h",
                        color="Count", color_continuous_scale="OrRd", text="Count")
    fig_reason.update_layout(height=350, margin=dict(t=10, b=20, l=20, r=20),
                             yaxis={"categoryorder": "total ascending"}, showlegend=False)
    st.plotly_chart(fig_reason, use_container_width=True)
else:
    st.info("No delayed shipments in the current filter selection.")

# -------------------------------------------------
# Asset & Waiting Time
# -------------------------------------------------
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Asset Utilization by Truck")
    util_by_asset = (filtered.groupby("Asset_ID")["Asset_Utilization"]
                     .mean().sort_values().reset_index())
    fig_util = px.bar(util_by_asset, x="Asset_ID", y="Asset_Utilization",
                      color="Asset_Utilization", color_continuous_scale="Viridis", text_auto=".1f")
    fig_util.update_layout(height=360, margin=dict(t=20, b=20, l=20, r=20), showlegend=False)
    fig_util.add_hline(y=util_by_asset["Asset_Utilization"].mean(), line_dash="dash",
                       line_color="red", annotation_text="Average")
    st.plotly_chart(fig_util, use_container_width=True)

with col_b:
    st.subheader("Waiting Time by Delay Status")
    fig_wait = px.box(filtered, x="Is_Delayed", y="Waiting_Time", color="Is_Delayed",
                      labels={"Is_Delayed": "Delayed", "Waiting_Time": "Waiting Time (min)"},
                      color_discrete_map={True: "#ef4444", False: "#22c55e"})
    fig_wait.update_layout(height=360, margin=dict(t=20, b=20, l=20, r=20), showlegend=False)
    fig_wait.update_xaxes(tickvals=[False, True], ticktext=["On Time", "Delayed"])
    st.plotly_chart(fig_wait, use_container_width=True)

# -------------------------------------------------
# Inventory vs Demand
# -------------------------------------------------
st.subheader("Inventory Level vs Demand Forecast")
fig_inv = px.scatter(filtered, x="Demand_Forecast", y="Inventory_Level", color="Is_Delayed",
                     color_discrete_map={True: "#ef4444", False: "#3b82f6"}, opacity=0.65,
                     labels={"Is_Delayed": "Delayed"},
                     hover_data=["Asset_ID", "Waiting_Time", "Traffic_Status"])
fig_inv.add_trace(go.Scatter(x=[100, 300], y=[100, 300], mode="lines", name="Perfect Match",
                             line=dict(color="gray", dash="dash")))
fig_inv.update_layout(height=400, margin=dict(t=20, b=20, l=20, r=20))
st.plotly_chart(fig_inv, use_container_width=True)

# -------------------------------------------------
# Data Preview
# -------------------------------------------------
with st.expander("View Filtered Data & Download"):
    st.dataframe(filtered.head(100), use_container_width=True)
    csv = filtered.to_csv(index=False).encode("utf-8")
    st.download_button("Download filtered data as CSV", data=csv,
                       file_name="filtered_logistics_kpi.csv", mime="text/csv")

st.divider()
st.caption("Logistics KPI Dashboard • Built for operational stand-ups and process improvement • Portfolio by Azizallah Farhadi")