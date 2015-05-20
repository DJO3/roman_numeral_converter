def convert(roman_numeral_string):
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    
    for pos in range(len(roman_numeral_string)):
        numeral = roman_numeral_string[pos]
        if pos == 0:
            total += nums[numeral]
        elif pos != len(roman_numeral_string)-1:
            last_numeral = roman_numeral_string[pos-1]
            next_numeral = roman_numeral_string[pos+1]
            if nums[numeral] > nums[last_numeral]:
                total += nums[numeral]
                total -= nums[last_numeral] * 2
            else:
                total += nums[numeral]
        else:
            last_numeral = roman_numeral_string[pos-1]
            if numeral != 'M' and nums[numeral] <= nums[last_numeral]:
                total += nums[numeral]
            else:
                total += nums[numeral]
                total -= nums[last_numeral] * 2
    return total

        
