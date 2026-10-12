import random
import streamlit as st


st.title("Game tebak angka")

if "angka_rahasia" not in st.session_state:
    st.session_state.angka_rahasia = random.randint(1, 100)
if "percobaan" not in st.session_state:
    st.session_state.percobaan = 0
if "selesai" not in st.session_state:
    st.session_state.selesai = False

tebakan = st.number_input(
    "Masukan tebakan lu (1-100)",min_value=1, max_value=100, step=1
)
if st.button("Tebak Sekarang!") and not st.session_state.selesai:
    st.session_state.percobaan += 1
    angka_rahasia = st.session_state.angka_rahasia

    if tebakan < angka_rahasia:
        st.error(
            f"Kekecilan, udah nyoba {st.session_state.percobaan} kali masih aja ga bisa "
        )

    elif tebakan > angka_rahasia:
        st.warning(
            f"Kegedaan poke, udah nyoba {st.session_state.percobaan} kali masih aja ga bisa "
        ) 

    else:
        st.success(
            f"Tumben benar ya tapi kan lu nyoba {st.session_state.percobaan} kali"
        )   

        st.session_state.selesai = True

if st.session_state.selesai:
    if st.button("Main lagi lah poke kalo lu jago"):
        st.session_state.angka_rahasia = random.randint(1,100)
        st.session_state.percobaan = 0
        st.session_state.selesai = False
        st.rerun()
    



