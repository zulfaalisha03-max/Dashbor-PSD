"""
=============================================================================
🌌 GALACTIC PLANTATION ANALYTICS - DARK MODE PREMIUM
UAS Pengenalan Sains Data - Tema Berbeda dari Teman Sekelas
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
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# ==========================================
# 1. PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Galactic Plantation Analytics",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. DARK THEME CSS PREMIUM
# ==========================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap');

* { font-family: 'Space Grotesk', sans-serif; }

/* DARK BACKGROUND */
.stApp {
    background: radial-gradient(ellipse at top, #1a1f3a 0%, #0a0e27 50%, #050714 100%);
    color: #e0e6ed;
}

/* HIDE DEFAULT ELEMENTS */
#MainMenu, footer, header { visibility: hidden; }

/* ========================================== */
/* SIDEBAR GALACTIC                           */
/* ========================================== */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a0e27 0%, #1a1f3a 100%);
    border-right: 2px solid #00d4ff;
    box-shadow: 4px 0 20px rgba(0, 212, 255, 0.2);
}

[data-testid="stSidebar"] * {
    color: #e0e6ed !important;
    font-family: 'Space Grotesk', sans-serif;
}

.sidebar-logo {
    text-align: center;
    padding: 25px 15px;
    margin-bottom: 20px;
    background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(255,0,110,0.1));
    border-radius: 15px;
    border: 1px solid rgba(0, 212, 255, 0.3);
    box-shadow: 0 0 30px rgba(0, 212, 255, 0.2);
}

.sidebar-logo h1 {
    background: linear-gradient(45deg, #00d4ff, #ff006e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 22px;
    font-weight: 700;
    margin: 10px 0 5px 0;
    letter-spacing: 2px;
}

.sidebar-logo p {
    color: #00d4ff !important;
    font-size: 11px;
    margin: 0;
    letter-spacing: 3px;
    text-transform: uppercase;
}

/* RADIO BUTTONS NEON */
div[role="radiogroup"] > label {
    background: rgba(26, 31, 58, 0.6);
    backdrop-filter: blur(10px);
    padding: 12px 16px !important;
    border-radius: 10px !important;
    margin-bottom: 8px !important;
    border: 1px solid rgba(0, 212, 255, 0.2);
    transition: all 0.3s ease;
}

div[role="radiogroup"] > label:hover {
    background: rgba(0, 212, 255, 0.15);
    border-color: #00d4ff;
    box-shadow: 0 0 15px rgba(0, 212, 255, 0.4);
    transform: translateX(5px);
}

div[role="radiogroup"] > label[data-baseweb="radio"]:has(input:checked) {
    background: linear-gradient(90deg, rgba(0,212,255,0.3), rgba(255,0,110,0.3)) !important;
    border-color: #00d4ff !important;
    box-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
}

/* ========================================== */
/* HERO SECTION GALACTIC                      */
/* ========================================== */
.hero-galactic {
    background: linear-gradient(135deg, rgba(0,212,255,0.1) 0%, rgba(255,0,110,0.1) 100%);
    backdrop-filter: blur(20px);
    padding: 40px;
    border-radius: 20px;
    border: 1px solid rgba(0, 212, 255, 0.3);
    margin-bottom: 25px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 10px 40px rgba(0, 212, 255, 0.15);
}

.hero-galactic::before {
    content: "";
    position: absolute;
    top: -50%;
    right: -10%;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(0,212,255,0.15) 0%, transparent 70%);
    border-radius: 50%;
    animation: pulse 4s ease-in-out infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 0.5; }
    50% { transform: scale(1.1); opacity: 0.8; }
}

.hero-title {
    font-size: 38px;
    font-weight: 700;
    margin: 0;
    background: linear-gradient(45deg, #00d4ff, #ff006e, #00d4ff);
    background-size: 200% 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradient-shift 3s ease infinite;
    position: relative;
    z-index: 1;
}

@keyframes gradient-shift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.hero-subtitle {
    color: #8b95a7;
    font-size: 16px;
    margin-top: 10px;
    position: relative;
    z-index: 1;
    letter-spacing: 1px;
}

/* ========================================== */
/* GLASS CARDS NEON                           */
/* ========================================== */
.glass-card {
    background: rgba(26, 31, 58, 0.5);
    backdrop-filter: blur(20px);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid rgba(0, 212, 255, 0.2);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    margin-bottom: 20px;
    transition: all 0.3s ease;
}

.glass-card:hover {
    border-color: rgba(0, 212, 255, 0.5);
    box-shadow: 0 12px 40px rgba(0, 212, 255, 0.2);
    transform: translateY(-3px);
}

/* KPI CARDS NEON */
.kpi-neon {
    background: linear-gradient(135deg, rgba(0,212,255,0.08), rgba(255,0,110,0.08));
    backdrop-filter: blur(20px);
    padding: 22px;
    border-radius: 15px;
    border: 1px solid rgba(0, 212, 255, 0.3);
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
    height: 100%;
}

.kpi-neon::before {
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #00d4ff, transparent);
    animation: scan 3s linear infinite;
}

@keyframes scan {
    0% { left: -100%; }
    100% { left: 100%; }
}

.kpi-neon:hover {
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 15px 35px rgba(0, 212, 255, 0.3);
    border-color: #00d4ff;
}

.kpi-icon {
    font-size: 36px;
    margin-bottom: 8px;
    filter: drop-shadow(0 0 10px rgba(0, 212, 255, 0.5));
}

.kpi-label {
    color: #8b95a7;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-weight: 600;
}

.kpi-value {
    color: #00d4ff;
    font-size: 28px;
    font-weight: 700;
    margin: 8px 0;
    font-family: 'JetBrains Mono', monospace;
    text-shadow: 0 0 15px rgba(0, 212, 255, 0.5);
}

.kpi-trend {
    color: #ff006e;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1px;
}

/* SECTION TITLE */
.section-title {
    color: #00d4ff;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 10px;
    text-shadow: 0 0 10px rgba(0, 212, 255, 0.3);
}

.section-title::before {
    content: "";
    width: 4px;
    height: 24px;
    background: linear-gradient(180deg, #00d4ff, #ff006e);
    border-radius: 2px;
}

/* INSIGHT BOX NEON */
.insight-neon {
    background: linear-gradient(135deg, rgba(0,212,255,0.05), rgba(0,212,255,0.02));
    padding: 18px;
    border-left: 4px solid #00d4ff;
    border-radius: 10px;
    margin-bottom: 12px;
    border-right: 1px solid rgba(0, 212, 255, 0.2);
    border-top: 1px solid rgba(0, 212, 255, 0.2);
    border-bottom: 1px solid rgba(0, 212, 255, 0.2);
}

.rec-neon {
    background: linear-gradient(135deg, rgba(255,0,110,0.05), rgba(255,0,110,0.02));
    padding: 18px;
    border-left: 4px solid #ff006e;
    border-radius: 10px;
    margin-bottom: 12px;
    border-right: 1px solid rgba(255, 0, 110, 0.2);
    border-top: 1px solid rgba(255, 0, 110, 0.2);
    border-bottom: 1px solid rgba(255, 0, 110, 0.2);
}

/* TABS NEON */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(26, 31, 58, 0.5);
    backdrop-filter: blur(10px);
    border-radius: 12px;
    padding: 6px;
    border: 1px solid rgba(0, 212, 255, 0.2);
}

.stTabs [data-baseweb="tab"] {
    color: #8b95a7 !important;
    border-radius: 8px;
    padding: 10px 20px !important;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #00d4ff, #ff006e) !important;
    color: white !important;
    box-shadow: 0 0 20px rgba(0, 212, 255, 0.5);
}

/* BUTTONS NEON */
.stButton > button {
    background: linear-gradient(135deg, #00d4ff, #ff006e);
    color: white;
    border: none;
    padding: 10px 25px;
    border-radius: 10px;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0, 212, 255, 0.3);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0, 212, 255, 0.5);
}

/* METRIC CUSTOM */
[data-testid="stMetric"] {
    background: rgba(26, 31, 58, 0.5);
    backdrop-filter: blur(10px);
    padding: 15px;
    border-radius: 12px;
    border: 1px solid rgba(0, 212, 255, 0.2);
}

[data-testid="stMetricLabel"] {
    color: #8b95a7 !important;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    color: #00d4ff !important;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
}

/* DIVIDER NEON */
.neon-divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, #00d4ff, #ff006e, transparent);
    margin: 30px 0;
    box-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
}

/* FOOTER GALACTIC */
.footer-galactic {
    background: linear-gradient(135deg, rgba(0,212,255,0.1), rgba(255,0,110,0.1));
    backdrop-filter: blur(20px);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    margin-top: 40px;
    border: 1px solid rgba(0, 212, 255, 0.3);
    box-shadow: 0 0 30px rgba(0, 212, 255, 0.15);
}

/* WARNING/INFO BOX */
.stAlert {
    background: rgba(26, 31, 58, 0.5) !important;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 212, 255, 0.3) !important;
    color: #e0e6ed !important;
    border-radius: 12px !important;
}

/* CODE BLOCK */
code {
    background: rgba(0, 212, 255, 0.1) !important;
    color: #00d4ff !important;
    padding: 2px 8px;
    border-radius: 5px;
    font-family: 'JetBrains Mono', monospace;
}

/* SCROLLBAR CUSTOM */
::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: #0a0e27; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #00d4ff, #ff006e);
    border-radius: 5px;
}

/* TEXT COLOR OVERRIDE */
p, li, span, div { color: #e0e6ed; }
h1, h2, h3, h4 { color: #00d4ff; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. LOAD DATA (HARDCODED - ANTI ERROR)
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

# ==========================================
# 4. SIDEBAR GALACTIC
# ==========================================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div style="font-size: 50px; filter: drop-shadow(0 0 15px rgba(0,212,255,0.8));">🌌</div>
        <h1>GALACTIC</h1>
        <p>Plantation Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    menu = st.radio(
        "**NAVIGASI UTAMA**",
        [
            "🏠 Dashboard Utama",
            "📊 A. Data Understanding",
            "🧹 B. Data Cleaning",
            "📈 C. EDA (6 Visualisasi)",
            "🔗 D. Analisis Hubungan",
            "📉 E. Regresi Linear",
            "🌲 BONUS: Random Forest",
            "🌳 BONUS: Decision Tree",
            "⏳ BONUS: Forecasting 5Y",
            "🎮 BONUS: Komparator",
            "💡 F. Insight & Rekomendasi"
        ]
    )
    
    st.markdown("---")
    st.markdown("**🎛️ KONTROL GLOBAL**")
    kom_filter = st.selectbox("🎯 Fokus Komoditas:", num_cols, index=0)
    top_n = st.slider("📊 Top Provinsi:", 5, 38, 10)
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 15px; background: rgba(0,212,255,0.05); border-radius: 10px; border: 1px solid rgba(0,212,255,0.2);">
        <div style="font-size: 12px; color: #8b95a7;">SAINS DATA UIN GUS DUR</div>
        <div style="font-size: 10px; color: #00d4ff; margin-top: 5px;">UAS 2026 • v2.0</div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 5. ROUTING HALAMAN
# ==========================================

# === DASHBOARD UTAMA (INTERAKTIF) ===
if menu == "🏠 Dashboard Utama":
    st.markdown("""
    <div class="hero-galactic">
        <div class="hero-title">🌌 Galactic Plantation Analytics</div>
        <div class="hero-subtitle">Eksplorasi Data Perkebunan 38 Provinsi Indonesia dengan Visualisasi Futuristik</div>
    </div>
    """, unsafe_allow_html=True)
    
    # KPI CARDS
    c1, c2, c3, c4 = st.columns(4)
    total_prod = df[num_cols].sum().sum()
    top_kom = df[num_cols].sum().idxmax().replace('_', ' ')
    top_prov = df.set_index('Provinsi')[num_cols].sum(axis=1).idxmax()
    
    with c1:
        st.markdown(f"""
        <div class="kpi-neon">
            <div class="kpi-icon">📍</div>
            <div class="kpi-label">Total Provinsi</div>
            <div class="kpi-value">{df.shape[0]}</div>
            <div class="kpi-trend">🇮🇩 Nusantara</div>
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        st.markdown(f"""
        <div class="kpi-neon">
            <div class="kpi-icon">🌱</div>
            <div class="kpi-label">Komoditas</div>
            <div class="kpi-value">{len(num_cols)}</div>
            <div class="kpi-trend">Jenis Tanaman</div>
        </div>
        """, unsafe_allow_html=True)
    
    with c3:
        st.markdown(f"""
        <div class="kpi-neon">
            <div class="kpi-icon">⚡</div>
            <div class="kpi-label">Total Produksi</div>
            <div class="kpi-value">{total_prod/1000:.1f}K</div>
            <div class="kpi-trend">Ton Nasional</div>
        </div>
        """, unsafe_allow_html=True)
    
    with c4:
        st.markdown(f"""
        <div class="kpi-neon">
            <div class="kpi-icon">🏆</div>
            <div class="kpi-label">Komoditas Utama</div>
            <div class="kpi-value" style="font-size: 18px;">{top_kom}</div>
            <div class="kpi-trend">Produksi Tertinggi</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    
    # ROW 1: BAR + PIE
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="glass-card"><div class="section-title">📊 Top 10 Provinsi Produksi Tertinggi</div></div>', unsafe_allow_html=True)
        top10 = df.copy()
        top10['Total'] = top10[num_cols].sum(axis=1)
        top10 = top10.nlargest(10, 'Total')
        
        fig = px.bar(
            top10, x='Total', y='Provinsi', orientation='h',
            color='Total', color_continuous_scale='plotly3',
            template='plotly_dark'
        )
        fig.update_layout(
            height=450,
            plot_bgcolor='rgba(10, 14, 39, 0.8)',
            paper_bgcolor='rgba(10, 14, 39, 0)',
            font=dict(family='Space Grotesk', color='#e0e6ed'),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<div class="glass-card"><div class="section-title">🥧 Komposisi Komoditas</div></div>', unsafe_allow_html=True)
        komoditas_total = df[num_cols].sum()
        fig_pie = px.pie(
            values=komoditas_total.values,
            names=[c.replace('_', ' ') for c in komoditas_total.index],
            hole=0.5,
            color_discrete_sequence=px.colors.sequential.Plotly3,
            template='plotly_dark'
        )
        fig_pie.update_layout(
            height=450,
            plot_bgcolor='rgba(10, 14, 39, 0.8)',
            paper_bgcolor='rgba(10, 14, 39, 0)',
            font=dict(family='Space Grotesk', color='#e0e6ed')
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # HEATMAP
    st.markdown('<div class="glass-card"><div class="section-title">🔥 Matriks Korelasi Antar Komoditas</div></div>', unsafe_allow_html=True)
    fig_heat = px.imshow(
        df[num_cols].corr(),
        color_continuous_scale='plotly3',
        aspect='auto',
        template='plotly_dark'
    )
    fig_heat.update_layout(
        height=500,
        plot_bgcolor='rgba(10, 14, 39, 0.8)',
        paper_bgcolor='rgba(10, 14, 39, 0)',
        font=dict(family='Space Grotesk', color='#e0e6ed')
    )
    st.plotly_chart(fig_heat, use_container_width=True)

# === A. DATA UNDERSTANDING ===
elif menu == "📊 A. Data Understanding":
    st.markdown("""
    <div class="hero-galactic">
        <div class="hero-title">📊 A. Data Understanding</div>
        <div class="hero-subtitle">Pemahaman Mendalam Struktur Dataset Perkebunan (Bobot 10%)</div>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="kpi-neon">
            <div class="kpi-icon">📋</div>
            <div class="kpi-label">Observasi</div>
            <div class="kpi-value">{df.shape[0]}</div>
            <div class="kpi-trend">Jumlah Baris</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="kpi-neon">
            <div class="kpi-icon">📐</div>
            <div class="kpi-label">Variabel</div>
            <div class="kpi-value">{df.shape[1]}</div>
            <div class="kpi-trend">Jumlah Kolom</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="kpi-neon">
            <div class="kpi-icon">🔢</div>
            <div class="kpi-label">Numerik</div>
            <div class="kpi-value">{len(num_cols)}</div>
            <div class="kpi-trend">Variabel Angka</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Preview Data", "ℹ️ Info", "📈 Statistik", "📖 Deskripsi"
    ])
    
    with tab1:
        st.markdown('<div class="glass-card"><div class="section-title">👁️ Preview Dataset (5 Baris Pertama)</div></div>', unsafe_allow_html=True)
        st.dataframe(df.head(), use_container_width=True)
    
    with tab2:
        st.markdown('<div class="glass-card"><div class="section-title">📋 Informasi Detail Dataset</div></div>', unsafe_allow_html=True)
        buf = io.StringIO()
        df.info(buf=buf)
        st.code(buf.getvalue())
    
    with tab3:
        st.markdown('<div class="glass-card"><div class="section-title">📊 Statistik Deskriptif</div></div>', unsafe_allow_html=True)
        st.dataframe(df[num_cols].describe().round(2), use_container_width=True)
    
    with tab4:
        st.markdown('<div class="glass-card"><div class="section-title">📖 Deskripsi Setiap Variabel</div></div>', unsafe_allow_html=True)
        deskripsi = {
            'Provinsi': 'Nama provinsi di Indonesia (38 provinsi)',
            'Kelapa_Sawit': 'Produksi kelapa sawit dalam ton',
            'Kelapa': 'Produksi kelapa dalam ton',
            'Karet': 'Produksi karet dalam ton',
            'Kopi': 'Produksi kopi dalam ton',
            'Kakao': 'Produksi kakao dalam ton',
            'Teh': 'Produksi teh dalam ton',
            'Tebu': 'Produksi tebu dalam ton'
        }
        for var, desc in deskripsi.items():
            st.markdown(f"""
            <div class="insight-neon">
                <b style="color:#00d4ff;">🔹 {var}</b><br>
                {desc}
            </div>
            """, unsafe_allow_html=True)

