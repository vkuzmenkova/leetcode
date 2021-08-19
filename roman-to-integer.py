class Solution:
    def romanToInt(self, s: str) -> int:
        roman_arabic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = roman_arabic[s[0]]

        for i in range(1, len(s)):
            if roman_arabic[s[i]] > roman_arabic[s[i - 1]]:
                sum += roman_arabic[s[i]] - 2 * roman_arabic[s[i - 1]]
            else:
                sum += roman_arabic[s[i]]

        return sum
