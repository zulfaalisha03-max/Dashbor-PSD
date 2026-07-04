import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="Tropical Heritage Dashboard",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CUSTOM CSS
# ============================================
st.markdown("""
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }

.main .block-container {
    padding: 2rem 3rem !important;
    max-width: 1400px !important;
}

.hero-header {
    background: linear-gradient(135deg, #0A0E17 0%, #1a2332 50%, #0d1b2a 100%);
    padding: 3rem 2rem;
    border-radius: 24px;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(255, 255, 255, 0.05);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.hero-title {
    font-size: 3rem !important;
    font-weight: 900 !important;
    background: linear-gradient(135deg, #4CAF50, #81C784, #A5D6A7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem !important;
    letter-spacing: -1px;
}

.hero-subtitle {
    font-size: 1.2rem !important;
    color: #9CA3AF !important;
    font-weight: 300 !important;
    letter-spacing: 0.5px;
}

.metric-card {
    background: linear-gradient(145deg, rgba(18, 24, 38, 0.9), rgba(26, 35, 50, 0.8));
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 1.8rem;
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}

.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #4CAF50, #81C784, #4CAF50);
}

.metric-card:hover {
    transform: translateY(-5px);
    border-color: rgba(76, 175, 80, 0.3);
    box-shadow: 0 20px 60px rgba(76, 175, 80, 0.15);
}

.metric-icon { font-size: 2.5rem; margin-bottom: 1rem; display: block; }
.metric-label {
    font-size: 0.85rem !important;
    color: #9CA3AF !important;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-weight: 600;
    margin-bottom: 0.5rem !important;
}
.metric-value {
    font-size: 2rem !important;
    font-weight: 800 !important;
    color: #E8EAF0 !important;
    line-height: 1.2 !important;
}
.metric-delta {
    font-size: 0.9rem !important;
    color: #4CAF50 !important;
    font-weight: 500 !important;
}

.section-header {
    margin: 3rem 0 2rem 0;
    padding-bottom: 1rem;
    border-bottom: 2px solid rgba(76, 175, 80, 0.2);
    position: relative;
}

.section-header::after {
    content: '';
    position: absolute;
    bottom: -2px; left: 0;
    width: 100px; height: 2px;
    background: linear-gradient(90deg, #4CAF50, transparent);
}

.section-title {
    font-size: 2rem !important;
    font-weight: 800 !important;
    color: #E8EAF0 !important;
    margin-bottom: 0.5rem !important;
}

.section-subtitle {
    font-size: 1rem !important;
    color: #6B7280 !important;
}

.chart-container {
    background: linear-gradient(145deg, rgba(18, 24, 38, 0.95), rgba(26, 35, 50, 0.9));
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 2rem;
    margin: 1.5rem 0;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
}

.chart-title {
    font-size: 1.3rem !important;
    font-weight: 700 !important;
    color: #E8EAF0 !important;
    margin-bottom: 1.5rem !important;
    padding-left: 1rem;
    border-left: 4px solid #4CAF50;
}

.map-container {
    background: linear-gradient(145deg, rgba(18, 24, 38, 0.95), rgba(26, 35, 50, 0.9));
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 24px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 12px 48px rgba(0, 0, 0, 0.3);
}

.insight-box {
    background: linear-gradient(135deg, rgba(27, 94, 32, 0.1), rgba(76, 175, 80, 0.05));
    border: 1px solid rgba(76, 175, 80, 0.3);
    border-left: 4px solid #4CAF50;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1.5rem 0;
}

.insight-title {
    font-weight: 700 !important;
    color: #4CAF50 !important;
    margin-bottom: 0.5rem !important;
    font-size: 1.1rem !important;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0D1117 0%, #161B22 100%) !important;
}

.sidebar-brand {
    text-align: center;
    padding: 2rem 1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    margin-bottom: 1.5rem;
}

.sidebar-brand h1 {
    font-size: 1.8rem !important;
    background: linear-gradient(135deg, #4CAF50, #81C784);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.3rem !important;
}

.sidebar-brand p {
    font-size: 0.8rem !important;
    color: #6B7280 !important;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.footer {
    text-align: center;
    padding: 3rem 2rem;
    margin-top: 4rem;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    color: #6B7280 !important;
    font-size: 0.9rem !important;
}

.footer-brand {
    font-size: 1.5rem !important;
    background: linear-gradient(135deg, #4CAF50, #81C784);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem !important;
}

.premium-divider {
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(76, 175, 80, 0.3), transparent);
    margin: 3rem 0;
    border: none;
}

@media (max-width: 768px) {
    .main .block-container { padding: 1rem !important; }
    .hero-title { font-size: 2rem !important; }
    .section-title { font-size: 1.5rem !important; }
    .chart-container { padding: 1.5rem; }
}
</style>
""", unsafe_allow_html=True)

