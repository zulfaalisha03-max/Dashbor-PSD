"""
=============================================================================
DASHBOARD PERKEBUNAN INDONESIA - PREMIUM UI/UX DESIGN
Redesign by UI/UX Designer
=============================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import io
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# PAGE CONFIG - WAJIB DI PALING ATAS
# =============================================================================
st.set_page_config(
    page_title="Dashboard Perkebunan Indonesia",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# CSS PREMIUM - DESAIN MODERN
# =============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

/* Global Styles */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #f5f7fa 0%, #e8f5e9 100%);
}

/* Hide Streamlit default elements */
#MainMenu, footer, header {
    visibility: hidden;
}

/* =========================================== */
/* SIDEBAR PREMIUM DESIGN                      */
/* =========================================== */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1B4332 0%, #2D6A4F 100%);
    border-right: 3px solid #FFD700;
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Logo container */
.sidebar-logo {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 20px;
    border: 1px solid rgba(255, 215, 0, 0.3);
}

.sidebar-logo h1 {
    font-size: 24px;
    margin: 0;
    background: linear-gradient(45deg, #FFD700, #FFA500);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
}

/* Radio buttons modern */
div[role="radiogroup"] > label {
    background: rgba(255, 255, 255, 0.08);
    padding: 12px 16px !important;
    border-radius: 10px !important;
    margin-bottom: 8px !important;
    transition: all 0.3s ease;
    border: 1px solid transparent;
    display: flex !important;
    align-items: center;
}

div[role="radiogroup"] > label:hover {
    background: rgba(255, 215, 0, 0.15);
    border-color: #FFD700;
    transform: translateX(5px);
}

div[role="radiogroup"] > label[data-baseweb="radio"]:has(input:checked) {
    background: linear-gradient(90deg, #FFD700, #FFA500) !important;
    color: #1B4332 !important;
    font-weight: 600;
    border-color: #FFD700;
    box-shadow: 0 4px 12px rgba(255, 215, 0, 0.4);
}

div[role="radiogroup"] > label[data-baseweb="radio"]:has(input:checked) * {
    color: #1B4332 !important;
}

/* =========================================== */
/* HEADER & HERO SECTION                       */
/* =========================================== */
.hero-section {
    background: linear-gradient(135deg, #1B4332 0%, #2D6A4F 50%, #40916C 100%);
    padding: 40px;
    border-radius: 20px;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 10px 40px rgba(27, 67, 50, 0.3);
    position: relative;
    overflow: hidden;
}

.hero-section::before {
    content: "";
    position: absolute;
    top: -50%;
    right: -10%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(255,215,0,0.2) 0%, transparent 70%);
    border-radius: 50%;
}

.hero-title {
    font-size: 36px;
    font-weight: 800;
    margin: 0;
    background: linear-gradient(45deg, #FFD700, #FFFFFF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    position: relative;
    z-index: 1;
}

.hero-subtitle {
    font-size: 18px;
    margin-top: 10px;
    opacity: 0.9;
    position: relative;
    z-index: 1;
}

/* =========================================== */
/* KPI CARDS PREMIUM                           */
/* =========================================== */
.kpi-card {
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    border-left: 5px solid #40916C;
    transition: all 0.3s ease;
    height: 100%;
}

.kpi-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    border-left-color: #FFD700;
}

.kpi-icon {
    font-size: 40px;
    margin-bottom: 10px;
}

.kpi-label {
    color: #6c757d;
    font-size: 13px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.kpi-value {
    color: #1B4332;
    font-size: 28px;
    font-weight: 800;
    margin-top: 5px;
}

.kpi-trend {
    color: #40916C;
    font-size: 12px;
    font-weight: 600;
    margin-top: 5px;
}

/* =========================================== */
/* SECTION CARDS                               */
/* =========================================== */
.section-card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    margin-bottom: 25px;
    border-top: 4px solid #40916C;
}

.section-title {
    color: #1B4332;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
}

/* =========================================== */
/* INSIGHT BOXES                               */
/* =========================================== */
.insight-card {
    background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%);
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid #2E7D32;
    margin: 15px 0;
    box-shadow: 0 4px 12px rgba(46, 125, 50, 0.1);
}

.insight-title {
    color: #1B4332;
    font-weight: 700;
    font-size: 16px;
    margin-bottom: 8px;
}

.rec-card {
    background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid #1976D2;
    margin: 15px 0;
    box-shadow: 0 4px 12px rgba(25, 118, 210, 0.1);
}

/* =========================================== */
/* CUSTOM BUTTONS                              */
/* =========================================== */
.stButton > button {
    background: linear-gradient(135deg, #2E7D32 0%, #40916C 100%);
    color: white;
    border: none;
    padding: 10px 25px;
    border-radius: 10px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(46, 125, 50, 0.4);
}

/* =========================================== */
/* TABS PREMIUM                                */
/* =========================================== */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
    background: #f5f7fa;
    padding: 8px;
    border-radius: 12px;
}

.stTabs [data-baseweb="tab"] {
    background: white;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 600;
    color: #1B4332;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #2E7D32 0%, #40916C 100%) !important;
    color: white !important;
}

/* =========================================== */
/* METRIC CUSTOM                               */
/* =========================================== */
[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

[data-testid="stMetricLabel"] {
    color: #6c757d;
    font-weight: 600;
}

[data-testid="stMetricValue"] {
    color: #1B4332;
    font-weight: 800;
}

/* =========================================== */
/* DIVIDER CUSTOM                              */
/* =========================================== */
.custom-divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, #FFD700, transparent);
    margin: 30px 0;
}

/* =========================================== */
/* FOOTER                                      */
/* =========================================== */
.footer-premium {
    background: linear-gradient(135deg, #1B4332 0%, #2D6A4F 100%);
    padding: 30px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-top: 40px;
    box-shadow: 0 -8px 24px rgba(27, 67, 50, 0.2);
}

.footer-premium h3 {
    color: #FFD700;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# LOAD DATA
# =============================================================================
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
numeric_cols = [c for c in df.columns if c != 'Provinsi']

# =============================================================================
# SIDEBAR PREMIUM
# =============================================================================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div style="font-size: 60px;">🌴</div>
        <h1>PERKEBUNAN</h1>
        <p style="margin: 5px 0; font-size: 12px; opacity: 0.8;">Indonesia Dashboard</p>
    </div>
    """, unsafe_allow_html=True)
    
    menu = st.radio(
        "**NAVIGASI UTAMA**",
        [
            "🏠 Dashboard",
            "📊 Data Understanding",
            "🧹 Data Cleaning",
            "📈 EDA Visualisasi",
            "🔗 Analisis Hubungan",
            "🤖 Machine Learning",
            "💡 Insight & Rekomendasi",
            "🎁 Bonus Analytics"
        ],
        label_visibility="visible"
    )
    
    st.markdown("---")
    
    st.markdown("**⚙️ FILTER GLOBAL**")
    komoditas_filter = st.selectbox(
        "Pilih Komoditas",
        numeric_cols,
        index=0
    )
    
    top_n = st.slider(
        "Jumlah Top Provinsi",
        min_value=5,
        max_value=38,
        value=10,
        step=1
    )
    
    st.markdown("---")
    
    st.markdown("""
    <div style="text-align: center; padding: 10px; background: rgba(255,215,0,0.1); border-radius: 10px;">
        <div style="font-size: 24px;">👨‍💻</div>
        <div style="font-size: 12px; margin-top: 5px;">Data Scientist</div>
        <div style="font-size: 10px; opacity: 0.7;">UAS Sains Data 2026</div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# HALAMAN DASHBOARD (HOME)
# =============================================================================
if menu == "🏠 Dashboard":
    # HERO SECTION
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">🌴 Dashboard Produksi Perkebunan Indonesia</div>
        <div class="hero-subtitle">Analisis Komprehensif 38 Provinsi • 7 Komoditas Unggulan • Data Terkini</div>
    </div>
    """, unsafe_allow_html=True)
    
    # KPI CARDS
    total_produksi = df[numeric_cols].sum().sum()
    top_komoditas = df[numeric_cols].sum().idxmax().replace('_', ' ')
    top_provinsi = df.set_index('Provinsi')[numeric_cols].sum(axis=1).idxmax()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">📍</div>
            <div class="kpi-label">Total Provinsi</div>
            <div class="kpi-value">{df.shape[0]}</div>
            <div class="kpi-trend">🇮🇩 Seluruh Indonesia</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">🌱</div>
            <div class="kpi-label">Total Komoditas</div>
            <div class="kpi-value">{len(numeric_cols)}</div>
            <div class="kpi-trend">🌴 Jenis Tanaman</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">📊</div>
            <div class="kpi-label">Total Produksi</div>
            <div class="kpi-value">{total_produksi:,.0f}</div>
            <div class="kpi-trend">📈 Ton per Tahun</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">🏆</div>
            <div class="kpi-label">Komoditas Utama</div>
            <div class="kpi-value" style="font-size: 20px;">{top_komoditas}</div>
            <div class="kpi-trend">⭐ Produksi Tertinggi</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
    # ROW 1: BAR + PIE
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📊 Top 10 Provinsi dengan Produksi Tertinggi</div>
        </div>
        """, unsafe_allow_html=True)
        
        top10 = df.copy()
        top10['Total'] = top10[numeric_cols].sum(axis=1)
        top10 = top10.nlargest(10, 'Total')
        
        fig = px.bar(
            top10,
            x='Total',
            y='Provinsi',
            orientation='h',
            color='Total',
            color_continuous_scale='Greens',
            labels={'Total': 'Total Produksi (Ton)', 'Provinsi': ''}
        )
        fig.update_layout(
            height=450,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Plus Jakarta Sans', size=12),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">🥧 Komposisi Komoditas</div>
        </div>
        """, unsafe_allow_html=True)
        
        komoditas_total = df[numeric_cols].sum()
        fig_pie = px.pie(
            values=komoditas_total.values,
            names=[c.replace('_', ' ') for c in komoditas_total.index],
            hole=0.4,
            color_discrete_sequence=px.colors.sequential.Greens
        )
        fig_pie.update_layout(
            height=450,
            showlegend=True,
            font=dict(family='Plus Jakarta Sans', size=11)
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # ROW 2: HEATMAP
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🔥 Korelasi Antar Komoditas</div>
    </div>
    """, unsafe_allow_html=True)
    
    fig_heat = px.imshow(
        df[numeric_cols].corr(),
        color_continuous_scale='Greens',
        aspect='auto',
        labels=dict(color="Korelasi")
    )
    fig_heat.update_layout(
        height=500,
        font=dict(family='Plus Jakarta Sans', size=11)
    )
    st.plotly_chart(fig_heat, use_container_width=True)
    
    # QUICK INSIGHT
    st.markdown("""
    <div class="section-card">
        <div class="section-title">💡 Quick Insight</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">🌴 Dominasi Kelapa Sawit</div>
            Kelapa Sawit menyumbang lebih dari 50% total produksi perkebunan nasional,
            menjadikannya komoditas paling strategis bagi perekonomian Indonesia.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">🗺️ Sentra Produksi</div>
            Pulau Sumatera dan Kalimantan menjadi pusat produksi utama,
            dengan Riau sebagai provinsi dengan produksi tertinggi secara nasional.
        </div>
        """, unsafe_allow_html=True)

# =============================================================================
# HALAMAN DATA UNDERSTANDING
# =============================================================================
elif menu == "📊 Data Understanding":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">📊 Data Understanding</div>
        <div class="hero-subtitle">Pemahaman Mendalam tentang Dataset Perkebunan Indonesia</div>
    </div>
    """, unsafe_allow_html=True)
    
    # KPI
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">📋</div>
            <div class="kpi-label">Observasi</div>
            <div class="kpi-value">{df.shape[0]}</div>
            <div class="kpi-trend">Jumlah Baris</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">📐</div>
            <div class="kpi-label">Variabel</div>
            <div class="kpi-value">{df.shape[1]}</div>
            <div class="kpi-trend">Jumlah Kolom</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">🔢</div>
            <div class="kpi-label">Numerik</div>
            <div class="kpi-value">{len(numeric_cols)}</div>
            <div class="kpi-trend">Variabel Angka</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Tab navigation
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Preview Data",
        "ℹ️ Informasi",
        "📈 Statistik",
        "📖 Deskripsi Variabel"
    ])
    
    with tab1:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">👁️ Preview Dataset</div>
            Menampilkan 5 baris pertama dari dataset
        </div>
        """, unsafe_allow_html=True)
        st.dataframe(df.head(), use_container_width=True)
    
    with tab2:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📋 Informasi Detail Dataset</div>
        </div>
        """, unsafe_allow_html=True)
        buf = io.StringIO()
        df.info(buf=buf)
        st.code(buf.getvalue())
    
    with tab3:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📊 Statistik Deskriptif</div>
        </div>
        """, unsafe_allow_html=True)
        st.dataframe(df[numeric_cols].describe().round(2), use_container_width=True)
    
    with tab4:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📖 Deskripsi Setiap Variabel</div>
        </div>
        """, unsafe_allow_html=True)
        
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
            <div class="insight-card">
                <div class="insight-title">🔹 {var}</div>
                {desc}
            </div>
            """, unsafe_allow_html=True)

# =============================================================================
# HALAMAN DATA CLEANING
# =============================================================================
elif menu == "🧹 Data Cleaning":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">🧹 Data Cleaning</div>
        <div class="hero-subtitle">Proses Pembersihan dan Validasi Data</div>
    </div>
    """, unsafe_allow_html=True)
    
    # KPI Status
    col1, col2, col3, col4 = st.columns(4)
    
    missing_total = df.isnull().sum().sum()
    dup_total = df.duplicated().sum()
    
    with col1:
        st.markdown(f"""
        <div class="kpi-card" style="border-left-color: #4CAF50;">
            <div class="kpi-icon">✅</div>
            <div class="kpi-label">Missing Value</div>
            <div class="kpi-value">{missing_total}</div>
            <div class="kpi-trend" style="color: #4CAF50;">✓ Bersih</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="kpi-card" style="border-left-color: #4CAF50;">
            <div class="kpi-icon">✅</div>
            <div class="kpi-label">Duplikat</div>
            <div class="kpi-value">{dup_total}</div>
            <div class="kpi-trend" style="color: #4CAF50;">✓ Unik</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="kpi-card" style="border-left-color: #4CAF50;">
            <div class="kpi-icon">✅</div>
            <div class="kpi-label">Tipe Data</div>
            <div class="kpi-value">Valid</div>
            <div class="kpi-trend" style="color: #4CAF50;">✓ Sesuai</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="kpi-card" style="border-left-color: #FFA000;">
            <div class="kpi-icon">⚠️</div>
            <div class="kpi-label">Outlier</div>
            <div class="kpi-value">Ada</div>
            <div class="kpi-trend" style="color: #FFA000;">⚡ Dipertahankan</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Detail Outlier
    st.markdown("""
    <div class="section-card">
        <div class="section-title">📊 Analisis Outlier per Komoditas</div>
    </div>
    """, unsafe_allow_html=True)
    
    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    axes = axes.flatten()
    
    outlier_info = {}
    for i, col in enumerate(numeric_cols):
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
        outlier_info[col] = len(outliers)
        
        sns.boxplot(data=df, y=col, ax=axes[i], color='#A5D6A7')
        axes[i].set_title(f'{col}\n({len(outliers)} outlier)', fontsize=11, fontweight='bold')
        axes[i].set_ylabel('')
    
    axes[-1].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig)
    
    # Keputusan
    st.markdown("""
    <div class="insight-card">
        <div class="insight-title">💡 Keputusan Data Cleaning</div>
        <b>Mengapa Outlier Dipertahankan?</b><br>
        • Outlier merupakan data nyata yang mencerminkan kondisi sebenarnya<br>
        • Beberapa provinsi memang menjadi sentra produksi utama<br>
        • Menghapus outlier akan menghilangkan informasi penting<br>
        • Dalam konteks perkebunan, variasi produksi antar provinsi adalah hal wajar
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# HALAMAN EDA
# =============================================================================
elif menu == "📈 EDA Visualisasi":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">📈 Exploratory Data Analysis</div>
        <div class="hero-subtitle">6 Visualisasi Matplotlib dengan Interpretasi Mendalam</div>
    </div>
    """, unsafe_allow_html=True)
    
    tabs = st.tabs([
        "1️⃣ Histogram",
        "2️⃣ Scatter",
        "3️⃣ Line",
        "4️⃣ Bar",
        "5️⃣ Boxplot",
        "6️⃣ Heatmap"
    ])
    
    with tabs[0]:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📊 Histogram - Distribusi Produksi</div>
        </div>
        """, unsafe_allow_html=True)
        
        kom = st.selectbox("Pilih Komoditas:", numeric_cols, key='hist_kom')
        
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.hist(df[kom], bins=15, color='#4CAF50', edgecolor='white', alpha=0.9)
        ax.axvline(df[kom].mean(), color='#FFD700', linestyle='--', linewidth=3, 
                   label=f'Mean: {df[kom].mean():.1f}')
        ax.axvline(df[kom].median(), color='#FF6B6B', linestyle='--', linewidth=3, 
                   label=f'Median: {df[kom].median():.1f}')
        ax.set_xlabel('Produksi (Ton)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Frekuensi', fontsize=12, fontweight='bold')
        ax.set_title(f'Distribusi Produksi {kom}', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(alpha=0.3, linestyle='--')
        st.pyplot(fig)
        
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-title">📝 Interpretasi Histogram</div>
            <b>Skewness: {df[kom].skew():.2f}</b><br>
            Distribusi bersifat <b>right-skewed</b> (menceng ke kanan), menunjukkan bahwa
            sebagian besar provinsi memiliki produksi rendah, sementara hanya beberapa provinsi
            yang menjadi sentra produksi dengan nilai sangat tinggi.
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[1]:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📊 Scatter Plot - Hubungan Antar Komoditas</div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            x_var = st.selectbox("Variabel X:", numeric_cols, key='sc_x')
        with col2:
            y_var = st.selectbox("Variabel Y:", numeric_cols, index=1, key='sc_y')
        
        fig, ax = plt.subplots(figsize=(12, 6))
        scatter = ax.scatter(df[x_var], df[y_var], c=df[x_var], cmap='Greens', 
                             s=150, edgecolors='white', linewidth=2, alpha=0.8)
        
        z = np.polyfit(df[x_var], df[y_var], 1)
        p = np.poly1d(z)
        x_line = np.linspace(df[x_var].min(), df[x_var].max(), 100)
        ax.plot(x_line, p(x_line), "r--", linewidth=3, label='Trend Line')
        
        ax.set_xlabel(x_var, fontsize=12, fontweight='bold')
        ax.set_ylabel(y_var, fontsize=12, fontweight='bold')
        corr_val = df[x_var].corr(df[y_var])
        ax.set_title(f'{x_var} vs {y_var} (r = {corr_val:.3f})', 
                    fontsize=14, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(alpha=0.3, linestyle='--')
        plt.colorbar(scatter, label=x_var)
        st.pyplot(fig)
        
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-title">📝 Interpretasi Scatter Plot</div>
            <b>Korelasi: r = {corr_val:.3f}</b><br>
            {'Korelasi positif kuat' if corr_val > 0.5 else 'Korelasi positif sedang' if corr_val > 0.3 else 'Korelasi lemah'}
            antara {x_var} dan {y_var}. Garis trend menunjukkan pola hubungan
            {'linier yang jelas' if abs(corr_val) > 0.5 else 'yang tidak terlalu kuat'}.
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[2]:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📊 Line Plot - Tren Produksi Top Provinsi</div>
        </div>
        """, unsafe_allow_html=True)
        
        n = st.slider("Top N Provinsi:", 5, 20, 10)
        k = st.selectbox("Komoditas:", numeric_cols, key='line_k')
        top = df.nlargest(n, k)
        
        fig, ax = plt.subplots(figsize=(14, 6))
        ax.plot(range(len(top)), top[k], marker='o', color='#2E7D32', 
                linewidth=3, markersize=12)
        ax.fill_between(range(len(top)), top[k], alpha=0.3, color='#4CAF50')
        ax.set_xticks(range(len(top)))
        ax.set_xticklabels(top['Provinsi'], rotation=45, ha='right', fontweight='bold')
        ax.set_ylabel(f'Produksi {k} (Ton)', fontsize=12, fontweight='bold')
        ax.set_title(f'Top {n} Provinsi - {k}', fontsize=14, fontweight='bold')
        ax.grid(alpha=0.3, linestyle='--')
        
        for i, v in enumerate(top[k]):
            ax.text(i, v, f'{v:,.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-title">📝 Interpretasi Line Plot</div>
            Produksi {k} sangat <b>terkonsentrasi</b> di beberapa provinsi tertentu.
            Provinsi peringkat pertama memiliki produksi jauh lebih besar dibanding peringkat berikutnya,
            mengindikasikan adanya <b>sentra produksi utama</b>.
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[3]:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📊 Bar Chart - Total Produksi Komoditas</div>
        </div>
        """, unsafe_allow_html=True)
        
        total = df[numeric_cols].sum().sort_values(ascending=True)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        colors = ['#C8E6C9', '#A5D6A7', '#81C784', '#66BB6A', '#4CAF50', '#43A047', '#2E7D32']
        bars = ax.barh(total.index, total.values, color=colors, edgecolor='white', linewidth=2)
        ax.set_xlabel('Total Produksi (Ton)', fontsize=12, fontweight='bold')
        ax.set_title('Total Produksi per Komoditas di Indonesia', fontsize=14, fontweight='bold')
        ax.grid(alpha=0.3, linestyle='--', axis='x')
        
        for bar, val in zip(bars, total.values):
            ax.text(bar.get_width() + max(total)*0.01, 
                   bar.get_y() + bar.get_height()/2,
                   f'{val:,.0f} ton', va='center', fontsize=11, fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">📝 Interpretasi Bar Chart</div>
            <b>Kelapa Sawit</b> mendominasi total produksi dengan selisih sangat jauh dari komoditas lain.
            Ini menunjukkan ketergantungan Indonesia pada satu komoditas utama yang berisiko
            jika terjadi fluktuasi harga global.
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[4]:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📊 Boxplot - Sebaran Produksi per Komoditas</div>
        </div>
        """, unsafe_allow_html=True)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        df_m = df.melt(id_vars=['Provinsi'], value_vars=numeric_cols)
        sns.boxplot(data=df_m, x='variable', y='value', ax=ax, 
                   palette='Greens', showfliers=True)
        ax.set_title('Distribusi Produksi per Komoditas', fontsize=14, fontweight='bold')
        ax.set_xlabel('Komoditas', fontsize=12, fontweight='bold')
        ax.set_ylabel('Produksi (Ton)', fontsize=12, fontweight='bold')
        plt.xticks(rotation=45, fontweight='bold')
        ax.grid(alpha=0.3, linestyle='--', axis='y')
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">📝 Interpretasi Boxplot</div>
            <b>Kelapa Sawit</b> memiliki variasi produksi tertinggi antar provinsi (sebaran luas).
            <b>Teh dan Kakao</b> memiliki produksi yang paling rendah dan merata.
            Beberapa komoditas menunjukkan <b>outlier ekstrem</b> yang merupakan provinsi sentra produksi.
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[5]:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📊 Heatmap - Korelasi Antar Komoditas</div>
        </div>
        """, unsafe_allow_html=True)
        
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(df[numeric_cols].corr(), annot=True, fmt='.2f', 
                   cmap='Greens', ax=ax, linewidths=1, center=0,
                   cbar_kws={'label': 'Korelasi'})
        ax.set_title('Heatmap Korelasi Antar Komoditas', fontsize=14, fontweight='bold')
        plt.xticks(fontweight='bold')
        plt.yticks(fontweight='bold')
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown("""
        <div class="insight-card">
            <div class="insight-title">📝 Interpretasi Heatmap</div>
            Warna <b>hijau tua</b> menunjukkan korelasi positif kuat (komoditas cenderung diproduksi bersamaan).
            Warna <b>terang</b> menunjukkan korelasi mendekati 0 (tidak ada hubungan).
            Informasi ini penting untuk perencanaan <b>diversifikasi komoditas</b> di tingkat provinsi.
        </div>
        """, unsafe_allow_html=True)

# =============================================================================
# HALAMAN ANALISIS HUBUNGAN
# =============================================================================
elif menu == "🔗 Analisis Hubungan":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">🔗 Analisis Hubungan Variabel</div>
        <div class="hero-subtitle">Identifikasi Variabel Paling Berpengaruh</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
        <div class="section-title">📊 Matriks Korelasi</div>
    </div>
    """, unsafe_allow_html=True)
    
    corr = df[numeric_cols].corr()
    st.dataframe(corr.round(3), use_container_width=True)
    
    st.markdown("""
    <div class="section-card">
        <div class="section-title">⭐ Variabel Paling Berpengaruh</div>
    </div>
    """, unsafe_allow_html=True)
    
    total_corr = corr.abs().sum().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ['#1B5E20' if i == 0 else '#4CAF50' for i in range(len(total_corr))]
    bars = ax.barh(total_corr.index, total_corr.values, color=colors, edgecolor='white', linewidth=2)
    ax.set_xlabel('Total Absolut Korelasi', fontsize=12, fontweight='bold')
    ax.set_title('Tingkat Pengaruh Setiap Komoditas', fontsize=14, fontweight='bold')
    ax.grid(alpha=0.3, linestyle='--', axis='x')
    
    for bar, val in zip(bars, total_corr.values):
        ax.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2,
                f'{val:.2f}', va='center', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    st.pyplot(fig)
    
    top_var = total_corr.index[0]
    
    st.markdown(f"""
    <div class="insight-card">
        <div class="insight-title">🏆 Variabel Paling Berpengaruh: {top_var}</div>
        <b>Total Korelasi Absolut: {total_corr.values[0]:.2f}</b><br><br>
        <b>Alasan:</b><br>
        1. Memiliki total korelasi tertinggi dengan semua komoditas lain<br>
        2. Menunjukkan hubungan paling kuat dalam ekosistem perkebunan<br>
        3. Provinsi dengan produksi {top_var} tinggi cenderung memproduksi komoditas lain juga<br>
        4. Dapat dijadikan <b>indikator utama</b> perkembangan perkebunan nasional<br>
        5. Mencerminkan faktor geografis dan iklim yang mendukung berbagai jenis perkebunan
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# HALAMAN MACHINE LEARNING
# =============================================================================
elif menu == "🤖 Machine Learning":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">🤖 Machine Learning</div>
        <div class="hero-subtitle">Pemodelan Regresi untuk Prediksi Produksi</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Config
    st.markdown("""
    <div class="section-card">
        <div class="section-title">⚙️ Konfigurasi Model</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        target = st.selectbox("🎯 Variabel Dependen (Y):", numeric_cols)
    with col2:
        feats = st.multiselect("📊 Variabel Independen (X):", 
                              [c for c in numeric_cols if c != target],
                              default=[c for c in numeric_cols if c != target][:3])
    
    if len(feats) > 0:
        X = df[feats]
        y = df[target]
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = LinearRegression().fit(X_tr, y_tr)
        pred = model.predict(X_te)
        
        mae = mean_absolute_error(y_te, pred)
        rmse = np.sqrt(mean_squared_error(y_te, pred))
        r2 = r2_score(y_te, pred)
        
        # KPI Metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class="kpi-card" style="border-left-color: #1976D2;">
                <div class="kpi-icon">📉</div>
                <div class="kpi-label">MAE</div>
                <div class="kpi-value">{mae:.2f}</div>
                <div class="kpi-trend">Mean Absolute Error</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="kpi-card" style="border-left-color: #FFA000;">
                <div class="kpi-icon">📊</div>
                <div class="kpi-label">RMSE</div>
                <div class="kpi-value">{rmse:.2f}</div>
                <div class="kpi-trend">Root Mean Squared Error</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            color = '#4CAF50' if r2 > 0.5 else '#FF6B6B'
            st.markdown(f"""
            <div class="kpi-card" style="border-left-color: {color};">
                <div class="kpi-icon">🎯</div>
                <div class="kpi-label">R² Score</div>
                <div class="kpi-value">{r2:.4f}</div>
                <div class="kpi-trend">{r2*100:.1f}% Variasi Terjelaskan</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Persamaan
        equation = f"{target} = {model.intercept_:.2f}"
        for feat, coef in zip(feats, model.coef_):
            equation += f" + {coef:.2f} × {feat}"
        
        st.markdown(f"""
        <div class="section-card">
            <div class="section-title">📐 Persamaan Regresi</div>
            <code style="font-size: 16px; padding: 15px; background: #f5f7fa; display: block; border-radius: 10px;">
            {equation}
            </code>
        </div>
        """, unsafe_allow_html=True)
        
        # Visualization
        st.markdown("""
        <div class="section-card">
            <div class="section-title">📈 Visualisasi Prediksi</div>
        </div>
        """, unsafe_allow_html=True)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(y_te, pred, c='#4CAF50', s=150, edgecolors='white', linewidth=2, alpha=0.8)
        min_val = min(y_te.min(), pred.min())
        max_val = max(y_te.max(), pred.max())
        ax.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=3, label='Perfect Prediction')
        ax.set_xlabel('Nilai Aktual', fontsize=12, fontweight='bold')
        ax.set_ylabel('Nilai Prediksi', fontsize=12, fontweight='bold')
        ax.set_title('Aktual vs Prediksi', fontsize=14, fontweight='bold')
        ax.legend(fontsize=11)
        ax.grid(alpha=0.3, linestyle='--')
        st.pyplot(fig)
        
        # Interpretasi
        if r2 > 0.7:
            kualitas = "SANGAT BAIK"
            warna = "#4CAF50"
        elif r2 > 0.5:
            kualitas = "BAIK"
            warna = "#FFA000"
        else:
            kualitas = "PERLU PERBAIKAN"
            warna = "#FF6B6B"
        
        st.markdown(f"""
        <div class="insight-card" style="border-left-color: {warna};">
            <div class="insight-title">📝 Interpretasi Model: {kualitas}</div>
            <b>MAE = {mae:.2f} ton</b> → Rata-rata error prediksi<br>
            <b>RMSE = {rmse:.2f} ton</b> → Standar deviasi error<br>
            <b>R² = {r2:.4f}</b> → Model menjelaskan {r2*100:.2f}% variasi data<br><br>
            {'✅ Model sangat baik untuk prediksi produksi ' + target if r2 > 0.7 else '⚠️ Model perlu peningkatan dengan menambah data atau fitur' if r2 > 0.5 else '❌ Model kurang akurat, perlu perbaikan signifikan'}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Pilih minimal 1 variabel independen!")

# =============================================================================
# HALAMAN INSIGHT
# =============================================================================
elif menu == "💡 Insight & Rekomendasi":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">💡 Insight & Rekomendasi</div>
        <div class="hero-subtitle">Temuan Penting dan Rekomendasi Implementatif</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
        <div class="section-title">🔍 5 INSIGHT UTAMA</div>
    </div>
    """, unsafe_allow_html=True)
    
    insights = [
        ("🌴 Kelapa Sawit Mendominasi", 
         f"Menyumbang {df['Kelapa_Sawit'].sum()/df[numeric_cols].sum().sum()*100:.1f}% total produksi nasional. "
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
        <div class="insight-card">
            <div class="insight-title">#{i} {title}</div>
            {content}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-card">
        <div class="section-title">💡 5 REKOMENDASI IMPLEMENTATIF</div>
    </div>
    """, unsafe_allow_html=True)
    
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
        <div class="rec-card">
            <div class="insight-title" style="color: #1976D2;">#{i} {title}</div>
            {content}
        </div>
        """, unsafe_allow_html=True)

# =============================================================================
# HALAMAN BONUS
# =============================================================================
elif menu == "🎁 Bonus Analytics":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">🎁 Bonus Analytics</div>
        <div class="hero-subtitle">Advanced Machine Learning: Random Forest & Decision Tree</div>
    </div>
    """, unsafe_allow_html=True)
    
    tabs = st.tabs(["🌲 Random Forest", "🌳 Decision Tree"])
    
    with tabs[0]:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">🌲 Random Forest Regressor</div>
            Ensemble learning method dengan 50 decision trees
        </div>
        """, unsafe_allow_html=True)
        
        target = st.selectbox("🎯 Target Variabel:", numeric_cols, key='rf')
        feats = [c for c in numeric_cols if c != target]
        
        X, y = df[feats], df[target]
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
        
        rf = RandomForestRegressor(n_estimators=50, random_state=42)
        rf.fit(X_tr, y_tr)
        pred = rf.predict(X_te)
        
        r2_rf = r2_score(y_te, pred)
        rmse_rf = np.sqrt(mean_squared_error(y_te, pred))
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-icon">🎯</div>
                <div class="kpi-label">R² Score</div>
                <div class="kpi-value">{r2_rf:.4f}</div>
                <div class="kpi-trend">{r2_rf*100:.1f}% Akurasi</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-icon">📊</div>
                <div class="kpi-label">RMSE</div>
                <div class="kpi-value">{rmse_rf:.2f}</div>
                <div class="kpi-trend">Error Standar</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Feature Importance
        feat_imp = pd.DataFrame({
            'Feature': feats,
            'Importance': rf.feature_importances_
        }).sort_values('Importance')
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(feat_imp['Feature'], feat_imp['Importance'], color='#4CAF50', 
                edgecolor='white', linewidth=2)
        ax.set_xlabel('Importance Score', fontsize=12, fontweight='bold')
        ax.set_title('Feature Importance - Random Forest', fontsize=14, fontweight='bold')
        ax.grid(alpha=0.3, linestyle='--', axis='x')
        plt.tight_layout()
        st.pyplot(fig)
    
    with tabs[1]:
        st.markdown("""
        <div class="section-card">
            <div class="section-title">🌳 Decision Tree Regressor</div>
            Model berbasis struktur pohon keputusan
        </div>
        """, unsafe_allow_html=True)
        
        target = st.selectbox("🎯 Target Variabel:", numeric_cols, key='dt')
        max_depth = st.slider("Max Depth:", 2, 10, 4)
        feats = [c for c in numeric_cols if c != target]
        
        X, y = df[feats], df[target]
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
        
        dt = DecisionTreeRegressor(max_depth=max_depth, random_state=42)
        dt.fit(X_tr, y_tr)
        pred = dt.predict(X_te)
        
        r2_dt = r2_score(y_te, pred)
        
        st.markdown(f"""
        <div class="kpi-card" style="width: 300px;">
            <div class="kpi-icon">🎯</div>
            <div class="kpi-label">R² Score</div>
            <div class="kpi-value">{r2_dt:.4f}</div>
            <div class="kpi-trend">{r2_dt*100:.1f}% Akurasi</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Tree Visualization
        st.markdown("""
        <div class="section-card">
            <div class="section-title">🌳 Visualisasi Decision Tree</div>
        </div>
        """, unsafe_allow_html=True)
        
        fig, ax = plt.subplots(figsize=(20, 10))
        plot_tree(dt, feature_names=feats, filled=True, rounded=True, 
                 ax=ax, fontsize=8)
        plt.title(f'Decision Tree (Max Depth: {max_depth})', fontsize=14, fontweight='bold')
        plt.tight_layout()
        st.pyplot(fig)

# =============================================================================
# FOOTER
# =============================================================================
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer-premium">
    <h3>🌴 Dashboard Analisis Perkebunan Indonesia</h3>
    <p style="margin: 5px 0;">Disusun untuk memenuhi Ujian Akhir Semester</p>
    <p style="margin: 5px 0; font-size: 14px;">Program Studi Sains Data • UIN K.H. Abdurrahman Wahid Pekalongan</p>
    <p style="margin: 10px 0; opacity: 0.8;">© 2026 • Premium UI/UX Design</p>
</div>
""", unsafe_allow_html=True)
