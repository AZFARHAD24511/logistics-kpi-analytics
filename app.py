"""
Logistics KPI Management Dashboard
Descriptive + Diagnostic + Temporal + Leading Indicators
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

st.markdown("""
<style>
    .main-header {font-size: 2rem; font-weight: 700; color: #0f172a; margin-bottom: 0.2rem;}
    .sub-header {font-size: 0.95rem; color: #64748b; margin-bottom: 1.2rem;}
    .stMetric {background: #f8fafc; padding: 10px 15px; border-radius: 8px; border: 1px solid #e2e8f0;}
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
            df["Hour"] = df["Timestamp"].dt.hour
            df["Day_Name"] = df["Timestamp"].dt.day_name()
            df["Month"] = df["Timestamp"].dt.month
            df["Month_Name"] = df["Timestamp"].dt.month_name()
            df["Is_Delayed"] = df["Logistics_Delay"].astype(bool)
            df["Inventory_Gap"] = df["Inventory_Level"] - df["Demand_Forecast"]

            def get_season(m):
                if m in [12, 1, 2]: return "Winter"
                if m in [3, 4, 5]: return "Spring"
                if m in [6, 7, 8]: return "Summer"
                return "Autumn"
            df["Season"] = df["Month"].apply(get_season)
            return df

    st.error("Dataset not found. Place `smart_logistics_dataset.csv` in the `data/` folder.")
    st.stop()

df = load_data()

# -------------------------------------------------
# Sidebar Filters
# -------------------------------------------------
st.sidebar.title("Filters")
st.sidebar.markdown("Focus the view for stand-up discussions.")

assets = ["All"] + sorted(df["Asset_ID"].unique().tolist())
selected_asset = st.sidebar.selectbox("Asset (Truck)", assets)

traffic_options = ["All"] + sorted(df["Traffic_Status"].unique().tolist())
selected_traffic = st.sidebar.selectbox("Traffic Status", traffic_options)

status_options = ["All"] + sorted(df["Shipment_Status"].unique().tolist())
selected_status = st.sidebar.selectbox("Shipment Status", status_options)

season_options = ["All"] + ["Winter", "Spring", "Summer", "Autumn"]
selected_season = st.sidebar.selectbox("Season", season_options)

only_delayed = st.sidebar.checkbox("Show only Delayed shipments", value=False)

filtered = df.copy()
if selected_asset != "All":
    filtered = filtered[filtered["Asset_ID"] == selected_asset]
if selected_traffic != "All":
    filtered = filtered[filtered["Traffic_Status"] == selected_traffic]
if selected_status != "All":
    filtered = filtered[filtered["Shipment_Status"] == selected_status]
if selected_season != "All":
    filtered = filtered[filtered["Season"] == selected_season]
if only_delayed:
    filtered = filtered[filtered["Logistics_Delay"] == 1]

# -------------------------------------------------
# Header
# -------------------------------------------------
st.markdown('<p class="main-header">🚚 Logistics KPI Management Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Descriptive • Diagnostic • Temporal • Leading Indicators — built for operational stand-ups and proactive decision making</p>', unsafe_allow_html=True)

# -------------------------------------------------
# KPI Cards
# -------------------------------------------------
total_records = len(filtered)
delay_rate = filtered["Logistics_Delay"].mean() * 100 if total_records > 0 else 0
avg_util = filtered["Asset_Utilization"].mean() if total_records > 0 else 0
avg_wait = filtered["Waiting_Time"].mean() if total_records > 0 else 0
delayed_count = int(filtered["Logistics_Delay"].sum()) if total_records > 0 else 0

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Records", f"{total_records:,}")
c2.metric("Delay Rate", f"{delay_rate:.1f}%",
          delta=f"{delay_rate - 45:.1f}% vs 45% target" if total_records else None,
          delta_color="inverse")
c3.metric("Delayed Shipments", f"{delayed_count:,}")
c4.metric("Avg Utilization", f"{avg_util:.1f}%")
c5.metric("Avg Waiting Time", f"{avg_wait:.1f} min")

st.divider()

# -------------------------------------------------
# Tabs
# -------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "Overview & Root Cause",
    "Temporal Patterns",
    "Leading Indicators",
    "Data"
])

# =========================
# TAB 1 – Overview
# =========================
with tab1:
    left, right = st.columns(2)

    with left:
        st.subheader("Shipment Status Distribution")
        status_counts = filtered["Shipment_Status"].value_counts().reset_index()
        status_counts.columns = ["Status", "Count"]
        fig = px.pie(status_counts, names="Status", values="Count",
                     color_discrete_sequence=px.colors.qualitative.Set2, hole=0.45)
        fig.update_layout(margin=dict(t=20, b=20, l=20, r=20), height=340)
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("Delay Rate by Traffic Status")
        traffic_delay = (filtered.groupby("Traffic_Status")["Logistics_Delay"]
                         .mean().mul(100).sort_values(ascending=False).reset_index())
        traffic_delay.columns = ["Traffic Status", "Delay Rate (%)"]
        fig = px.bar(traffic_delay, x="Traffic Status", y="Delay Rate (%)",
                     color="Delay Rate (%)", color_continuous_scale="Reds", text_auto=".1f")
        fig.update_layout(margin=dict(t=20, b=20, l=20, r=20), height=340, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Root Cause of Delays")
    delayed_df = filtered[filtered["Logistics_Delay"] == 1]
    if len(delayed_df) > 0:
        reason_counts = delayed_df["Logistics_Delay_Reason"].value_counts(dropna=False).reset_index()
        reason_counts.columns = ["Reason", "Count"]
        reason_counts["Reason"] = reason_counts["Reason"].fillna("Unknown / Not Specified")
        fig = px.bar(reason_counts, x="Count", y="Reason", orientation="h",
                     color="Count", color_continuous_scale="OrRd", text="Count")
        fig.update_layout(height=350, margin=dict(t=10, b=20, l=20, r=20),
                          yaxis={"categoryorder": "total ascending"}, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No delayed shipments in the current filter.")

    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Asset Utilization by Truck")
        util = (filtered.groupby("Asset_ID")["Asset_Utilization"].mean()
                .sort_values().reset_index())
        fig = px.bar(util, x="Asset_ID", y="Asset_Utilization",
                     color="Asset_Utilization", color_continuous_scale="Viridis", text_auto=".1f")
        fig.update_layout(height=360, margin=dict(t=20, b=20, l=20, r=20), showlegend=False)
        if len(util) > 0:
            fig.add_hline(y=util["Asset_Utilization"].mean(), line_dash="dash",
                          line_color="red", annotation_text="Average")
        st.plotly_chart(fig, use_container_width=True)

    with col_b:
        st.subheader("Waiting Time by Delay Status")
        fig = px.box(filtered, x="Is_Delayed", y="Waiting_Time", color="Is_Delayed",
                     labels={"Is_Delayed": "Delayed", "Waiting_Time": "Waiting Time (min)"},
                     color_discrete_map={True: "#ef4444", False: "#22c55e"})
        fig.update_layout(height=360, margin=dict(t=20, b=20, l=20, r=20), showlegend=False)
        fig.update_xaxes(tickvals=[False, True], ticktext=["On Time", "Delayed"])
        st.plotly_chart(fig, use_container_width=True)

# =========================
# TAB 2 – Temporal
# =========================
with tab2:
    st.markdown("**Time is a critical dimension in logistics.** Patterns by hour, day and season help teams plan capacity and act earlier.")

    # Hourly
    st.subheader("Delay Rate & Waiting Time by Hour of Day")
    hourly = filtered.groupby("Hour").agg(
        Delay_Rate=("Logistics_Delay", "mean"),
        Avg_Waiting=("Waiting_Time", "mean"),
        Count=("Logistics_Delay", "count")
    ).reset_index()
    hourly["Delay_Rate"] *= 100

    h1, h2 = st.columns(2)
    with h1:
        fig = px.line(hourly, x="Hour", y="Delay_Rate", markers=True,
                      labels={"Delay_Rate": "Delay Rate (%)", "Hour": "Hour of Day"})
        fig.update_traces(line_color="#dc2626")
        fig.update_layout(height=320, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig, use_container_width=True)
    with h2:
        fig = px.bar(hourly, x="Hour", y="Avg_Waiting",
                     labels={"Avg_Waiting": "Avg Waiting (min)", "Hour": "Hour of Day"})
        fig.update_layout(height=320, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig, use_container_width=True)

    # Day of week
    st.subheader("Performance by Day of Week")
    dow_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    daily = filtered.groupby("Day_Name").agg(
        Delay_Rate=("Logistics_Delay", "mean"),
        Avg_Waiting=("Waiting_Time", "mean"),
        Count=("Logistics_Delay", "count")
    ).reindex(dow_order).reset_index()
    daily["Delay_Rate"] *= 100

    d1, d2 = st.columns(2)
    with d1:
        fig = px.bar(daily, x="Day_Name", y="Delay_Rate",
                     labels={"Delay_Rate": "Delay Rate (%)", "Day_Name": ""},
                     color="Delay_Rate", color_continuous_scale="Reds")
        fig.update_layout(height=320, margin=dict(t=20, b=20, l=20, r=20), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    with d2:
        fig = px.bar(daily, x="Day_Name", y="Avg_Waiting",
                     labels={"Avg_Waiting": "Avg Waiting (min)", "Day_Name": ""})
        fig.update_layout(height=320, margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig, use_container_width=True)

    # Season
    st.subheader("Delay Rate by Season")
    seasonal = filtered.groupby("Season").agg(
        Delay_Rate=("Logistics_Delay", "mean"),
        Avg_Waiting=("Waiting_Time", "mean"),
        Count=("Logistics_Delay", "count")
    ).reindex(["Winter", "Spring", "Summer", "Autumn"]).reset_index()
    seasonal["Delay_Rate"] *= 100

    fig = px.bar(seasonal, x="Season", y="Delay_Rate", text_auto=".1f",
                 labels={"Delay_Rate": "Delay Rate (%)"},
                 color="Delay_Rate", color_continuous_scale="OrRd")
    fig.update_layout(height=340, margin=dict(t=20, b=20, l=20, r=20), showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    st.info("Observed pattern in full data: **Summer** has the highest delay rate (~62.5%). **Tuesday** is the weakest weekday (~65%). Peak risk hours include 14:00–17:00.")

# =========================
# TAB 3 – Leading Indicators
# =========================
with tab3:
    st.markdown("""
    **Prevention is better than reaction.**  
    These signals can be reviewed in daily stand-ups to act before delays fully materialize.
    """)

    # Simple leading indicator flags on filtered data
    lead = filtered.copy()
    lead["High_Waiting"] = lead["Waiting_Time"] >= 45
    lead["Difficult_Traffic"] = lead["Traffic_Status"].isin(["Heavy", "Detour"])
    lead["Low_Utilization"] = lead["Asset_Utilization"] < 70
    lead["Inventory_Risk"] = lead["Inventory_Gap"] < -50

    l1, l2, l3, l4 = st.columns(4)
    l1.metric("High Waiting Time (≥45m)", int(lead["High_Waiting"].sum()))
    l2.metric("Difficult Traffic", int(lead["Difficult_Traffic"].sum()))
    l3.metric("Low Utilization (<70%)", int(lead["Low_Utilization"].sum()))
    l4.metric("Inventory Shortage Risk", int(lead["Inventory_Risk"].sum()))

    st.subheader("Suggested thresholds for stand-ups")
    st.table(pd.DataFrame({
        "Leading Indicator": ["Waiting Time", "Traffic Status", "Asset Utilization", "Inventory Gap"],
        "Example Threshold": ["≥ 45 minutes", "Heavy or Detour", "< 70%", "Large negative gap"],
        "Suggested Action": [
            "Escalate / investigate bottleneck",
            "Review routing options",
            "Check load planning",
            "Align with planning team"
        ]
    }))

    st.subheader("Records currently flagged")
    flagged = lead[lead["High_Waiting"] | lead["Difficult_Traffic"] | lead["Low_Utilization"] | lead["Inventory_Risk"]]
    if len(flagged) > 0:
        show_cols = ["Timestamp", "Asset_ID", "Traffic_Status", "Waiting_Time",
                     "Asset_Utilization", "Inventory_Gap", "Logistics_Delay",
                     "High_Waiting", "Difficult_Traffic", "Low_Utilization", "Inventory_Risk"]
        st.dataframe(flagged[show_cols].head(50), use_container_width=True)
    else:
        st.success("No records match the current leading-indicator thresholds.")

# =========================
# TAB 4 – Data
# =========================
with tab4:
    st.dataframe(filtered.head(200), use_container_width=True)
    csv = filtered.to_csv(index=False).encode("utf-8")
    st.download_button("Download filtered data as CSV", data=csv,
                       file_name="filtered_logistics_kpi.csv", mime="text/csv")

st.divider()
st.caption("Logistics KPI Dashboard • Descriptive • Temporal • Leading Indicators • Portfolio by Azizallah Farhadi")