# ============================================
# DATA DUMMY
# ============================================
map_data = pd.DataFrame({
    'provinsi': ['Riau', 'Kalimantan Tengah', 'Sumatera Utara', 'Kalimantan Barat', 
                 'Sumatera Selatan', 'Kalimantan Timur', 'Jambi', 'Sumatera Barat', 
                 'Jawa Timur', 'Bengkulu'],
    'lat': [0.507, -1.596, 2.684, -0.267, -3.139, 0.780, -1.610, -0.796, -7.536, -3.568],
    'lon': [101.462, 113.982, 99.123, 110.040, 104.214, 116.631, 102.579, 100.490, 112.238, 102.123],
    'produksi': [8500, 6200, 5800, 4900, 4500, 4200, 3800, 3200, 2800, 2500]
})

komoditas_data = pd.DataFrame({
    'komoditas': ['Kelapa Sawit', 'Kelapa', 'Tebu', 'Karet', 'Kopi', 'Kakao', 'Teh'],
    'persentase': [83.6, 5.12, 4.53, 3.92, 1.5, 1.14, 0.219]
})

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <h1>🌴 Tropical Heritage</h1>
        <p>Indonesian Plantation Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📍 NAVIGASI")
    
    menu_options = [
        "🏠 Beranda & Peta",
        "📊 A. Data Understanding",
        "🧹 B. Data Cleaning",
        "📈 C. EDA (6 Visualisasi)",
        "🔗 D. Analisis Hubungan",
        "📉 E. Regresi Linear",
        "🌲 BONUS: Random Forest",
        "🌳 BONUS: Decision Tree",
        "🔮 BONUS: Forecasting",
        "⚖️ BONUS: Komparator",
        "💡 F. Insight & Rekomendasi"
    ]
    
    selected_page = st.radio("Pilih Halaman", options=menu_options)
    
    st.markdown("---")
    st.markdown("### 🎯 FILTER KOMODITAS")
    komoditas_options = ['Kelapa_Sawit', 'Kelapa', 'Tebu', 'Karet', 'Kopi', 'Kakao', 'Teh']
    selected_komoditas = st.selectbox("Pilih Komoditas", options=komoditas_options, index=0)
    
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 1rem; color: #6B7280; font-size: 0.8rem;">
        <div style="font-weight: 600; color: #4CAF50; margin-bottom: 0.5rem;">UAS SAINS DATA 2026</div>
        <div>UIN GUS DUR PEKALONGAN</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PAGE: BERANDA & PETA
