import streamlit as st
from mpin_utils.four_digit_mpin.part_a import is_commonly_used_four_digit_mpin
from mpin_utils.six_digit_mpin.part_a import is_commonly_used_six_digit_mpin
from mpin_utils.four_digit_mpin.part_b import check_four_digit_mpin_strength
from mpin_utils.four_digit_mpin.part_c import find_weak_four_digit_mpin_reasons
from mpin_utils.six_digit_mpin.part_b import check_six_digit_mpin_strength
from mpin_utils.six_digit_mpin.part_c import find_weak_six_digit_mpin_reasons
import datetime

st.set_page_config(page_title="MPIN Strength Evaluator", layout="centered")
st.title("MPIN Strength Evaluation Tool")

# MPIN Length
mpin_length = st.radio("Select MPIN Length", ["4-digit", "6-digit"], horizontal=True)

# Evaluation Part
st.markdown("### Select Evaluation Part")
part_options = {
    "PART A – Check if MPIN is commonly used": "A",
    "PART B – Evaluate MPIN strength based on user demographics": "B",
    "PART C – Provide reasons if MPIN is weak": "C"
}
selected_part_label = st.radio("Choose a part:", list(part_options.keys()), key="section_radio")
section = part_options[selected_part_label]

# MPIN Input
length_value = 4 if mpin_length == "4-digit" else 6
mpin = st.text_input(f"Enter your {mpin_length} MPIN", max_chars=length_value)
if mpin:
    if not mpin.isdigit():
        st.error("MPIN should contain digits only (0–9).")
        st.stop()
    if len(mpin) != length_value:
        st.error(f"MPIN should be exactly {length_value} digits long.")
        st.stop()



# Demographic Inputs for Part B and C
dob, spouse_dob, anniversary = "", "", ""
if section != "A":
    st.markdown("### Demographic Details")
    today = datetime.date.today()
    placeholder_date = datetime.date(1900, 1, 1)  # Special marker for 'empty'
    dob=st.date_input(
        "Date of Birth (Required)",
        value=placeholder_date,
        min_value=placeholder_date,
        max_value=today
    )
    spouse_dob_raw = st.date_input(
        "Spouse's Date of Birth (Leave as it is if you are not applicable)",
        value=placeholder_date,
        min_value=placeholder_date,
        max_value=today
    )

    anniversary_raw = st.date_input(
        "Anniversary Date (Leave as it is if you are not applicable)",
        value=placeholder_date,
        min_value=placeholder_date,
        max_value=today
    )

    # Convert marker to None
    spouse_dob = None if spouse_dob_raw == placeholder_date else spouse_dob_raw
    anniversary = None if anniversary_raw == placeholder_date else anniversary_raw


# Evaluation Logic
if st.button("Evaluate MPIN"):
    st.markdown("## Result")
    if(len(mpin)==0):
        st.error("MPIN cannot be empty")
        st.stop()
    if dob == datetime.date(1900, 1, 1) and section != "A":
        st.error("Date of Birth is required.")
        st.stop()
    if length_value == 4:
        if section == 'A':
            if is_commonly_used_four_digit_mpin(mpin):
                st.warning("This MPIN is commonly used.")
            else:
                st.success("This MPIN is not commonly used.")
        elif section == 'B':
            strength = check_four_digit_mpin_strength(mpin, dob, spouse_dob, anniversary)
            if(strength=="WEAK"):
                st.warning(f"Password Strength: **{strength}**")
            else:
                st.success(f"Password Strength: **{strength}**")
        else:
            strength, reasons = find_weak_four_digit_mpin_reasons(mpin, dob, spouse_dob, anniversary)
            if(strength=="WEAK"):
                st.warning(f"Password Strength: **{strength}**")
            else:
                st.success(f"Password Strength: **{strength}**")
           
            st.markdown("**Reasons:**")
            st.warning(str(reasons))
            
    else:  # 6-digit
        if section == 'A':
            if is_commonly_used_six_digit_mpin(mpin):
                st.warning("This MPIN is commonly used.")
            else:
                st.success("This MPIN is not commonly used.")
        elif section == 'B':
            strength = check_six_digit_mpin_strength(mpin, dob, spouse_dob, anniversary)
            if(strength=="WEAK"):
                st.warning(f"Password Strength: **{strength}**")
            else:
                st.success(f"Password Strength: **{strength}**")
        else:
            strength, reasons = find_weak_six_digit_mpin_reasons(mpin, dob, spouse_dob, anniversary)
            if(strength=="WEAK"):
                st.warning(f"Password Strength: **{strength}**")
            else:
                st.success(f"Password Strength: **{strength}**")
            
            st.markdown("**Reasons:**")
            st.warning(str(reasons))
            
