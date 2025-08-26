
import io
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Warehouse Location Mapper", layout="wide")
st.title("📍 Warehouse Location Mapper")

st.markdown(
    """
    Upload a CSV with **Latitude in column A** and **Longitude in column B**.
    No headers are required. If headers exist, the app will try to auto-detect them.
    After upload, pick a **custom color for each warehouse** and view them on the map.
    """
)

uploaded = st.file_uploader("Upload CSV (latitude in col A, longitude in col B)", type=["csv"])

def _load_csv(uploaded_file):
    if uploaded_file is None:
        return None

    # Read the bytes so we can attempt multiple parses
    data = uploaded_file.read()
    # Try header=None first, then header=0
    for header in [None, 0]:
        buf = io.BytesIO(data)
        try:
            df = pd.read_csv(buf, header=header, usecols=[0, 1])
            df.columns = ["Latitude", "Longitude"]
            # Coerce to numeric and drop rows that fail
            df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
            df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
            df = df.dropna(subset=["Latitude", "Longitude"]).reset_index(drop=True)
            if len(df) > 0:
                return df
        except Exception:
            continue
    return None

df = _load_csv(uploaded)

if df is None and uploaded is not None:
    st.error("Couldn't parse the CSV. Ensure column A is latitude and column B is longitude.")
    st.stop()

if df is not None:
    st.subheader("Data preview")
    st.dataframe(df.head(50), use_container_width=True)

    st.subheader("Marker colors")
    st.caption("Pick a color for each plotted warehouse.")
    default_color = st.color_picker("Default color", "#3388ff", key="default_color")

    # Build color pickers per row
    color_map = {}
    with st.expander("Customize colors per warehouse", expanded=True):
        for i in range(len(df)):
            color_map[i] = st.color_picker(f"Warehouse {i+1} color", default_color, key=f"color_{i}")

    # Center map on the mean coordinates
    center_lat = float(df["Latitude"].mean())
    center_lon = float(df["Longitude"].mean())
    m = folium.Map(location=[center_lat, center_lon], zoom_start=6)

    # Add markers
    for i, row in df.iterrows():
        color = color_map.get(i, default_color)
        folium.CircleMarker(
            location=[float(row["Latitude"]), float(row["Longitude"])],
            radius=8,
            color=color,
            fill=True,
            fill_color=color,
            popup=f"Warehouse {i+1}: ({row['Latitude']:.6f}, {row['Longitude']:.6f})"
        ).add_to(m)

    st.subheader("Map")
    st_folium(m, width=900, height=600)
else:
    st.info("Upload a CSV to get started.")
