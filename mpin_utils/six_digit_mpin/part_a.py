def is_commonly_used_six_digit_mpin(mpin: str) -> bool:
    """
    Returns True if the 6-digit MPIN is considered weak/common based on known patterns.
    """

    def is_consecutive(mpin):
        return mpin in "0123456789" or mpin in "9876543210"

    def is_repeated_digit(mpin):
        return all(ch == mpin[0] for ch in mpin)

    def is_palindrome(mpin):
        return mpin == mpin[::-1]

    def is_repeating_pattern(mpin):
        return (
            mpin[:2] * 3 == mpin or
            mpin[:3] * 2 == mpin or
            mpin[:1] * 6 == mpin or
            mpin[:2] + mpin[:2] + mpin[:2] == mpin
        )

    keyboard_patterns = [
        "123456", "654321", "121212", "112233", "123123", "789456",
        "258369", "147258", "321321", "159357", "246810"
    ]
    def is_keyboard_pattern(mpin):
        return any(sorted(mpin) == sorted(pattern) for pattern in keyboard_patterns)

    def has_many_zeros(mpin):
        return mpin.count("0") > 3 or mpin[0] == "0"

    def is_strictly_consecutive_subsequence(mpin):
        for i in range(1, len(mpin)):
            if not (int(mpin[i]) - int(mpin[i - 1]) in {1, -1}):
                return False
        return True

    return (
        is_consecutive(mpin) or
        is_repeated_digit(mpin) or
        is_palindrome(mpin) or
        is_repeating_pattern(mpin) or
        is_keyboard_pattern(mpin) or
        has_many_zeros(mpin) or
        is_strictly_consecutive_subsequence(mpin)
    )
