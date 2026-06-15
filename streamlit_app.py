import { useState, useEffect, useRef } from "react"; import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, BarChart, Bar, ReferenceLine, Cell, ResponsiveContainer } from "recharts"; const ANGGOTA = [ { nama: "Daffa Attahilah Pratikyo", nim: "2530604", inisial: "DA" }, { nama: "Dicky Afriansyah", nim: "2530608", inisial: "Di" }, { nama: "Fajrian Pasya", nim: "2530612", inisial: "FP" }, { nama: "Much Harun Al Rasyid", nim: "2530628", inisial: "MH" }, { nama: "Muhammad Dzaki Al Fatih", nim: "2530631", inisial: "MD" }, ]; const DEFAULT_KALIBRASI = [ { konsentrasi: 0.0, absorbansi: 0.000 }, { konsentrasi: 0.2, absorbansi: 0.085 }, { konsentrasi: 0.4, absorbansi: 0.172 }, { konsentrasi: 0.6, absorbansi: 0.258 }, { konsentrasi: 0.8, absorbansi: 0.341 }, { konsentrasi: 1.0, absorbansi: 0.430 }, ]; const DEFAULT_SAMPEL = [ { nama: "Air Sumur", absorbansi: 0.215, kategori: "Air Bersih" }, { nama: "Air Sungai Ciliwung", absorbansi: 0.318, kategori: "Air Sungai" }, { nama: "Air PDAM", absorbansi: 0.042, kategori: "Air Minum" }, ]; function linearRegression(data) { const n = data.length; if (n < 2) return { m: 0, b: 0, r2: 0 }; const sumX = data.reduce((s, d) => s + d.konsentrasi, 0); const sumY = data.reduce((s, d) => s + d.absorbansi, 0); const sumXY = data.reduce((s, d) => s + d.konsentrasi * d.absorbansi, 0); const sumX2 = data.reduce((s, d) => s + d.konsentrasi ** 2, 0); const denom = n * sumX2 - sumX ** 2; if (denom === 0) return { m: 0, b: 0, r2: 0 }; const m = (n * sumXY - sumX * sumY) / denom; const b = (sumY - m * sumX) / n; const meanY = sumY / n; const ssTot = data.reduce((s, d) => s + (d.absorbansi - meanY) ** 2, 0); const ssRes = data.reduce((s, d) => s + (d.absorbansi - (m * d.konsentrasi + b)) ** 2, 0); const r2 = ssTot === 0 ? 1 : 1 - ssRes / ssTot; return { m, b, r2 }; } function EditableTable({ data, onChange, columns }) { return ( 
{columns.map((col) => ( 
{col.label} 	))} 
Aksi
{data.map((row, i) => ( 
{columns.map((col) => ( 
{col.type === "select" ? ( )}  ) : ( { const next = [...data]; next[i] = { ...next[i], [col.key]: col.type === "number" ? parseFloat(e.target.value) || 0 : e.target.value }; onChange(next); }} style={{ border: "1px solid #c3dffe", borderRadius: 6, padding: "3px 8px", fontSize: 12, width: col.width || 90, background: "white", color: "#0f4c75" }} /> )} 	))} 
onChange(data.filter((_, j) => j !== i))} style={{ background: "#fde8e8", color: "#a01a1a", border: "none", borderRadius: 6, padding: "3px 10px", cursor: "pointer", fontSize: 12 }} > Hapus 
))} 
); } function MetricCard({ label, value, sub, highlight }) { return ( 
{label}
{value}
{sub}
); } const CustomDot = (props) => { const { cx, cy } = props; return ; }; export default function App() { const [fp, setFp] = useState(2.0); const [bmMinum, setBmMinum] = useState(0.3); const [bmBersih, setBmBersih] = useState(1.0); const [bmSungai, setBmSungai] = useState(0.3); const [kalibrasi, setKalibrasi] = useState(DEFAULT_KALIBRASI); const [sampel, setSampel] = useState(DEFAULT_SAMPEL); const [activeTab, setActiveTab] = useState(0); const [sidebarOpen, setSidebarOpen] = useState(true); const { m, b, r2 } = linearRegression(kalibrasi); const regresiLine = (() => { if (kalibrasi.length < 2) return []; const xs = kalibrasi.map((d) => d.konsentrasi); const min = Math.min(...xs), max = Math.max(...xs); const pts = []; for (let i = 0; i <= 20; i++) { const x = min + (max - min) * (i / 20); pts.push({ konsentrasi: parseFloat(x.toFixed(4)), fit: parseFloat((m * x + b).toFixed(6)) }); } return pts; })(); const chartKalibrasi = kalibrasi.map((d) => ({ ...d, fit: parseFloat((m * d.konsentrasi + b).toFixed(6)) })); const hasil = sampel.map((s) => { const absorb = parseFloat(s.absorbansi) || 0; const cTer = m !== 0 ? (absorb - b) / m : 0; const cAkt = cTer * fp; let bm = bmBersih, ref = "Permenkes 416/1990"; if (s.kategori === "Air Minum") { bm = bmMinum; ref = "Permenkes 492/2010"; } else if (s.kategori === "Air Sungai") { bm = bmSungai; ref = "PP 82/2001 Kls II"; } const persen = bm > 0 ? (cAkt / bm) * 100 : 0; const status = cAkt <= bm ? "AMAN" : "TIDAK AMAN"; return { ...s, absorb, cTer: parseFloat(cTer.toFixed(4)), cAkt: parseFloat(cAkt.toFixed(4)), bm, ref, persen: parseFloat(persen.toFixed(1)), status }; }); const sign = b >= 0 ? "+" : "-"; return ( 
{/* HEADER */} 
ðŸ’§ 
Laporan Praktik Kerja (LPK)
Penentuan Kadar Besi (Fe) Â· Spektrofotometri UV-Vis Â· SNI 6989.4:2009 Â· Î» = 510 nm
Politeknik AKA Bogor Â· Program Studi Pengolahan Limbah Industri Â· Kelas 1F
{/* SIDEBAR */} 
setSidebarOpen(!sidebarOpen)} style={{ background: "#e8f1fb", border: "none", borderRadius: 8, cursor: "pointer", padding: "6px 10px", marginBottom: sidebarOpen ? 14 : 0, display: "block", color: "#0f4c75", fontWeight: 600, fontSize: 13, width: "100%" }}> {sidebarOpen ? "â—€ Tutup" : "â–¶"} {sidebarOpen && ( <> 
âš™ï¸ Pengaturan
Faktor Pengenceran (FP) setFp(parseFloat(e.target.value) || 1)} style={{ width: "100%", border: "1.5px solid #c3dffe", borderRadius: 8, padding: "6px 10px", fontSize: 13, color: "#0f4c75", background: "#f7fbff", marginBottom: 14, boxSizing: "border-box" }} /> 
Baku Mutu (mg/L)
{[ { label: "Air Minum (Permenkes 492/2010)", val: bmMinum, set: setBmMinum }, { label: "Air Bersih (Permenkes 416/1990)", val: bmBersih, set: setBmBersih }, { label: "Air Sungai (PP 82/2001 Kls II)", val: bmSungai, set: setBmSungai }, ].map(({ label, val, set }) => ( 
{label} set(parseFloat(e.target.value) || 0)} style={{ width: "100%", border: "1.5px solid #c3dffe", borderRadius: 8, padding: "5px 8px", fontSize: 13, color: "#0f4c75", background: "#f7fbff", boxSizing: "border-box" }} /> 
))} 
Referensi Metode
SNI 6989.4:2009
Spektrofotometri UV-Vis
Î» = 510 nm
Pereaksi: 1,10-Fenantrolin 
)} 
{/* MAIN CONTENT */} 
{/* ANGGOTA */} 
Anggota Kelompok 5
{ANGGOTA.map((a) => ( 
{a.inisial}
{a.nama}
{a.nim}
))} 
{/* SECTION A: KURVA KALIBRASI */} 
A. Kurva Kalibrasi
Masukkan data absorbansi larutan standar Fe dari hasil pengukuran spektrofotometer. Klik "Tambah Baris" untuk menambah data baru. 
setKalibrasi([...kalibrasi, { konsentrasi: 0, absorbansi: 0 }])} style={{ marginTop: 10, background: "#e8f1fb", border: "1.5px solid #c3dffe", borderRadius: 8, padding: "6px 16px", cursor: "pointer", color: "#0f4c75", fontSize: 13, fontWeight: 600 }} > + Tambah Baris {/* Metric Cards */} 
= 0.999 ? "âœ… Baik (>0.999)" : "âš ï¸ Periksa data"} highlight={r2 >= 0.999 ? "#1a6b35" : "#a01a1a"} /> 
{/* Persamaan */} 
ðŸ“ Persamaan Regresi:   y = {m.toFixed(4)}x {sign} {Math.abs(b).toFixed(4)}
          A = {m.toFixed(4)} Â· C {sign} {Math.abs(b).toFixed(4)}

