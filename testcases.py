from datetime import datetime
from mpin_utils.four_digit_mpin.part_c import find_weak_four_digit_mpin_reasons
from mpin_utils.six_digit_mpin.part_c import find_weak_six_digit_mpin_reasons


def format_date(date_str):
    """Convert DDMMYYYY to datetime.date"""
    try:
        return datetime.strptime(date_str, "%d%m%Y").date()
    except Exception:
        return None


def compare_results(mpin, dob, spouse, anniv, expected_strength, expected_reasons, actual_strength, actual_reasons):
    match_strength = actual_strength == expected_strength
    match_reasons = set(actual_reasons) == set(expected_reasons)

    print(f"\n MPIN: {mpin}")
    print(f" DOB: {dob}, SPOUSE_DOB: {spouse}, ANNIVERSARY: {anniv}")
    print(f" Expected Strength: {expected_strength}")
    print(f" Expected Reasons : {expected_reasons}")
    print(f" Actual Strength  : {actual_strength}")
    print(f" Actual Reasons   : {actual_reasons}")

    if match_strength and match_reasons:
        print(" RESULT: PASSED ")
    else:
        print(" RESULT: FAILED ")


def run_test_cases():
    print("====== 4-Digit MPIN Tests ======")
    test_cases_4 = [
        {"mpin": "1234", "dob": "01011990", "spouse": "05051991", "anniv": "12062020",
         "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},

        {"mpin": "0101", "dob": "01011990", "spouse": "05051991", "anniv": "12062020",
         "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED", "DEMOGRAPHIC_DOB_SELF"]},

        {"mpin": "1111", "dob": "11071993", "spouse": None, "anniv": None,
         "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},

        {"mpin": "2580", "dob": "25081997", "spouse": "01012001", "anniv": "15022018",
         "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},

        {"mpin": "4321", "dob": "02021992", "spouse": "03031991", "anniv": "04041990",
         "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},

        {"mpin": "0701", "dob": "07011999", "spouse": "07011995", "anniv": None,
         "expected_strength": "WEAK", "expected_reasons": ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE"]},

        {"mpin": "0112", "dob": "01121999", "spouse": None, "anniv": None,
         "expected_strength": "WEAK", "expected_reasons": ["DEMOGRAPHIC_DOB_SELF"]},

        {"mpin": "2001", "dob": "01012001", "spouse": "02022002", "anniv": "03032003",
         "expected_strength": "WEAK", "expected_reasons": ["DEMOGRAPHIC_DOB_SELF", "COMMONLY_USED", "DEMOGRAPHIC_DOB_SPOUSE", "DEMOGRAPHIC_ANNIVERSARY"]},

        {"mpin": "2000", "dob": "01012000", "spouse": None, "anniv": None,
         "expected_strength": "WEAK", "expected_reasons": ["DEMOGRAPHIC_DOB_SELF", "COMMONLY_USED"]},

        {"mpin": "1900", "dob": "01011900", "spouse": None, "anniv": None,
         "expected_strength": "WEAK", "expected_reasons": ["DEMOGRAPHIC_DOB_SELF", "COMMONLY_USED"]}
    ]

    for test in test_cases_4:
        dob = format_date(test["dob"]) if test["dob"] else None
        spouse = format_date(test["spouse"]) if test["spouse"] else None
        anniv = format_date(test["anniv"]) if test["anniv"] else None

        actual_strength, actual_reasons = find_weak_four_digit_mpin_reasons(
            test["mpin"], dob, spouse, anniv
        )

        compare_results(test["mpin"], test["dob"], test["spouse"], test["anniv"],
                        test["expected_strength"], test["expected_reasons"],
                        actual_strength, actual_reasons)

    print("\n====== 6-Digit MPIN Tests ======")
    test_cases_6 = [
        {"mpin": "123456", "dob": "01011990", "spouse": "05051991", "anniv": "12062020",
         "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},

        {"mpin": "010199", "dob": "01011999", "spouse": None, "anniv": None,
         "expected_strength": "WEAK", "expected_reasons": ["DEMOGRAPHIC_DOB_SELF", "COMMONLY_USED"]},

        {"mpin": "112233", "dob": "11071993", "spouse": None, "anniv": None,
         "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},

        {"mpin": "258963", "dob": "25081997", "spouse": "01012001", "anniv": "15022018",
         "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},

        {"mpin": "200000", "dob": "01012000", "spouse": None, "anniv": None,
         "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},

        {"mpin": "010120", "dob": "01012020", "spouse": None, "anniv": None,
         "expected_strength": "WEAK", "expected_reasons": ["DEMOGRAPHIC_DOB_SELF", "COMMONLY_USED"]},

        {"mpin": "000000", "dob": "01011999", "spouse": "02021998", "anniv": "03031997",
         "expected_strength": "WEAK", "expected_reasons": ["COMMONLY_USED"]},

        {"mpin": "190120", "dob": "19012000", "spouse": None, "anniv": None,
         "expected_strength": "WEAK", "expected_reasons": ["DEMOGRAPHIC_DOB_SELF"]},

        {"mpin": "010505", "dob": "01010101", "spouse": "05050505", "anniv": None,
         "expected_strength": "WEAK", "expected_reasons": ["DEMOGRAPHIC_DOB_SELF", "DEMOGRAPHIC_DOB_SPOUSE", "COMMONLY_USED"]}
    ]

    for test in test_cases_6:
        dob = format_date(test["dob"]) if test["dob"] else None
        spouse = format_date(test["spouse"]) if test["spouse"] else None
        anniv = format_date(test["anniv"]) if test["anniv"] else None

        actual_strength, actual_reasons = find_weak_six_digit_mpin_reasons(
            test["mpin"], dob, spouse, anniv
        )

        compare_results(test["mpin"], test["dob"], test["spouse"], test["anniv"],
                        test["expected_strength"], test["expected_reasons"],
                        actual_strength, actual_reasons)


if __name__ == "__main__":
    run_test_cases()
