import re

def main():
    # get the lines
    fp = open('games.txt', 'r')
    lines = fp.readlines()
    fp.close()
    
    power_sum = 0
    # test_lines = lines[:5]
    
    for game in lines:
        min_red = 0
        min_green = 0
        min_blue = 0
        power = 0
        
        # get rounds in game
        rounds = game.split(':')[1].split(';')
        # print(rounds)
        
        for round in rounds:
            # get color from rounds
            colors = round.split(',')
            # print(colors)
            
            for color in colors:
                raw_number = re.findall(r'\d+', color)
                number = int(''.join(raw_number))
                # print(number)
                # check if current color val is larger than previous minimum (must be new minimum)
                if "red" in color and number > min_red:
                    min_red = number
                elif "blue" in color and number > min_blue:
                    min_blue = number
                elif "green" in color and number > min_green:
                    min_green = number
        
        # print('min blue: ' + str(min_blue), ', min green: ' + str(min_green), ', min red: ' + str(min_red))    
        power = min_blue * min_green * min_red
        power_sum += power
                    
    print('sum of powers: ' + str(power_sum))        

if __name__ == '__main__':
    main()