# ============================================
if selected_page == "🏠 Beranda & Peta":
    st.markdown("""
    <div class="hero-header">
        <h1 class="hero-title">Tropical Heritage Dashboard</h1>
        <p class="hero-subtitle">Menelusuri Jejak Perkebunan Nusantara dari Sabang sampai Merauke</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <span class="metric-icon">🗺️</span>
            <div class="metric-label">Provinsi Terdata</div>
            <div class="metric-value">38</div>
            <div class="metric-delta">Nusantara</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <span class="metric-icon">🌱</span>
            <div class="metric-label">Jenis Komoditas</div>
            <div class="metric-value">7</div>
            <div class="metric-delta">Tanaman Tropis</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <span class="metric-icon">📊</span>
            <div class="metric-label">Total Produksi</div>
            <div class="metric-value">54.4K</div>
            <div class="metric-delta">Ton Nasional</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card">
            <span class="metric-icon">🏆</span>
            <div class="metric-label">Primadona</div>
            <div class="metric-value">Kelapa Sawit</div>
            <div class="metric-delta">Produksi Tertinggi</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<hr class="premium-divider">', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">🗺️ PETA PERKEBUNAN INDONESIA</h2>
        <div class="section-subtitle">Sebaran produksi per provinsi di seluruh Indonesia</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="map-container">', unsafe_allow_html=True)
    
    # ✅ FIXED: projection (bukan projection_type)
    fig_map = px.scatter_geo(
        map_data,
        lat='lat',
        lon='lon',
        size='produksi',
        color='produksi',
        hover_name='provinsi',
        hover_data={'produksi': True, 'lat': False, 'lon': False},
        color_continuous_scale='Viridis',
        scope='asia',
        center={"lat": -2.5, "lon": 118.0},
        projection="mercator",
        size_max=40,
        opacity=0.8
    )
    
    fig_map.update_layout(
        margin={"r": 0, "t": 30, "l": 0, "b": 0},
        height=600,
        geo=dict(
            showland=True,
            landcolor="rgb(30, 40, 50)",
            countrycolor="rgb(60, 70, 80)",
            showocean=True,
            oceancolor="rgb(10, 14, 23)",
            showlakes=True,
            lakecolor="rgb(15, 20, 30)",
            showsubunits=True,
            subunitcolor="rgb(50, 60, 70)",
            showframe=False,
            showcoastlines=True,
            coastlinecolor="rgb(70, 80, 90)",
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E8EAF0')
    )
    
    st.plotly_chart(fig_map, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
        <div class="insight-title">💡 Insight Peta</div>
        <p>Lingkaran besar menunjukkan provinsi sentra produksi Kelapa Sawit. Terlihat jelas konsentrasi produksi di wilayah Sumatera dan Kalimantan.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<hr class="premium-divider">', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="section-header">
        <h2 class="section-title">🏆 Top 10 Provinsi Sentra Produksi</h2>
        <div class="section-subtitle">Peringkat provinsi dengan produksi {selected_komoditas.replace('_', ' ')} tertinggi</div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig_bar = go.Figure(data=[
            go.Bar(
                x=map_data['produksi'],
                y=map_data['provinsi'],
                orientation='h',
                marker=dict(
                    color=map_data['produksi'],
                    colorscale='Viridis',
                    showscale=False
                ),
                text=map_data['produksi'].apply(lambda x: f'{x:,.0f} Ton'),
                textposition='auto',
                textfont=dict(color='white', size=12)
            )
        ])
        
        fig_bar.update_layout(
            height=500,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E8EAF0'),
            xaxis=dict(gridcolor='rgba(255,255,255,0.1)', title='Total Produksi (Ton)'),
            yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        st.plotly_chart(fig_bar, use_container_width=True)
    
    with col2:
        st.markdown("#### Komposisi Komoditas")
        
        fig_pie = go.Figure(data=[
            go.Pie(
                labels=komoditas_data['komoditas'],
                values=komoditas_data['persentase'],
                hole=0.4,
                marker=dict(colors=['#4CAF50', '#81C784', '#A5D6A7', '#C8E6C9', '#E8F5E9', '#F1F8E9', '#DCEDC8']),
                textinfo='percent',
                textfont=dict(size=12, color='white'),
                hovertemplate='<b>%{label}</b><br>Persentase: %{percent}<extra></extra>'
            )
        ])
        
        fig_pie.update_layout(
            height=500,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E8EAF0'),
            showlegend=True
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)

# ============================================
# PAGE: DATA UNDERSTANDING
# ============================================
elif selected_page == "📊 A. Data Understanding":
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">📊 Data Understanding</h2>
        <div class="section-subtitle">Memahami struktur dan karakteristik dataset perkebunan Indonesia</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">📋 Informasi Dataset</div>
        <p><strong style="color: #4CAF50;">Dataset:</strong> Produksi Perkebunan Indonesia</p>
        <p><strong style="color: #4CAF50;">Jumlah Provinsi:</strong> 38 Provinsi</p>
        <p><strong style="color: #4CAF50;">Komoditas:</strong> 7 Jenis (Kelapa Sawit, Kelapa, Tebu, Karet, Kopi, Kakao, Teh)</p>
        <p><strong style="color: #4CAF50;">Periode:</strong> Data produksi tahunan</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PAGE: DATA CLEANING
# ============================================
elif selected_page == "🧹 B. Data Cleaning":
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">🧹 Data Cleaning</h2>
        <div class="section-subtitle">Proses pembersihan dan preparasi data</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">🔧 Data Cleaning Pipeline</div>
        <ul style="color: #9CA3AF; margin-left: 2rem;">
            <li>Handling missing values</li>
            <li>Outlier detection</li>
            <li>Data transformation</li>
            <li>Feature engineering</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PAGE: EDA
# ============================================
elif selected_page == "📈 C. EDA (6 Visualisasi)":
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">📈 Exploratory Data Analysis</h2>
        <div class="section-subtitle">6 Visualisasi untuk memahami pola dan distribusi data</div>
    </div>
    """, unsafe_allow_html=True)
    
    viz_option = st.selectbox(
        "Pilih Visualisasi",
        ["1. Distribusi Produksi", "2. Tren Tahunan", "3. Box Plot", 
         "4. Histogram", "5. Scatter Plot", "6. Radar Chart"]
    )
    
    st.markdown(f"""
    <div class="chart-container">
        <div class="chart-title">📊 {viz_option}</div>
        <p style="color: #9CA3AF;">Tambahkan kode visualisasi Anda di sini</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PAGE: ANALISIS HUBUNGAN
# ============================================
elif selected_page == "🔗 D. Analisis Hubungan":
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">🔗 Analisis Hubungan</h2>
        <div class="section-subtitle">Menganalisis korelasi dan hubungan antar variabel</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">📊 Correlation Matrix</div>
        <p style="color: #9CA3AF;">Tambahkan kode analisis korelasi Anda di sini</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PAGE: REGRESI LINEAR
# ============================================
elif selected_page == "📉 E. Regresi Linear":
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">📉 Regresi Linear</h2>
        <div class="section-subtitle">Model prediksi dengan regresi linear</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">📈 Linear Regression Model</div>
        <p style="color: #9CA3AF;">Tambahkan kode regresi linear Anda di sini</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PAGE: RANDOM FOREST
# ============================================
elif selected_page == "🌲 BONUS: Random Forest":
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">🌲 Random Forest</h2>
        <div class="section-subtitle">Model ensemble dengan Random Forest</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">🌳 Random Forest Model</div>
        <p style="color: #9CA3AF;">Tambahkan kode Random Forest Anda di sini</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PAGE: DECISION TREE
# ============================================
elif selected_page == "🌳 BONUS: Decision Tree":
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">🌳 Decision Tree</h2>
        <div class="section-subtitle">Model klasifikasi/regresi dengan Decision Tree</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">🌲 Decision Tree Model</div>
        <p style="color: #9CA3AF;">Tambahkan kode Decision Tree Anda di sini</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PAGE: FORECASTING
# ============================================
elif selected_page == "🔮 BONUS: Forecasting":
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">🔮 Forecasting</h2>
        <div class="section-subtitle">Prediksi produksi masa depan</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">📊 Time Series Forecasting</div>
        <p style="color: #9CA3AF;">Tambahkan kode forecasting Anda di sini</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PAGE: KOMPARATOR
# ============================================
elif selected_page == "⚖️ BONUS: Komparator":
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">⚖️ Komparator Model</h2>
        <div class="section-subtitle">Perbandingan performa antar model</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">📊 Model Comparison</div>
        <p style="color: #9CA3AF;">Tambahkan kode komparasi model Anda di sini</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# PAGE: INSIGHT
# ============================================
elif selected_page == "💡 F. Insight & Rekomendasi":
    st.markdown("""
    <div class="section-header">
        <h2 class="section-title">💡 Insight & Rekomendasi</h2>
        <div class="section-subtitle">Temuan utama dan rekomendasi strategis</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
        <div class="insight-title">🎯 Insight Utama</div>
        <p>Kelapa sawit mendominasi produksi perkebunan Indonesia dengan kontribusi lebih dari 80%.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
        <div class="insight-title">💼 Rekomendasi Strategis</div>
        <ol style="color: #9CA3AF; margin-left: 2rem;">
            <li>Fokus pada optimalisasi produksi kelapa sawit di provinsi sentra</li>
            <li>Diversifikasi komoditas untuk mengurangi ketergantungan</li>
            <li>Pengembangan infrastruktur di wilayah potensial</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown("""
<div class="footer">
    <div class="footer-brand">🌴 Tropical Heritage</div>
    <p>Dashboard Analitik Perkebunan Indonesia</p>
    <p style="margin-top: 1rem; font-size: 0.8rem;">© 2026 UAS Sains Data - UIN Gus Dur Pekalongan</p>
</div>
""", unsafe_allow_html=True)
