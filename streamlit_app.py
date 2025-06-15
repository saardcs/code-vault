import streamlit as st
import qrcode
import io

st.set_page_config(page_title="Code Vault", page_icon="🔐")

# Sidebar with QR code
st.sidebar.header("Scan This QR Code to View Menu Online")

qr_link = "https://code-vault.streamlit.app"  # Replace with your actual URL
qr = qrcode.make(qr_link)
buf = io.BytesIO()
qr.save(buf)
buf.seek(0)

st.sidebar.image(buf, width=300, caption=qr_link)

st.title("🔐 Code Vault Challenge")

st.write("Enter the 5 code numbers you've calculated to try and unlock the vault!")

# Define correct answers (based on your worksheet)
correct_answers = {
    1: 30240,      # 10 x 9 x 8 x 7 x 6
    2: 1413720,    # 36 x 35 x 34 X 33
    3: 1679616,    # 36 x 36 x 36 X 36
    4: 311875200,  # 52 x 51 x 50 x 49 x 48
    5: 776520240 # 62 x 61 x 60 x 59 X 58 x 57
}

# Mapping from number to letter
code_map = {
    1679616: "C",
    1413720: "O",
    30240: "D",
    311875200: "E",
    776520240: "!"
}

user_inputs = {}
final_code = ""

with st.form("vault_form"):
    for i in range(1, 6):
        user_inputs[i] = st.number_input(f"Code Part {i}:", min_value=0, value=0, step=1)
    submitted = st.form_submit_button("🔓 Try Unlocking")

if submitted:
    all_correct = True
    for i in range(1, 6):
        if user_inputs[i] != correct_answers[i]:
            all_correct = False
            break
    
    if all_correct:
        final_code = "".join(code_map[correct_answers[i]] for i in range(1, 6))
        st.success(f"✅ Vault Unlocked! The code is: {final_code}")
        st.balloons()
    else:
        st.error("❌ Incorrect code combination. Try again!")
