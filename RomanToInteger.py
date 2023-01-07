class Solution:
    def romanToInt(self, roman):
        
        
        # Create a dictionary of Roman numeral values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Initialize the result
        result = 0

        # Iterate through the Roman numeral string
        for i in range(len(roman)):
            # Get the current and next Roman numeral
            current = roman[i]
            if i+1 < len(roman):
                next = roman[i+1]
            else:
                next = None

            # If the current Roman numeral is smaller than the next one,
            # it means that it is being subtracted (e.g. IV = 4)
            if next and roman_values[current] < roman_values[next]:
                result -= roman_values[current]
            else:
                result += roman_values[current]

        return result

        """
        :type s: str
        :rtype: int"""

    # romanToInt('XIV')
                
            
#              
            

            
            
sol = Solution()
sol.romanToInt("XVIIIIII")