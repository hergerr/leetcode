class Solution:
    symbols_descending = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }
    symbols_ascending = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

    def intToRoman(self, num: int) -> str:
        result = ''
        reminder = num
        while reminder > 0:
            first_digit = int(str(reminder)[0])
            if first_digit == 4 or first_digit == 9:
                value, char = self.get_subtractive_form(reminder)
            else:
                value, char = self.get_largest_symbol(reminder)
            reminder = reminder - value
            result += char

        return result

    def get_largest_symbol(self, number):
        for value, char in self.symbols_descending.items():
            if number - value < 0:
                continue
            else:
                return value, char
            
    def get_subtractive_form(self, number):
        for value, char in self.symbols_ascending.items():
            if number - value < 0:
                second_char = char
                if second_char == 'D' or second_char == 'M':
                    first_char = 'C'
                    first_value = 100
                elif second_char == 'L' or second_char == 'C':
                    first_char = 'X'
                    first_value = 10
                elif second_char == 'V' or second_char == 'X':
                    first_char = 'I'
                    first_value = 1
                return (value - first_value, first_char + second_char)


x = Solution()
y = x.intToRoman(1994)
print(y)