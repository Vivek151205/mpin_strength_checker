def is_commonly_used_four_digit_mpin(mpin: str) -> bool:
    """
    Returns True if the 4-digit MPIN is considered weak/common based on known patterns.
    """

    def all_digits_same(mpin):
        return mpin[0] == mpin[1] == mpin[2] == mpin[3]

    def is_consecutive(mpin):
        ascending = True
        descending = True
        for i in range(3):
            if int(mpin[i+1]) - int(mpin[i]) != 1:
                ascending = False
            if int(mpin[i]) - int(mpin[i+1]) != 1:
                descending = False
        return ascending or descending

    def has_repeat_pattern(mpin):
        return (mpin[0] == mpin[2] and mpin[1] == mpin[3]) or \
               (mpin[0] == mpin[1] and mpin[2] == mpin[3])

    def is_palindrome(mpin):
        return mpin == mpin[::-1]

    def is_year(mpin):
        year = int(mpin)
        return 1900 <= year <= 2100

    def has_many_zeroes(mpin):
        return mpin.count('0') >= 3

    def is_keyboard_pattern(mpin):
        COMMON_PATTERNS = {
            "1234", "4567", "7890",
            "7410", "8520", "9630",
            "159", "3572", "9512", "2580", "1470",
            "1245", "2563", "5698", "8965", "3265", "7532",
            "9874", "6541", "3214", "7896", "4563", "1236",
            "1258", "8963", "2369", "7852", "2301","0102"
        }
        return any(sorted(mpin) == sorted(p) for p in COMMON_PATTERNS)

    def has_consecutive_subsequence(mpin):
        digits = [int(d) for d in mpin]
        for i in range(len(digits) - 2):
            d1, d2, d3 = digits[i], digits[i+1], digits[i+2]
            if d2 - d1 == 1 and d3 - d2 == 1:
                return True
            if d1 - d2 == 1 and d2 - d3 == 1:
                return True
        return False

    # Apply all checks
    return (
        all_digits_same(mpin) or
        is_consecutive(mpin) or
        has_repeat_pattern(mpin) or
        is_palindrome(mpin) or
        is_year(mpin) or
        has_many_zeroes(mpin) or
        is_keyboard_pattern(mpin) or
        has_consecutive_subsequence(mpin)
    )

