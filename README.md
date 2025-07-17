# 🔐 MPIN Strength Checker

A lightweight yet robust utility to evaluate the strength of a 4-digit or 6-digit MPIN (Mobile PIN), simulating real-world banking app scenarios. The tool checks if the MPIN is guessable or derived from easily available personal data (like DOB or anniversaries).

Built using **Python** and **Streamlit**, the logic is fully modular and self-contained — no external datasets are used.

---
## 👉 [Working Project Deployed on Streamlit](https://vivek151205-mpin-strength-checker-main-v7fhcu.streamlit.app/) 

## 🧠 Features

- ✅ **Supports both 4-digit and 6-digit MPINs**
- 🔍 **Section A**: Detects commonly used MPINs (`1234`, `1111`, `000000`, etc.)
- 🧬 **Section B**: Flags MPINs derived from user-specific demographic info:
  - Self DOB
  - Spouse's DOB
  - Anniversary
- 📋 **Section C**: Provides clear reasons if the MPIN is flagged as weak
- 🧪 **Test Suite**: Automated test cases are included via `testcases.py` and Colab notebook
- 💡 **Streamlit UI**: Simple and interactive web interface for manual testing

---

## 🔍 Logic Breakdown

### 🔹 Section A: Commonly Used MPINs

Flags MPINs that are highly predictable:
- 4-digit examples: `'0000'`, `'1234'`, `'1111'`, `'1212'`, `'2580'`
- 6-digit examples: `'000000'`, `'123456'`, `'112233'`, `'121212'`, `'654321'`

Patterns include:
- Repeated digits (e.g., `1111`)
- Sequences (e.g., `1234`, `4321`)
- Keypad patterns (e.g., `2580` = vertical middle of keypad)

---

### 🔹 Section B: Demographic-Based MPINs

Detects MPINs derived from:
- Self **DOB**
- **Spouse's DOB**
- **Anniversary**

Pattern logic:
- Extracts all meaningful combinations like:
  - For 4-digit: `DDMM`, `MMYY`, `YYYY`, etc.
  - For 6-digit: `DDMMYY`, `MMYYYY`, `YYYYMM`, `YYMMDD`, etc.
- Matches input MPIN against these combinations

---

### 🔹 Section C: Reasoning Engine

- Merges results from Section A and B
- Final verdict:
  - `"WEAK"` → if matched in either Section A or B
  - `"STRONG"` → if no match found
- Reasons returned:
  - `COMMONLY_USED`
  - `DEMOGRAPHIC_DOB_SELF`
  - `DEMOGRAPHIC_DOB_SPOUSE`
  - `DEMOGRAPHIC_ANNIVERSARY`

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Vivek151205/mpin_strength_checker.git
cd mpin_strength_checker
```

### 2. Install Dependencies

```bash
pip install streamlit
```

### 3. Run the Application

```bash
streamlit run main.py
```

---

## 📂 Project Directory Structure

```bash
mpin_strength_checker/
├── app.py                       # Streamlit UI logic
├── testcases.py                # Collection of MPIN test cases and validation output
├── Raw Logic for MPIN strength.py  # Experimental playground for logic development
├── Working Demo Video          # Local video file (for demo or sharing)
├── mpin_utils/
│   ├── four_digit/
│   │   ├── part_a.py           # Section A logic for 4-digit MPINs
│   │   ├── part_b.py           # Section B logic for 4-digit MPINs
│   │   └── part_c.py           # Final decision logic for 4-digit MPINs
│   └── six_digit/
│       ├── part_a.py           # Section A logic for 6-digit MPINs
│       ├── part_b.py           # Section B logic for 6-digit MPINs
│       └── part_c.py           # Final decision logic for 6-digit MPINs
├── README.md                   # You're here!
```

---

## 🧪 Testing & Validation

- All critical scenarios are covered in `testcases.py`, including:
  - Commonly used MPINs
  - Demographic matches for each date field
  - Strong MPINs for sanity check

- A dedicated Google Colab notebook was also created during development for logic exploration and debugging.

👉 [Open in Colab](https://colab.research.google.com/drive/1tutJyZZXtIqOE6wrtntyPZdzVHkqPqar?usp=sharing)

---
## 🎥 Video Demo

<p align="center">
  <a href="https://youtu.be/2z2UQ1qKiUg?si=P3oKtQ-RmDQaq5e6" target="_blank">
    <img src="https://img.youtube.com/vi/2z2UQ1qKiUg/0.jpg" alt="Watch the Demo" width="600"/>
  </a>
</p>

---

## 👨‍💻 Author

**Vivek Tripathi**

📫 [Mail](mailto:vivektripathi373@gmail.com)  
🌐 [GitHub: Vivek151205](https://github.com/Vivek151205)

---

✅ Built with ❤️ for secure digital banking and intelligent validation.