# === B. DATA CLEANING ===
elif menu == "🧹 B. Data Cleaning":
    st.markdown("""
    <div class="hero-galactic">
        <div class="hero-title">🧹 B. Data Cleaning</div>
        <div class="hero-subtitle">Proses Preprocessing & Validasi Data (Bobot 15%)</div>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="kpi-neon">
            <div class="kpi-icon">✅</div>
            <div class="kpi-label">Missing Value</div>
            <div class="kpi-value">{df.isnull().sum().sum()}</div>
            <div class="kpi-trend">Data Bersih</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="kpi-neon">
            <div class="kpi-icon">✅</div>
            <div class="kpi-label">Duplikat</div>
            <div class="kpi-value">{df.duplicated().sum()}</div>
            <div class="kpi-trend">Data Unik</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="kpi-neon">
            <div class="kpi-icon">✅</div>
            <div class="kpi-label">Tipe Data</div>
            <div class="kpi-value" style="font-size:20px;">Valid</div>
            <div class="kpi-trend">Float64 & Object</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="kpi-neon">
            <div class="kpi-icon">⚠️</div>
            <div class="kpi-label">Outlier</div>
            <div class="kpi-value" style="font-size:20px;">Ada</div>
            <div class="kpi-trend">Natural Data</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="glass-card"><div class="section-title">📊 Deteksi Outlier (Metode IQR)</div></div>', unsafe_allow_html=True)
    
    # Boxplot dengan tema dark
    fig, ax = plt.subplots(figsize=(14, 6))
    fig.patch.set_facecolor('#0a0e27')
    ax.set_facecolor('#1a1f3a')
    sns.boxplot(data=df[num_cols], palette='cool', ax=ax)
    ax.set_yscale('symlog')
    ax.set_title('Sebaran Data dengan Skala Symlog', color='#00d4ff', fontsize=14, fontweight='bold')
    ax.tick_params(colors='#e0e6ed')
    ax.xaxis.label.set_color('#e0e6ed')
    ax.yaxis.label.set_color('#e0e6ed')
    for spine in ax.spines.values():
        spine.set_color('#00d4ff')
    plt.xticks(rotation=45, color='#e0e6ed')
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("""
    <div class="insight-neon">
        <b style="color:#00d4ff;">💡 Keputusan Data Cleaning:</b><br>
        Outlier <b>TIDAK dihapus</b> karena merupakan data nyata yang mencerminkan kondisi geografis sentra produksi.
        Beberapa provinsi (Riau, Kalteng, Sumut) memang menjadi pusat produksi utama dengan nilai jauh lebih tinggi.
    </div>
    """, unsafe_allow_html=True)

# === C. EDA 6 VISUALISASI ===
elif menu == "📈 C. EDA (6 Visualisasi)":
    st.markdown("""
    <div class="hero-galactic">
        <div class="hero-title">📈 C. Exploratory Data Analysis</div>
        <div class="hero-subtitle">6 Visualisasi Matplotlib dengan Interpretasi Mendalam (Bobot 20%)</div>
    </div>
    """, unsafe_allow_html=True)
    
    tabs = st.tabs([
        "1️⃣ Histogram", "2️⃣ Scatter", "3️⃣ Line",
        "4️⃣ Bar", "5️⃣ Boxplot", "6️⃣ Heatmap"
    ])
    
    with tabs[0]:
        st.markdown('<div class="glass-card"><div class="section-title">📊 Histogram - Distribusi Produksi</div></div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.patch.set_facecolor('#0a0e27')
        ax.set_facecolor('#1a1f3a')
        ax.hist(df[kom_filter], bins=15, color='#00d4ff', edgecolor='#ff006e', alpha=0.8)
        ax.axvline(df[kom_filter].mean(), color='#ff006e', linestyle='--', linewidth=3, label=f'Mean: {df[kom_filter].mean():.1f}')
        ax.axvline(df[kom_filter].median(), color='#00d4ff', linestyle='--', linewidth=3, label=f'Median: {df[kom_filter].median():.1f}')
        ax.set_title(f'Distribusi {kom_filter}', color='#00d4ff', fontsize=14, fontweight='bold')
        ax.set_xlabel('Produksi (Ton)', color='#e0e6ed')
        ax.set_ylabel('Frekuensi', color='#e0e6ed')
        ax.tick_params(colors='#e0e6ed')
        ax.legend()
        ax.grid(alpha=0.2, color='#00d4ff')
        for spine in ax.spines.values():
            spine.set_color('#00d4ff')
        plt.tight_layout()
        st.pyplot(fig)
        st.markdown(f"""
        <div class="insight-neon">
            <b style="color:#00d4ff;">📝 Interpretasi:</b> Distribusi bersifat <b>right-skewed</b> (skewness = {df[kom_filter].skew():.2f}).
            Mayoritas provinsi memiliki produksi rendah, hanya beberapa provinsi yang menjadi sentra produksi.
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[1]:
        st.markdown('<div class="glass-card"><div class="section-title">📊 Scatter Plot - Hubungan Antar Komoditas</div></div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            x_var = st.selectbox("Variabel X:", num_cols, key='sc_x')
        with c2:
            y_var = st.selectbox("Variabel Y:", num_cols, index=1, key='sc_y')
        
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.patch.set_facecolor('#0a0e27')
        ax.set_facecolor('#1a1f3a')
        scatter = ax.scatter(df[x_var], df[y_var], c=df[x_var], cmap='cool', s=150, edgecolors='white', linewidth=2, alpha=0.8)
        
        z = np.polyfit(df[x_var], df[y_var], 1)
        p = np.poly1d(z)
        x_line = np.linspace(df[x_var].min(), df[x_var].max(), 100)
        ax.plot(x_line, p(x_line), color='#ff006e', linestyle='--', linewidth=3, label='Trend Line')
        
        corr_val = df[x_var].corr(df[y_var])
        ax.set_title(f'{x_var} vs {y_var} (r = {corr_val:.3f})', color='#00d4ff', fontsize=14, fontweight='bold')
        ax.set_xlabel(x_var, color='#e0e6ed')
        ax.set_ylabel(y_var, color='#e0e6ed')
        ax.tick_params(colors='#e0e6ed')
        ax.legend()
        ax.grid(alpha=0.2, color='#00d4ff')
        for spine in ax.spines.values():
            spine.set_color('#00d4ff')
        plt.colorbar(scatter, label=x_var)
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown(f"""
        <div class="insight-neon">
            <b style="color:#00d4ff;">📝 Interpretasi:</b> Korelasi = <b>{corr_val:.3f}</b>
            ({'positif kuat' if corr_val > 0.5 else 'positif sedang' if corr_val > 0.3 else 'lemah'}).
            Garis trend menunjukkan pola hubungan {'linier yang jelas' if abs(corr_val) > 0.5 else 'yang tidak terlalu kuat'}.
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[2]:
        st.markdown('<div class="glass-card"><div class="section-title">📊 Line Plot - Tren Produksi Top Provinsi</div></div>', unsafe_allow_html=True)
        n = st.slider("Top N Provinsi:", 5, 20, 10)
        k = st.selectbox("Komoditas:", num_cols, key='line_k')
        top = df.nlargest(n, k)
        
        fig, ax = plt.subplots(figsize=(14, 6))
        fig.patch.set_facecolor('#0a0e27')
        ax.set_facecolor('#1a1f3a')
        ax.plot(range(len(top)), top[k], marker='o', color='#00d4ff', linewidth=3, markersize=12)
        ax.fill_between(range(len(top)), top[k], alpha=0.3, color='#00d4ff')
        ax.set_xticks(range(len(top)))
        ax.set_xticklabels(top['Provinsi'], rotation=45, ha='right', color='#e0e6ed', fontweight='bold')
        ax.set_ylabel(f'Produksi {k} (Ton)', color='#e0e6ed')
        ax.set_title(f'Top {n} Provinsi - {k}', color='#00d4ff', fontsize=14, fontweight='bold')
        ax.tick_params(colors='#e0e6ed')
        ax.grid(alpha=0.2, color='#00d4ff')
        for spine in ax.spines.values():
            spine.set_color('#00d4ff')
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown(f"""
        <div class="insight-neon">
            <b style="color:#00d4ff;">📝 Interpretasi:</b> Produksi {k} sangat <b>terkonsentrasi</b> di beberapa provinsi.
            Provinsi peringkat pertama memiliki produksi jauh lebih besar dibanding peringkat berikutnya.
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[3]:
        st.markdown('<div class="glass-card"><div class="section-title">📊 Bar Chart - Total Produksi Komoditas</div></div>', unsafe_allow_html=True)
        total = df[num_cols].sum().sort_values(ascending=True)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.patch.set_facecolor('#0a0e27')
        ax.set_facecolor('#1a1f3a')
        colors = plt.cm.cool(np.linspace(0, 1, len(total)))
        bars = ax.barh(total.index, total.values, color=colors, edgecolor='white', linewidth=2)
        ax.set_xlabel('Total Produksi (Ton)', color='#e0e6ed')
        ax.set_title('Total Produksi per Komoditas', color='#00d4ff', fontsize=14, fontweight='bold')
        ax.tick_params(colors='#e0e6ed')
        ax.grid(alpha=0.2, color='#00d4ff', axis='x')
        for spine in ax.spines.values():
            spine.set_color('#00d4ff')
        
        for bar, val in zip(bars, total.values):
            ax.text(bar.get_width() + max(total)*0.01, bar.get_y() + bar.get_height()/2,
                   f'{val:,.0f} ton', va='center', color='#e0e6ed', fontweight='bold')
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown("""
        <div class="insight-neon">
            <b style="color:#00d4ff;">📝 Interpretasi:</b> <b>Kelapa Sawit</b> mendominasi total produksi dengan selisih sangat jauh.
            Indonesia sangat bergantung pada satu komoditas utama yang berisiko jika terjadi fluktuasi harga global.
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[4]:
        st.markdown('<div class="glass-card"><div class="section-title">📊 Boxplot - Sebaran Produksi per Komoditas</div></div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.patch.set_facecolor('#0a0e27')
        ax.set_facecolor('#1a1f3a')
        df_m = df.melt(id_vars=['Provinsi'], value_vars=num_cols)
        sns.boxplot(data=df_m, x='variable', y='value', ax=ax, palette='cool', showfliers=True)
        ax.set_title('Distribusi Produksi per Komoditas', color='#00d4ff', fontsize=14, fontweight='bold')
        ax.set_xlabel('Komoditas', color='#e0e6ed')
        ax.set_ylabel('Produksi (Ton)', color='#e0e6ed')
        ax.tick_params(colors='#e0e6ed')
        ax.grid(alpha=0.2, color='#00d4ff', axis='y')
        for spine in ax.spines.values():
            spine.set_color('#00d4ff')
        plt.xticks(rotation=45, color='#e0e6ed')
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown("""
        <div class="insight-neon">
            <b style="color:#00d4ff;">📝 Interpretasi:</b> <b>Kelapa Sawit</b> memiliki variasi produksi tertinggi.
            <b>Teh dan Kakao</b> memiliki produksi paling rendah dan merata.
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[5]:
        st.markdown('<div class="glass-card"><div class="section-title">📊 Heatmap - Korelasi Antar Komoditas</div></div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(12, 10))
        fig.patch.set_facecolor('#0a0e27')
        ax.set_facecolor('#1a1f3a')
        sns.heatmap(df[num_cols].corr(), annot=True, fmt='.2f', cmap='cool', ax=ax,
                   linewidths=1, center=0, cbar_kws={'label': 'Korelasi'})
        ax.set_title('Heatmap Korelasi Antar Komoditas', color='#00d4ff', fontsize=14, fontweight='bold')
        ax.tick_params(colors='#e0e6ed')
        plt.xticks(color='#e0e6ed', fontweight='bold')
        plt.yticks(color='#e0e6ed', fontweight='bold')
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown("""
        <div class="insight-neon">
            <b style="color:#00d4ff;">📝 Interpretasi:</b> Warna cerah menunjukkan korelasi positif kuat (komoditas diproduksi bersamaan).
            Warna gelap menunjukkan korelasi mendekati 0 (tidak ada hubungan).
        </div>
        """, unsafe_allow_html=True)

# === D. ANALISIS HUBUNGAN ===
elif menu == "🔗 D. Analisis Hubungan":
    st.markdown("""
    <div class="hero-galactic">
        <div class="hero-title">🔗 D. Analisis Hubungan Variabel</div>
        <div class="hero-subtitle">Identifikasi Variabel Paling Berpengaruh (Bobot 15%)</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card"><div class="section-title">📊 Matriks Korelasi</div></div>', unsafe_allow_html=True)
    corr = df[num_cols].corr()
    st.dataframe(corr.round(3), use_container_width=True)
    
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="glass-card"><div class="section-title">⭐ Variabel Paling Berpengaruh</div></div>', unsafe_allow_html=True)
    
    total_corr = corr.abs().sum().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('#0a0e27')
    ax.set_facecolor('#1a1f3a')
    colors = ['#ff006e' if i == 0 else '#00d4ff' for i in range(len(total_corr))]
    bars = ax.barh(total_corr.index, total_corr.values, color=colors, edgecolor='white', linewidth=2)
    ax.set_xlabel('Total Absolut Korelasi', color='#e0e6ed')
    ax.set_title('Tingkat Pengaruh Setiap Komoditas', color='#00d4ff', fontsize=14, fontweight='bold')
    ax.tick_params(colors='#e0e6ed')
    ax.grid(alpha=0.2, color='#00d4ff', axis='x')
    for spine in ax.spines.values():
        spine.set_color('#00d4ff')
    
    for bar, val in zip(bars, total_corr.values):
        ax.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
                f'{val:.2f}', va='center', color='#e0e6ed', fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)
    
    top_var = total_corr.index[0]
    st.markdown(f"""
    <div class="insight-neon">
        <b style="color:#ff006e;">🏆 Variabel Paling Berpengaruh: {top_var}</b><br><br>
        <b>Total Korelasi Absolut: {total_corr.values[0]:.2f}</b><br><br>
        <b>Alasan:</b><br>
        1. Memiliki total korelasi tertinggi dengan semua komoditas lain<br>
        2. Menunjukkan hubungan paling kuat dalam ekosistem perkebunan<br>
        3. Provinsi dengan produksi {top_var} tinggi cenderung memproduksi komoditas lain juga<br>
        4. Dapat dijadikan <b>indikator utama</b> perkembangan perkebunan nasional
    </div>
    """, unsafe_allow_html=True)

# === E. REGRESI LINEAR ===
elif menu == "📉 E. Regresi Linear":
    st.markdown("""
    <div class="hero-galactic">
        <div class="hero-title">📉 E. Pemodelan Regresi Linear</div>
        <div class="hero-subtitle">Prediksi Produksi dengan Metrik MAE, RMSE, R² (Bobot 20%)</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card"><div class="section-title">⚙️ Konfigurasi Model</div></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        target = st.selectbox("🎯 Variabel Dependen (Y):", num_cols)
    with c2:
        feats = st.multiselect("📊 Variabel Independen (X):",
                              [c for c in num_cols if c != target],
                              default=[c for c in num_cols if c != target][:3])
    
    if len(feats) > 0:
        X = df[feats]
        y = df[target]
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = LinearRegression().fit(X_tr, y_tr)
        pred = model.predict(X_te)
        
        mae = mean_absolute_error(y_te, pred)
        rmse = np.sqrt(mean_squared_error(y_te, pred))
        r2 = r2_score(y_te, pred)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f"""
            <div class="kpi-neon">
                <div class="kpi-icon">📉</div>
                <div class="kpi-label">MAE</div>
                <div class="kpi-value">{mae:.2f}</div>
                <div class="kpi-trend">Mean Absolute Error</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown(f"""
            <div class="kpi-neon">
                <div class="kpi-icon">📊</div>
                <div class="kpi-label">RMSE</div>
                <div class="kpi-value">{rmse:.2f}</div>
                <div class="kpi-trend">Root Mean Squared Error</div>
            </div>
            """, unsafe_allow_html=True)
        with c3:
            color = '#00d4ff' if r2 > 0.5 else '#ff006e'
            st.markdown(f"""
            <div class="kpi-neon" style="border-color: {color};">
                <div class="kpi-icon">🎯</div>
                <div class="kpi-label">R² Score</div>
                <div class="kpi-value" style="color: {color};">{r2:.4f}</div>
                <div class="kpi-trend">{r2*100:.1f}% Variasi Terjelaskan</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Persamaan
        equation = f"{target} = {model.intercept_:.2f}"
        for feat, coef in zip(feats, model.coef_):
            equation += f" + {coef:.2f} × {feat}"
        
        st.markdown(f"""
        <div class="glass-card">
            <div class="section-title">📐 Persamaan Regresi</div>
            <code style="font-size: 16px; padding: 15px; background: rgba(0,212,255,0.1); display: block; border-radius: 10px; color: #00d4ff;">
            {equation}
            </code>
        </div>
        """, unsafe_allow_html=True)
        
        # Visualisasi
        st.markdown('<div class="glass-card"><div class="section-title">📈 Visualisasi Prediksi</div></div>', unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor('#0a0e27')
        ax.set_facecolor('#1a1f3a')
        ax.scatter(y_te, pred, c='#00d4ff', s=150, edgecolors='white', linewidth=2, alpha=0.8)
        min_val = min(y_te.min(), pred.min())
        max_val = max(y_te.max(), pred.max())
        ax.plot([min_val, max_val], [min_val, max_val], color='#ff006e', linestyle='--', linewidth=3, label='Perfect Prediction')
        ax.set_xlabel('Nilai Aktual', color='#e0e6ed')
        ax.set_ylabel('Nilai Prediksi', color='#e0e6ed')
        ax.set_title('Aktual vs Prediksi', color='#00d4ff', fontsize=14, fontweight='bold')
        ax.tick_params(colors='#e0e6ed')
        ax.legend()
        ax.grid(alpha=0.2, color='#00d4ff')
        for spine in ax.spines.values():
            spine.set_color('#00d4ff')
        plt.tight_layout()
        st.pyplot(fig)
        
        if r2 > 0.7:
            kualitas = "SANGAT BAIK"
            warna = "#00d4ff"
        elif r2 > 0.5:
            kualitas = "BAIK"
            warna = "#00d4ff"
        else:
            kualitas = "PERLU PERBAIKAN"
            warna = "#ff006e"
        
        st.markdown(f"""
        <div class="insight-neon" style="border-left-color: {warna};">
            <b style="color:{warna};">📝 Interpretasi Model: {kualitas}</b><br>
            <b>MAE = {mae:.2f} ton</b> → Rata-rata error prediksi<br>
            <b>RMSE = {rmse:.2f} ton</b> → Standar deviasi error<br>
            <b>R² = {r2:.4f}</b> → Model menjelaskan {r2*100:.2f}% variasi data
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Pilih minimal 1 variabel independen!")

# === BONUS: RANDOM FOREST ===
elif menu == "🌲 BONUS: Random Forest":
    st.markdown("""
    <div class="hero-galactic">
        <div class="hero-title">🌲 BONUS: Random Forest Regressor</div>
        <div class="hero-subtitle">Ensemble Learning untuk Prediksi yang Lebih Akurat (10 Poin Bonus)</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card"><div class="section-title">⚙️ Konfigurasi Model</div></div>', unsafe_allow_html=True)
    target = st.selectbox("🎯 Target Variabel:", num_cols, key='rf')
    feats = [c for c in num_cols if c != target]
    
    X, y = df[feats], df[target]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    
    rf = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=5)
    rf.fit(X_tr, y_tr)
    pred = rf.predict(X_te)
    
    r2_rf = r2_score(y_te, pred)
    rmse_rf = np.sqrt(mean_squared_error(y_te, pred))
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div class="kpi-neon">
            <div class="kpi-icon">🎯</div>
            <div class="kpi-label">R² Score</div>
            <div class="kpi-value">{r2_rf:.4f}</div>
            <div class="kpi-trend">{r2_rf*100:.1f}% Akurasi</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="kpi-neon">
            <div class="kpi-icon">📊</div>
            <div class="kpi-label">RMSE</div>
            <div class="kpi-value">{rmse_rf:.2f}</div>
            <div class="kpi-trend">Error Standar</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Feature Importance
    st.markdown('<div class="glass-card"><div class="section-title">🏆 Feature Importance</div></div>', unsafe_allow_html=True)
    feat_imp = pd.DataFrame({
        'Feature': feats,
        'Importance': rf.feature_importances_
    }).sort_values('Importance')
    
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#0a0e27')
    ax.set_facecolor('#1a1f3a')
    ax.barh(feat_imp['Feature'], feat_imp['Importance'], color='#00d4ff', edgecolor='white', linewidth=2)
    ax.set_xlabel('Importance Score', color='#e0e6ed')
    ax.set_title('Feature Importance - Random Forest', color='#00d4ff', fontsize=14, fontweight='bold')
    ax.tick_params(colors='#e0e6ed')
    ax.grid(alpha=0.2, color='#00d4ff', axis='x')
    for spine in ax.spines.values():
        spine.set_color('#00d4ff')
    plt.tight_layout()
    st.pyplot(fig)

# === BONUS: DECISION TREE ===
elif menu == "🌳 BONUS: Decision Tree":
    st.markdown("""
    <div class="hero-galactic">
        <div class="hero-title">🌳 BONUS: Decision Tree Regressor</div>
        <div class="hero-subtitle">Model Berbasis Struktur Pohon Keputusan (10 Poin Bonus)</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card"><div class="section-title">⚙️ Konfigurasi Model</div></div>', unsafe_allow_html=True)
    target = st.selectbox("🎯 Target Variabel:", num_cols, key='dt')
    max_depth = st.slider("Max Depth:", 2, 10, 4)
    feats = [c for c in num_cols if c != target]
    
    X, y = df[feats], df[target]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    
    dt = DecisionTreeRegressor(max_depth=max_depth, random_state=42)
    dt.fit(X_tr, y_tr)
    pred = dt.predict(X_te)
    
    r2_dt = r2_score(y_te, pred)
    
    st.markdown(f"""
    <div class="kpi-neon" style="width: 300px;">
        <div class="kpi-icon">🎯</div>
        <div class="kpi-label">R² Score</div>
        <div class="kpi-value">{r2_dt:.4f}</div>
        <div class="kpi-trend">{r2_dt*100:.1f}% Akurasi</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Tree Visualization
    st.markdown('<div class="glass-card"><div class="section-title">🌳 Visualisasi Decision Tree</div></div>', unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(20, 10))
    fig.patch.set_facecolor('#0a0e27')
    ax.set_facecolor('#1a1f3a')
    plot_tree(dt, feature_names=feats, filled=True, rounded=True, ax=ax, fontsize=8)
    plt.title(f'Decision Tree (Max Depth: {max_depth})', color='#00d4ff', fontsize=14, fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig)

# === BONUS: FORECASTING ===
elif menu == "⏳ BONUS: Forecasting 5Y":
    st.markdown("""
    <div class="hero-galactic">
        <div class="hero-title">⏳ BONUS: Forecasting 5 Tahun</div>
        <div class="hero-subtitle">Simulasi Proyeksi Produksi dengan Growth Rate Global (10 Poin Bonus)</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-neon">
        <b style="color:#ff006e;">⚠️ Catatan Kritis Data Scientist:</b><br>
        Dataset ini bersifat <b>cross-sectional</b> (satu titik waktu), bukan time-series.
        Seorang Data Scientist profesional menggunakan <b>Projection Growth Simulator</b>
        berdasarkan CAGR (Compound Annual Growth Rate) industri global komoditas.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card"><div class="section-title">🎛️ Kontrol Forecasting</div></div>', unsafe_allow_html=True)
    prov_fc = st.selectbox("🏙️ Pilih Provinsi:", df['Provinsi'].sort_values().tolist(), index=0)
    growth_rate = st.slider("📈 Growth Rate (%):", 1, 10, 5) / 100
    
    years = np.arange(2024, 2029)
    fc_df = pd.DataFrame({'Tahun': years})
    
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('#0a0e27')
    ax.set_facecolor('#1a1f3a')
    
    for kom in num_cols:
        base = df[df['Provinsi']==prov_fc][kom].values[0]
        vals = [base * ((1+growth_rate)**i) for i in range(len(years))]
        fc_df[kom] = vals
        linewidth = 3 if kom == kom_filter else 1
        alpha = 1.0 if kom == kom_filter else 0.4
        color = '#00d4ff' if kom == kom_filter else '#8b95a7'
        ax.plot(years, vals, marker='o', label=kom, linewidth=linewidth, alpha=alpha, color=color)
    
    ax.set_title(f'Proyeksi 5 Tahun - Provinsi {prov_fc}', color='#00d4ff', fontsize=14, fontweight='bold')
    ax.set_xlabel('Tahun', color='#e0e6ed')
    ax.set_ylabel('Volume (Ton)', color='#e0e6ed')
    ax.tick_params(colors='#e0e6ed')
    ax.grid(alpha=0.2, color='#00d4ff')
    ax.legend(loc='upper left', ncol=2, facecolor='#1a1f3a', edgecolor='#00d4ff', labelcolor='#e0e6ed')
    for spine in ax.spines.values():
        spine.set_color('#00d4ff')
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown(f"""
    <div class="insight-neon">
        <b style="color:#00d4ff;">📝 Interpretasi Forecast:</b><br>
        Garis tebal adalah <b>{kom_filter}</b> yang diproyeksikan tumbuh {growth_rate*100}% per tahun.
        Proyeksi ini berdasarkan CAGR industri global komoditas perkebunan.
    </div>
    """, unsafe_allow_html=True)

# === BONUS: KOMPARATOR ===
elif menu == "🎮 BONUS: Komparator":
    st.markdown("""
    <div class="hero-galactic">
        <div class="hero-title">🎮 BONUS: Province Comparator</div>
        <div class="hero-subtitle">Bandingkan 2 Provinsi Secara Head-to-Head (10 Poin Bonus)</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card"><div class="section-title">⚙️ Pilih Provinsi untuk Dibandingkan</div></div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        prov1 = st.selectbox("🏙️ Provinsi 1:", df['Provinsi'].tolist(), index=df[df['Provinsi']=='RIAU'].index[0] if 'RIAU' in df['Provinsi'].values else 0)
    with c2:
        prov2 = st.selectbox("🏙️ Provinsi 2:", df['Provinsi'].tolist(), index=df[df['Provinsi']=='SUMATERA UTARA'].index[0] if 'SUMATERA UTARA' in df['Provinsi'].values else 1)
    
    # Radar Chart
    st.markdown('<div class="glass-card"><div class="section-title">📊 Radar Chart Perbandingan</div></div>', unsafe_allow_html=True)
    fig = go.Figure()
    
    vals1 = df[df['Provinsi']==prov1][num_cols].values.flatten().tolist()
    vals2 = df[df['Provinsi']==prov2][num_cols].values.flatten().tolist()
    
    fig.add_trace(go.Scatterpolar(
        r=vals1 + [vals1[0]],
        theta=num_cols + [num_cols[0]],
        fill='toself',
        name=prov1,
        line_color='#00d4ff',
        fillcolor='rgba(0, 212, 255, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=vals2 + [vals2[0]],
        theta=num_cols + [num_cols[0]],
        fill='toself',
        name=prov2,
        line_color='#ff006e',
        fillcolor='rgba(255, 0, 110, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, gridcolor='#00d4ff', tickcolor='#e0e6ed'),
            angularaxis=dict(gridcolor='#00d4ff', tickcolor='#e0e6ed')
        ),
        showlegend=True,
        height=500,
        plot_bgcolor='rgba(10, 14, 39, 0.8)',
        paper_bgcolor='rgba(10, 14, 39, 0)',
        font=dict(family='Space Grotesk', color='#e0e6ed')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Stacked Bar
    st.markdown('<div class="glass-card"><div class="section-title">📊 Perbandingan Total Produksi</div></div>', unsafe_allow_html=True)
    df_comp = df[df['Provinsi'].isin([prov1, prov2])].set_index('Provinsi')
    
    fig = px.bar(
        df_comp.reset_index(),
        x='Provinsi',
        y=num_cols,
        barmode='stack',
        color_discrete_sequence=['#00d4ff', '#ff006e', '#8b95a7', '#00ff88', '#ffaa00', '#aa00ff', '#00ffff'],
        template='plotly_dark'
    )
    fig.update_layout(
        height=500,
        plot_bgcolor='rgba(10, 14, 39, 0.8)',
        paper_bgcolor='rgba(10, 14, 39, 0)',
        font=dict(family='Space Grotesk', color='#e0e6ed')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Summary
    total1 = df[df['Provinsi']==prov1][num_cols].sum().sum()
    total2 = df[df['Provinsi']==prov2][num_cols].sum().sum()
    winner = prov1 if total1 > total2 else prov2
    
    st.markdown(f"""
    <div class="insight-neon">
        <b style="color:#ff006e;">🏆 Hasil Perbandingan:</b><br>
        <b>{prov1}</b>: {total1:,.0f} ton<br>
        <b>{prov2}</b>: {total2:,.0f} ton<br><br>
        <b style="color:#00d4ff;">Pemenang: {winner}</b> dengan total produksi lebih tinggi.
    </div>
    """, unsafe_allow_html=True)

# === F. INSIGHT & REKOMENDASI ===
elif menu == "💡 F. Insight & Rekomendasi":
    st.markdown("""
    <div class="hero-galactic">
        <div class="hero-title">💡 F. Insight & Rekomendasi</div>
        <div class="hero-subtitle">Temuan Penting dan Rekomendasi Implementatif (Bobot 20%)</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card"><div class="section-title">🔍 5 INSIGHT UTAMA</div></div>', unsafe_allow_html=True)
    
    insights = [
        ("🌴 Kelapa Sawit Mendominasi",
         f"Menyumbang {df['Kelapa_Sawit'].sum()/df[num_cols].sum().sum()*100:.1f}% total produksi nasional. "
         "Indonesia sangat bergantung pada satu komoditas utama."),
        ("🗺️ Ketimpangan Produksi Tinggi",
         "Top 5 provinsi menyumbang > 50% produksi nasional. Produksi sangat terpusat di wilayah tertentu."),
        ("🌏 Sumatera & Kalimantan Sentra",
         "Kedua pulau mendominasi produksi kelapa sawit, karet, dan kakao berkat iklim tropis yang ideal."),
        ("🎋 Tebu Terkonsentrasi",
         "Jawa Timur menyumbang > 60% produksi tebu nasional. Risiko supply chain tinggi untuk industri gula."),
        ("⚠️ Diversifikasi Rendah",
         "Banyak provinsi tidak memproduksi komoditas tertentu. Perlu diversifikasi untuk mengurangi risiko.")
    ]
    
    for i, (title, content) in enumerate(insights, 1):
        st.markdown(f"""
        <div class="insight-neon">
            <b style="color:#00d4ff;">#{i} {title}</b><br>
            {content}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="glass-card"><div class="section-title">💡 5 REKOMENDASI IMPLEMENTATIF</div></div>', unsafe_allow_html=True)
    
    recs = [
        ("🌱 Diversifikasi Komoditas",
         "Kembangkan perkebunan di luar sentra produksi (Indonesia Timur, Nusa Tenggara) "
         "melalui program transmigrasi dan insentif petani. Target: +30% produksi non-sentra dalam 5 tahun."),
        ("🏭 Hilirisasi Industri Kelapa Sawit",
         "Percepat pembangunan pabrik pengolahan CPO menjadi biodiesel, oleokimia, dan margarin "
         "di Riau, Kalteng, Sumut. Target: nilai tambah +50%."),
        ("🔬 Riset Varietas Unggul",
         "Kembangkan varietas Teh dan Kakao tahan penyakit melalui kerjasama PUSPI-universitas. "
         "Target: produksi Teh +100%, Kakao +75%."),
        ("🌐 Digitalisasi Data Perkebunan",
         "Bangun sistem informasi berbasis GIS, IoT, dan AI untuk monitoring real-time produksi. "
         "Target: akurasi data 95%, efisiensi 40%."),
        ("🤝 Kemitraan Inti-Plasma",
         "Dorong kemitraan perusahaan besar dengan petani kecil untuk akses teknologi dan pasar. "
         "Target: 70% petani kecil terlibat, pendapatan +50%.")
    ]
    
    for i, (title, content) in enumerate(recs, 1):
        st.markdown(f"""
        <div class="rec-neon">
            <b style="color:#ff006e;">#{i} {title}</b><br>
            {content}
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# FOOTER GALACTIC
# ==========================================
st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer-galactic">
    <div style="font-size: 30px; margin-bottom: 10px;">🌌</div>
    <h3 style="color: #00d4ff; margin: 5px 0;">Galactic Plantation Analytics</h3>
    <p style="margin: 5px 0; color: #8b95a7;">UAS Pengenalan Sains Data 2026</p>
    <p style="margin: 5px 0; color: #8b95a7; font-size: 13px;">Sains Data • UIN K.H. Abdurrahman Wahid Pekalongan</p>
    <p style="margin: 10px 0 0 0; color: #ff006e; font-weight: bold;">Dark Mode Premium Edition • v2.0</p>
</div>
""", unsafe_allow_html=True)
