from mpin_utils.six_digit_mpin.part_a import is_commonly_used_six_digit_mpin

def extract_date_parts(date_obj):
    """Extract DD, MM, YYYY, YY (last 2 digits) from date."""
    date_str = date_obj.strftime("%d%m%Y")
    return [
        date_str[:2],    
        date_str[2:4], 
        date_str[4:6],   
        date_str[6:],    
    ]

def check_six_digit_mpin_strength(mpin: str, dob_self=None, dob_spouse=None, anniversary=None) -> str:
    if is_commonly_used_six_digit_mpin(mpin):
        return "WEAK"

    parts = []
    for date in [dob_self, dob_spouse, anniversary]:
        if date:
            parts.extend(extract_date_parts(date))

    # Try all combinations of 2 parts to form the 6-digit pin
    for i in range(len(parts)):
        for j in range(len(parts)):
            for k in range(len(parts)):
                if len({i, j, k}) == 3:  # Make sure all indices are unique
                    combo = parts[i] + parts[j] + parts[k]
                    if combo == mpin:
                        return "WEAK"
    return "STRONG"
