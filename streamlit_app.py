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
    1: 1000,   # 10 x 10 x 10
    2: 358800, # 26 x 25 x 24 x 23
    3: 300,    # 6 x 5 x 10
    4: 24,     # 4 x 3 x 2
    5: 60      # 5 x 4 x 3
}

# Mapping from number to letter
code_map = {
    60: "C",
    24: "O",
    300: "D",
    1000: "E",
    358800: "!"
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
