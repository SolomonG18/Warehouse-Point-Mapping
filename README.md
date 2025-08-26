# 🗺️ Streamlit Warehouse Mapper

A Streamlit app that maps warehouse locations from a CSV upload and lets you customize the color for each plotted point.
Basemaps: **CARTO** and **OpenStreetMap**.

## ✅ CSV Format
- Column A: latitude
- Column B: longitude
- Optional: `color` column with hex values (e.g., `#FF0000`). If omitted, colors are auto-assigned.

You can also edit colors in-app via a color picker and download the updated CSV.

## ▶️ Quickstart (Local)
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 🧪 Sample Data
See `sample_data/warehouses.csv`.

## 🗺️ Basemap Sources
- CARTO: `https://basemaps.cartocdn.com/*`
- OpenStreetMap: `https://tile.openstreetmap.org/{z}/{x}/{y}.png`

> Attribution: © OpenStreetMap contributors; © CARTO basemaps.

## 🚀 Deploy
Upload these files to GitHub, then deploy to Streamlit Cloud pointing to `streamlit_app.py`.
