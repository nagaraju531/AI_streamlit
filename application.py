import re

import streamlit as st

st.set_page_config(page_title="User Details Form", page_icon="📝", layout="centered")

EMAIL_PATTERN = re.compile(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$")
PHONE_PATTERN = re.compile(r"^\+?[0-9\s-]{7,15}$")


def validate(username: str, last_name: str, phone: str, email: str) -> list[str]:
    """Return a list of validation error messages (empty if all good)."""
    errors = []
    if not username.strip():
        errors.append("Username is required.")
    if not last_name.strip():
        errors.append("Last name is required.")
    if not PHONE_PATTERN.match(phone.strip()):
        errors.append("Enter a valid phone number (7-15 digits, optional +, spaces or dashes).")
    if not EMAIL_PATTERN.match(email.strip()):
        errors.append("Enter a valid email address.")
    return errors


st.title("📝 User Details Form")
st.write("Please fill in your details below.")

with st.form("user_form", clear_on_submit=False):
    username = st.text_input("Username", placeholder="e.g. johndoe")
    last_name = st.text_input("Last Name", placeholder="e.g. Doe")
    phone = st.text_input("Phone Number", placeholder="e.g. +91 98765 43210")
    email = st.text_input("Email", placeholder="e.g. john@example.com")

    submitted = st.form_submit_button("Submit")

if submitted:
    errors = validate(username, last_name, phone, email)
    if errors:
        for err in errors:
            st.error(err)
    else:
        st.success("Details submitted successfully!")
        st.subheader("Submitted Details")
        st.table(
            {
                "Field": ["Username", "Last Name", "Phone Number", "Email"],
                "Value": [username.strip(), last_name.strip(), phone.strip(), email.strip()],
            }
        )