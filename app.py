import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="CiviPulse — The Future of Privacy-First Communication",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom High-End Styling Matching the HTML Template
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .stApp {
            background-color: #030712;
            color: #f8fafc;
            font-family: 'Inter', sans-serif;
        }
        .glass-panel {
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(52, 211, 153, 0.15);
            border-radius: 1.5rem;
            padding: 2rem;
        }
        .glass-card {
            background: rgba(30, 41, 59, 0.5);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 1.5rem;
            padding: 1.75rem;
            transition: all 0.3s ease;
        }
        .glass-card:hover {
            border-color: rgba(52, 211, 153, 0.4);
            transform: translateY(-2px);
        }
        .gradient-text {
            background: linear-gradient(135deg, #34d399 0%, #2dd4bf 50%, #22d3ee 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .download-btn {
            background: linear-gradient(135deg, #34d399 0%, #0d9488 100%);
            color: #030712 !important;
            font-weight: 700;
            padding: 0.85rem 1.75rem;
            border-radius: 1rem;
            text-align: center;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 10px 25px -5px rgba(52, 211, 153, 0.3);
            text-decoration: none;
            width: 100%;
            transition: all 0.2s ease;
        }
        .download-btn:hover {
            opacity: 0.95;
            transform: translateY(-1px);
        }
        /* Hide Streamlit default UI chrome for clean landing look */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Top Navbar Banner
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 0; border-bottom: 1px solid rgba(30, 41, 59, 0.8); margin-bottom: 3rem;">
        <div style="display: flex; align-items: center; gap: 0.75rem;">
            <div style="width: 40px; height: 40px; border-radius: 12px; background: linear-gradient(135deg, #059669, #2dd4bf); display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 20px rgba(5, 150, 105, 0.3);">
                <i class="fa-solid fa-wave-square" style="color: white; font-size: 1.1rem;"></i>
            </div>
            <span style="font-size: 1.5rem; font-weight: 800; letter-spacing: -0.025em;" class="gradient-text">CiviPulse</span>
        </div>
        <div style="font-size: 0.875rem; color: #94a3b8; background: rgba(15, 23, 42, 0.8); padding: 0.5rem 1rem; border-radius: 9999px; border: 1px solid rgba(52, 211, 153, 0.2);">
            <i class="fa-solid fa-lock" style="color: #34d399; margin-right: 0.35rem;"></i> E2EE Secured Node
        </div>
    </div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div style="text-align: center; max-w: 50rem; margin: 0 auto 4rem auto;">
        <div style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.35rem 1rem; border-radius: 9999px; background: rgba(6, 78, 59, 0.6); border: 1px solid rgba(52, 211, 153, 0.3); color: #34d399; font-size: 0.85rem; font-weight: 500; margin-bottom: 2rem;">
            <span style="width: 8px; height: 8px; border-radius: 50%; background: #34d399; display: inline-block;"></span>
            The Future of Private Communication is Here
        </div>
        <h1 style="font-size: clamp(2.5rem, 5vw, 4.5rem); font-weight: 800; line-height: 1.15; letter-spacing: -0.03em; margin-bottom: 1.5rem; color: white;">
            Total Privacy. <span class="gradient-text">System ID Routing.</span> Co-Watching & Chats.
        </h1>
        <p style="font-size: 1.15rem; color: #94a3b8; line-height: 1.7; max-width: 42rem; margin: 0 auto 2.5rem auto;">
            Say goodbye to vulnerable email addresses and data tracking. Send messages directly to secure system numbers, encrypt chats, share files, and stream cinema or music together in real-time.
        </p>
    </div>
""", unsafe_allow_html=True)

# Download Action Section (Direct GitHub Release Link)
github_exe_url = "https://github.com/oladipupo-daniel/civichat/releases/download/v1.0.3/CiviChat_Installation.exe"

col_dl1, col_dl2, col_dl3 = st.columns([1, 2, 1])
with col_dl2:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 4rem;">
            <a href="{github_exe_url}" target="_blank" class="download-btn">
                <i class="fa-solid fa-cloud-arrow-down" style="font-size: 1.25rem; margin-right: 0.75rem;"></i> Download CiviChat (.exe)
            </a>
            <p style="font-size: 0.75rem; color: #64748b; margin-top: 0.75rem;">Official Standalone Desktop Build (PyInstaller / InnoDB Bundle)</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border-color: rgba(30, 41, 59, 0.8); margin: 3rem 0;'>", unsafe_allow_html=True)

# Features Grid Section
st.markdown("""
    <div style="text-align: center; margin-bottom: 3rem;">
        <h2 style="font-size: 2.25rem; font-weight: 700; color: white; margin-bottom: 1rem;">Engineered for Absolute Control</h2>
        <p style="color: #94a3b8; font-size: 1.1rem;">CiviPulse integrates robust privacy architecture with immersive group collaboration features.</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="glass-card">
            <div style="width: 50px; height: 50px; border-radius: 12px; background: rgba(6, 78, 59, 0.8); border: 1px solid rgba(52, 211, 153, 0.3); display: flex; align-items: center; justify-content: center; color: #34d399; font-size: 1.25rem; margin-bottom: 1.25rem;">
                <i class="fa-solid fa-hashtag"></i>
            </div>
            <h3 style="font-size: 1.15rem; font-weight: 700; color: white; margin-bottom: 0.75rem;">System ID Email Routing</h3>
            <p style="font-size: 0.875rem; color: #94a3b8; line-height: 1.6;">Send emails straight to system numbers instead of exposing standard personal emails. Complete masking & routing control.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="glass-card">
            <div style="width: 50px; height: 50px; border-radius: 12px; background: rgba(17, 94, 89, 0.8); border: 1px solid rgba(45, 212, 191, 0.3); display: flex; align-items: center; justify-content: center; color: #2dd4bf; font-size: 1.25rem; margin-bottom: 1.25rem;">
                <i class="fa-solid fa-shield-halved"></i>
            </div>
            <h3 style="font-size: 1.15rem; font-weight: 700; color: white; margin-bottom: 0.75rem;">Privacy & Full Control</h3>
            <p style="font-size: 0.875rem; color: #94a3b8; line-height: 1.6;">You own your digital footprint. Zero invasive data tracking, encrypted logs, and decentralized safety parameters.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="glass-card">
            <div style="width: 50px; height: 50px; border-radius: 12px; background: rgba(8, 145, 178, 0.2); border: 1px solid rgba(34, 211, 238, 0.3); display: flex; align-items: center; justify-content: center; color: #22d3ee; font-size: 1.25rem; margin-bottom: 1.25rem;">
                <i class="fa-solid fa-comments"></i>
            </div>
            <h3 style="font-size: 1.15rem; font-weight: 700; color: white; margin-bottom: 0.75rem;">Instant Chat & Files</h3>
            <p style="font-size: 0.875rem; color: #94a3b8; line-height: 1.6;">Lightning-fast instant messaging with secure group channels, threads, and high-speed encrypted file sharing.</p>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="glass-card">
            <div style="width: 50px; height: 50px; border-radius: 12px; background: rgba(6, 78, 59, 0.8); border: 1px solid rgba(52, 211, 153, 0.3); display: flex; align-items: center; justify-content: center; color: #34d399; font-size: 1.25rem; margin-bottom: 1.25rem;">
                <i class="fa-solid fa-film"></i>
            </div>
            <h3 style="font-size: 1.15rem; font-weight: 700; color: white; margin-bottom: 0.75rem;">Cinema & Music Rooms</h3>
            <p style="font-size: 0.875rem; color: #94a3b8; line-height: 1.6;">Watch synced cinema streams or enjoy shared song playlists together with friends while inside your active group chat.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border-color: rgba(30, 41, 59, 0.8); margin: 4rem 0 3rem 0;'>", unsafe_allow_html=True)

# Interactive System ID & Chat Demo Section
st.markdown("""
    <div style="text-align: center; margin-bottom: 3rem;">
        <h2 style="font-size: 2.25rem; font-weight: 700; color: white; margin-bottom: 1rem;">Interactive CiviPulse Preview</h2>
        <p style="color: #94a3b8; font-size: 1.1rem;">Test drive the routing system right here inside Streamlit.</p>
    </div>
""", unsafe_allow_html=True)

demo_col1, demo_col2 = st.columns(2, gap="large")

with demo_col1:
    st.markdown("""
        <div class="glass-panel">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 1px solid rgba(30, 41, 59, 0.8);">
                <span style="font-size: 0.95rem; font-weight: 700; color: white;"><i class="fa-solid fa-envelope-circle-check" style="color: #34d399; margin-right: 0.5rem;"></i> System ID Mail Simulator</span>
                <span style="font-size: 0.75rem; font-family: monospace; color: #34d399; background: rgba(6, 78, 59, 0.6); padding: 0.25rem 0.5rem; border-radius: 4px;">SECURE-9042</span>
            </div>
    """, unsafe_allow_html=True)
    
    target_id = st.text_input("Recipient System ID", value="8841-SECURE")
    msg_content = st.text_area("Encrypted Message / Subject", value="Project Blueprint & Confidential Asset Transfer")
    
    if st.button("Transmit via System Number", use_container_width=True):
        st.success(f"Message successfully routed through CiviPulse nodes to CIVI-{target_id}. Zero metadata leaked.")
    
    st.markdown("</div>", unsafe_allow_html=True)

with demo_col2:
    st.markdown("""
        <div class="glass-panel">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 1px solid rgba(30, 41, 59, 0.8);">
                <span style="font-size: 0.95rem; font-weight: 700; color: white;"><i class="fa-solid fa-film" style="color: #22d3ee; margin-right: 0.5rem;"></i> Co-Watching & Cinema Room</span>
                <span style="font-size: 0.75rem; font-family: monospace; color: #22d3ee; background: rgba(8, 145, 178, 0.2); padding: 0.25rem 0.5rem; border-radius: 4px;">LIVE SYNC</span>
            </div>
            <div style="background: rgba(3, 7, 18, 0.9); border-radius: 1rem; padding: 2rem; text-align: center; border: 1px solid rgba(30, 41, 59, 0.8); margin-bottom: 1rem;">
                <div style="font-size: 2.5rem; color: #34d399; margin-bottom: 0.75rem;">
                    <i class="fa-solid fa-clapperboard"></i>
                </div>
                <h4 style="color: white; font-weight: 700; margin-bottom: 0.5rem;">Cyberpunk Odyssey (4K Stream)</h4>
                <p style="font-size: 0.85rem; color: #94a3b8;">Synced with 3 active peers in group chat.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Creator Love Dedication Footer
st.markdown("<hr style='border-color: rgba(30, 41, 59, 0.8); margin: 4rem 0 3rem 0;'>", unsafe_allow_html=True)

st.markdown(f"""
    <div style="text-align: center; max-width: 40rem; margin: 0 auto 3rem auto; padding: 2rem; border-radius: 1.5rem; background: rgba(15, 23, 42, 0.5); border: 1px solid rgba(52, 211, 153, 0.2);">
        <p style="font-style: italic; color: #cbd5e1; font-size: 1rem; margin-bottom: 1rem;">
            "The app was built by me with love to you. Download today and join the privacy revolution."
        </p>
        <div style="font-size: 0.8rem; font-weight: 700; color: #34d399; letter-spacing: 0.1em; text-transform: uppercase;">
            — Creator of CiviPulse
        </div>
    </div>
    
    <div style="text-align: center; color: #64748b; font-size: 0.85rem; padding-bottom: 3rem;">
        &copy; 2026 CiviPulse (formerly CiviChat). All rights reserved. Hosted on Streamlit Community Cloud.
    </div>
""", unsafe_allow_html=True)