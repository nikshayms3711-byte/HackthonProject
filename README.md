# DualStride — Privacy-First Personal Fitness Intelligence

A local Python and Streamlit dashboard that reconciles budget fitness tracker logs with smartphone accelerometer baselines to filter out phantom steps, visualize heart rate and sleep recovery, and deliver spoken AI nudges.

---

## Problem Statement

Imagine committing to a daily goal of **10,000 steps** and staying consistent for one or two weeks. You rely on an affordable fitness tracker to measure your progress, only for it to miscount—logging phantom steps during a car ride or missing real walking effort.

Instead of keeping you consistent, inaccurate numbers turn the device into a psychological barrier. When you cannot trust the count on your wrist, motivation drops and the habit breaks. Premium wearables like the Apple Watch or Whoop solve accuracy, but their high price tags make them unrealistic for most students and everyday beginners.

---

## Our Solution

DualStride improves the reliability of affordable hardware through local software instead of expensive upgrades:

* **Local Dual-Sensor Reconciliation:** Cross-checks raw budget watch step logs against your smartphone's accelerometer baseline on your own device to identify and filter out non-walking noise (such as commute and vehicle vibrations).
* **Privacy-First by Design:** All sensor processing and trend analysis stay strictly local in Python—zero personal health data is uploaded to third-party cloud servers.
* **Holistic Recovery Insights & Spoken Nudges:** Combines verified step counts with watch heart rate and sleep stage logs to generate actionable, spoken recovery reminders via **ElevenLabs** (for example, recommending a lighter recovery target after short deep sleep or an elevated resting heart rate).

---

## Why Not Buy Premium Wearables?

High-end trackers deliver strong sensor accuracy, but their upfront cost and subscription fees lock out everyday users. DualStride democratizes dependable fitness tracking by making budget trackers trustworthy through software.

---

## Target Users

* **Students and fitness beginners** who want accurate daily tracking without spending heavily on premium smartwatches.
* **Budget wearable owners** frustrated by phantom steps breaking their daily targets.
* **Privacy-conscious individuals** who prefer keeping their biometric and activity logs locally on their own machine.

---

## Prototype Features

* **Sensor Upload & Demo Mode:** Upload budget watch exports and phone accelerometer baselines (CSV), or toggle built-in sample scenarios (*High Exertion & Short Sleep* vs. *Well-Rested & Consistent Day*).
* **Daily Summary Cards:** Side-by-side overview of Verified Steps (with phantom steps removed), Sleep Duration, Resting Heart Rate, and a local Daily Readiness score.
* **Interactive Analytics Tabs:**
  * *Step Reconciliation:* Hourly comparison chart of raw watch counts vs. phone-verified steps.
  * *Heart Rate & Sleep:* Heart rate trend curves and sleep stage breakdowns (Deep, REM, Light, Awake).
  * *AI Recovery Nudges:* Tailored coaching cards across steps, heart rate, and sleep with ElevenLabs voice nudge previews.

---

## Impact & Future Roadmap

* **Immediate Impact:** Removes the trust gap in affordable fitness trackers so users stay motivated to hit daily movement goals without upgrading hardware.
* **Future Roadmap:** After validating step reconciliation as the core foundation, future iterations will expand local verification algorithms deeper into **heart rate accuracy** and **sleep stage tracking**.

---

## Tech Stack

* **Language:** Python
* **Dashboard UI:** Streamlit
* **Data Processing:** Pandas
* **Voice Nudges:** ElevenLabs (audio preview integration)

---

## Running Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/nikshayms3711-byte/HackthonProject.git](https://github.com/nikshayms3711-byte/HackthonProject.git)
   cd HackthonProject
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the dashboard:
   ```bash
   streamlit run app.py
   ```
   *(If `streamlit` is not recognized in your terminal, run `python -m streamlit run app.py` instead.)*
