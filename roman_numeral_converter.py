def convert(roman_numeral_string):
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    
    for pos in range(len(data)):
        numeral = data[pos]
        if pos == 0:
            total += nums[numeral]
        elif pos != len(data)-1:
            last_numeral = data[pos-1]
            next_numeral = data[pos+1]
            if nums[numeral] > nums[last_numeral]:
                total += nums[numeral]
                total -= nums[last_numeral] * 2
            else:
                total += nums[numeral]
        else:
            if numeral in ['I', 'V']:
                total += nums[numeral]
            else:
                last_numeral = data[pos-1]
                total += nums[numeral]
                total -= nums[last_numeral] * 2
    return total
        
