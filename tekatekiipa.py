import streamlit as st

st.set_page_config(page_title="Teka-Teki IPA", page_icon="🧪")

st.title("🧪=== TEKA-TEKI IPA ===")
st.subheader("Jawablah pertanyaan berikut dengan memilih A, B, C, atau D!\n")

# Soal dan jawaban
soal = [
    {
        "pertanyaan": "1. Alat pernapasan utama pada manusia adalah?",
        "pilihan": ["A. Hidung", "B. Paru-paru", "C. Tenggorokan", "D. Bronkus"],
        "jawaban": "B"
    },
    {
        "pertanyaan": "2. Planet manakah yang disebut 'planet merah'?",
        "pilihan": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturnus"],
        "jawaban": "B"
    },
    {
        "pertanyaan": "3. Zat yang dibutuhkan tumbuhan untuk fotosintesis adalah?",
        "pilihan": ["A. Karbon dioksida", "B. Oksigen", "C. Nitrogen", "D. Hidrogen"],
        "jawaban": "A"
    },
    {
        "pertanyaan": "4. Benda yang bisa memantulkan cahaya disebut?",
        "pilihan": ["A. Transparan", "B. Benda gelap", "C. Cermin", "D. Konduktor"],
        "jawaban": "C"
    },
    {
        "pertanyaan": "5. Bagian sel tumbuhan yang berfungsi sebagai tempat fotosintesis adalah?",
        "pilihan": ["A. Inti sel", "B. Mitokondria", "C. Kloroplas", "D. Sitoplasma"],
        "jawaban": "C"
    }
]

# Inisialisasi session state
if "skor" not in st.session_state:
    st.session_state.skor = 0
if "index" not in st.session_state:
    st.session_state.index = 0
if "selesai" not in st.session_state:
    st.session_state.selesai = False

# Tampilkan pertanyaan
if not st.session_state.selesai:
    s = soal[st.session_state.index]
    st.write(s["pertanyaan"])
    pilihan = st.radio("Pilih jawabanmu:", s["pilihan"], key=st.session_state.index)

    if st.button("Kirim Jawaban"):
        jawaban_user = pilihan[0]  # Ambil huruf A/B/C/D
        if jawaban_user == s["jawaban"]:
            st.success("✅ Benar!")
            st.session_state.skor += 20
        else:
            st.error(f"❌ Salah! Jawaban yang benar adalah {s['jawaban']}")

        # Pindah ke soal berikutnya
        if st.session_state.index < len(soal) - 1:
            st.session_state.index += 1
            st.experimental_rerun()
        else:
            st.session_state.selesai = True
            st.experimental_rerun()

# Tampilkan hasil akhir
if st.session_state.selesai:
    st.subheader("=== HASIL AKHIR ===")
    st.write(f"Skormu: {st.session_state.skor}/100")

    if st.session_state.skor == 100:
        st.success("🎉 Hebat! Kamu jago IPA 🔬🌍")
    elif st.session_state.skor >= 60:
        st.info("👍 Bagus, tapi masih perlu belajar lagi 💡")
    else:
        st.warning("📘 Jangan menyerah, ayo belajar lebih rajin!")

    if st.button("Main Lagi"):
        st.session_state.skor = 0
        st.session_state.index = 0
        st.session_state.selesai = False
        st.experimental_rerun()
