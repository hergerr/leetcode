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

    def intToRomanBis(self, num:int):
        ones = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
        tens = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
        hundrets = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
        thousands = {0: '', 1: 'M', 2: 'MM', 3: 'MMM'}

        return thousands[(num // 1000)] + hundrets[((num % 1000) // 100)] + tens[((num % 100) // 10)] + ones[(num % 10)]

x = Solution()
y = x.intToRomanBis(1994)
print(y)