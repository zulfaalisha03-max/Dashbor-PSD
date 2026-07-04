import streamlit as st
import pandas as pd
import numpy as np
import io

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import warnings
warnings.filterwarnings("ignore")

# ===========================================
# PAGE CONFIG
# ===========================================

st.set_page_config(
    page_title="Dashboard Perkebunan Indonesia",
    page_icon="🌴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===========================================
# CSS PREMIUM
# ===========================================

st.markdown("""

<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

.block-container{
padding-top:1rem;
padding-bottom:2rem;
padding-left:2rem;
padding-right:2rem;
}

[data-testid="stSidebar"]{

background:#1B4332;

}

[data-testid="stSidebar"] *{

color:white;

}

.card{

background:white;

padding:20px;

border-radius:18px;

box-shadow:0px 4px 15px rgba(0,0,0,.08);

margin-bottom:15px;

}

.metric-card{

background:white;

padding:18px;

border-radius:18px;

text-align:center;

box-shadow:0 5px 15px rgba(0,0,0,.08);

}

.metric-value{

font-size:34px;

font-weight:bold;

color:#2E7D32;

}

.metric-title{

font-size:15px;

color:gray;

}

.hero{

background:linear-gradient(90deg,#2E7D32,#43A047);

padding:35px;

border-radius:20px;

color:white;

margin-bottom:25px;

}

.section-title{

font-size:28px;

font-weight:bold;

color:#1B4332;

margin-bottom:15px;

}

.insight{

background:#E8F5E9;

padding:15px;

border-left:6px solid #2E7D32;

border-radius:12px;

margin-top:10px;

}

</style>

""",unsafe_allow_html=True)
if menu == "🏠 Overview":

    # ===============================
    # HERO
    # ===============================

    st.markdown("""
    <div class="hero">

    <h1>🌴 Dashboard Analisis Produksi Perkebunan Indonesia</h1>

    <h4>
    Visualisasi Interaktif Produksi Komoditas Perkebunan
    pada 38 Provinsi Indonesia
    </h4>

    </div>
    """, unsafe_allow_html=True)

    total_produksi = df[numeric_cols].sum().sum()

    total_provinsi = len(df)

    total_komoditas = len(numeric_cols)

    komoditas_terbesar = df[numeric_cols].sum().idxmax().replace("_"," ")

    # ===============================
    # KPI
    # ===============================

    c1,c2,c3,c4 = st.columns(4)

    with c1:

        st.markdown(f"""

        <div class="metric-card">

        <div class="metric-title">
        🌾 Total Produksi
        </div>

        <div class="metric-value">

        {total_produksi:,.0f}

        </div>

        Ton

        </div>

        """,unsafe_allow_html=True)

    with c2:

        st.markdown(f"""

        <div class="metric-card">

        <div class="metric-title">

        🗺 Provinsi

        </div>

        <div class="metric-value">

        {total_provinsi}

        </div>

        Indonesia

        </div>

        """,unsafe_allow_html=True)

    with c3:

        st.markdown(f"""

        <div class="metric-card">

        <div class="metric-title">

        🌱 Komoditas

        </div>

        <div class="metric-value">

        {total_komoditas}

        </div>

        Jenis

        </div>

        """,unsafe_allow_html=True)

    with c4:

        st.markdown(f"""

        <div class="metric-card">

        <div class="metric-title">

        🏆 Komoditas Terbesar

        </div>

        <div class="metric-value">

        🌴

        </div>

        {komoditas_terbesar}

        </div>

        """,unsafe_allow_html=True)

    st.write("")

    # ===============================
    # BAR CHART
    # ===============================

    kiri, kanan = st.columns((2,1))

    with kiri:

        top = df.copy()

        top["Total"] = top[numeric_cols].sum(axis=1)

        top = top.sort_values("Total",ascending=False).head(top_n)

        fig = px.bar(

            top,

            x="Provinsi",

            y="Total",

            color="Total",

            color_continuous_scale="Greens",

            title=f"Top {top_n} Produksi Perkebunan"

        )

        fig.update_layout(

            template="plotly_white",

            height=500,

            xaxis_title="",

            yaxis_title="Total Produksi"

        )

        st.plotly_chart(fig,use_container_width=True)

    with kanan:

        total = df[numeric_cols].sum()

        fig2 = px.pie(

            values=total.values,

            names=[i.replace("_"," ") for i in total.index],

            hole=.55,

            title="Komposisi Produksi"

        )

        fig2.update_layout(height=500)

        st.plotly_chart(fig2,use_container_width=True)

    # ===============================
    # KOMODITAS
    # ===============================

    st.markdown("## 🌱 Persebaran Komoditas")

    fig = px.bar(

        df.sort_values(komoditas,ascending=False).head(top_n),

        x="Provinsi",

        y=komoditas,

        color=komoditas,

        color_continuous_scale="Greens"

    )

    fig.update_layout(

        template="plotly_white",

        height=450,

        xaxis_title="",

        yaxis_title="Produksi"

    )

    st.plotly_chart(fig,use_container_width=True)

    # ===============================
    # INSIGHT
    # ===============================

    st.markdown("## 💡 Ringkasan Insight")

    a,b=st.columns(2)

    with a:

        st.markdown(f"""

        <div class="insight">

        <h4>🌴 Kelapa Sawit Dominan</h4>

        Menyumbang sekitar
        <b>{df["Kelapa_Sawit"].sum()/total_produksi*100:.1f}% </b>
        dari total produksi nasional.

        </div>

        """,unsafe_allow_html=True)

        st.markdown("""

        <div class="insight">

        <h4>🗺 Sentra Produksi</h4>

        Produksi nasional didominasi
        Provinsi di Pulau Sumatera
        dan Kalimantan.

        </div>

        """,unsafe_allow_html=True)

    with b:

        st.markdown("""

        <div class="insight">

        <h4>🌱 Diversifikasi</h4>

        Masih terdapat banyak provinsi
        dengan produksi nol pada beberapa
        komoditas.

        </div>

        """,unsafe_allow_html=True)

        st.markdown("""

        <div class="insight">

        <h4>📈 Potensi</h4>

        Pemerataan pengembangan komoditas
        dapat meningkatkan produktivitas nasional.

        </div>

        """,unsafe_allow_html=True)
        # ==========================================================
# DATA UNDERSTANDING
# ==========================================================

elif menu == "📊 Data Understanding":

    st.markdown("""
    <div class="hero">
        <h2>📊 Data Understanding</h2>
        <p>Memahami struktur, karakteristik, dan kualitas dataset produksi perkebunan Indonesia.</p>
    </div>
    """, unsafe_allow_html=True)

    # =============================
    # KPI
    # =============================

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "📍 Jumlah Provinsi",
        df.shape[0]
    )

    c2.metric(
        "🌱 Komoditas",
        len(numeric_cols)
    )

    c3.metric(
        "📋 Total Kolom",
        df.shape[1]
    )

    c4.metric(
        "❌ Missing Value",
        df.isnull().sum().sum()
    )

    st.divider()

    # =============================
    # INFORMASI DATASET
    # =============================

    kiri,kanan=st.columns((2,1))

    with kiri:

        st.subheader("📑 Informasi Dataset")

        info=pd.DataFrame({

            "Kolom":df.columns,

            "Tipe Data":df.dtypes.astype(str),

            "Non Null":df.count().values,

            "Missing":df.isnull().sum().values

        })

        st.dataframe(
            info,
            use_container_width=True,
            hide_index=True
        )

    with kanan:

        st.subheader("📌 Ringkasan")

        st.info(f"""

Jumlah Data

: **{df.shape[0]} baris**

Jumlah Variabel

: **{df.shape[1]} kolom**

Variabel Numerik

: **{len(numeric_cols)}**

Variabel Kategori

: **1**

        """)

    st.divider()

    # =============================
    # PREVIEW
    # =============================

    tab1,tab2,tab3=st.tabs([

        "👀 Preview",

        "📈 Statistik",

        "📚 Deskripsi"

    ])

    with tab1:

        st.subheader("5 Data Pertama")

        st.dataframe(

            df.head(),

            use_container_width=True,

            height=250

        )

    with tab2:

        desc=df[numeric_cols].describe().round(2)

        st.dataframe(

            desc,

            use_container_width=True

        )

    with tab3:

        deskripsi=pd.DataFrame({

            "Variabel":[

                "Provinsi",

                "Kelapa Sawit",

                "Kelapa",

                "Karet",

                "Kopi",

                "Kakao",

                "Teh",

                "Tebu"

            ],

            "Keterangan":[

                "Nama Provinsi",

                "Produksi Kelapa Sawit (Ton)",

                "Produksi Kelapa (Ton)",

                "Produksi Karet (Ton)",

                "Produksi Kopi (Ton)",

                "Produksi Kakao (Ton)",

                "Produksi Teh (Ton)",

                "Produksi Tebu (Ton)"

            ]

        })

        st.dataframe(

            deskripsi,

            use_container_width=True,

            hide_index=True

        )

    st.divider()

    # =============================
    # VISUALISASI
    # =============================

    st.subheader("📈 Total Produksi per Komoditas")

    total=df[numeric_cols].sum().sort_values(ascending=False)

    fig=px.bar(

        x=total.index,

        y=total.values,

        color=total.values,

        color_continuous_scale="Greens"

    )

    fig.update_layout(

        template="plotly_white",

        height=450,

        xaxis_title="",

        yaxis_title="Total Produksi"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # =============================
    # KESIMPULAN
    # =============================

    st.markdown("""

<div class="insight">

<h4>📌 Kesimpulan Data Understanding</h4>

<ul>

<li>Dataset terdiri dari <b>38 provinsi</b>.</li>

<li>Terdapat <b>7 komoditas perkebunan</b>.</li>

<li>Tidak ditemukan missing value.</li>

<li>Seluruh variabel numerik bertipe float.</li>

<li>Kelapa Sawit merupakan komoditas dengan total produksi terbesar.</li>

</ul>

</div>

""",unsafe_allow_html=True)
    # ==========================================================
# DATA CLEANING
# ==========================================================

elif menu == "🧹 Data Cleaning":

    st.markdown("""
    <div class="hero">
        <h2>🧹 Data Cleaning & Data Quality</h2>
        <p>Evaluasi kualitas dataset sebelum dilakukan analisis dan pemodelan.</p>
    </div>
    """, unsafe_allow_html=True)

    # =====================================
    # HITUNG DATA QUALITY
    # =====================================

    total_missing = int(df.isnull().sum().sum())
    total_duplicate = int(df.duplicated().sum())

    quality = 100

    if total_missing > 0:
        quality -= 25

    if total_duplicate > 0:
        quality -= 25

    # =====================================
    # KPI
    # =====================================

    c1,c2,c3,c4 = st.columns(4)

    c1.metric(
        "📋 Total Data",
        len(df)
    )

    c2.metric(
        "❌ Missing",
        total_missing
    )

    c3.metric(
        "📑 Duplicate",
        total_duplicate
    )

    c4.metric(
        "⭐ Data Quality",
        f"{quality}%"
    )

    st.divider()

    # =====================================
    # PROGRESS
    # =====================================

    st.subheader("📈 Data Quality Score")

    st.progress(quality/100)

    if quality == 100:

        st.success("Dataset berada dalam kondisi **Sangat Baik** dan siap dianalisis.")

    elif quality >=80:

        st.warning("Dataset cukup baik tetapi masih memerlukan perbaikan.")

    else:

        st.error("Dataset masih memiliki banyak masalah kualitas data.")

    st.divider()

    # =====================================
    # CEK MISSING & DUPLIKAT
    # =====================================

    kiri,kanan = st.columns(2)

    with kiri:

        st.subheader("❌ Missing Value")

        missing = pd.DataFrame({

            "Kolom":df.columns,

            "Missing":df.isnull().sum().values

        })

        fig = px.bar(

            missing,

            x="Kolom",

            y="Missing",

            color="Missing",

            color_continuous_scale="Greens"

        )

        fig.update_layout(

            template="plotly_white",

            height=400

        )

        st.plotly_chart(fig,use_container_width=True)

    with kanan:

        st.subheader("📑 Duplicate")

        duplicate_df = pd.DataFrame({

            "Status":["Duplicate","Normal"],

            "Jumlah":[

                total_duplicate,

                len(df)-total_duplicate

            ]

        })

        fig = px.pie(

            duplicate_df,

            values="Jumlah",

            names="Status",

            hole=.6,

            color_discrete_sequence=["#ef5350","#43A047"]

        )

        fig.update_layout(height=400)

        st.plotly_chart(fig,use_container_width=True)

    st.divider()

    # =====================================
    # OUTLIER
    # =====================================

    st.subheader("📊 Outlier Detection")

    pilih = st.selectbox(

        "Pilih Komoditas",

        numeric_cols,

        key="outlier"

    )

    fig = px.box(

        df,

        y=pilih,

        color_discrete_sequence=["#2E7D32"]

    )

    fig.update_layout(

        template="plotly_white",

        height=500

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # Hitung Outlier

    q1 = df[pilih].quantile(.25)
    q3 = df[pilih].quantile(.75)

    iqr = q3-q1

    bawah = q1-1.5*iqr
    atas = q3+1.5*iqr

    outlier = df[
        (df[pilih]<bawah) |
        (df[pilih]>atas)
    ]

    st.info(
        f"Jumlah Outlier pada **{pilih}** : **{len(outlier)} provinsi**"
    )

    st.divider()

    # =====================================
    # DATA TYPES
    # =====================================

    st.subheader("📚 Tipe Data")

    dtype = pd.DataFrame({

        "Kolom":df.columns,

        "Tipe":df.dtypes.astype(str)

    })

    st.dataframe(

        dtype,

        use_container_width=True,

        hide_index=True

    )

    st.divider()

    # =====================================
    # KESIMPULAN
    # =====================================

    st.markdown("""

<div class="insight">

<h4>✅ Kesimpulan Data Cleaning</h4>

<ul>

<li>Tidak ditemukan missing value.</li>

<li>Tidak ditemukan data duplikat.</li>

<li>Tipe data seluruh variabel sudah sesuai.</li>

<li>Outlier dipertahankan karena merupakan karakteristik produksi nyata antar provinsi.</li>

<li>Dataset layak digunakan untuk analisis statistik maupun machine learning.</li>

</ul>

</div>

""",unsafe_allow_html=True)
    # ==========================================================
# EXPLORATORY DATA ANALYSIS
# ==========================================================

elif menu == "📈 Exploratory Data":

    st.markdown("""
    <div class="hero">
        <h2>📈 Exploratory Data Analysis</h2>
        <p>Eksplorasi pola distribusi, hubungan antar variabel, serta karakteristik data produksi perkebunan Indonesia.</p>
    </div>
    """, unsafe_allow_html=True)

    kom = st.selectbox(
        "🌱 Pilih Komoditas",
        numeric_cols
    )

    st.divider()

    col1,col2 = st.columns(2)

    # ==========================================
    # HISTOGRAM
    # ==========================================

    with col1:

        st.subheader("Histogram")

        fig = px.histogram(
            df,
            x=kom,
            nbins=15,
            color_discrete_sequence=["#2E7D32"]
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # ==========================================
    # BOXPLOT
    # ==========================================

    with col2:

        st.subheader("Boxplot")

        fig = px.box(
            df,
            y=kom,
            color_discrete_sequence=["#66BB6A"]
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # ==========================================
    # SCATTER
    # ==========================================

    kiri,kanan = st.columns(2)

    with kiri:

        x = st.selectbox(
            "Variabel X",
            numeric_cols,
            key="x1"
        )

    with kanan:

        y = st.selectbox(
            "Variabel Y",
            numeric_cols,
            index=1,
            key="y1"
        )

    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=y,
        trendline="ols",
        color_continuous_scale="Greens"
    )

    fig.update_layout(
        template="plotly_white",
        height=550
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # BAR
    # ==========================================

    st.subheader("Top Produksi")

    top = df.sort_values(
        kom,
        ascending=False
    ).head(top_n)

    fig = px.bar(
        top,
        x="Provinsi",
        y=kom,
        color=kom,
        color_continuous_scale="Greens"
    )

    fig.update_layout(
        template="plotly_white",
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # PIE
    # ==========================================

    st.subheader("Persentase Top 10")

    pie = top[["Provinsi",kom]]

    fig = px.pie(
        pie,
        values=kom,
        names="Provinsi",
        hole=.55
    )

    fig.update_layout(
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # HEATMAP
    # ==========================================

    st.subheader("Korelasi Antar Komoditas")

    corr = df[numeric_cols].corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="Greens",
        aspect="auto"
    )

    fig.update_layout(
        height=650
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ==========================================
    # STATISTIK
    # ==========================================

    st.subheader("Ringkasan Statistik")

    statistik = pd.DataFrame({

        "Mean":df[numeric_cols].mean(),

        "Median":df[numeric_cols].median(),

        "Std":df[numeric_cols].std(),

        "Minimum":df[numeric_cols].min(),

        "Maximum":df[numeric_cols].max()

    }).round(2)

    st.dataframe(
        statistik,
        use_container_width=True
    )

    st.divider()

    st.markdown("""

<div class="insight">

<h4>📌 Insight Hasil EDA</h4>

<ul>

<li>Distribusi sebagian besar komoditas bersifat right-skewed.</li>

<li>Kelapa Sawit merupakan komoditas dengan variasi produksi paling tinggi.</li>

<li>Sebagian besar provinsi memiliki produksi rendah dibanding provinsi sentra.</li>

<li>Terdapat beberapa hubungan positif antar komoditas yang dapat dimanfaatkan dalam pemodelan.</li>

</ul>

</div>

""",unsafe_allow_html=True)
