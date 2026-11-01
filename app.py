
import streamlit as st
import secrets
import string

from password_analyzer import analyze_password


# Page configuration
st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐",
    layout="centered"
)


# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f4f7fc;
    }

    .main-title {
        text-align: center;
        color: #173b70;
        font-size: 36px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 16px;
    }

    .section-title {
        color: #173b70;
        font-size: 21px;
        font-weight: bold;
    }

    div.stButton > button {
        background-color: #2563eb;
        color: white;
        border-radius: 9px;
        border: none;
        padding: 10px;
        font-weight: bold;
    }

    div.stButton > button:hover {
        background-color: #1d4ed8;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# Generate a secure password
def generate_password(length=16):

    characters = (
        string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + "!@#$%^&*"
    )

    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*")
    ]

    for i in range(length - 4):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


# Application heading
st.markdown(
    '<p class="main-title">🔐 Password Strength Analyzer</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Check your password security and create stronger passwords.</p>',
    unsafe_allow_html=True
)

st.divider()


# Password input section
st.markdown(
    '<p class="section-title">Check Your Password</p>',
    unsafe_allow_html=True
)

show_password = st.checkbox("Show Password")

password = st.text_input(
    "Enter your password",
    type="default" if show_password else "password",
    placeholder="Enter a password to analyze..."
)


# Analyze button
if st.button("Analyze Password", use_container_width=True):

    if not password:
        st.warning("Please enter a password first.")

    else:

        result = analyze_password(password)

        st.divider()

        st.markdown(
            '<p class="section-title">Analysis Results</p>',
            unsafe_allow_html=True
        )

        # Display password strength
        strength = result["strength"]
        score = result["score"]

        colors = {
            "Weak": "🔴",
            "Medium": "🟠",
            "Strong": "🟢",
            "Very Strong": "💚"
        }

        st.subheader(
            f'{colors[strength]} Password Strength: {strength}'
        )

        st.progress(score / 6)

        st.write(f"Security Score: **{score}/6**")

        # Security checklist
        st.markdown(
            '<p class="section-title">Security Checklist</p>',
            unsafe_allow_html=True
        )

        for check, status in result["checks"].items():

            if status:
                st.success(f"✓ {check}")

            else:
                st.error(f"✗ {check}")

        # Improvement suggestions
        st.markdown(
            '<p class="section-title">Improvement Suggestions</p>',
            unsafe_allow_html=True
        )

        if result["suggestions"]:

            for suggestion in result["suggestions"]:
                st.warning(suggestion)

        else:
            st.success("Your password meets all six basic checks!")


# Password generator section
st.divider()

st.markdown(
    '<p class="section-title">Generate a Strong Password</p>',
    unsafe_allow_html=True
)

st.write(
    "Generate a random password using uppercase letters, "
    "lowercase letters, numbers and special characters."
)

length = st.slider(
    "Select password length",
    min_value=12,
    max_value=32,
    value=16
)

if st.button("Generate Strong Password", use_container_width=True):

    generated = generate_password(length)

    st.success("Your new password has been generated:")

    st.code(generated, language=None)

    st.caption(
        "Save this password securely. It is not stored by this application."
    )


# Footer
st.divider()

st.caption(
    "Password Strength Analyzer | Developed using Python and Streamlit"
)

st.caption(
    "Your passwords are analyzed in the application and are not saved "
    "to a database."
)
