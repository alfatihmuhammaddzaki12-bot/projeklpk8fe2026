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
