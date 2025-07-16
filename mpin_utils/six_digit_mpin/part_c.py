from mpin_utils.six_digit_mpin.part_a import is_commonly_used_six_digit_mpin
from mpin_utils.six_digit_mpin.part_b import extract_date_parts
from itertools import permutations

def extract_all_date_parts_with_sources(dob_self, dob_spouse, anniversary):
    """Return a list of tuples: (part, source)"""
    all_parts = []

    if dob_self:
        all_parts.extend([(p, "DEMOGRAPHIC_DOB_SELF") for p in extract_date_parts(dob_self)])
    if dob_spouse:
        all_parts.extend([(p, "DEMOGRAPHIC_DOB_SPOUSE") for p in extract_date_parts(dob_spouse)])
    if anniversary:
        all_parts.extend([(p, "DEMOGRAPHIC_ANNIVERSARY") for p in extract_date_parts(anniversary)])

    return all_parts

def find_weak_six_digit_mpin_reasons(mpin: str, dob_self=None, dob_spouse=None, anniversary=None):
    reasons = set()

    # 1. Check if it's commonly used
    if is_commonly_used_six_digit_mpin(mpin):
        reasons.add("COMMONLY_USED")

    # 2. Extract parts with their origin
    parts_with_sources = extract_all_date_parts_with_sources(dob_self, dob_spouse, anniversary)

    # 3. Generate all permutations of 3 parts where total length is 6
    for combo in permutations(parts_with_sources, 3):
        part1, part2, part3 = combo
        combined = part1[0] + part2[0] + part3[0]

        if combined == mpin:
            # Add sources of the parts involved
            reasons.add(part1[1])
            reasons.add(part2[1])
            reasons.add(part3[1])

    strength = "WEAK" if reasons else "STRONG"
    return strength, list(reasons)
