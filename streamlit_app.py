import streamlit as st
import pandas as pd
import numpy as np

# ==========================================================
# KONFIGURASI
# ==========================================================
st.set_page_config(page_title="LPK Kadar Fe", page_icon="💧", layout="wide")

# CSS Kustom
st.markdown("""
<style>
    .header-box {
        background: linear-gradient(135deg, #1a5276, #2980b9);
        color: white;
        padding: 24px 28px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .header-box h1 { margin: 0 0 4px 0; font-size: 1.8rem; }
    .header-box p  { margin: 0; opacity: 0.85; font-size: 0.95rem; }

    .anggota-box {
        background: #eaf4fb;
        border-left: 5px solid #2980b9;
        padding: 14px 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        font-size: 0.92rem;
    }
    .anggota-box b { color: #1a5276; }

    .rumus-box {
        background: #fdfefe;
        border: 1px solid #d5dbdb;
        border-radius: 10px;
        padding: 16px 20px;
        margin-bottom: 16px;
    }
    .rumus-box h4 { color: #1a5276; margin-top: 0; }

    .bm-table th { background-color: #2980b9 !important; color: white !important; }
    .status-aman    { color: #1e8449; font-weight: bold; }
    .status-tidak   { color: #c0392b; font-weight: bold; }

    .section-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1a5276;
        border-bottom: 2px solid #2980b9;
        padding-bottom: 6px;
        margin-bottom: 14px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================
st.markdown("""
<div class="header-box">
    <h1>💧 Laporan Praktikum Kimia (LPK)</h1>
    <p>Analisis Kadar Besi (Fe) pada Sampel Air — Metode Spektrofotometri</p>
</div>
""", unsafe_allow_html=True)

# Anggota Kelompok
st.markdown("""
<div class="anggota-box">
    <b>👥 Anggota Kelompok:</b><br>
    1. Daffa Attahilah Pratikyo &nbsp;— 2530604 &nbsp;|&nbsp;
    2. Dicky Afriansyah &nbsp;— 2530608 &nbsp;|&nbsp;
    3. Fajrian Pasya &nbsp;— 2530612<br>
    4. Much Harun Al Rasyid &nbsp;— 2530628 &nbsp;|&nbsp;
    5. Muhammad Dzaki Al Fatih &nbsp;— 2530631
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================================================
# SIDEBAR
# ==========================================================
st.sidebar.header("⚙️ Pengaturan")
fp = st.sidebar.number_input("Faktor Pengenceran (FP)", value=2.0, step=0.5, min_value=1.0)
st.sidebar.markdown("---")
st.sidebar.subheader("📋 Baku Mutu (mg/L)")
bm_minum  = st.sidebar.number_input("Air Minum  (PerMenKes 492/2010)",  value=0.3, step=0.1)
bm_bersih = st.sidebar.number_input("Air Bersih (PerMenKes 416/1990)", value=1.0, step=0.1)
bm_sungai = st.sidebar.number_input("Air Sungai (PP 22/2021 Kelas II)", value=0.3, step=0.1)
st.sidebar.markdown("---")
st.sidebar.info("Ubah nilai di atas untuk menyesuaikan parameter analisis.")

# ==========================================================
# LANDASAN TEORI & RUMUS
# ==========================================================
with st.expander("📖 Landasan Teori & Rumus Perhitungan", expanded=True):

    col_t1, col_t2 = st.columns(2)

    with col_t1:
        st.markdown("""
        <div class="rumus-box">
            <h4>📐 1. Persamaan Regresi Linear (Kurva Kalibrasi)</h4>
            <b>y = m·x + b</b><br><br>
            <b>Slope (m):</b><br>
            m = (n·Σxy − Σx·Σy) / (n·Σx² − (Σx)²)<br><br>
            <b>Intercept (b):</b><br>
            b = (Σy − m·Σx) / n<br><br>
            <b>Koefisien Korelasi (r):</b><br>
            r = Σ[(x−x̄)(y−ȳ)] / √[Σ(x−x̄)²·Σ(y−ȳ)²]<br><br>
            <b>Koefisien Determinasi:</b><br>
            R² = r²
        </div>
        """, unsafe_allow_html=True)

    with col_t2:
        st.markdown("""
        <div class="rumus-box">
            <h4>🧪 2. Perhitungan Kadar Fe Sampel</h4>
            <b>Konsentrasi Terukur (C<sub>terukur</sub>):</b><br>
            C<sub>terukur</sub> = (A<sub>sampel</sub> − b) / m<br><br>
            &nbsp;&nbsp;A<sub>sampel</sub> = Absorbansi sampel (AU)<br>
            &nbsp;&nbsp;m = slope kurva kalibrasi<br>
            &nbsp;&nbsp;b = intercept kurva kalibrasi<br><br>
            <b>Konsentrasi Aktual (C<sub>aktual</sub>):</b><br>
            C<sub>aktual</sub> = C<sub>terukur</sub> × FP<br><br>
            &nbsp;&nbsp;FP = Faktor Pengenceran
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="rumus-box">
        <h4>📏 3. Baku Mutu Kadar Besi (Fe) di Indonesia</h4>
    </div>
    """, unsafe_allow_html=True)

    bm_ref = pd.DataFrame({
        "Jenis Air": ["Air Minum", "Air Bersih", "Air Sungai (Kelas II)"],
        "Regulasi": [
            "PerMenKes No. 492 Tahun 2010",
            "PerMenKes No. 416 Tahun 1990",
            "PP No. 22 Tahun 2021"
        ],
        "Batas Maksimum Fe (mg/L)": [0.3, 1.0, 0.3],
        "Parameter": ["Kadar Fe terlarut", "Kadar Fe terlarut", "Kadar Fe terlarut"]
    })
    st.dataframe(bm_ref, use_container_width=True, hide_index=True)

st.markdown("---")

# ==========================================================
# DATA KURVA KALIBRASI
# ==========================================================
st.markdown('<div class="section-title">📊 Data Kurva Kalibrasi</div>', unsafe_allow_html=True)

kalibrasi = pd.DataFrame({
    "Konsentrasi (mg/L)": [0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
    "Absorbansi (AU)":    [0.000, 0.085, 0.172, 0.258, 0.341, 0.430]
})
df_kal = st.data_editor(kalibrasi, num_rows="dynamic", key="kal", use_container_width=True)

# ==========================================================
# REGRESI LINEAR
# ==========================================================
x = df_kal["Konsentrasi (mg/L)"].dropna().values
y = df_kal["Absorbansi (AU)"].dropna().values

# Pastikan panjang sama
min_len = min(len(x), len(y))
x, y = x[:min_len], y[:min_len]

n = len(x)
sum_x  = np.sum(x)
sum_y  = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x ** 2)

denom_m = (n * sum_x2 - sum_x ** 2)
m = (n * sum_xy - sum_x * sum_y) / denom_m if denom_m != 0 else 0
b = (sum_y - m * sum_x) / n

mean_x = np.mean(x)
mean_y = np.mean(y)
num_r  = np.sum((x - mean_x) * (y - mean_y))
den_r  = np.sqrt(np.sum((x - mean_x) ** 2) * np.sum((y - mean_y) ** 2))
r      = num_r / den_r if den_r != 0 else 0
r2     = r ** 2

st.markdown("#### 📈 Hasil Regresi Linear")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Slope (m)",      f"{m:.4f}")
col2.metric("Intercept (b)",  f"{b:.4f}")
col3.metric("r (Korelasi)",   f"{r:.5f}")
col4.metric("R² (Determinasi)", f"{r2:.5f}")

# Persamaan
st.info(f"**Persamaan Kurva Kalibrasi:** y = {m:.4f}x + ({b:.4f})")

if r2 >= 0.999:
    st.success(f"✅ R² = {r2:.5f} — Linearitas sangat baik (R² ≥ 0,999)")
elif r2 >= 0.99:
    st.warning(f"⚠️ R² = {r2:.5f} — Linearitas baik (0,99 ≤ R² < 0,999)")
else:
    st.error(f"❌ R² = {r2:.5f} — Linearitas kurang memenuhi syarat (R² < 0,99)")

# Tabel perhitungan regresi rinci
with st.expander("🔢 Tabel Perhitungan Regresi (Detail)"):
    df_reg = pd.DataFrame({
        "x (Konsentrasi)": x,
        "y (Absorbansi)":  y,
        "x·y":             np.round(x * y, 6),
        "x²":              np.round(x ** 2, 6),
        "ŷ (y prediksi)":  np.round(m * x + b, 6),
        "Residual (y−ŷ)":  np.round(y - (m * x + b), 6),
    })
    st.dataframe(df_reg, use_container_width=True, hide_index=True)
    st.markdown(f"""
    **Σx** = {sum_x:.4f} &nbsp;|&nbsp;
    **Σy** = {sum_y:.4f} &nbsp;|&nbsp;
    **Σxy** = {sum_xy:.4f} &nbsp;|&nbsp;
    **Σx²** = {sum_x2:.4f} &nbsp;|&nbsp;
    **n** = {n}
    """)

st.markdown("---")

# ==========================================================
# DATA SAMPEL
# ==========================================================
st.markdown('<div class="section-title">🧪 Data Sampel</div>', unsafe_allow_html=True)

sampel = pd.DataFrame({
    "Nama Sampel": ["Air Sumur", "Air Sungai", "Air PDAM"],
    "Absorbansi":  [0.215, 0.318, 0.042],
    "Kategori":    ["Air Bersih", "Air Sungai", "Air Minum"]
})
df_samp = st.data_editor(sampel, num_rows="dynamic", key="samp", use_container_width=True)

# ==========================================================
# HASIL PERHITUNGAN
# ==========================================================
st.markdown("---")
st.markdown('<div class="section-title">📋 Hasil Perhitungan Kadar Fe</div>', unsafe_allow_html=True)

hasil = []
for i in range(len(df_samp)):
    try:
        nama   = df_samp.loc[i, "Nama Sampel"]
        absorb = float(df_samp.loc[i, "Absorbansi"])
        kat    = df_samp.loc[i, "Kategori"]

        c_ter  = (absorb - b) / m if m != 0 else 0
        c_akt  = c_ter * fp

        if "Minum" in str(kat):
            bm = bm_minum
        elif "Sungai" in str(kat):
            bm = bm_sungai
        else:
            bm = bm_bersih

        status = "✅ AMAN" if c_akt <= bm else "❌ TIDAK AMAN"
        persen = (c_akt / bm * 100) if bm != 0 else 0

        hasil.append({
            "No.":                i + 1,
            "Nama Sampel":        nama,
            "Kategori":           kat,
            "Absorbansi (A)":     round(absorb, 4),
            "C_terukur (mg/L)":   round(c_ter, 4),
            "FP":                 fp,
            "C_aktual (mg/L)":    round(c_akt, 4),
            "Baku Mutu (mg/L)":   bm,
            "% thd Baku Mutu":    round(persen, 2),
            "Status":             status
        })
    except Exception:
        pass

df_hasil = pd.DataFrame(hasil)

# Tampilkan tabel hasil
st.dataframe(df_hasil, use_container_width=True, hide_index=True)

# ==========================================================
# LANGKAH PERHITUNGAN MANUAL (TRANSPARAN)
# ==========================================================
with st.expander("🔍 Detail Langkah Perhitungan Per Sampel"):
    for row in hasil:
        absorb = row["Absorbansi (A)"]
        c_ter  = row["C_terukur (mg/L)"]
        c_akt  = row["C_aktual (mg/L)"]
        bm_val = row["Baku Mutu (mg/L)"]

        st.markdown(f"**{row['No.']}. {row['Nama Sampel']} ({row['Kategori']})**")
        st.markdown(f"""
        - Absorbansi sampel (A) = **{absorb}** AU
        - Kurva kalibrasi: y = {m:.4f}x + ({b:.4f})
        - C_terukur = (A − b) / m = ({absorb} − ({b:.4f})) / {m:.4f} = **{c_ter:.4f} mg/L**
        - C_aktual = C_terukur × FP = {c_ter:.4f} × {fp} = **{c_akt:.4f} mg/L**
        - Baku Mutu ({row['Kategori']}) = **{bm_val} mg/L**
        - Perbandingan: {c_akt:.4f} {'≤' if c_akt <= bm_val else '>'} {bm_val} → **{row['Status']}**
        """)
        st.markdown("---")

# ==========================================================
# GRAFIK KURVA KALIBRASI + POSISI SAMPEL
# ==========================================================
st.markdown('<div class="section-title">📉 Grafik Kurva Kalibrasi</div>', unsafe_allow_html=True)

import streamlit as st

# Data untuk chart
x_line = np.linspace(0, max(x) * 1.1, 100)
y_line = m * x_line + b

chart_data_kalibrasi = pd.DataFrame({
    "Konsentrasi (mg/L)": x,
    "Absorbansi Kalibrasi": y
})
chart_data_fit = pd.DataFrame({
    "Konsentrasi (mg/L)": x_line,
    "Garis Regresi": y_line
})

col_g1, col_g2 = st.columns(2)

with col_g1:
    st.markdown("**Titik Kalibrasi & Garis Regresi**")
    import altair as alt

    scatter = alt.Chart(chart_data_kalibrasi).mark_circle(size=80, color="#2980b9").encode(
        x=alt.X("Konsentrasi (mg/L):Q", title="Konsentrasi (mg/L)"),
        y=alt.Y("Absorbansi Kalibrasi:Q", title="Absorbansi (AU)"),
        tooltip=["Konsentrasi (mg/L)", "Absorbansi Kalibrasi"]
    )
    line = alt.Chart(chart_data_fit).mark_line(color="#e74c3c", strokeWidth=2).encode(
        x="Konsentrasi (mg/L):Q",
        y="Garis Regresi:Q"
    )
    st.altair_chart(scatter + line, use_container_width=True)

with col_g2:
    st.markdown("**Kadar Fe Sampel vs Baku Mutu**")
    sampel_chart = pd.DataFrame({
        "Sampel": [r["Nama Sampel"] for r in hasil],
        "Kadar Fe (mg/L)": [r["C_aktual (mg/L)"] for r in hasil],
        "Baku Mutu": [r["Baku Mutu (mg/L)"] for r in hasil],
    })

    bar = alt.Chart(sampel_chart).mark_bar(color="#2980b9", opacity=0.8).encode(
        x=alt.X("Sampel:N"),
        y=alt.Y("Kadar Fe (mg/L):Q"),
        tooltip=["Sampel", "Kadar Fe (mg/L)", "Baku Mutu"]
    )
    bm_line_chart = alt.Chart(sampel_chart).mark_line(
        color="#e74c3c", strokeDash=[5, 3], strokeWidth=2
    ).encode(
        x="Sampel:N",
        y="Baku Mutu:Q"
    )
    bm_point = alt.Chart(sampel_chart).mark_point(
        color="#e74c3c", shape="triangle-up", size=80
    ).encode(
        x="Sampel:N",
        y="Baku Mutu:Q",
        tooltip=alt.value("Baku Mutu")
    )
    st.altair_chart(bar + bm_line_chart + bm_point, use_container_width=True)
    st.caption("🔴 Garis merah = batas baku mutu masing-masing sampel")

# ==========================================================
# KESIMPULAN
# ==========================================================
st.markdown("---")
st.markdown('<div class="section-title">📝 Kesimpulan</div>', unsafe_allow_html=True)

aman_count   = sum(1 for r in hasil if "AMAN" in r["Status"] and "TIDAK" not in r["Status"])
tidak_count  = sum(1 for r in hasil if "TIDAK" in r["Status"])
total        = len(hasil)

st.markdown(f"""
Berdasarkan analisis spektrofotometri menggunakan kurva kalibrasi dengan persamaan
**y = {m:.4f}x + ({b:.4f})** dan R² = **{r2:.5f}**, diperoleh hasil sebagai berikut:
""")

for row in hasil:
    if "TIDAK" in row["Status"]:
        st.error(
            f"❌ **{row['Nama Sampel']}** ({row['Kategori']}): "
            f"Kadar Fe = **{row['C_aktual (mg/L)']} mg/L** — "
            f"MELEBIHI baku mutu {row['Baku Mutu (mg/L)']} mg/L "
            f"({row['% thd Baku Mutu']}% dari batas)"
        )
    else:
        st.success(
            f"✅ **{row['Nama Sampel']}** ({row['Kategori']}): "
            f"Kadar Fe = **{row['C_aktual (mg/L)']} mg/L** — "
            f"Memenuhi baku mutu {row['Baku Mutu (mg/L)']} mg/L "
            f"({row['% thd Baku Mutu']}% dari batas)"
        )

st.info(
    f"**Ringkasan:** Dari {total} sampel yang dianalisis, "
    f"**{aman_count} sampel memenuhi** baku mutu dan "
    f"**{tidak_count} sampel tidak memenuhi** baku mutu kadar besi (Fe) yang berlaku."
)

st.markdown("---")
st.caption(
    "Laporan Praktikum Kimia | Analisis Kadar Fe — Metode Spektrofotometri | "
    "Kelompok: Daffa Attahilah Pratikyo · Dicky Afriansyah · Fajrian Pasya · "
    "Much Harun Al Rasyid · Muhammad Dzaki Al Fatih"
)
