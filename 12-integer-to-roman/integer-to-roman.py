class Solution:
    def intToRoman(self, num: int) -> str:
        # Mapping of values to Roman numerals in descending order
        value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
            (1, "I")
        ]
        
        roman = []
        for val, symbol in value_map:
            if num == 0:
                break
            count = num // val
            roman.append(symbol * count)
            num %= val
            
        return "".join(roman)