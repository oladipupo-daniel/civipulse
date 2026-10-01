import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="CiviPulse - The Future of Communication",
    page_icon="⚡",
    layout="centered"
)

# Custom Styling (Dark/Neon Theme)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.75rem 1.5rem;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        opacity: 0.9;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("⚡ CiviPulse")
st.subheader("Control your privacy. Connect without limits.")

st.markdown("""
Welcome to the future of communication. **CiviPulse** (powered by CiviChat) gives you total control over your digital footprint. 
Send messages directly to a **system ID** instead of a vulnerable email address, enjoy instant group chats, share files, and even watch cinema or listen to music together with your friends!
""")

st.markdown("---")

# Direct Download Section for CiviChat
st.header("📥 Download CiviChat")
st.write("Ready to experience the future? Download the official standalone CiviChat application for your desktop today.")

download_url = "https://github.com/oladipupo-daniel/civichat/releases/download/v1.0.3/CiviChat_Installation.exe"

# Call to Action Button linking directly to your GitHub release file
st.markdown(f"""
    <a href="{download_url}" target="_blank">
        <button style="
            background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            width: 100%;
            text-align: center;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
        ">
            🚀 Download CiviChat (.exe)
        </button>
    </a>
""", unsafe_allow_html=True)

st.markdown("---")

# Features Grid
st.header("✨ Why Choose CiviPulse?")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔒 System ID Routing")
    st.write("Instead of `someone@email.com`, send mail securely to a system number. Full control over your privacy.")
    
    st.markdown("### 🎬 Co-Watching Cinemas")
    st.write("Enjoy synchronized movies and music videos with friends directly inside your group chat rooms.")

with col2:
    st.markdown("### 💬 Instant Group Chat")
    st.write("Blazing-fast messaging paired with secure file sharing designed for close teams and communities.")
    
    st.markdown("### 🛡️ Built With Love")
    st.write("Crafted from the ground up to guarantee independence, performance, and user-first data safety.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Built with Top Security.</p>", unsafe_allow_html=True)