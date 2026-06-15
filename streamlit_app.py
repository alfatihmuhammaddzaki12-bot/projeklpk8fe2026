# ==========================================================
# IDENTITAS PRAKTIKAN
# ==========================================================
st.subheader("Identitas Praktikan")

st.markdown("""
### Kelompok Praktikum Kadar Besi (Fe)

| No | Nama | NIM |
|----|------|------|
| 1 | Daffa Attahilah Pratikyo | 2530604 |
| 2 | Dicky Afriansyah | 2530608 |
| 3 | Fajrian Pasya | 2530612 |
| 4 | Much Harun Al Rasyid | 2530628 |
| 5 | Muhammad Dzaki Al Fatih | 2530631 |
""")
# ==========================================================
# RUMUS DAN PERHITUNGAN
# ==========================================================
st.markdown("---")
st.subheader("Rumus Perhitungan")

st.latex(r"A = mC + b")

st.write("""
Keterangan:
- A = Absorbansi
- C = Konsentrasi (mg/L)
- m = Slope
- b = Intercept
""")

st.latex(r"C = \frac{A-b}{m}")

st.latex(r"C_{aktual}=C_{terukur}\times FP")

st.write(f"""
Hasil regresi linear:

- Slope (m) = **{m:.6f}**
- Intercept (b) = **{b:.6f}**
- Koefisien Korelasi (R²) = **{r2:.6f}**

Persamaan kurva kalibrasi:

**A = ({m:.6f})C + ({b:.6f})**
""")
# ==========================================================
# BAKU MUTU
# ==========================================================
st.markdown("---")
st.subheader("Baku Mutu Besi (Fe)")

baku_mutu = pd.DataFrame({
    "Kategori": ["Air Minum", "Air Bersih", "Air Sungai"],
    "Baku Mutu Fe (mg/L)": [bm_minum, bm_bersih, bm_sungai]
})

st.table(baku_mutu)
hasil.append({
    "Nama": nama,
    "Absorbansi": round(absorb,4),
    "Kadar Terukur (mg/L)": round(c_ter,4),
    "Faktor Pengenceran": fp,
    "Kadar Aktual (mg/L)": round(c_akt,4),
    "Baku Mutu": bm,
    "Status": status
})