ðŸ“Œ Persamaan Balik:   C (mg/L) = (A âˆ’ {b.toFixed(4)}) / {m.toFixed(4)} 
{/* Grafik */} [v?.toFixed(4), n === "absorbansi" ? "Data Standar" : "Fit Regresi"]} contentStyle={{ borderRadius: 8, border: "1px solid #c3dffe", fontSize: 12 }} /> } name="Data Standar" /> 
{/* SECTION B: DATA SAMPEL */} 
B. Data Sampel Air
Masukkan absorbansi sampel yang telah diukur. Pilih kategori sesuai jenis air untuk penentuan baku mutu yang tepat. 
setSampel([...sampel, { nama: "Sampel Baru", absorbansi: 0, kategori: "Air Bersih" }])} style={{ marginTop: 10, background: "#e8f1fb", border: "1.5px solid #c3dffe", borderRadius: 8, padding: "6px 16px", cursor: "pointer", color: "#0f4c75", fontSize: 13, fontWeight: 600 }} > + Tambah Sampel 
{/* SECTION C: HASIL */} 
C. Hasil Perhitungan Kadar Fe
{["Nama Sampel", "Absorbansi", "C Terukur (mg/L)", "FP", "Kadar Fe (mg/L)", "Baku Mutu", "% BM", "Status"].map((h) => ( 
{h}
))} {hasil.map((r, i) => ( 
{r.nama}	{r.absorb.toFixed(4)}	{r.cTer.toFixed(4)}	{fp}	{r.cAkt.toFixed(4)}	{r.bm.toFixed(2)}	{r.persen.toFixed(1)}% 	{r.status === "AMAN" ? "âœ… AMAN" : "âŒ TIDAK AMAN"} 
))} 
{/* Bar Chart */} [v?.toFixed(4) + " mg/L"]} contentStyle={{ borderRadius: 8, border: "1px solid #c3dffe", fontSize: 12 }} /> {hasil.map((r, i) => ( ))} {hasil.map((r, i) => ( ))} 
Aman Tidak Aman Baku Mutu 
{/* SECTION D: PERHITUNGAN DETAIL */} 
D. Langkah Perhitungan Detail
{/* Tabs */} 
{hasil.map((r, i) => ( setActiveTab(i)} style={{ background: activeTab === i ? "#1b6ca8" : "#e8f1fb", color: activeTab === i ? "white" : "#0f4c75", border: "1.5px solid #c3dffe", borderRadius: 8, padding: "6px 14px", cursor: "pointer", fontSize: 12, fontWeight: 600, transition: "all 0.15s" }} > {r.nama} ))} 
{hasil[activeTab] && (() => { const r = hasil[activeTab]; return ( 
ðŸ“‹ Data Input 
â€¢ Absorbansi (A) = {r.absorb.toFixed(4)} AU
â€¢ Slope (m) = {m.toFixed(4)}
â€¢ Intercept (b) = {b.toFixed(4)}
â€¢ Faktor Pengenceran = {fp}
â€¢ Kategori = {r.kategori} 
ðŸ§® Langkah Perhitungan 
Step 1 â€” Konsentrasi Terukur:
C = (A âˆ’ b) / m
C = ({r.absorb.toFixed(4)} âˆ’ {b.toFixed(4)}) / {m.toFixed(4)}
C = {r.cTer.toFixed(4)} mg/L

Step 2 â€” Koreksi Pengenceran:
C aktual = C Ã— FP = {r.cTer.toFixed(4)} Ã— {fp} = {r.cAkt.toFixed(4)} mg/L

Step 3 â€” Bandingkan Baku Mutu:
BM ({r.ref}) = {r.bm} mg/L
{r.cAkt.toFixed(4)} {r.status === "AMAN" ? "â‰¤" : ">"} {r.bm} mg/L â†’ {r.status} 
); })()} 
{/* SECTION E: KESIMPULAN */} 
E. Kesimpulan
{hasil.map((r, i) => ( 
{r.status === "AMAN" ? "âœ…" : "âŒ"} {r.nama} 
Kadar Fe: {r.cAkt.toFixed(4)} mg/L
Baku Mutu: {r.bm.toFixed(2)} mg/L
{r.persen.toFixed(1)}% dari BM
{r.status === "AMAN" ? "Memenuhi" : "Melebihi"} {r.ref} 
))} 
{hasil.filter((r) => r.status !== "AMAN").length > 0 && ( 
âš ï¸ {hasil.filter((r) => r.status !== "AMAN").map((r) => r.nama).join(", ")} memiliki kadar Fe di atas baku mutu yang berlaku dan tidak layak digunakan sesuai peruntukannya tanpa pengolahan lebih lanjut. 
)} {hasil.filter((r) => r.status === "AMAN").length > 0 && ( 
â„¹ï¸ {hasil.filter((r) => r.status === "AMAN").map((r) => r.nama).join(", ")} memiliki kadar Fe yang masih dalam ambang batas baku mutu yang berlaku. 
)} 
{/* FOOTER */} 
LPK Penentuan Kadar Besi (Fe) Â· Metode Spektrofotometri UV-Vis (SNI 6989.4:2009)
Kelompok 5 Â· Kelas 1F Â· Politeknik AKA Bogor Â· 2024/2025 
); } 
