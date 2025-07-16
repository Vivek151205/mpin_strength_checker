from mpin_utils.four_digit_mpin.part_a import is_commonly_used_four_digit_mpin
from mpin_utils.four_digit_mpin.part_b import extract_date_parts
def extract_all_date_parts(*dates):
    parts = []
    for date in dates:
        if date:
            parts.extend(extract_date_parts(date))
    return parts

def find_weak_four_digit_mpin_reasons(mpin: str, dob_self=None, dob_spouse=None, anniversary=None):
    reasons = []

    # 1. Commonly used
    if is_commonly_used_four_digit_mpin(mpin):
        reasons.append("COMMONLY_USED")

    # 2. Check date-based combinations across all parts
    all_parts = extract_all_date_parts(dob_self, dob_spouse, anniversary)
    for i in range(len(all_parts)):
        for j in range(len(all_parts)):
            if i != j:
                combo = all_parts[i] + all_parts[j]
                if len(combo) == 4 and combo == mpin:
                    # Now determine source of parts
                    if dob_self and (all_parts[i] in extract_date_parts(dob_self) or all_parts[j] in extract_date_parts(dob_self)):
                        reasons.append("DEMOGRAPHIC_DOB_SELF")
                    if dob_spouse and (all_parts[i] in extract_date_parts(dob_spouse) or all_parts[j] in extract_date_parts(dob_spouse)):
                        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
                    if anniversary and (all_parts[i] in extract_date_parts(anniversary) or all_parts[j] in extract_date_parts(anniversary)):
                        reasons.append("DEMOGRAPHIC_ANNIVERSARY")
                    break  # No need to keep searching
    reasons = list(set(reasons))  # Remove duplicates
    strength = "WEAK" if reasons else "STRONG"
    return strength, reasons
