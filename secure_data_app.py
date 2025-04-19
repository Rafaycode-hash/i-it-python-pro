import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# 🔑 Generate encryption key (auto-generated every run)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# 🧠 In-memory data storage
stored_data = {}  # Format: {"encrypted_text": {"encrypted_text": "...", "passkey": "hashed_passkey"}}
failed_attempts = 0

# 🔁 Hashing function for passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# 🔒 Encrypt user data
def encrypt_data(text, passkey):
    return cipher.encrypt(text.encode()).decode()

# 🔓 Decrypt user data
def decrypt_data(encrypted_text, passkey):
    global failed_attempts
    hashed_pass = hash_passkey(passkey)

    if encrypted_text in stored_data and stored_data[encrypted_text]["passkey"] == hashed_pass:
        failed_attempts = 0
        return cipher.decrypt(encrypted_text.encode()).decode()
    
    failed_attempts += 1
    return None

# 🌐 Streamlit Interface
st.set_page_config(page_title="Secure App", layout="centered")
st.title("🔐 Secure Data Encryption App")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome!")
    st.markdown("Store and retrieve your data **securely** using encryption.")

elif choice == "Store Data":
    st.subheader("📥 Store Data")
    user_data = st.text_area("Enter your data:")
    passkey = st.text_input("Enter a passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed = hash_passkey(passkey)
            encrypted = encrypt_data(user_data, passkey)
            stored_data[encrypted] = {"encrypted_text": encrypted, "passkey": hashed}
            st.success("✅ Data encrypted and stored!")
            st.code(encrypted, language='text')
        else:
            st.warning("⚠️ Please fill both fields.")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Data")
    encrypted_input = st.text_area("Paste your encrypted data:")
    passkey_input = st.text_input("Enter your passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_input and passkey_input:
            result = decrypt_data(encrypted_input, passkey_input)
            if result:
                st.success("✅ Decrypted Data:")
                st.code(result, language='text')
            else:
                st.error(f"❌ Incorrect passkey! Attempts remaining: {3 - failed_attempts}")
                if failed_attempts >= 3:
                    st.warning("🔐 Too many failed attempts! Redirecting to login...")
                    st.experimental_rerun()
        else:
            st.warning("⚠️ Fill both fields.")

elif choice == "Login":
    st.subheader("🔑 Login to Retry")
    master_pass = st.text_input("Enter master password:", type="password")

    if st.button("Login"):
        if master_pass == "admin123":
            failed_attempts = 0
            st.success("✅ Logged in again! Now go back to retrieve your data.")
        else:
            st.error("❌ Incorrect login password.")

