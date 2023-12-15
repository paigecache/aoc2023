import re

def main():
    # get the lines
    fp = open('games.txt', 'r')
    lines = fp.readlines()
    fp.close()
    
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14
    
    id_sum = 0
    #test_lines = lines[:10]
    
    for game in lines:
        isGamePossible = True
        
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
                # check if color possible
                if "red" in color and number > MAX_RED:
                    isGamePossible = False
                elif "blue" in color and number > MAX_BLUE:
                    isGamePossible = False
                elif "green" in color and number > MAX_GREEN:
                    isGamePossible = False
                
                # if game can't happen stop checking colors in round
                if isGamePossible is False:
                    break
            
            # if game can't happen stop checking colors in game
            if isGamePossible is False:
                break
            
        if isGamePossible is True:
            game_id_full = game.split(':')[0]
            game_id = int(game_id_full.split()[1])
            # print(str(game_id))
            id_sum += game_id
                    
    print('sum of calibration values: ' + str(id_sum))        

if __name__ == '__main__':
    main()