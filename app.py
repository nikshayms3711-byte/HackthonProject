import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="StepVerify — Local Health Intelligence",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Clean, minimal CSS for a modern health-app look
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .privacy-badge {
        display: inline-block;
        background-color: #ECFDF5;
        color: #065F46;
        border: 1px solid #A7F3D0;
        padding: 4px 12px;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .nudge-card {
        background-color: #F8FAFC;
        border-left: 4px solid #0F766E;
        padding: 16px 20px;
        border-radius: 8px;
        margin-bottom: 14px;
        color: #1E293B;
    }
    .nudge-card.warning {
        border-left-color: #D97706;
        background-color: #FFFBEB;
    }
    .nudge-card.alert {
        border-left-color: #E11D48;
        background-color: #FFF1F2;
    }
    .nudge-title {
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 4px;
        color: #0F172A;
    }
    .nudge-meta {
        font-size: 0.78rem;
        color: #64748B;
        margin-top: 6px;
    }
</style>
""", unsafe_allow_html=True)

# Demo datasets so you can switch states live during your pitch
SCENARIOS = {
    "High Exertion & Short Sleep": {
        "raw_steps": 11420,
        "true_steps": 9850,
        "phantom_steps": 1570,
        "sleep_total": "5h 40m",
        "sleep_delta": "-1h 50m vs baseline",
        "deep_sleep": "1h 05m",
        "resting_hr": "72 bpm",
        "hr_delta": "+6 bpm (elevated)",
        "hr_delta_color": "inverse",
        "readiness": "62 / 100",
        "step_chart": pd.DataFrame({
            "Hour": ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"],
            "Raw Watch Steps": [1200, 2400, 1500, 1800, 920, 2600, 1000],
            "Verified Steps": [1150, 1300, 1480, 1650, 900, 2420, 950],
        }).set_index("Hour"),
        "hr_chart": pd.DataFrame({
            "Hour": ["06:00", "09:00", "12:00", "15:00", "18:00", "21:00"],
            "Heart Rate (bpm)": [68, 84, 92, 88, 134, 78],
        }).set_index("Hour"),
        "sleep_chart": pd.DataFrame({
            "Stage": ["Deep", "REM", "Light", "Awake"],
            "Hours": [1.1, 1.2, 3.3, 0.5],
        }).set_index("Stage"),
        "nudges": [
            {
                "type": "warning",
                "tag": "Sleep Recovery • Watch Sleep Log",
                "title": "Short Deep Sleep Detected (1h 05m)",
                "body": "You logged 5h 40m of total sleep with low deep-sleep recovery. Consider adjusting tomorrow's 10,000-step goal to a lighter 7,500-step recovery target and winding down 45 minutes earlier tonight.",
                "voice": "Your deep sleep dropped below baseline last night. Keep today's movement light and aim for an earlier bedtime."
            },
            {
                "type": "alert",
                "tag": "Heart Rate • Elevated Resting HR",
                "title": "Resting Heart Rate Up +6 bpm (72 bpm)",
                "body": "Your resting heart rate is higher than your 7-day average of 66 bpm, paired with an evening peak of 134 bpm. Skip high-intensity workouts today and stick to steady-pace walking.",
                "voice": "Your resting heart rate is slightly elevated today, signaling mild fatigue. Stick to low-intensity walks instead of a hard workout."
            },
            {
                "type": "normal",
                "tag": "Step Verification • Watch + Phone Fusion",
                "title": "1,570 Phantom Steps Filtered Out",
                "body": "A commute spike at 10:00 AM was flagged using your phone's accelerometer baseline. Your true verified count is 9,850 steps—just a 2-minute walk completes your 10,000-step goal accurately.",
                "voice": "We filtered out 1,570 false commute steps. You are 150 real steps away from hitting your ten thousand step target."
            },
        ],
    },
    "Well-Rested & Consistent Day": {
        "raw_steps": 10680,
        "true_steps": 10240,
        "phantom_steps": 440,
        "sleep_total": "7h 45m",
        "sleep_delta": "+15m vs baseline",
        "deep_sleep": "1h 55m",
        "resting_hr": "64 bpm",
        "hr_delta": "-2 bpm (recovered)",
        "hr_delta_color": "normal",
        "readiness": "91 / 100",
        "step_chart": pd.DataFrame({
            "Hour": ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"],
            "Raw Watch Steps": [1500, 1200, 1900, 1400, 1680, 2100, 900],
            "Verified Steps": [1460, 1120, 1850, 1340, 1590, 2010, 870],
        }).set_index("Hour"),
        "hr_chart": pd.DataFrame({
            "Hour": ["06:00", "09:00", "12:00", "15:00", "18:00", "21:00"],
            "Heart Rate (bpm)": [61, 76, 82, 79, 118, 66],
        }).set_index("Hour"),
        "sleep_chart": pd.DataFrame({
            "Stage": ["Deep", "REM", "Light", "Awake"],
            "Hours": [1.9, 1.8, 4.0, 0.2],
        }).set_index("Stage"),
        "nudges": [
            {
                "type": "normal",
                "tag": "Sleep Recovery • Optimal Baseline",
                "title": "Strong Sleep Efficiency (7h 45m)",
                "body": "Nearly 2 hours of deep sleep puts your recovery in the optimal zone. Your body is ready for your full 10,000-step target or an extra cardio session.",
                "voice": "Great recovery last night with nearly two hours of deep sleep. You are cleared for full activity today."
            },
            {
                "type": "normal",
                "tag": "Heart Rate • Stable Baseline",
                "title": "Resting Heart Rate Steady at 64 bpm",
                "body": "Your cardiovascular recovery looks solid with quick heart-rate drop-off after your 6:00 PM walk.",
                "voice": "Your resting heart rate is steady at 64 beats per minute, showing strong cardiovascular recovery."
            },
            {
                "type": "normal",
                "tag": "Step Verification • Goal Achieved",
                "title": "10,240 Verified Steps Completed",
                "body": "Only 440 minor false counts were removed today. Your daily 10,000-step streak is verified and intact.",
                "voice": "Nice work. You hit 10,240 verified steps today and kept your streak alive."
            },
        ],
    },
}

# --- Sidebar ---
with st.sidebar:
    st.header("Data Sources")
    st.caption("All sensor fusion runs locally on your machine.")

    watch_file = st.file_uploader("Budget Watch Export (Steps, HR, Sleep CSV)", type="csv")
    phone_file = st.file_uploader("Phone Accelerometer Baseline (CSV)", type="csv")

    st.divider()
    st.subheader("Demo Mode")
    use_demo = st.toggle("Use Sample Sensor Data", value=True)
    scenario_name = st.selectbox("Select Demo Scenario", list(SCENARIOS.keys()), disabled=not use_demo)

# --- Header ---
st.markdown('<div class="privacy-badge">LOCAL-ONLY PROCESSING • ZERO CLOUD UPLOADS</div>', unsafe_allow_html=True)
st.title("StepVerify Dashboard")
st.caption("Reconciling budget wearable logs with phone accelerometer baselines for accurate steps and recovery insights.")

if not use_demo and not (watch_file and phone_file):
    st.info("Upload your watch and phone CSV logs in the sidebar, or turn on **Use Sample Sensor Data** to preview the dashboard.")
    st.stop()

data = SCENARIOS[scenario_name]

# --- Top Summary Cards ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    with st.container(border=True):
        st.metric(
            label="Verified Steps",
            value=f"{data['true_steps']:,}",
            delta=f"-{data['phantom_steps']:,} phantom steps",
            delta_color="inverse",
        )
with col2:
    with st.container(border=True):
        st.metric(
            label="Sleep Duration",
            value=data["sleep_total"],
            delta=data["sleep_delta"],
        )
with col3:
    with st.container(border=True):
        st.metric(
            label="Resting Heart Rate",
            value=data["resting_hr"],
            delta=data["hr_delta"],
            delta_color=data["hr_delta_color"],
        )
with col4:
    with st.container(border=True):
        st.metric(
            label="Daily Readiness",
            value=data["readiness"],
            delta="Local AI Score",
            delta_color="off",
        )

st.write("")

# --- Main Tabs ---
tab1, tab2, tab3 = st.tabs(["Step Reconciliation", "Heart Rate & Sleep", "AI Recovery Nudges (ElevenLabs)"])

with tab1:
    with st.container(border=True):
        st.subheader("Hourly Watch Count vs. Phone-Verified Steps")
        st.line_chart(data["step_chart"], color=["#94A3B8", "#0F766E"])
        st.caption(
            f"Raw watch total: **{data['raw_steps']:,} steps** | "
            f"Phone-verified total: **{data['true_steps']:,} steps** | "
            f"Noise filtered: **{data['phantom_steps']:,} steps**"
        )

with tab2:
    left, right = st.columns(2)
    with left:
        with st.container(border=True):
            st.subheader("Heart Rate Trend (Watch)")
            st.area_chart(data["hr_chart"], color="#E11D48")
            st.caption(f"Resting baseline: **{data['resting_hr']}** • Used to detect fatigue and overtraining.")
    with right:
        with st.container(border=True):
            st.subheader("Sleep Stages Breakdown")
            st.bar_chart(data["sleep_chart"], color="#4F46E5")
            st.caption(f"Total sleep: **{data['sleep_total']}** • Deep sleep: **{data['deep_sleep']}**")

with tab3:
    st.subheader("Personalized Local AI Nudges")
    st.caption("Generated by combining verified step counts, watch heart rate trends, and sleep recovery stages.")

    for idx, nudge in enumerate(data["nudges"]):
        css_class = "nudge-card"
        if nudge["type"] == "warning":
            css_class += " warning"
        elif nudge["type"] == "alert":
            css_class += " alert"

        st.markdown(
            f"""
            <div class="{css_class}">
                <div class="nudge-title">{nudge['title']}</div>
                <div>{nudge['body']}</div>
                <div class="nudge-meta">{nudge['tag']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button(f"Preview ElevenLabs Voice Nudge #{idx + 1}", key=f"voice_{idx}"):
            st.success(f'Playing ElevenLabs Audio Preview: "{nudge["voice"]}"')