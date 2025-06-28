
import streamlit as st
from PIL import Image
import pandas as pd
import datetime

st.set_page_config(page_title="Klasifikasi Iklan Visual", layout="centered")

st.title("📸 Klasifikasi Iklan Visual (Manual Based on YOLOv8 Logic)")
st.markdown("Upload gambar iklan, dan sistem akan mengklasifikasikan secara manual apakah gambar tersebut **Menarik** atau **Tidak Menarik** berdasarkan logika visual.")

uploaded_file = st.file_uploader("Upload gambar iklan", type=["jpg", "jpeg", "png"])
results = []

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diunggah", use_column_width=True)

    st.subheader("🧠 Logika Visual:")
    st.markdown("""
    - Apakah objek utama tampak jelas?
    - Apakah warna kontras dan terang?
    - Apakah ada teks ajakan seperti 'diskon', 'beli sekarang'?
    - Apakah layout rapi dan tidak berantakan?
    """)

    label = st.radio("Hasil Klasifikasi Manual Anda:", ["Menarik", "Tidak Menarik"])

    if st.button("✅ Simpan Hasil"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        results.append({
            "nama_file": uploaded_file.name,
            "prediksi": label,
            "waktu": timestamp
        })
        st.success(f"Hasil '{label}' untuk {uploaded_file.name} telah disimpan.")

    st.write("---")
    st.subheader("📄 Ekspor Hasil ke CSV")

    if results:
        df = pd.DataFrame(results)
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download hasil CSV", data=csv, file_name='hasil_klasifikasi.csv', mime='text/csv')
    else:
        st.info("Belum ada hasil klasifikasi yang disimpan.")
else:
    st.info("Silakan upload gambar terlebih dahulu.")
