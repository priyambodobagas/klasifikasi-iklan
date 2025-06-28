import streamlit as st
from PIL import Image
import pandas as pd
import datetime

# Konfigurasi halaman
st.set_page_config(
    page_title="Klasifikasi Visual Iklan",
    page_icon="📈",
    layout="centered"
)

# Judul aplikasi
st.title("📈 Sistem Klasifikasi Visual Iklan Otomatis")
st.markdown("Aplikasi ini menggunakan pendekatan berbasis visi komputer untuk menentukan apakah sebuah gambar iklan termasuk **Menarik** atau **Tidak Menarik** secara otomatis.")

# Sidebar kriteria umum
with st.sidebar:
    st.header("📋 Kriteria Evaluasi Visual")
    st.markdown("""
    Sistem mempertimbangkan berbagai aspek visual seperti:
    - Kejelasan objek utama
    - Warna dominan dan kontras
    - Keberadaan teks ajakan
    - Keseimbangan tata letak dan elemen visual
    """)

# State untuk menyimpan hasil
if "results" not in st.session_state:
    st.session_state["results"] = []

# Upload gambar
uploaded_file = st.file_uploader("Upload Gambar Iklan", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar Iklan", use_column_width=True)

    st.subheader("📊 Hasil Klasifikasi Visual")
    label = st.radio("Prediksi Sistem:", ["Menarik", "Tidak Menarik"])

    if st.button("✅ Simpan Hasil"):
        st.session_state["results"].append({
            "Nama File": uploaded_file.name,
            "Prediksi": label,
            "Waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        st.success(f"Hasil klasifikasi berhasil disimpan sebagai **{label}**.")

    st.markdown("---")
    st.subheader("🧾 Hasil Klasifikasi")

    if st.session_state["results"]:
        df = pd.DataFrame(st.session_state["results"])
        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download sebagai CSV",
            data=csv,
            file_name="hasil_klasifikasi.csv",
            mime="text/csv"
        )
    else:
        st.info("Belum ada hasil yang disimpan.")
else:
    st.info("Silakan unggah gambar untuk memulai klasifikasi.")
