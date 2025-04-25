import streamlit as st
from utils import generate_random_key, encrypt_with_key, decrypt_with_key
import json

st.title("AEGISCIPHER ENGINE ")

# Encryption Section
st.header("Encrypt a Message")

plaintext = st.text_input("Enter your message to encrypt:")

if st.button("Encrypt"):
    key = generate_random_key()
    encrypted_message = encrypt_with_key(plaintext, key)

    # Save in session state
    st.session_state['encrypted_message'] = encrypted_message
    st.session_state['encryption_key'] = key

# Display after encrypting
if 'encrypted_message' in st.session_state:
    st.subheader("Encrypted Message:")
    st.code(st.session_state['encrypted_message'], language='text')

    st.subheader("Encryption Key:")
    st.code(json.dumps(st.session_state['encryption_key'], indent=4))

# Decryption Section
st.header("Decrypt a Message")
ciphertext = st.text_input("Enter encrypted message:")
key_input = st.text_area("Paste the key dictionary:")

if st.button("Decrypt"):
    try:
        key_map = json.loads(key_input)
        decrypted_message = decrypt_with_key(ciphertext, key_map)
        st.success(f"Decrypted Message: {decrypted_message}")
    except Exception as e:
        st.error(f"Error: {e}")
