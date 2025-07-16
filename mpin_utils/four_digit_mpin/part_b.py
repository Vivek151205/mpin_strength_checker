from mpin_utils.four_digit_mpin.part_a import is_commonly_used_four_digit_mpin

def extract_date_parts(date_obj):
    """
    Extract relevant parts from a date: DD, MM, YYYY, YY (first 2 + last 2)
    """
    date_str = date_obj.strftime("%d%m%Y")
    return [
        date_str[:2],    # DD
        date_str[2:4],   # MM
        date_str[4:8],   # YYYY
        date_str[4:6],   # YY (first 2)
        date_str[6:8],   # YY (last 2)
    ]


def is_four_digit_mpin_from_any_date_combo(mpin: str, dates: list) -> bool:
    """
    Check if the 4-digit MPIN is formed using parts from any two date components
    across DOB, Spouse DOB, or Anniversary.
    """
    if not dates:
        return False

    parts = []
    for date in dates:
        if date:
            parts.extend(extract_date_parts(date))

    # Try all 2-part combinations
    for i in range(len(parts)):
        for j in range(len(parts)):
            if i != j:
                combo = parts[i] + parts[j]
                if len(combo) == 4 and combo == mpin:
                    return True
    return False


def check_four_digit_mpin_strength(mpin: str, dob_self=None, dob_spouse=None, anniversary=None) -> str:
    """
    Returns "WEAK" or "STRONG" based on common pattern or any demographic combinations.
    """
    if is_commonly_used_four_digit_mpin(mpin):
        return "WEAK"

    if is_four_digit_mpin_from_any_date_combo(mpin, [dob_self, dob_spouse, anniversary]):
        return "WEAK"

    return "STRONG"
