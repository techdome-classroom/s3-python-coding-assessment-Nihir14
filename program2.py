class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Roman numerals and their values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Initialize result
        result = 0
        
        # Iterate through the string
        for i in range(len(s)):
            # If this is not the last character and the current numeral is smaller than the next one
            if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
                result -= roman_values[s[i]]
            else:
                result += roman_values[s[i]]

        return result
