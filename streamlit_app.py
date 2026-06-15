import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ==========================================================
# KONFIGURASI HALAMAN
# ==========================================================
st.set_page_config(
    page_title="LPK Kadar Fe | Kelompok 5",
    page_icon="💧",
    layout="wide"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Header utama */
    .header-box {
        background: linear-gradient(135deg, #0f4c75 0%, #1b6ca8 50%, #1e90ff 100%);
        border-radius: 16px;
        padding: 32px 36px;
        margin-bottom: 28px;
        color: white;
        box-shadow: 0 8px 32px rgba(15,76,117,0.25);
    }
    .header-box h1 {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0 0 4px 0;
        letter-spacing: -0.5px;
    }
    .header-box p {
        font-size: 0.97rem;
        opacity: 0.85;
        margin: 0;
    }

    /* Card anggota */
    .team-grid {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 12px;
        margin-bottom: 8px;
    }
    .team-card {
        background: #f0f7ff;
        border: 1.5px solid #c3dffe;
        border-radius: 12px;
        padding: 14px 12px;
        text-align: center;
    }
    .team-card .avatar {
        width: 44px;
        height: 44px;
        background: linear-gradient(135deg, #1b6ca8, #1e90ff);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 8px;
        font-size: 1.1rem;
        color: white;
        font-weight: 700;
    }
    .team-card .name {
        font-size: 0.78rem;
        font-weight: 600;
        color: #0f4c75;
        line-height: 1.3;
    }
    .team-card .nim {
        font-size: 0.72rem;
        color: #5a7fa8;
        margin-top: 3px;
    }

    /* Section label */
    .section-label {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #1b6ca8;
        margin-bottom: 6px;
    }

    /* Metric card custom */
    .metric-row {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
        margin: 16px 0;
    }
    .metric-card {
        background: white;
        border: 1.5px solid #e2edf7;
        border-radius: 12px;
        padding: 18px 20px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .metric-card .label {
        font-size: 0.75rem;
        color: #7a9bbf;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    .metric-card .value {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.7rem;
        font-weight: 700;
        color: #0f4c75;
        margin-top: 2px;
    }
    .metric-card .sub {
        font-size: 0.72rem;
        color: #a0b8cc;
        margin-top: 2px;
    }

    /* Status badge */
    .badge-aman {
        background: #d4edda;
        color: #1a6b35;
        border: 1.5px solid #a8d5b5;
        border-radius: 20px;
        padding: 3px 12px;
        font-size: 0.78rem;
        font-weight: 600;
    }
    .badge-tidak {
        background: #fde8e8;
        color: #a01a1a;
        border: 1.5px solid #f3b0b0;
        border-radius: 20px;
        padding: 3px 12px;
        font-size: 0.78rem;
        font-weight: 600;
    }

    /* Divider */
    .divider {
        border: none;
        border-top: 2px solid #e8f1fb;
        margin: 28px 0;
    }

    /* Info box */
    .info-box {
        background: #eef5ff;
        border-left: 4px solid #1b6ca8;
        border-radius: 0 10px 10px 0;
        padding: 14px 18px;
        margin: 12px 0;
        font-size: 0.88rem;
        color: #1a3a55;
    }

    /* Rumus box */
    .rumus-box {
        background: #fff8e1;
        border: 1.5px solid #ffe082;
        border-radius: 10px;
        padding: 16px 20px;
        font-size: 0.9rem;
        color: #5a4200;
        margin: 10px 0;
    }

    /* Footer */
    .footer {
        text-align: center;
        font-size: 0.78rem;
        color: #a0b8cc;
        margin-top: 32px;
        padding: 16px;
        border-top: 1.5px solid #e8f1fb;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: #f7fbff;
    }

    /* Hide default streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================
st.markdown("""
<div class="header-box">
    <h1>💧 Laporan Praktik Kerja (LPK)</h1>
    <p>Penentuan Kadar Besi (Fe) dalam Air menggunakan Metode Spektrofotometri UV-Vis</p>
    <p style="margin-top:6px; font-size:0.85rem; opacity:0.7;">
        Politeknik AKA Bogor · Program Studi Pengolahan Limbah Industri · Kelas 1F
    </p>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# ANGGOTA KELOMPOK
# ==========================================================
st.markdown('<div class="section-label">Anggota Kelompok 5</div>', unsafe_allow_html=True)

anggota = [
    ("Daffa Attahilah Pratikyo", "2530604", "D"),
    ("Dicky Afriansyah",         "2530608", "Di"),
    ("Fajrian Pasya",            "2530612", "F"),
    ("Much Harun Al Rasyid",     "2530628", "H"),
    ("Muhammad Dzaki Al Fatih",  "2530631", "Dz"),
]

cols = st.columns(5)
for i, (nama, nim, inisial) in enumerate(anggota):
    with cols[i]:
        st.markdown(f"""
        <div class="team-card">
            <div class="avatar">{inisial}</div>
            <div class="name">{nama}</div>
            <div class="nim">{nim}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ==========================================================
# SIDEBAR — PENGATURAN
# ==========================================================
with st.sidebar:
    st.markdown("### ⚙️ Pengaturan")
    st.markdown("---")

    st.markdown("**Faktor Pengenceran**")
    fp = st.number_input("FP", value=2.0, step=0.5, min_value=1.0, label_visibility="collapsed")

    st.markdown("---")
    st.markdown("**Baku Mutu (mg/L)**")

    bm_minum  = st.number_input("Air Minum (Permenkes 492/2010)",  value=0.3, step=0.1, format="%.2f")
    bm_bersih = st.number_input("Air Bersih (Permenkes 416/1990)", value=1.0, step=0.1, format="%.2f")
    bm_sungai = st.number_input("Air Sungai (PP 82/2001 Kls II)", value=0.3, step=0.1, format="%.2f")

    st.markdown("---")
    st.markdown("**Referensi Metode**")
    st.info("SNI 6989.4:2009\nSpektrofotometri UV-Vis\nλ = 510 nm\nPereaksi: 1,10-Fenantrolin")

    st.markdown("---")
    st.caption("© Kelompok 5 · Kelas 1F · 2024/2025")

# ==========================================================
# LAYOUT UTAMA — DUA KOLOM
# ==========================================================
col_kiri, col_kanan = st.columns([1.05, 1], gap="large")

# ── KOLOM KIRI: KURVA KALIBRASI ──
with col_kiri:
    st.markdown('<div class="section-label">A. Kurva Kalibrasi</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        Masukkan data absorbansi larutan standar Fe dari hasil pengukuran spektrofotometer.
        Klik baris terakhir untuk menambah data baru.
    </div>
    """, unsafe_allow_html=True)

    kalibrasi_default = pd.DataFrame({
        "Konsentrasi (mg/L)": [0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
        "Absorbansi (AU)":    [0.000, 0.085, 0.172, 0.258, 0.341, 0.430]
    })

    df_kal = st.data_editor(
        kalibrasi_default,
        num_rows="dynamic",
        key="kal",
        use_container_width=True,
        column_config={
            "Konsentrasi (mg/L)": st.column_config.NumberColumn(format="%.3f"),
            "Absorbansi (AU)":    st.column_config.NumberColumn(format="%.4f"),
        }
    )

    # ── REGRESI LINEAR ──
    df_kal_clean = df_kal.dropna()
    x = df_kal_clean["Konsentrasi (mg/L)"].values.astype(float)
    y = df_kal_clean["Absorbansi (AU)"].values.astype(float)

    n      = len(x)
    sum_x  = np.sum(x)
    sum_y  = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x ** 2)

    denom_m = (n * sum_x2 - sum_x ** 2)
    if denom_m != 0:
        m = (n * sum_xy - sum_x * sum_y) / denom_m
        b = (sum_y - m * sum_x) / n
    else:
        m, b = 0, 0

    mean_x = np.mean(x)
    mean_y = np.mean(y)
    num = np.sum((x - mean_x) * (y - mean_y))
    den = np.sqrt(np.sum((x - mean_x)**2) * np.sum((y - mean_y)**2))
    r   = num / den if den != 0 else 0
    r2  = r ** 2

    # Metric cards
    st.markdown(f"""
    <div class="metric-row">
        <div class="metric-card">
            <div class="label">Slope (m)</div>
            <div class="value">{m:.4f}</div>
            <div class="sub">AU·L/mg</div>
        </div>
        <div class="metric-card">
            <div class="label">Intercept (b)</div>
            <div class="value">{b:.4f}</div>
            <div class="sub">AU</div>
        </div>
        <div class="metric-card">
            <div class="label">R²</div>
            <div class="value">{r2:.5f}</div>
            <div class="sub">{'✅ Baik (>0.999)' if r2>=0.999 else '⚠️ Periksa data'}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Persamaan regresi
    sign = "+" if b >= 0 else "-"
    st.markdown(f"""
    <div class="rumus-box">
        📐 <strong>Persamaan Regresi:</strong> &nbsp; y = {m:.4f}x {sign} {abs(b):.4f}<br>
        &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
        &nbsp; A = {m:.4f} · C {sign} {abs(b):.4f}<br><br>
        📌 <strong>Persamaan Balik (C = ?):</strong><br>
        &nbsp; C (mg/L) = (A − {b:.4f}) / {m:.4f}
    </div>
    """, unsafe_allow_html=True)

    # Grafik kurva kalibrasi
    fig, ax = plt.subplots(figsize=(6, 3.8))
    fig.patch.set_facecolor('#f7fbff')
    ax.set_facecolor('#f7fbff')

    x_line = np.linspace(min(x), max(x), 200)
    y_line = m * x_line + b

    ax.scatter(x, y, color='#1b6ca8', s=55, zorder=5, label='Data Standar', edgecolors='white', linewidths=1.2)
    ax.plot(x_line, y_line, color='#e74c3c', linewidth=2, label=f'y = {m:.4f}x {"+" if b>=0 else ""}{b:.4f}')

    ax.set_xlabel("Konsentrasi Fe (mg/L)", fontsize=9, color='#3a5a7a')
    ax.set_ylabel("Absorbansi (AU)", fontsize=9, color='#3a5a7a')
    ax.set_title(f"Kurva Kalibrasi Fe  |  R² = {r2:.5f}", fontsize=10, fontweight='bold', color='#0f4c75', pad=10)
    ax.legend(fontsize=8, framealpha=0.7)
    ax.tick_params(labelsize=8, colors='#5a7a9a')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#c5d8e8')
    ax.spines['bottom'].set_color('#c5d8e8')
    ax.grid(True, alpha=0.3, color='#c5d8e8', linestyle='--')

    plt.tight_layout()
    st.pyplot(fig, use_container_width=True)
    plt.close()

# ── KOLOM KANAN: SAMPEL & HASIL ──
with col_kanan:
    st.markdown('<div class="section-label">B. Data Sampel Air</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        Masukkan absorbansi sampel yang telah diukur. Pilih kategori sesuai jenis air
        untuk penentuan baku mutu yang tepat.
    </div>
    """, unsafe_allow_html=True)

    sampel_default = pd.DataFrame({
        "Nama Sampel": ["Air Sumur", "Air Sungai Ciliwung", "Air PDAM"],
        "Absorbansi":  [0.215, 0.318, 0.042],
        "Kategori":    ["Air Bersih", "Air Sungai", "Air Minum"]
    })

    df_samp = st.data_editor(
        sampel_default,
        num_rows="dynamic",
        key="samp",
        use_container_width=True,
        column_config={
            "Nama Sampel": st.column_config.TextColumn(),
            "Absorbansi":  st.column_config.NumberColumn(format="%.4f"),
            "Kategori":    st.column_config.SelectboxColumn(
                options=["Air Minum", "Air Bersih", "Air Sungai"]
            ),
        }
    )

    st.markdown('<hr class="divider" style="margin:18px 0;">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">C. Hasil Perhitungan Kadar Fe</div>', unsafe_allow_html=True)

    # ── PERHITUNGAN ──
    hasil = []
    for i in range(len(df_samp)):
        try:
            nama   = df_samp.loc[i, "Nama Sampel"]
            absorb = float(df_samp.loc[i, "Absorbansi"])
            kat    = df_samp.loc[i, "Kategori"]

            # Konsentrasi terukur dari kurva kalibrasi
            c_ter = (absorb - b) / m if m != 0 else 0
            # Konsentrasi aktual (koreksi pengenceran)
            c_akt = c_ter * fp

            # Pilih baku mutu
            if "Minum" in str(kat):
                bm      = bm_minum
                ref     = "Permenkes 492/2010"
            elif "Sungai" in str(kat):
                bm      = bm_sungai
                ref     = "PP 82/2001 Kls II"
            else:
                bm      = bm_bersih
                ref     = "Permenkes 416/1990"

            # % terhadap baku mutu
            persen_bm = (c_akt / bm * 100) if bm > 0 else 0
            status    = "AMAN" if c_akt <= bm else "TIDAK AMAN"

            hasil.append({
                "Nama Sampel":     nama,
                "Absorbansi":      absorb,
                "C terukur (mg/L)": round(c_ter, 4),
                "FP":              fp,
                "Kadar Fe (mg/L)": round(c_akt, 4),
                "Baku Mutu":       bm,
                "Referensi BM":    ref,
                "% BM":            round(persen_bm, 1),
                "Status":          status,
            })
        except Exception:
            continue

    if hasil:
        df_hasil = pd.DataFrame(hasil)

        # Tampilkan tabel hasil
        st.dataframe(
            df_hasil[[
                "Nama Sampel", "Absorbansi",
                "C terukur (mg/L)", "Kadar Fe (mg/L)",
                "Baku Mutu", "% BM", "Status"
            ]],
            use_container_width=True,
            hide_index=True,
            column_config={
                "% BM":            st.column_config.ProgressColumn(
                    "% thd BM", min_value=0, max_value=200, format="%.1f%%"
                ),
                "Kadar Fe (mg/L)": st.column_config.NumberColumn(format="%.4f mg/L"),
                "Absorbansi":      st.column_config.NumberColumn(format="%.4f"),
            }
        )

        # Grafik batang perbandingan kadar vs BM
        fig2, ax2 = plt.subplots(figsize=(6, 3.6))
        fig2.patch.set_facecolor('#f7fbff')
        ax2.set_facecolor('#f7fbff')

        names  = df_hasil["Nama Sampel"].tolist()
        kadar  = df_hasil["Kadar Fe (mg/L)"].tolist()
        bm_val = df_hasil["Baku Mutu"].tolist()
        colors = ['#2ecc71' if s == "AMAN" else '#e74c3c'
                  for s in df_hasil["Status"]]

        x_pos = np.arange(len(names))
        bars  = ax2.bar(x_pos, kadar, width=0.45, color=colors,
                        alpha=0.85, zorder=3, label='Kadar Fe Sampel',
                        edgecolor='white', linewidth=1.2)

        for i, (bar, bm_i) in enumerate(zip(bars, bm_val)):
            ax2.hlines(bm_i, bar.get_x() - 0.05, bar.get_x() + bar.get_width() + 0.05,
                       colors='#f39c12', linewidths=2, linestyles='--', zorder=4)
            ax2.text(bar.get_x() + bar.get_width() / 2,
                     bar.get_height() + 0.005,
                     f"{bar.get_height():.4f}", ha='center', va='bottom',
                     fontsize=8, fontweight='bold',
                     color='#1a6b35' if colors[i] == '#2ecc71' else '#a01a1a')

        from matplotlib.lines import Line2D
        legend_els = [
            Line2D([0], [0], color='#f39c12', linewidth=2, linestyle='--', label='Baku Mutu'),
            plt.Rectangle((0,0), 1, 1, color='#2ecc71', alpha=0.85, label='Aman'),
            plt.Rectangle((0,0), 1, 1, color='#e74c3c', alpha=0.85, label='Tidak Aman'),
        ]
        ax2.legend(handles=legend_els, fontsize=8, framealpha=0.7)

        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(names, fontsize=8.5, color='#3a5a7a')
        ax2.set_ylabel("Konsentrasi Fe (mg/L)", fontsize=9, color='#3a5a7a')
        ax2.set_title("Perbandingan Kadar Fe vs Baku Mutu", fontsize=10,
                      fontweight='bold', color='#0f4c75', pad=10)
        ax2.tick_params(labelsize=8, colors='#5a7a9a')
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.spines['left'].set_color('#c5d8e8')
        ax2.spines['bottom'].set_color('#c5d8e8')
        ax2.grid(axis='y', alpha=0.3, color='#c5d8e8', linestyle='--')
        ax2.set_ylim(0, max(max(kadar), max(bm_val)) * 1.35 if kadar else 1)

        plt.tight_layout()
        st.pyplot(fig2, use_container_width=True)
        plt.close()

# ==========================================================
# SECTION D — LANGKAH PERHITUNGAN MANUAL
# ==========================================================
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown('<div class="section-label">D. Langkah Perhitungan Detail</div>', unsafe_allow_html=True)

if hasil:
    tab_names = [r["Nama Sampel"] for r in hasil]
    tabs = st.tabs(tab_names)

    for tab, r in zip(tabs, hasil):
        with tab:
            col_r1, col_r2 = st.columns(2)
            with col_r1:
                st.markdown(f"""
                <div class="rumus-box">
                <strong>📋 Data Input</strong><br>
                • Absorbansi (A) = <b>{r['Absorbansi']:.4f} AU</b><br>
                • Slope (m) = <b>{m:.4f}</b><br>
                • Intercept (b) = <b>{b:.4f}</b><br>
                • Faktor Pengenceran = <b>{fp}</b><br>
                • Kategori = <b>{df_samp.loc[list(df_hasil["Nama Sampel"]).index(r["Nama Sampel"]), "Kategori"]}</b>
                </div>
                """, unsafe_allow_html=True)
            with col_r2:
                st.markdown(f"""
                <div class="rumus-box">
                <strong>🧮 Langkah Perhitungan</strong><br>
                <b>Step 1 — Konsentrasi Terukur:</b><br>
                C = (A − b) / m<br>
                C = ({r['Absorbansi']:.4f} − {b:.4f}) / {m:.4f}<br>
                C = <b>{r['C terukur (mg/L)']:.4f} mg/L</b><br><br>
                <b>Step 2 — Koreksi Pengenceran:</b><br>
                C aktual = C × FP<br>
                C aktual = {r['C terukur (mg/L)']:.4f} × {fp}<br>
                C aktual = <b>{r['Kadar Fe (mg/L)']:.4f} mg/L</b><br><br>
                <b>Step 3 — Bandingkan Baku Mutu:</b><br>
                BM ({r['Referensi BM']}) = {r['Baku Mutu']} mg/L<br>
                {r['Kadar Fe (mg/L)']:.4f} {'≤' if r['Status']=='AMAN' else '>'} {r['Baku Mutu']} mg/L
                → <b>{r['Status']}</b>
                </div>
                """, unsafe_allow_html=True)

# ==========================================================
# SECTION E — KESIMPULAN
# ==========================================================
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown('<div class="section-label">E. Kesimpulan</div>', unsafe_allow_html=True)

if hasil:
    col_k = st.columns(len(hasil))
    for col, r in zip(col_k, hasil):
        with col:
            if r["Status"] == "AMAN":
                st.success(f"""
                **✅ {r['Nama Sampel']}**

                Kadar Fe: **{r['Kadar Fe (mg/L)']} mg/L**

                Baku Mutu: {r['Baku Mutu']} mg/L

                **{r['% BM']}% dari BM**

                *Memenuhi {r['Referensi BM']}*
                """)
            else:
                st.error(f"""
                **❌ {r['Nama Sampel']}**

                Kadar Fe: **{r['Kadar Fe (mg/L)']} mg/L**

                Baku Mutu: {r['Baku Mutu']} mg/L

                **{r['% BM']}% dari BM**

                *Melebihi {r['Referensi BM']}*
                """)

    # Ringkasan teks
    aman_list  = [r["Nama Sampel"] for r in hasil if r["Status"] == "AMAN"]
    tidak_list = [r["Nama Sampel"] for r in hasil if r["Status"] != "AMAN"]

    st.markdown("---")
    if tidak_list:
        st.warning(
            f"⚠️ **{', '.join(tidak_list)}** memiliki kadar Fe di atas baku mutu yang berlaku "
            f"dan **tidak layak digunakan** sesuai peruntukannya tanpa pengolahan lebih lanjut."
        )
    if aman_list:
        st.info(
            f"ℹ️ **{', '.join(aman_list)}** memiliki kadar Fe yang masih dalam ambang batas "
            f"baku mutu yang berlaku."
        )

# ==========================================================
# FOOTER
# ==========================================================
st.markdown("""
<div class="footer">
    LPK Penentuan Kadar Besi (Fe) · Metode Spektrofotometri UV-Vis (SNI 6989.4:2009)<br>
    Kelompok 5 · Kelas 1F · Politeknik AKA Bogor · 2024/2025
</div>
""", unsafe_allow_html=True)
