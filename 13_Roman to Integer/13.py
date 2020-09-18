def romanToInt(s: str) -> int:
    total = 0
    i = 0
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    while i < len(s):
        # If this is the subtractive case.
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            total += values[s[i + 1]] - values[s[i]]
            i += 2
        # Else this is NOT the subtractive case.
        else:
            total += values[s[i]]
            i += 1
    return total


def romanToInt2(s: str) -> int:
    total = 0
    i = 0
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    while i < len(s):
        # This is the subtractive case.
        if i < len(s) - 1 and s[i:i+2] in values:
            total += values[s[i:i+2]]
            i += 2
        else:
            total += values[s[i]]
            i += 1
    return total