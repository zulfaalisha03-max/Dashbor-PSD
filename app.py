"""
=============================================================================
🏆 TROPICAL HERITAGE DASHBOARD - FINAL COMPLETE EDITION
UAS Pengenalan Sains Data - UIN K.H. Abdurrahman Wahid Pekalongan
Mencakup: Soal A-F + 4 Bonus + Peta Premium + Fix Warna Teks
=============================================================================
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import io
import base64
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ==========================================
# 1. PAGE CONFIG & COMPLETE CSS
# ==========================================
st.set_page_config(
    page_title="Tropical Heritage Dashboard",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Lato:wght@300;400;700&display=swap');

* { font-family: 'Lato', sans-serif; }
h1, h2, h3, .brand-title { font-family: 'Playfair Display', serif !important; }

.stApp {
    background: #f8f5f0;
    background-image:
        radial-gradient(at 20% 30%, rgba(42, 157, 143, 0.08) 0px, transparent 50%),
        radial-gradient(at 80% 70%, rgba(233, 196, 106, 0.08) 0px, transparent 50%);
}

#MainMenu, footer, header { visibility: hidden; }

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a4d2e 0%, #2d7a4a 100%);
    border-right: 3px solid #e9c46a;
}
[data-testid="stSidebar"] * { color: #f8f5f0 !important; }

.sidebar-brand {
    text-align: center; padding: 25px 15px; margin-bottom: 20px;
    background: rgba(248, 245, 240, 0.08); border-radius: 15px;
    border: 1px solid rgba(233, 196, 106, 0.3);
    animation: fadeInUp 0.8s ease-out;
}
.sidebar-brand .logo-emoji { font-size: 50px; display: block; margin-bottom: 10px; }
.sidebar-brand h1 { color: #e9c46a !important; font-size: 24px; font-weight: 900; margin: 0; letter-spacing: 1px; }
.sidebar-brand p { color: #f8f5f0 !important; font-size: 11px; margin: 5px 0 0 0; letter-spacing: 3px; text-transform: uppercase; opacity: 0.9; }

div[role="radiogroup"] > label {
    background: rgba(248, 245, 240, 0.08); padding: 12px 16px !important;
    border-radius: 10px !important; margin-bottom: 6px !important;
    border-left: 3px solid transparent; transition: all 0.3s ease;
}
div[role="radiogroup"] > label:hover { background: rgba(233, 196, 106, 0.15); border-left-color: #e9c46a; transform: translateX(4px); }
div[role="radiogroup"] > label[data-baseweb="radio"]:has(input:checked) {
    background: linear-gradient(90deg, #e9c46a, #f4a261) !important;
    color: #1a4d2e !important; font-weight: 700; border-left-color: #e76f51 !important;
}
div[role="radiogroup"] > label[data-baseweb="radio"]:has(input:checked) * { color: #1a4d2e !important; }

.hero-tropical {
    background: linear-gradient(135deg, #1a4d2e 0%, #2a9d8f 50%, #e9c46a 100%);
    padding: 45px 40px; border-radius: 20px; color: #f8f5f0; margin-bottom: 25px;
    position: relative; overflow: hidden; box-shadow: 0 15px 40px rgba(26, 77, 46, 0.25);
    animation: fadeInUp 0.6s ease-out;
}
.hero-tropical::before { content: "🌴"; position: absolute; right: 40px; top: 20%; font-size: 100px; opacity: 0.2; transform: rotate(-15deg); }
.hero-title { font-family: 'Playfair Display', serif !important; font-size: 40px; font-weight: 900; margin: 0; color: #f8f5f0 !important; position: relative; z-index: 1; }
.hero-subtitle { color: #e9c46a !important; font-size: 17px; margin-top: 10px; font-style: italic; position: relative; z-index: 1; }

.tropical-card {
    background: #ffffff; padding: 28px; border-radius: 18px; border-top: 5px solid #2a9d8f;
    box-shadow: 0 5px 20px rgba(26, 77, 46, 0.08); margin-bottom: 20px;
    transition: all 0.3s ease; animation: fadeInUp 0.8s ease-out;
}
.tropical-card:hover { box-shadow: 0 12px 30px rgba(26, 77, 46, 0.15); transform: translateY(-3px); }

.kpi-tropical {
    background: linear-gradient(135deg, #ffffff 0%, #f8f5f0 100%); padding: 22px; border-radius: 15px;
    border-left: 6px solid #e9c46a; box-shadow: 0 5px 20px rgba(0,0,0,0.06);
    position: relative; overflow: hidden; transition: all 0.3s ease; height: 100%;
    animation: fadeInUp 0.8s ease-out;
}
.kpi-tropical::after {
    content: ""; position: absolute; bottom: 0; left: 0; width: 100%; height: 3px;
    background: linear-gradient(90deg, #2a9d8f, #e9c46a, #e76f51);
}
.kpi-tropical:hover { transform: translateY(-5px); box-shadow: 0 12px 28px rgba(26, 77, 46, 0.15); }
.kpi-icon { font-size: 34px; margin-bottom: 8px; }
.kpi-label { color: #7a6f5f; font-size: 11px; text-transform: uppercase; letter-spacing: 2px; font-weight: 700; }
.kpi-value { color: #1a4d2e; font-size: 28px; font-weight: 900; margin: 5px 0; font-family: 'Playfair Display', serif; }
.kpi-trend { color: #e76f51; font-size: 12px; font-weight: 600; font-style: italic; }

.section-title {
    font-family: 'Playfair Display', serif; color: #1a4d2e; font-size: 24px; font-weight: 900;
    margin-bottom: 15px; padding-bottom: 10px; border-bottom: 2px solid #e9c46a; display: inline-block;
}

.insight-leaf {
    background: linear-gradient(135deg, #f4a261 0%, #e9c46a 100%); padding: 20px; border-radius: 12px;
    margin-bottom: 15px; position: relative; color: #1a4d2e; box-shadow: 0 4px 15px rgba(244, 162, 97, 0.3);
    animation: fadeInUp 0.5s ease-out;
}
.insight-leaf::before { content: "🌿"; position: absolute; top: -10px; right: 15px; font-size: 30px; }
.insight-leaf b { color: #1a4d2e; }

.rec-leaf {
    background: linear-gradient(135deg, #2a9d8f 0%, #2d7a4a 100%); padding: 20px; border-radius: 12px;
    margin-bottom: 15px; color: #f8f5f0; box-shadow: 0 4px 15px rgba(42, 157, 143, 0.3); position: relative;
    animation: fadeInUp 0.5s ease-out;
}
.rec-leaf::before { content: "🌴"; position: absolute; top: -10px; right: 15px; font-size: 30px; }
.rec-leaf b { color: #e9c46a; }

.stTabs [data-baseweb="tab-list"] { background: #ffffff; border-radius: 12px; padding: 5px; border: 2px solid #e9c46a; }
.stTabs [data-baseweb="tab"] { color: #7a6f5f !important; border-radius: 8px; padding: 10px 20px !important; font-weight: 700; }
.stTabs [aria-selected="true"] { background: linear-gradient(135deg, #1a4d2e 0%, #2a9d8f 100%) !important; color: #e9c46a !important; }

.stButton > button {
    background: linear-gradient(135deg, #1a4d2e, #2a9d8f); color: #e9c46a; border: 2px solid #e9c46a;
    padding: 10px 25px; border-radius: 10px; font-weight: 700; letter-spacing: 1px; transition: all 0.3s;
}
.stButton > button:hover { background: #e9c46a; color: #1a4d2e; transform: translateY(-2px); box-shadow: 0 5px 15px rgba(233, 196, 106, 0.4); }

.tropical-divider { height: 3px; background: linear-gradient(90deg, transparent, #e9c46a, #2a9d8f, transparent); margin: 30px 0; border-radius: 3px; }
.map-info { background: linear-gradient(135deg, #f4a261, #e76f51); padding: 20px; border-radius: 12px; color: white; margin: 15px 0; box-shadow: 0 4px 15px rgba(231, 111, 81, 0.3); }
.footer-tropical { background: linear-gradient(135deg, #1a4d2e, #2d7a4a); padding: 30px; border-radius: 20px; text-align: center; color: #f8f5f0; margin-top: 40px; border-top: 4px solid #e9c46a; }
.stAlert { border-radius: 12px !important; border-left: 4px solid #e9c46a !important; }

/* FIX: WARNA TEKS PENCARIAN & WIDGET AGAR TERBACA */
[data-testid="stWidgetLabel"] { color: #1a4d2e !important; font-weight: 700 !important; }
[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
[data-testid="stMultiSelect"] div[data-baseweb="select"] > div,
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input {
    color: #1a4d2e !important; background-color: #ffffff !important;
    border: 2px solid #e9c46a !important; border-radius: 10px !important;
}
[data-testid="stSelectbox"] input::placeholder,
[data-testid="stMultiSelect"] input::placeholder,
[data-testid="stTextInput"] input::placeholder { color: #7a6f5f !important; opacity: 1 !important; }
div[data-baseweb="popover"] li { color: #1a4d2e !important; background-color: #ffffff !important; }
div[data-baseweb="popover"] li:hover,
div[data-baseweb="popover"] li[aria-selected="true"] { background-color: #e9c46a !important; color: #1a4d2e !important; }
[data-testid="stMultiSelect"] span[data-baseweb="tag"] { background-color: #2a9d8f !important; color: #ffffff !important; border-radius: 8px !important; }
[data-testid="stSlider"] label,
[data-testid="stSlider"] div[data-testid="stTickBar"] { color: #1a4d2e !important; }
[data-testid="stCaptionContainer"] { color: #7a6f5f !important; }
/* === FIX FINAL: SELECTBOX & WIDGET DI SIDEBAR === */

/* 1. Label Widget di Sidebar */
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
    color: #e9c46a !important;
    font-weight: 700 !important;
    font-size: 14px !important;
}

/* 2. Kotak Selectbox/Multiselect di Sidebar - Background Gelap + Teks Terang */
[data-testid="stSidebar"] div[data-baseweb="select"] > div {
    background-color: rgba(255, 255, 255, 0.1) !important;
    border: 2px solid #e9c46a !important;
    border-radius: 10px !important;
    color: #ffffff !important;
}

/* 3. Teks Nilai yang Dipilih di Selectbox Sidebar */
[data-testid="stSidebar"] div[data-baseweb="select"] span {
    color: #ffffff !important;
    font-weight: 600 !important;
}

/* 4. Placeholder Text di Sidebar */
[data-testid="stSidebar"] input::placeholder {
    color: rgba(255, 255, 255, 0.6) !important;
    opacity: 1 !important;
}

/* 5. Dropdown Options (Popover) - Tetap Gelap agar Terbaca */
div[data-baseweb="popover"] li {
    color: #1a4d2e !important;
    background-color: #ffffff !important;
}

div[data-baseweb="popover"] li:hover,
div[data-baseweb="popover"] li[aria-selected="true"] {
    background-color: #e9c46a !important;
    color: #1a4d2e !important;
    font-weight: 700 !important;
}

/* 6. Slider di Sidebar */
[data-testid="stSidebar"] [data-testid="stSlider"] label {
    color: #e9c46a !important;
}

[data-testid="stSidebar"] [data-testid="stTickBar"] {
    color: #f8f5f0 !important;
}

/* 7. Caption/Helper Text di Sidebar */
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: rgba(248, 245, 240, 0.7) !important;
}

/* 8. Multiselect Tags di Sidebar */
[data-testid="stSidebar"] span[data-baseweb="tag"] {
    background-color: #e9c46a !important;
    color: #1a4d2e !important;
    border-radius: 8px !important;
}

/* 9. Icon Panah Selectbox di Sidebar */
[data-testid="stSidebar"] div[data-baseweb="select"] svg {
    fill: #e9c46a !important;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATA & HELPER FUNCTIONS
# ==========================================
CSV_DATA = """Provinsi,Kelapa_Sawit,Kelapa,Karet,Kopi,Kakao,Teh,Tebu
ACEH,1092.71,64.1,51.17,74.13,34.17,0.0,0.0
SUMATERA UTARA,5120.02,103.64,251.52,91.69,38.48,10.14,14.52
SUMATERA BARAT,1410.64,79.06,99.67,15.32,34.58,5.6,0.0
RIAU,9136.1,399.95,180.74,1.83,0.84,0.0,0.0
JAMBI,2113.97,115.35,222.56,23.23,0.69,4.24,0.0
SUMATERA SELATAN,3967.39,61.65,619.55,219.59,4.4,2.62,124.37
BENGKULU,1298.17,7.25,64.6,55.63,2.36,1.88,0.0
LAMPUNG,375.24,83.76,84.83,120.38,48.11,0.0,644.48
KEP. BANGKA BELITUNG,860.24,4.55,26.04,0.11,0.29,0.0,0.0
KEP. RIAU,24.19,12.16,8.41,0.0,0.01,0.0,0.0
DKI JAKARTA,0.0,0.0,0.0,0.0,0.0,0.0,0.0
JAWA BARAT,46.75,88.14,21.17,26.48,0.71,80.24,55.17
JAWA TENGAH,0.0,139.01,20.73,26.79,1.31,11.81,250.07
DI YOGYAKARTA,0.0,50.08,0.01,1.88,2.03,0.23,3.22
JAWA TIMUR,0.0,194.14,16.27,53.25,10.56,2.14,1252.84
BANTEN,32.84,45.83,5.77,2.02,2.12,0.01,0.0
BALI,0.0,68.39,0.0,14.71,4.87,0.0,0.0
NUSA TENGGARA BARAT,0.0,49.81,0.0,6.42,2.59,0.0,18.22
NUSA TENGGARA TIMUR,0.0,62.15,0.0,24.38,21.08,0.0,10.77
KALIMANTAN BARAT,4958.54,76.8,158.41,2.98,0.6,0.0,0.0
KALIMANTAN TENGAH,7458.14,16.6,108.29,0.24,1.61,0.0,0.0
KALIMANTAN SELATAN,1255.08,24.01,127.96,0.89,0.05,0.0,0.0
KALIMANTAN TIMUR,3905.19,9.82,53.49,0.12,1.03,0.0,0.0
KALIMANTAN UTARA,611.14,0.64,0.16,0.11,0.79,0.0,0.0
SULAWESI UTARA,0.0,270.3,0.0,3.72,5.62,0.0,0.0
SULAWESI TENGAH,384.2,199.64,1.37,3.13,125.2,0.0,0.0
SULAWESI SELATAN,133.5,67.57,3.77,31.79,80.52,0.0,22.56
SULAWESI TENGGARA,75.47,42.87,0.22,2.61,98.02,0.0,15.41
GORONTALO,22.83,66.7,0.0,0.13,1.54,0.0,53.89
SULAWESI BARAT,366.68,36.72,0.0,4.75,67.14,0.0,0.0
MALUKU,22.33,107.73,0.6,0.49,8.59,0.0,0.0
MALUKU UTARA,20.14,204.17,0.0,0.02,7.38,0.0,0.0
PAPUA BARAT,40.38,2.02,0.0,0.01,0.24,0.0,0.0
PAPUA BARAT DAYA,43.44,14.35,0.0,0.0,0.76,0.0,0.0
PAPUA,130.55,9.77,0.0,0.09,8.0,0.0,0.0
PAPUA SELATAN,482.37,4.35,4.82,0.0,0.01,0.0,0.0
PAPUA TENGAH,47.98,1.2,0.0,1.18,0.82,0.0,0.0
PAPUA PEGUNUNGAN,0.0,0.02,0.0,3.27,0.0,0.0,0.0"""

df = pd.read_csv(io.StringIO(CSV_DATA))
num_cols = [c for c in df.columns if c != 'Provinsi']

COORDS = {
    'ACEH': (5.55, 95.32), 'SUMATERA UTARA': (2.59, 99.07), 'SUMATERA BARAT': (-0.79, 100.35),
    'RIAU': (1.08, 101.74), 'JAMBI': (-1.61, 103.61), 'SUMATERA SELATAN': (-2.98, 104.76),
    'BENGKULU': (-3.80, 102.26), 'LAMPUNG': (-4.56, 105.41), 'KEP. BANGKA BELITUNG': (-2.74, 106.43),
    'KEP. RIAU': (1.05, 104.03), 'DKI JAKARTA': (-6.17, 106.83), 'JAWA BARAT': (-6.91, 107.61),
    'JAWA TENGAH': (-7.15, 110.42), 'DI YOGYAKARTA': (-7.80, 110.36), 'JAWA TIMUR': (-7.27, 112.74),
    'BANTEN': (-6.44, 106.14), 'BALI': (-8.41, 115.19), 'NUSA TENGGARA BARAT': (-8.59, 116.10),
    'NUSA TENGGARA TIMUR': (-8.65, 121.08), 'KALIMANTAN BARAT': (-0.03, 109.33),
    'KALIMANTAN TENGAH': (-1.69, 113.38), 'KALIMANTAN SELATAN': (-3.32, 114.59),
    'KALIMANTAN TIMUR': (0.54, 116.42), 'KALIMANTAN UTARA': (3.08, 116.04),
    'SULAWESI UTARA': (1.47, 124.84), 'SULAWESI TENGAH': (-1.44, 121.44),
    'SULAWESI SELATAN': (-3.67, 119.97), 'SULAWESI TENGGARA': (-3.98, 122.51),
    'GORONTALO': (0.72, 122.44), 'SULAWESI BARAT': (-2.84, 119.23), 'MALUKU': (-3.24, 130.14),
    'MALUKU UTARA': (1.57, 127.79), 'PAPUA BARAT': (-1.34, 133.44), 'PAPUA BARAT DAYA': (-1.50, 132.00),
    'PAPUA': (-4.27, 138.08), 'PAPUA SELATAN': (-7.27, 140.44), 'PAPUA TENGAH': (-3.50, 137.00),
    'PAPUA PEGUNUNGAN': (-4.00, 138.50)
}

def make_premium_map(df_map, komoditas):
    df_map = df_map.copy()
    df_map['lat'] = df_map['Provinsi'].map(lambda x: COORDS.get(x, (0, 0))[0])
    df_map['lon'] = df_map['Provinsi'].map(lambda x: COORDS.get(x, (0, 0))[1])
    df_map = df_map[df_map['lat'] != 0]
    df_map['Rank'] = df_map[komoditas].rank(ascending=False).astype(int)
    total_nasional = df_map[komoditas].sum()
    df_map['Kontribusi %'] = ((df_map[komoditas] / total_nasional) * 100).round(1)
    df_map['hover_text'] = df_map.apply(
        lambda row: (
            f"<b style='font-size:14px;'>🏝️ {row['Provinsi']}</b><br>"
            f"<span style='color:#2a9d8f;'>━━━━━━━━━━━━━━━━━━</span><br>"
            f"🌱 <b>{komoditas.replace('_', ' ')}</b>: {row[komoditas]:,.1f} Ton<br>"
            f"🏆 Ranking Nasional: <b>#{int(row['Rank'])}</b> dari {len(df_map)}<br>"
            f"📊 Kontribusi: <b>{row['Kontribusi %']}%</b> dari total nasional"
        ), axis=1
    )
    fig = px.scatter_geo(
        df_map, lat='lat', lon='lon', size=komoditas, color=komoditas,
        hover_name=None, hover_data=None, custom_data=['hover_text'],
        color_continuous_scale=[(0, '#f8f5f0'), (0.2, '#e9c46a'), (0.5, '#f4a261'), (0.8, '#e76f51'), (1, '#c1121f')],
        scope='asia', center=dict(lat=-2.5, lon=118), projection='natural earth', size_max=50
    )
    fig.update_traces(hovertemplate='%{customdata[0]}<extra></extra>', marker=dict(line=dict(width=2, color='#1a4d2e'), opacity=0.9))
    fig.update_geos(showcountries=True, countrycolor='#2a9d8f', countrywidth=1.5, showcoastlines=True, coastlinecolor='#1a4d2e', coastlinewidth=1.5, showland=True, landcolor='#f4e4bc', showocean=True, oceancolor='#a8d5e2', showlakes=False, resolution=50, lataxis_range=[-12, 8], lonaxis_range=[93, 143])
    fig.update_layout(height=650, margin=dict(l=0, r=0, t=60, b=0), paper_bgcolor='#f8f5f0', dragmode='pan', font=dict(family='Lato', color='#1a4d2e'),
        coloraxis_colorbar=dict(title=dict(text=f"Produksi {komoditas.replace('_', ' ')}<br>(Ton)", font=dict(size=14, family='Playfair Display', color='#1a4d2e')), thickness=20, len=0.75, bgcolor='rgba(255,255,255,0.9)', bordercolor='#e9c46a', borderwidth=2, tickfont=dict(size=11, color='#1a4d2e'), outlinewidth=0, x=1.02),
        title=dict(text=f"🗺️ Peta Sebaran Produksi {komoditas.replace('_', ' ')} di Indonesia", font=dict(family='Playfair Display', size=24, color='#1a4d2e'), x=0.5, y=0.98),
        modebar=dict(bgcolor='rgba(255,255,255,0.8)', color='#1a4d2e', activecolor='#e76f51')
    )
    return fig

def get_table_download_link(df_data, filename="data_perkebunan.csv"):
    csv = df_data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}" style="background:linear-gradient(135deg,#1a4d2e,#2a9d8f);color:#e9c46a;padding:10px 20px;border-radius:10px;text-decoration:none;font-weight:bold;border:2px solid #e9c46a;display:inline-block;margin-top:10px;">📥 Download Dataset CSV</a>'
    return href

# ==========================================
# 3. SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <span class="logo-emoji">🌿</span>
        <h1>TROPICAL<br>HERITAGE</h1>
        <p>Indonesian Plantation</p>
    </div>
    """, unsafe_allow_html=True)
    
    menu = st.radio("**NAVIGASI**", [
        "Beranda & Peta", "A. Data Understanding", "B. Data Cleaning",
        "C. EDA (6 Visualisasi)", "D. Analisis Hubungan", "E. Regresi Linear",
        "BONUS: Random Forest", "BONUS: Decision Tree", "BONUS: Forecasting",
        "BONUS: Komparator", "F. Insight & Rekomendasi"
    ])
    
    st.markdown("---")
    st.markdown("**FILTER KOMODITAS**")
    kom_filter = st.selectbox("Pilih Komoditas:", num_cols, index=0)
    
    st.markdown("---")
    st.markdown(get_table_download_link(df), unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align:center; padding:12px; background:rgba(233,196,106,0.15); border-radius:10px; border:1px solid rgba(233,196,106,0.3); margin-top:20px;">
        <div style="font-size:10px; letter-spacing:2px;">UAS SAINS DATA 2026</div>
        <div style="font-size:9px; margin-top:4px; opacity:0.8;">UIN GUS DUR PEKALONGAN</div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 4. ROUTING HALAMAN
# ==========================================

if menu == "Beranda & Peta":
    st.markdown('<div class="hero-tropical"><div class="hero-title">Tropical Heritage Dashboard</div><div class="hero-subtitle">Menelusuri Jejak Perkebunan Nusantara dari Sabang sampai Merauke</div></div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    total_prod = df[num_cols].sum().sum()
    top_kom = df[num_cols].sum().idxmax().replace('_', ' ')
    with c1: st.markdown(f'<div class="kpi-tropical"><div class="kpi-icon">🗺️</div><div class="kpi-label">Provinsi Terdata</div><div class="kpi-value">{df.shape[0]}</div><div class="kpi-trend">Nusantara</div></div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="kpi-tropical"><div class="kpi-icon">🌱</div><div class="kpi-label">Jenis Komoditas</div><div class="kpi-value">{len(num_cols)}</div><div class="kpi-trend">Tanaman Tropis</div></div>', unsafe_allow_html=True)
    with c3: st.markdown(f'<div class="kpi-tropical"><div class="kpi-icon">📊</div><div class="kpi-label">Total Produksi</div><div class="kpi-value">{total_prod/1000:.1f}K</div><div class="kpi-trend">Ton Nasional</div></div>', unsafe_allow_html=True)
    with c4: st.markdown(f'<div class="kpi-tropical"><div class="kpi-icon">🏆</div><div class="kpi-label">Primadona</div><div class="kpi-value" style="font-size:20px;">{top_kom}</div><div class="kpi-trend">Produksi Tertinggi</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="tropical-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="tropical-card"><div class="section-title">PETA PERKEBUNAN INDONESIA</div><p style="color:#7a6f5f; margin-top:-5px;">🖱️ <b>Hover</b> untuk detail | 🔍 <b>Scroll</b> untuk zoom | ✋ <b>Drag</b> untuk geser</p></div>', unsafe_allow_html=True)
    fig_map = make_premium_map(df, kom_filter)
    st.plotly_chart(fig_map, use_container_width=True)
    top_prov = df.loc[df[kom_filter].idxmax(), 'Provinsi']
    top_val = df[kom_filter].max()
    top_pct = (top_val / df[kom_filter].sum()) * 100
    st.markdown(f'<div class="map-info"><b>🌿 Insight Peta {kom_filter.replace("_"," ")}:</b><br>• Sentra utama: <b>{top_prov}</b> dengan {top_val:,.1f} ton ({top_pct:.1f}% nasional)<br>• Ukuran lingkaran merepresentasikan volume produksi<br>• Warna lebih gelap = produksi lebih tinggi</div>', unsafe_allow_html=True)
    st.markdown('<div class="tropical-divider"></div>', unsafe_allow_html=True)
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown('<div class="tropical-card"><div class="section-title">Top 10 Provinsi Sentra Produksi</div></div>', unsafe_allow_html=True)
        top10 = df.copy(); top10['Total'] = top10[num_cols].sum(axis=1); top10 = top10.nlargest(10, 'Total')
        fig = px.bar(top10, x='Total', y='Provinsi', orientation='h', color='Total', color_continuous_scale=[(0, '#f4a261'), (0.5, '#e76f51'), (1, '#1a4d2e')])
        fig.update_layout(height=450, plot_bgcolor='#f8f5f0', paper_bgcolor='#ffffff', font=dict(family='Lato', color='#1a4d2e'), showlegend=False, margin=dict(l=20, r=20, t=20, b=20))
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown('<div class="tropical-card"><div class="section-title">Komposisi Komoditas</div></div>', unsafe_allow_html=True)
        kom_total = df[num_cols].sum()
        fig_pie = px.pie(values=kom_total.values, names=[c.replace('_', ' ') for c in kom_total.index], hole=0.4, color_discrete_sequence=['#1a4d2e', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51', '#7a6f5f', '#d4a373'])
        fig_pie.update_layout(height=450, plot_bgcolor='#ffffff', paper_bgcolor='#ffffff', font=dict(family='Lato', color='#1a4d2e'))
        st.plotly_chart(fig_pie, use_container_width=True)

elif menu == "A. Data Understanding":
    st.markdown('<div class="hero-tropical"><div class="hero-title">A. Data Understanding</div><div class="hero-subtitle">Mengenal Struktur Data Perkebunan Nusantara (Bobot 10%)</div></div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f'<div class="kpi-tropical"><div class="kpi-icon">📋</div><div class="kpi-label">Observasi</div><div class="kpi-value">{df.shape[0]}</div><div class="kpi-trend">Provinsi</div></div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="kpi-tropical"><div class="kpi-icon">📐</div><div class="kpi-label">Variabel</div><div class="kpi-value">{df.shape[1]}</div><div class="kpi-trend">Total Kolom</div></div>', unsafe_allow_html=True)
    with c3: st.markdown(f'<div class="kpi-tropical"><div class="kpi-icon">🔢</div><div class="kpi-label">Numerik</div><div class="kpi-value">{len(num_cols)}</div><div class="kpi-trend">Komoditas</div></div>', unsafe_allow_html=True)
    tab1, tab2, tab3, tab4 = st.tabs(["Preview", "Info", "Statistik", "Deskripsi"])
    with tab1: st.markdown('<div class="tropical-card"><div class="section-title">Preview Data</div></div>', unsafe_allow_html=True); st.dataframe(df.head(), use_container_width=True)
    with tab2: st.markdown('<div class="tropical-card"><div class="section-title">Info Data</div></div>', unsafe_allow_html=True); buf = io.StringIO(); df.info(buf=buf); st.code(buf.getvalue())
    with tab3: st.markdown('<div class="tropical-card"><div class="section-title">Statistik Deskriptif</div></div>', unsafe_allow_html=True); st.dataframe(df[num_cols].describe().round(2), use_container_width=True)
    with tab4:
        st.markdown('<div class="tropical-card"><div class="section-title">Deskripsi Variabel</div></div>', unsafe_allow_html=True)
        for col in df.columns:
            desc = 'Nama provinsi (38 provinsi)' if col == 'Provinsi' else f'Produksi {col.replace("_"," ").lower()} dalam ton'
            st.markdown(f'<div class="insight-leaf"><b>{col}:</b> {desc}</div>', unsafe_allow_html=True)

elif menu == "B. Data Cleaning":
    st.markdown('<div class="hero-tropical"><div class="hero-title">B. Data Cleaning</div><div class="hero-subtitle">Proses Pembersihan Data Sebelum Analisis (Bobot 15%)</div></div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown(f'<div class="kpi-tropical" style="border-left-color:#2a9d8f;"><div class="kpi-icon">✅</div><div class="kpi-label">Missing Values</div><div class="kpi-value">{df.isnull().sum().sum()}</div><div class="kpi-trend" style="color:#2a9d8f;">Data Lengkap</div></div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="kpi-tropical" style="border-left-color:#2a9d8f;"><div class="kpi-icon">✅</div><div class="kpi-label">Duplikat</div><div class="kpi-value">{df.duplicated().sum()}</div><div class="kpi-trend" style="color:#2a9d8f;">Data Unik</div></div>', unsafe_allow_html=True)
    with c3: st.markdown(f'<div class="kpi-tropical" style="border-left-color:#2a9d8f;"><div class="kpi-icon">✅</div><div class="kpi-label">Tipe Data</div><div class="kpi-value" style="font-size:20px;">Valid</div><div class="kpi-trend" style="color:#2a9d8f;">Float & Object</div></div>', unsafe_allow_html=True)
    with c4: st.markdown(f'<div class="kpi-tropical" style="border-left-color:#e76f51;"><div class="kpi-icon">⚠️</div><div class="kpi-label">Outlier</div><div class="kpi-value" style="font-size:20px;">Natural</div><div class="kpi-trend">Data Sentra</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="tropical-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="tropical-card"><div class="section-title">Boxplot Deteksi Outlier</div></div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(14, 6)); fig.patch.set_facecolor('#ffffff'); ax.set_facecolor('#f8f5f0')
    sns.boxplot(data=df[num_cols], palette=['#1a4d2e', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51', '#7a6f5f', '#d4a373'], ax=ax)
    ax.set_yscale('symlog'); ax.set_title('Distribusi Produksi dengan Skala Symlog', color='#1a4d2e', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, color='#1a4d2e'); plt.tight_layout(); st.pyplot(fig)
    st.markdown('<div class="insight-leaf"><b>Keputusan:</b> Outlier TIDAK dihapus karena merupakan sentra produksi alami. Provinsi seperti Riau (Sawit: 9.136 ton) dan Jawa Timur (Tebu: 1.252 ton) memang sentra utama.</div>', unsafe_allow_html=True)

elif menu == "C. EDA (6 Visualisasi)":
    st.markdown('<div class="hero-tropical"><div class="hero-title">C. Exploratory Data Analysis</div><div class="hero-subtitle">6 Visualisasi Matplotlib dengan Interpretasi (Bobot 20%)</div></div>', unsafe_allow_html=True)
    tabs = st.tabs(["Histogram", "Scatter", "Line", "Bar", "Boxplot", "Heatmap"])
    with tabs[0]:
        st.markdown('<div class="tropical-card"><div class="section-title">Histogram - Distribusi Produksi</div></div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(12, 6)); fig.patch.set_facecolor('#ffffff'); ax.set_facecolor('#f8f5f0')
        ax.hist(df[kom_filter], bins=15, color='#2a9d8f', edgecolor='#1a4d2e', alpha=0.9)
        ax.axvline(df[kom_filter].mean(), color='#e76f51', linestyle='--', linewidth=3, label=f'Mean: {df[kom_filter].mean():.1f}')
        ax.set_title(f'Distribusi {kom_filter.replace("_"," ")}', color='#1a4d2e', fontsize=14, fontweight='bold')
        ax.set_xlabel('Produksi (Ton)', color='#1a4d2e'); ax.set_ylabel('Frekuensi', color='#1a4d2e')
        ax.legend(); ax.grid(alpha=0.2); plt.tight_layout(); st.pyplot(fig)
        st.markdown(f'<div class="insight-leaf"><b>Interpretasi:</b> Skewness = {df[kom_filter].skew():.2f} (right-skewed). Mayoritas provinsi produksi rendah.</div>', unsafe_allow_html=True)
    with tabs[1]:
        st.markdown('<div class="tropical-card"><div class="section-title">Scatter Plot - Hubungan Komoditas</div></div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: x = st.selectbox("X:", num_cols, key='sx')
        with c2: y = st.selectbox("Y:", num_cols, index=1, key='sy')
        fig, ax = plt.subplots(figsize=(12, 6)); fig.patch.set_facecolor('#ffffff'); ax.set_facecolor('#f8f5f0')
        ax.scatter(df[x], df[y], c='#f4a261', s=150, edgecolors='#1a4d2e', linewidth=2, alpha=0.9)
        z = np.polyfit(df[x], df[y], 1); p = np.poly1d(z)
        ax.plot(sorted(df[x]), p(sorted(df[x])), color='#e76f51', linestyle='--', linewidth=3, label='Trend')
        corr_val = df[x].corr(df[y])
        ax.set_title(f'{x} vs {y} (r = {corr_val:.3f})', color='#1a4d2e', fontsize=14, fontweight='bold')
        ax.legend(); ax.grid(alpha=0.2); plt.tight_layout(); st.pyplot(fig)
        strength = 'kuat' if abs(corr_val) > 0.5 else 'sedang' if abs(corr_val) > 0.3 else 'lemah'
        st.markdown(f'<div class="insight-leaf"><b>Interpretasi:</b> Korelasi = {corr_val:.3f} ({strength})</div>', unsafe_allow_html=True)
    with tabs[2]:
        st.markdown('<div class="tropical-card"><div class="section-title">Line Plot - Top Provinsi</div></div>', unsafe_allow_html=True)
        n = st.slider("Top N:", 5, 20, 10); top = df.nlargest(n, kom_filter)
        fig, ax = plt.subplots(figsize=(14, 6)); fig.patch.set_facecolor('#ffffff'); ax.set_facecolor('#f8f5f0')
        ax.plot(range(len(top)), top[kom_filter], marker='o', color='#e76f51', linewidth=3, markersize=12)
        ax.fill_between(range(len(top)), top[kom_filter], alpha=0.3, color='#f4a261')
        ax.set_xticks(range(len(top))); ax.set_xticklabels(top['Provinsi'], rotation=45, ha='right', color='#1a4d2e', fontweight='bold')
        ax.set_ylabel('Produksi (Ton)', color='#1a4d2e'); ax.set_title(f'Top {n} - {kom_filter}', color='#1a4d2e', fontsize=14, fontweight='bold')
        ax.grid(alpha=0.2); plt.tight_layout(); st.pyplot(fig)
        st.markdown('<div class="insight-leaf"><b>Interpretasi:</b> Produksi sangat terkonsentrasi. Provinsi #1 mendominasi.</div>', unsafe_allow_html=True)
    with tabs[3]:
        st.markdown('<div class="tropical-card"><div class="section-title">Bar Chart - Total Komoditas</div></div>', unsafe_allow_html=True)
        total = df[num_cols].sum().sort_values(ascending=True)
        fig, ax = plt.subplots(figsize=(12, 6)); fig.patch.set_facecolor('#ffffff'); ax.set_facecolor('#f8f5f0')
        colors = ['#f8f5f0', '#e9c46a', '#f4a261', '#e76f51', '#2a9d8f', '#1a4d2e', '#7a6f5f']
        bars = ax.barh(total.index, total.values, color=colors[:len(total)], edgecolor='#1a4d2e', linewidth=2)
        ax.set_title('Total Produksi per Komoditas', color='#1a4d2e', fontsize=14, fontweight='bold')
        for bar, val in zip(bars, total.values): ax.text(bar.get_width() + max(total)*0.01, bar.get_y() + bar.get_height()/2, f'{val:,.0f}', va='center', color='#1a4d2e', fontweight='bold')
        ax.grid(alpha=0.2, axis='x'); plt.tight_layout(); st.pyplot(fig)
        st.markdown('<div class="insight-leaf"><b>Interpretasi:</b> Kelapa Sawit mendominasi dengan selisih sangat jauh.</div>', unsafe_allow_html=True)
    with tabs[4]:
        st.markdown('<div class="tropical-card"><div class="section-title">Boxplot - Sebaran per Komoditas</div></div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(12, 6)); fig.patch.set_facecolor('#ffffff'); ax.set_facecolor('#f8f5f0')
        df_m = df.melt(id_vars=['Provinsi'], value_vars=num_cols)
        sns.boxplot(data=df_m, x='variable', y='value', ax=ax, palette=['#1a4d2e', '#2a9d8f', '#e9c46a', '#f4a261', '#e76f51', '#7a6f5f', '#d4a373'])
        ax.set_title('Distribusi Produksi per Komoditas', color='#1a4d2e', fontsize=14, fontweight='bold')
        plt.xticks(rotation=45, color='#1a4d2e'); ax.set_yscale('symlog'); ax.grid(alpha=0.2, axis='y'); plt.tight_layout(); st.pyplot(fig)
        st.markdown('<div class="insight-leaf"><b>Interpretasi:</b> Sawit variasi tertinggi, Teh & Kakao terendah.</div>', unsafe_allow_html=True)
    with tabs[5]:
        st.markdown('<div class="tropical-card"><div class="section-title">Heatmap - Korelasi Komoditas</div></div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(12, 10)); fig.patch.set_facecolor('#ffffff'); ax.set_facecolor('#f8f5f0')
        sns.heatmap(df[num_cols].corr(), annot=True, fmt='.2f', cmap='YlOrRd', ax=ax, linewidths=2, center=0)
        ax.set_title('Heatmap Korelasi', color='#1a4d2e', fontsize=14, fontweight='bold')
        plt.xticks(color='#1a4d2e', fontweight='bold'); plt.yticks(color='#1a4d2e', fontweight='bold'); plt.tight_layout(); st.pyplot(fig)
        st.markdown('<div class="insight-leaf"><b>Interpretasi:</b> Komoditas dengan iklim serupa cenderung berkorelasi positif.</div>', unsafe_allow_html=True)

elif menu == "D. Analisis Hubungan":
    st.markdown('<div class="hero-tropical"><div class="hero-title">D. Analisis Hubungan Variabel</div><div class="hero-subtitle">Identifikasi Variabel Paling Berpengaruh (Bobot 15%)</div></div>', unsafe_allow_html=True)
    corr = df[num_cols].corr()
    st.markdown('<div class="tropical-card"><div class="section-title">Matriks Korelasi</div></div>', unsafe_allow_html=True); st.dataframe(corr.round(3), use_container_width=True)
    st.markdown('<div class="tropical-divider"></div>', unsafe_allow_html=True)
    total_corr = corr.abs().sum().sort_values(ascending=False)
    st.markdown('<div class="tropical-card"><div class="section-title">Variabel Paling Berpengaruh</div></div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(12, 6)); fig.patch.set_facecolor('#ffffff'); ax.set_facecolor('#f8f5f0')
    colors = ['#e76f51' if i == 0 else '#2a9d8f' for i in range(len(total_corr))]
    bars = ax.barh(total_corr.index, total_corr.values, color=colors, edgecolor='#1a4d2e', linewidth=2)
    ax.set_title('Total Absolut Korelasi', color='#1a4d2e', fontsize=14, fontweight='bold'); ax.grid(alpha=0.2, axis='x')
    for bar, val in zip(bars, total_corr.values): ax.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2, f'{val:.2f}', va='center', color='#1a4d2e', fontweight='bold')
    plt.tight_layout(); st.pyplot(fig)
    top_var = total_corr.index[0]
    st.markdown(f'<div class="insight-leaf"><b>Paling Berpengaruh: {top_var.replace("_"," ").upper()}</b><br>Total korelasi absolut: <b>{total_corr.values[0]:.2f}</b><br>Variabel ini paling terhubung dengan komoditas lain - bisa jadi indikator utama sektor perkebunan.</div>', unsafe_allow_html=True)

elif menu == "E. Regresi Linear":
    st.markdown('<div class="hero-tropical"><div class="hero-title">E. Pemodelan Regresi Linear</div><div class="hero-subtitle">Prediksi dengan Metrik MAE, RMSE, R² (Bobot 20%)</div></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: target = st.selectbox("Target (Y):", num_cols)
    with c2: feats = st.multiselect("Fitur (X):", [c for c in num_cols if c != target], default=[c for c in num_cols if c != target][:3])
    if len(feats) > 0:
        X, y = df[feats], df[target]; X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression().fit(X_tr, y_tr); pred = model.predict(X_te)
        mae = mean_absolute_error(y_te, pred); rmse = np.sqrt(mean_squared_error(y_te, pred)); r2 = r2_score(y_te, pred)
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown(f'<div class="kpi-tropical" style="border-left-color:#f4a261;"><div class="kpi-icon">📉</div><div class="kpi-label">MAE</div><div class="kpi-value">{mae:.2f}</div><div class="kpi-trend">Rata-rata Error</div></div>', unsafe_allow_html=True)
        with c2: st.markdown(f'<div class="kpi-tropical" style="border-left-color:#e76f51;"><div class="kpi-icon">📊</div><div class="kpi-label">RMSE</div><div class="kpi-value">{rmse:.2f}</div><div class="kpi-trend">Std Error</div></div>', unsafe_allow_html=True)
        with c3:
            warna = '#2a9d8f' if r2 > 0.5 else '#e76f51'
            st.markdown(f'<div class="kpi-tropical" style="border-left-color:{warna};"><div class="kpi-icon">🎯</div><div class="kpi-label">R²</div><div class="kpi-value">{r2:.4f}</div><div class="kpi-trend">{r2*100:.1f}% Variasi</div></div>', unsafe_allow_html=True)
        eq = f"{target} = {model.intercept_:.2f}"
        for f, c in zip(feats, model.coef_): eq += f" + {c:.2f} × {f}"
        st.markdown(f'<div class="tropical-card"><div class="section-title">Persamaan Regresi</div><code style="font-size:14px; padding:15px; background:#f8f5f0; display:block; border-radius:10px; color:#1a4d2e; font-weight:bold;">{eq}</code></div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(10, 6)); fig.patch.set_facecolor('#ffffff'); ax.set_facecolor('#f8f5f0')
        ax.scatter(y_te, pred, c='#f4a261', s=150, edgecolors='#1a4d2e', linewidth=2, alpha=0.9)
        mn, mx = min(y_te.min(), pred.min()), max(y_te.max(), pred.max())
        ax.plot([mn, mx], [mn, mx], color='#e76f51', linestyle='--', linewidth=3, label='Perfect')
        ax.set_xlabel('Aktual', color='#1a4d2e'); ax.set_ylabel('Prediksi', color='#1a4d2e')
        ax.set_title('Aktual vs Prediksi', color='#1a4d2e', fontsize=14, fontweight='bold'); ax.legend(); ax.grid(alpha=0.2); plt.tight_layout(); st.pyplot(fig)
    else: st.warning("Pilih minimal 1 variabel independen!")

elif menu == "BONUS: Random Forest":
    st.markdown('<div class="hero-tropical"><div class="hero-title">BONUS: Random Forest Regressor</div><div class="hero-subtitle">Ensemble Learning dengan 100 Pohon Keputusan (10 Poin Bonus)</div></div>', unsafe_allow_html=True)
    target = st.selectbox("Target:", num_cols, key='rf'); feats = [c for c in num_cols if c != target]
    X, y = df[feats], df[target]; X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    rf = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=5).fit(X_tr, y_tr); pred = rf.predict(X_te)
    r2_rf = r2_score(y_te, pred); rmse_rf = np.sqrt(mean_squared_error(y_te, pred))
    c1, c2 = st.columns(2)
    with c1: st.markdown(f'<div class="kpi-tropical" style="border-left-color:#2a9d8f;"><div class="kpi-icon">🎯</div><div class="kpi-label">R² Score</div><div class="kpi-value">{r2_rf:.4f}</div><div class="kpi-trend">{r2_rf*100:.1f}% Akurasi</div></div>', unsafe_allow_html=True)
    with c2: st.markdown(f'<div class="kpi-tropical" style="border-left-color:#f4a261;"><div class="kpi-icon">📊</div><div class="kpi-label">RMSE</div><div class="kpi-value">{rmse_rf:.2f}</div><div class="kpi-trend">Error Standar</div></div>', unsafe_allow_html=True)
    fi = pd.DataFrame({'Feature': feats, 'Importance': rf.feature_importances_}).sort_values('Importance')
    fig, ax = plt.subplots(figsize=(10, 6)); fig.patch.set_facecolor('#ffffff'); ax.set_facecolor('#f8f5f0')
    ax.barh(fi['Feature'], fi['Importance'], color='#2a9d8f', edgecolor='#1a4d2e', linewidth=2)
    ax.set_title('Feature Importance', color='#1a4d2e', fontsize=14, fontweight='bold'); ax.grid(alpha=0.2, axis='x'); plt.tight_layout(); st.pyplot(fig)

elif menu == "BONUS: Decision Tree":
    st.markdown('<div class="hero-tropical"><div class="hero-title">BONUS: Decision Tree Regressor</div><div class="hero-subtitle">Model Berbasis Aturan IF-ELSE (10 Poin Bonus)</div></div>', unsafe_allow_html=True)
    target = st.selectbox("Target:", num_cols, key='dt'); depth = st.slider("Max Depth:", 2, 10, 4)
    feats = [c for c in num_cols if c != target]; X, y = df[feats], df[target]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    dt = DecisionTreeRegressor(max_depth=depth, random_state=42).fit(X_tr, y_tr); r2_dt = r2_score(y_te, dt.predict(X_te))
    st.markdown(f'<div class="kpi-tropical" style="width:300px;"><div class="kpi-icon">🎯</div><div class="kpi-label">R² Score</div><div class="kpi-value">{r2_dt:.4f}</div><div class="kpi-trend">{r2_dt*100:.1f}% Akurasi</div></div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(20, 10)); fig.patch.set_facecolor('#ffffff'); ax.set_facecolor('#f8f5f0')
    plot_tree(dt, feature_names=feats, filled=True, rounded=True, ax=ax, fontsize=8, impurity=False, proportion=False)
    plt.title(f'Decision Tree (Depth: {depth})', color='#1a4d2e', fontsize=14, fontweight='bold'); plt.tight_layout(); st.pyplot(fig)

elif menu == "BONUS: Forecasting":
    st.markdown('<div class="hero-tropical"><div class="hero-title">BONUS: Forecasting 5 Tahun</div><div class="hero-subtitle">Proyeksi dengan Growth Simulator (10 Poin Bonus)</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="insight-leaf"><b>Scientific Note:</b> Dataset cross-sectional, digunakan <b>Growth Projection Simulator</b> berbasis CAGR industri global.</div>', unsafe_allow_html=True)
    prov_fc = st.selectbox("Provinsi:", df['Provinsi'].tolist()); gr = st.slider("Growth Rate (%):", 1, 10, 5) / 100
    years = np.arange(2024, 2029); fig, ax = plt.subplots(figsize=(12, 6)); fig.patch.set_facecolor('#ffffff'); ax.set_facecolor('#f8f5f0')
    for kom in num_cols:
        base = df[df['Provinsi'] == prov_fc][kom].values[0]; vals = [base * ((1 + gr) ** i) for i in range(len(years))]
        lw = 3 if kom == kom_filter else 1; al = 1.0 if kom == kom_filter else 0.4; col = '#e76f51' if kom == kom_filter else '#7a6f5f'
        ax.plot(years, vals, marker='o', label=kom, linewidth=lw, alpha=al, color=col)
    ax.set_title(f'Forecast - {prov_fc}', color='#1a4d2e', fontsize=14, fontweight='bold')
    ax.set_xlabel('Tahun', color='#1a4d2e'); ax.set_ylabel('Produksi (Ton)', color='#1a4d2e')
    ax.legend(loc='upper left', ncol=2, facecolor='#ffffff', edgecolor='#e9c46a'); ax.grid(alpha=0.2); plt.tight_layout(); st.pyplot(fig)

elif menu == "BONUS: Komparator":
    st.markdown('<div class="hero-tropical"><div class="hero-title">BONUS: Province Comparator</div><div class="hero-subtitle">Bandingkan 2 Provinsi dengan Radar Chart (10 Poin Bonus)</div></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1: p1 = st.selectbox("Provinsi 1:", df['Provinsi'].tolist())
    with c2: p2 = st.selectbox("Provinsi 2:", df['Provinsi'].tolist(), index=1)
    fig = go.Figure()
    v1 = df[df['Provinsi'] == p1][num_cols].values.flatten().tolist(); v2 = df[df['Provinsi'] == p2][num_cols].values.flatten().tolist()
    fig.add_trace(go.Scatterpolar(r=v1+[v1[0]], theta=num_cols+[num_cols[0]], fill='toself', name=p1, line_color='#e76f51', fillcolor='rgba(231,111,81,0.3)'))
    fig.add_trace(go.Scatterpolar(r=v2+[v2[0]], theta=num_cols+[num_cols[0]], fill='toself', name=p2, line_color='#2a9d8f', fillcolor='rgba(42,157,143,0.3)'))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, gridcolor='#e9c46a'), angularaxis=dict(gridcolor='#e9c46a')), height=550, plot_bgcolor='#ffffff', paper_bgcolor='#ffffff', font=dict(family='Lato', color='#1a4d2e'))
    st.plotly_chart(fig, use_container_width=True)
    t1 = df[df['Provinsi'] == p1][num_cols].sum().sum(); t2 = df[df['Provinsi'] == p2][num_cols].sum().sum()
    win = p1 if t1 > t2 else p2
    st.markdown(f'<div class="insight-leaf"><b>Pemenang: {win}</b> dengan {max(t1,t2):,.0f} ton.</div>', unsafe_allow_html=True)

elif menu == "F. Insight & Rekomendasi":
    st.markdown('<div class="hero-tropical"><div class="hero-title">F. Insight & Rekomendasi</div><div class="hero-subtitle">Temuan & Rekomendasi Kebijakan (Bobot 20%)</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="tropical-card"><div class="section-title">5 INSIGHT UTAMA</div></div>', unsafe_allow_html=True)
    insights = [
        ("Kelapa Sawit Mendominasi", f"Menyumbang {df['Kelapa_Sawit'].sum()/df[num_cols].sum().sum()*100:.1f}% total produksi. Risiko ketergantungan tinggi."),
        ("Ketimpangan Spasial Tinggi", "Top 5 provinsi menyumbang > 50% produksi nasional."),
        ("Sumatera & Kalimantan Sentra", "Kedua pulau mendominasi karena iklim tropis ideal."),
        ("Tebu Terkonsentrasi di Jatim", "Risiko supply chain tinggi untuk industri gula."),
        ("Diversifikasi Rendah", "Banyak provinsi tidak memproduksi komoditas tertentu.")
    ]
    for i, (t, c) in enumerate(insights, 1): st.markdown(f'<div class="insight-leaf"><b>#{i} {t}:</b> {c}</div>', unsafe_allow_html=True)
    st.markdown('<div class="tropical-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="tropical-card"><div class="section-title">5 REKOMENDASI</div></div>', unsafe_allow_html=True)
    recs = [
        ("Diversifikasi Geografis", "Kembangkan perkebunan di Indonesia Timur dengan insentif petani."),
        ("Hilirisasi Kelapa Sawit", "Bangun pabrik pengolahan CPO menjadi biodiesel di Riau & Kalteng."),
        ("Riset Varietas Unggul", "Kembangkan varietas Teh & Kakao tahan penyakit."),
        ("Digitalisasi dengan IoT", "Sistem monitoring real-time dengan sensor & AI."),
        ("Kemitraan Inti-Plasma", "Kerjasama perusahaan besar dengan petani kecil.")
    ]
    for i, (t, c) in enumerate(recs, 1): st.markdown(f'<div class="rec-leaf"><b>#{i} {t}:</b> {c}</div>', unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================
st.markdown('<div class="tropical-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer-tropical">
    <div style="font-size:35px;">🌿🌴🌺</div>
    <h3 style="color:#e9c46a; margin:10px 0; font-family:'Playfair Display', serif;">Tropical Heritage Dashboard</h3>
    <p style="margin:5px 0;">UAS Pengenalan Sains Data 2026</p>
    <p style="margin:5px 0; font-size:13px;">Program Studi Sains Data - UIN K.H. Abdurrahman Wahid Pekalongan</p>
    <p style="margin:10px 0 0 0; color:#f4a261; font-style:italic;">Menjaga Warisan Perkebunan Nusantara</p>
</div>
""", unsafe_allow_html=True)
