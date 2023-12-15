# Your calculation isn't quite right. It looks like some of the digits are actually
# spelled out with letters: one, two, three, four, five, six, seven, eight, and nine
# also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last
# digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. 
# Adding these together produces 281.

# What is the sum of all of the calibration values?

def main():
    # get the lines
    fp = open('calibration.txt', 'r')
    lines = fp.readlines()
    fp.close()
    
    total = 0
    # test_lines = lines[:20]
    
    for line in lines:
        # print("\nstart")
        
        line_new = line.rstrip()
        # print(line_new)
        
        # replace each number string with the value
        line_new = line_new.replace('one', 'o1e')
        line_new = line_new.replace('two', 't2o')
        line_new = line_new.replace('three', 't3e')
        line_new = line_new.replace('four', 'f4r')
        line_new = line_new.replace('five', 'f5e')
        line_new = line_new.replace('six', 's6x')
        line_new = line_new.replace('seven', 's7n')
        line_new = line_new.replace('eight', 'e8t')
        line_new = line_new.replace('nine', 'n9e')
        # print(line_new)
        
        numbers = ''
        
        # get numbers in each line
        for char in line_new:
            if char.isdecimal():
                numbers += char
        # print(numbers)
        
        cb_string = ''
        # check if 1 digit or 1+
        if (len(numbers) == 1):
            cb_string += numbers
            cb_string += numbers
        else:
            cb_string += numbers[0]
            cb_string += numbers[-1]
        # print(cb_string)
    
        # add together calibration values
        cb_value = int(cb_string)
        total += cb_value
    
    print('sum of calibration values: ' + str(total))
    

if __name__ == '__main__':
    main()