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

Then open the URL shown in your terminal.

## 🧪 Sample Data
See `sample_data/warehouses.csv` for a quick test.

## 🗺️ Basemap Sources
- CARTO: `https://basemaps.cartocdn.com/*`
- OpenStreetMap: `https://tile.openstreetmap.org/{z}/{x}/{y}.png`

> Attribution: © OpenStreetMap contributors; © CARTO basemaps.

## 🚀 Deploy to GitHub + Streamlit Cloud
1. Create a new GitHub repository and upload the files in this folder.
2. On Streamlit Community Cloud, create a new app pointing to `streamlit_app.py`.
3. No extra secrets are required because the app uses raster tiles directly (no Mapbox token).

## 📁 Project Structure
```
streamlit_app.py
requirements.txt
README.md
sample_data/
  └─ warehouses.csv
```

## 📄 License
MIT
