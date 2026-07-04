import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import folium
from streamlit_folium import st_folium
import base64
import io

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="Tropical Heritage - Dashboard Analitik Perkebunan Indonesia",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# LOAD CUSTOM CSS
# ============================================
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

try:
    load_css('assets/style.css')
except:
    # Fallback inline CSS jika file tidak ditemukan
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@700;800;900&display=swap');
    
    * { margin: 0; padding: 0; box-sizing: border-box; }
    html, body { font-family: 'Inter', sans-serif !important; background: #0A0E17 !important; color: #E8EAF0 !important; }
    .main .block-container { padding: 2rem 3rem !important; max-width: 1400px !important; }
    
    .hero-header {
        background: linear-gradient(135deg, #0A0E17 0%, #1a2332 50%, #0d1b2a 100%);
        padding: 3rem 2rem; border-radius: 24px; margin-bottom: 2rem;
        position: relative; overflow: hidden; border: 1px solid rgba(255,255,255,0.05);
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    .hero-title {
        font-family: 'Playfair Display', serif !important; font-size: 3.5rem !important;
        font-weight: 900 !important; background: linear-gradient(135deg, #4CAF50, #81C784, #A5D6A7);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
        margin-bottom: 0.5rem !important; letter-spacing: -1px;
    }
    .hero-subtitle { font-size: 1.2rem !important; color: #9CA3AF !important; font-weight: 300 !important; }
    
    .metric-card {
        background: linear-gradient(145deg, rgba(18,24,38,0.9), rgba(26,35,50,0.8));
        backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px; padding: 1.8rem; transition: all 0.4s ease;
        position: relative; overflow: hidden; box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }
    .metric-card::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
        background: linear-gradient(90deg, #4CAF50, #81C784, #4CAF50);
        background-size: 200% 100%; animation: shimmer 3s ease-in-out infinite;
    }
    @keyframes shimmer { 0% { background-position: -200% 0; } 100% { background-position: 200% 0; } }
    .metric-card:hover { transform: translateY(-8px) scale(1.02); border-color: rgba(76,175,80,0.3); box-shadow: 0 20px 60px rgba(76,175,80,0.15); }
    .metric-icon { font-size: 2.5rem; margin-bottom: 1rem; display: block; }
    .metric-label { font-size: 0.85rem !important; color: #9CA3AF !important; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 600; }
    .metric-value { font-size: 2.2rem !important; font-weight: 800 !important; color: #E8EAF0 !important; line-height: 1.2 !important; }
    
    .section-header { margin: 3rem 0 2rem 0; padding-bottom: 1rem; border-bottom: 2px solid rgba(76,175,80,0.2); position: relative; }
    .section-header::after { content: ''; position: absolute; bottom: -2px; left: 0; width: 100px; height: 2px; background: linear-gradient(90deg, #4CAF50, transparent); }
    .section-title { font-family: 'Playfair Display', serif !important; font-size: 2.2rem !important; font-weight: 800 !important; color: #E8EAF0 !important; }
    .section-subtitle { font-size: 1rem !important; color: #6B7280 !important; }
    
    .chart-container {
        background: linear-gradient(145deg, rgba(18,24,38,0.95), rgba(26,35,50,0.9));
        backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px; padding: 2rem; margin: 1.5rem 0;
        transition: all 0.3s ease; box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    }
    .chart-container:hover { border-color: rgba(76,175,80,0.2); box-shadow: 0 12px 40px rgba(76,175,80,0.1); }
    .chart-title { font-size: 1.3rem !important; font-weight: 700 !important; color: #E8EAF0 !important; margin-bottom: 1.5rem !important; display: flex; align-items: center; gap: 0.8rem; }
    .chart-title::before { content: ''; width: 4px; height: 24px; background: linear-gradient(180deg, #4CAF50, #81C784); border-radius: 2px; }
    
    .map-container {
        background: linear-gradient(145deg, rgba(18,24,38,0.95), rgba(26,35,50,0.9));
        border: 1px solid rgba(255,255,255,0.08); border-radius: 24px; padding: 2rem; margin: 2rem 0;
        box-shadow: 0 12px 48px rgba(0,0,0,0.3); position: relative; overflow: hidden;
    }
    .map-container::before {
        content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
        background: linear-gradient(90deg, #1B5E20, #4CAF50, #81C784, #4CAF50, #1B5E20);
        background-size: 200% 100%; animation: shimmer 4s linear infinite;
    }
    
    .insight-box {
        background: linear-gradient(135deg, rgba(27,94,32,0.1), rgba(76,175,80,0.05));
        border: 1px solid rgba(76,175,80,0.3); border-left: 4px solid #4CAF50;
        border-radius: 12px; padding: 1.5rem; margin: 1.5rem 0;
    }
    
    .footer { text-align: center; padding: 3rem 2rem; margin-top: 4rem; border-top: 1px solid rgba(255,255,255,0.05); color: #6B7280 !important; }
    .footer-brand { font-family: 'Playfair Display', serif !important; font-size: 1.5rem !important; background: linear-gradient(135deg, #4CAF50, #81C784); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
    
    .badge { display: inline-block; padding: 0.3rem 0.8rem; background: rgba(76,175,80,0.15); color: #4CAF50; border-radius: 20px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; border: 1px solid rgba(76,175,80,0.3); }
    
    .premium-divider { height: 2px; background: linear-gradient(90deg, transparent, rgba(76,175,80,0.3), transparent); margin: 3rem 0; border: none; }
    
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
    .metric-card, .chart-container, .map-container { animation: fadeInUp 0.6s ease-out; }
    
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: rgba(18,24,38,0.5); }
    ::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #1B5E20, #4CAF50); border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True)

# ============================================
# HELPER FUNCTIONS
# ============================================
def create_metric_card(icon, label, value, delta=None):
    """Create a premium metric card"""
    delta_html = f'<div class="metric-delta">{delta}</div>' if delta else ''
    return f"""
    <div class="metric-card">
        <span class="metric-icon">{icon}</span>
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """

def create_section_header(title, subtitle=""):
    """Create a section header"""
    subtitle_html = f'<div class="section-subtitle">{subtitle}</div>' if subtitle else ''
    return f"""
    <div class="section-header">
        <h2 class="section-title">{title}</h2>
        {subtitle_html}
    </div>
    """

def create_chart_container(title, chart_html):
    """Wrap chart in premium container"""
    return f"""
    <div class="chart-container">
        <div class="chart-title">{title}</div>
        {chart_html}
    </div>
    """

def create_insight_box(title, content):
    """Create insight/recommendation box"""
    return f"""
    <div class="insight-box">
        <div class="insight-title">{title}</div>
        <div>{content}</div>
    </div>
    """

# ============================================
# SIDEBAR NAVIGATION
# ============================================
with st.sidebar:
    # Brand Header
    st.markdown("""
    <div class="sidebar-brand">
        <h1>🌴 Tropical Heritage</h1>
        <p>Indonesian Plantation Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation Menu
    st.markdown("### 📍 NAVIGASI")
    
    menu_items = {
        "🏠 Beranda & Peta": "beranda",
        "📊 A. Data Understanding": "data_understanding",
        "🧹 B. Data Cleaning": "data_cleaning",
        "📈 C. EDA (6 Visualisasi)": "eda",
        "🔗 D. Analisis Hubungan": "hubungan",
        "📉 E. Regresi Linear": "regresi",
        "🌲 Random Forest": "random_forest",
        "🌳 Decision Tree": "decision_tree",
        "🔮 Forecasting": "forecasting",
        "⚖️ Komparator": "komparator",
        "💡 F. Insight & Rekomendasi": "insight"
    }
    
    selected_page = st.radio(
        "Pilih Halaman",
        options=list(menu_items.keys()),
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Commodity Filter
    st.markdown("### 🎯 FILTER KOMODITAS")
    komoditas_options = ['Kelapa_Sawit', 'Kelapa', 'Tebu', 'Karet', 'Kopi', 'Kakao', 'Teh']
    selected_komoditas = st.selectbox(
        "Pilih Komoditas",
        options=komoditas_options,
        index=0,
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Footer Info
    st.markdown("""
    <div style="text-align: center; padding: 1rem; color: #6B7280; font-size: 0.8rem;">
        <div style="font-weight: 600; color: #4CAF50; margin-bottom: 0.5rem;">UAS SAINS DATA 2026</div>
        <div>UIN GUS DUR PEKALONGAN</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# MAIN CONTENT - BERANDA & PETA
# ============================================
if selected_page == "🏠 Beranda & Peta":
    # Hero Header
    st.markdown("""
    <div class="hero-header">
        <h1 class="hero-title">Tropical Heritage Dashboard</h1>
        <p class="hero-subtitle">Menelusuri Jejak Perkebunan Nusantara dari Sabang sampai Merauke</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Premium Metric Cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(create_metric_card("🗺️", "Provinsi Terdata", "38", "Nusantara"), unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_metric_card("🌱", "Jenis Komoditas", "7", "Tanaman Tropis"), unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_metric_card("📊", "Total Produksi", "54.4K", "Ton Nasional"), unsafe_allow_html=True)
    
    with col4:
        st.markdown(create_metric_card("🏆", "Primadona", "Kelapa Sawit", "Produksi Tertinggi"), unsafe_allow_html=True)
    
    st.markdown('<hr class="premium-divider">', unsafe_allow_html=True)
    
    # Map Section
    st.markdown(create_section_header("🗺️ PETA PERKEBUNAN INDONESIA", "Klik lingkaran untuk melihat detail produksi setiap provinsi"), unsafe_allow_html=True)
    
    # Map Container
    st.markdown('<div class="map-container">', unsafe_allow_html=True)
    
    # Create interactive map with Plotly
    # Sample data - replace with your actual data loading
    map_data = pd.DataFrame({
        'provinsi': ['Riau', 'Kalimantan Tengah', 'Sumatera Utara', 'Kalimantan Barat', 
                     'Sumatera Selatan', 'Kalimantan Timur', 'Jambi', 'Sumatera Barat', 
                     'Jawa Timur', 'Bengkulu'],
        'lat': [0.507, -1.596, 2.684, -0.267, -3.139, 0.780, -1.610, -0.796, -7.536, -3.568],
        'lon': [101.462, 113.982, 99.123, 110.040, 104.214, 116.631, 102.579, 100.490, 112.238, 102.123],
        'produksi': [8500, 6200, 5800, 4900, 4500, 4200, 3800, 3200, 2800, 2500]
    })
    
    fig_map = px.scatter_mapbox(
        map_data,
        lat='lat',
        lon='lon',
        size='produksi',
        color='produksi',
        hover_name='provinsi',
        hover_data={'produksi': True, 'lat': False, 'lon': False},
        color_continuous_scale=px.colors.sequential.Viridis,
        mapbox_style="carto-darkmatter",
        center={"lat": -2.5, "lon": 118.0},
        zoom=4,
        size_max=40,
        opacity=0.8
    )
    
    fig_map.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        height=600,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E8EAF0')
    )
    
    st.plotly_chart(fig_map, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Map Insight
    st.markdown(create_insight_box(
        "Insight Peta",
        "Lingkaran besar menunjukkan provinsi sentra produksi Kelapa Sawit. Terlihat jelas konsentrasi produksi di wilayah Sumatera (untuk kelapa sawit & karet) dan Jawa Timur (untuk tebu & kopi)."
    ), unsafe_allow_html=True)
    
    st.markdown('<hr class="premium-divider">', unsafe_allow_html=True)
    
    # Top 10 Provinces
    st.markdown(create_section_header("🏆 Top 10 Provinsi Sentra Produksi", f"Peringkat provinsi dengan produksi {selected_komoditas} tertinggi"), unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Bar chart
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
                textfont=dict(color='#E8EAF0', size=12)
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
        # Pie chart - Komposisi
        st.markdown("#### Komposisi Komoditas")
        
        komoditas_data = pd.DataFrame({
            'komoditas': ['Kelapa Sawit', 'Kelapa', 'Tebu', 'Karet', 'Kopi', 'Kakao', 'Teh'],
            'persentase': [83.6, 5.12, 4.53, 3.92, 1.5, 1.14, 0.219]
        })
        
        fig_pie = go.Figure(data=[
            go.Pie(
                labels=komoditas_data['komoditas'],
                values=komoditas_data['persentase'],
                hole=0.4,
                marker=dict(colors=['#4CAF50', '#81C784', '#A5D6A7', '#C8E6C9', '#E8F5E9', '#F1F8E9', '#DCEDC8']),
                textinfo='percent',
                textfont=dict(size=12, color='#E8EAF0'),
                hovertemplate='<b>%{label}</b><br>Persentase: %{percent}<extra></extra>'
            )
        ])
        
        fig_pie.update_layout(
            height=500,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E8EAF0'),
            showlegend=True,
            legend=dict(font=dict(size=11))
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)

# ============================================
# OTHER PAGES (Template Structure)
# ============================================
elif selected_page == "📊 A. Data Understanding":
    st.markdown(create_section_header("📊 Data Understanding", "Memahami struktur dan karakteristik dataset perkebunan Indonesia"), unsafe_allow_html=True)
    
    # Add your existing Data Understanding code here
    # Wrap with chart-container class for premium look
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">Informasi Dataset</div>
        <p>Halaman ini menampilkan informasi detail tentang dataset yang digunakan dalam analisis.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Your existing code for data understanding...

elif selected_page == "🧹 B. Data Cleaning":
    st.markdown(create_section_header("🧹 Data Cleaning", "Proses pembersihan dan preparasi data"), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">Data Cleaning Pipeline</div>
        <p>Proses pembersihan data meliputi handling missing values, outlier detection, dan data transformation.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Your existing code for data cleaning...

elif selected_page == "📈 C. EDA (6 Visualisasi)":
    st.markdown(create_section_header("📈 Exploratory Data Analysis", "6 Visualisasi untuk memahami pola dan distribusi data"), unsafe_allow_html=True)
    
    # Create tabs for 6 visualizations
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📊 Distribusi 1", "📊 Distribusi 2", "📊 Distribusi 3",
        "📊 Tren 1", "📊 Tren 2", "📊 Komparasi"
    ])
    
    with tab1:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">Visualisasi 1</div>
        </div>
        """, unsafe_allow_html=True)
        # Your existing visualization 1 code...
    
    with tab2:
        st.markdown("""
        <div class="chart-container">
            <div class="chart-title">Visualisasi 2</div>
        </div>
        """, unsafe_allow_html=True)
        # Your existing visualization 2 code...
    
    # Continue for other tabs...

elif selected_page == "🔗 D. Analisis Hubungan":
    st.markdown(create_section_header("🔗 Analisis Hubungan", "Menganalisis korelasi dan hubungan antar variabel"), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">Correlation Matrix</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Your existing correlation analysis code...

elif selected_page == "📉 E. Regresi Linear":
    st.markdown(create_section_header("📉 Regresi Linear", "Model prediksi dengan regresi linear"), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">Linear Regression Model</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Your existing regression code...

elif selected_page == "🌲 Random Forest":
    st.markdown(create_section_header("🌲 Random Forest", "Model ensemble dengan Random Forest"), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">Random Forest Model</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Your existing Random Forest code...

elif selected_page == "🌳 Decision Tree":
    st.markdown(create_section_header("🌳 Decision Tree", "Model klasifikasi/regresi dengan Decision Tree"), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">Decision Tree Model</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Your existing Decision Tree code...

elif selected_page == "🔮 Forecasting":
    st.markdown(create_section_header("🔮 Forecasting", "Prediksi produksi masa depan"), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">Time Series Forecasting</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Your existing forecasting code...

elif selected_page == "⚖️ Komparator":
    st.markdown(create_section_header("⚖️ Komparator Model", "Perbandingan performa antar model"), unsafe_allow_html=True)
    
    st.markdown("""
    <div class="chart-container">
        <div class="chart-title">Model Comparison</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Your existing model comparison code...

elif selected_page == "💡 F. Insight & Rekomendasi":
    st.markdown(create_section_header("💡 Insight & Rekomendasi", "Temuan utama dan rekomendasi strategis"), unsafe_allow_html=True)
    
    st.markdown(create_insight_box(
        "Insight Utama",
        "Berdasarkan analisis menyeluruh, kelapa sawit mendominasi produksi perkebunan Indonesia dengan kontribusi lebih dari 80%."
    ), unsafe_allow_html=True)
    
    st.markdown(create_insight_box(
        "Rekomendasi Strategis",
        "1. Fokus pada optimalisasi produksi kelapa sawit di provinsi sentra<br>2. Diversifikasi komoditas untuk mengurangi ketergantungan<br>3. Pengembangan infrastruktur di wilayah potensial"
    ), unsafe_allow_html=True)
    
    # Your existing insight code...

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
