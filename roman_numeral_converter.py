# Generates roman numeral from integer
def roman_generator(integer):
    nums = [('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)]
    numeral = str()
    
    # Converts integer to value based roman numeral
    while integer > 0:
        for roman, value in nums:
            if integer - value >= 0:
                integer -= value
                numeral = numeral + roman
                break

    # Repairs invalid sequence 4 in a row
    for item in range(len(nums)):
        roman = nums[item][0]
        last_roman = nums[item-1][0]
        if numeral.count(roman) == 4:
            numeral = numeral.replace(roman*4, roman + last_roman)

    # Repairs invalid sequence Large-Small-Large
    for item in range(len(numeral)):
        if item >= 2 and item < len(numeral):
            first = numeral[item-2]
            second = numeral[item-1]
            third = numeral[item]
            if first == third:
                val = dict(nums)[first] * 2
                for letter in nums:
                    if letter[1] == val:
                        roman = letter[0]
                        numeral = numeral.replace(first + second + third, second + roman)

    return numeral


# Converts roman numeral to integer
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

        
