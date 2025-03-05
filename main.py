# Professional Password Strength Analyzer

import streamlit as st
import random
import string

def generate_password(length=16):
    """
    Generates a strong password of the specified length.

    Args:
        length (int): The desired length of the password. Defaults to 16.

    Returns:
        str: A randomly generated strong password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_password_strength(password):
    """
    Checks the strength of a password based on length and character diversity.

    Args:
        password (str): The password to check.

    Returns:
        str: A string indicating the password strength level (e.g., "Weak", "Moderate", "Strong").
    """
    length = len(password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    if length < 8:
        return "Very Weak"
    elif length < 12:
        if sum([has_lower, has_upper, has_digit, has_symbol]) < 2:
            return "Weak"
        else:
            return "Moderate"
    elif length < 16:
        if sum([has_lower, has_upper, has_digit, has_symbol]) < 3:
            return "Moderate"
        else:
            return "Strong"
    else: # length >= 16
        if sum([has_lower, has_upper, has_digit, has_symbol]) == 4:
            return "Very Strong"
        else:
            return "Strong"

# Streamlit app
st.title("Password Security Analyzer")
st.markdown("Analyze and Strengthen Your Passwords")

password = st.text_input("Password:", type="password")
strength_level = check_password_strength(password)

st.markdown(f"**Password Strength:** {strength_level}")

if strength_level == "Very Weak":
    st.warning("Very Weak: This password is too short and easily guessable. Minimum length is 8 characters.")
elif strength_level == "Weak":
    st.warning("Weak: This password is still vulnerable. Use a longer password with a mix of character types.")
elif strength_level == "Moderate":
    st.info("Moderate: This password is okay, but can be improved. Consider adding more character types and length.")
elif strength_level == "Strong":
    st.success("Strong: This is a good password! But longer and more complex is always better.")
elif strength_level == "Very Strong":
    st.success("Very Strong: Excellent password! This password is very secure.")

# Password history (basic - consider security implications for real-world apps)
if 'password_history' not in st.session_state:
    st.session_state.password_history = []

if st.button("Save Password (for this session)"):
    if password:
        st.session_state.password_history.append(password)
        st.success("Password saved to history (session only).")

st.subheader("Password History (Session)")
show_passwords = st.checkbox("Show saved passwords") # Add checkbox to toggle password visibility
if st.session_state.password_history:
    for pwd in st.session_state.password_history:
        if show_passwords:
            st.write("🔑 " + pwd) # Display actual password if checkbox is checked
        else:
            st.write("🔒 " + "*" * len(pwd)) # Masking displayed passwords in history
else:
    st.write("No passwords saved in history yet.")


if st.button("Generate Strong Password"):
    strong_password = generate_password()
    st.code(f"Generated Password: {strong_password}", language="plaintext")
    st.success("Copy and use this strong password.")
st.markdown("---")
st.markdown("<footer style='text-align: center; margin-top: 20px; padding: 10px; color: #555; font-size: 0.9em; border-top: 1px solid #ddd;'>\
    © 2023 Password Strength Analyzer | Developed by <a href='https://www.linkedin.com/in/your-linkedin-profile' style='color: #555; text-decoration: none;'>Muhammad Sami</a>\
</footer>", unsafe_allow_html=True)