# The newly-improved calibration document consists of lines of text; each line 
# originally contained a specific calibration value that the Elves now need
# to recover. On each line, the calibration value can be found by combining the 
# first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are 12, 38, 15, and 77.
# Adding these together produces 142.

def main():
    # get the lines
    fp = open('calibration.txt', 'r')
    lines = fp.readlines()
    fp.close()
    
    total = 0
    
    for line in lines:
        numbers = ''
        
        # get numbers in each line
        for char in line:
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