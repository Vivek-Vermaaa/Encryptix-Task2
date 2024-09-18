import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_specials):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_specials:
        characters += string.punctuation
    if characters:
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    else:
        return "Please select at least one character set!"

# Streamlit UI
st.title("Password Generator")

# Input for password length
length = st.number_input("Enter the password length", min_value=6, max_value=50, value=12)

# Options for character sets
use_uppercase = st.checkbox("Include Uppercase Letters (A-Z)", value=True)
use_lowercase = st.checkbox("Include Lowercase Letters (a-z)", value=True)
use_numbers = st.checkbox("Include Numbers (0-9)", value=True)
use_specials = st.checkbox("Include Special Characters (!@#$%^&*)", value=True)

# Button to generate the password
if st.button("Generate Password"):
    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_specials)
    st.text_area("Generated Password", value=password, height=50)
    
    # Option to copy password to clipboard
    if st.button("Copy to Clipboard"):
        
        st.success("Password copied to clipboard!")