import random

board = """    a     b     c
       |     |     
1   a1 |  b1 |  c1 
  _____|_____|_____
       |     |     
2   a2 |  b2 |  c2  
  _____|_____|_____
       |     |     
3   a3 |  b3 |  c3  
       |     |"""
board_show = """    a     b     c
       |     |     
1      |     |    
  _____|_____|_____
       |     |     
2      |     |    
  _____|_____|_____
       |     |     
3      |     |    
       |     |"""
player_choose_location = []
computer_choose_location = []
valid_location_board = [i+str(j) for i in 'abc' for j in range(1, 4)]

x_or_o_player = input("Player: Please choose your shape(capital 'X' or capital 'O'):\n") + ' '
if x_or_o_player != 'X ' and x_or_o_player != 'O ':
    raise ValueError("enter only capital 'X' or capital 'O'!")
x_or_o_computer = 'X ' if x_or_o_player == 'O ' else 'O '
print('\nComputer shape is:', x_or_o_computer)

print('\n' + board_show + '\n')


def locatin_on_board_player():
    global board
    global board_show
    global player_choose_location
    global valid_location_board
    
    location = input("Player: Please enter a location:\n")
    
    if location in valid_location_board: 
        player_choose_location += [location]
        valid_location_board.remove(location)
        board = board.replace(location, x_or_o_player)
        board_show = board
    
        for i in valid_location_board:
            board_show = board_show.replace(i, '  ')
        
        return board_show + '\n'
    
    else:
        print('You type illegal location or this location used before! Your turn is skip!\n')
        return board_show + '\n'

def locatin_on_board_computer():
    global board
    global board_show
    global computer_choose_location
    global valid_location_board
    
    print('Computer turn:\n')
    location = random.choice(valid_location_board)
     
    computer_choose_location += [location]
    valid_location_board.remove(location)
    board = board.replace(location, x_or_o_computer)
    board_show = board
    
    for i in valid_location_board:
        board_show = board_show.replace(i, '  ')
        
    return board_show + '\n'

def check_win_player():
    c1 = 0
    c2 = 0
    
    for x in player_choose_location:
        if x == 'a1' or x == 'b2' or x == 'c3':
            c1 += 1
   
        if x == 'a3' or x == 'b2' or x == 'c1':
            c2 += 1

    if c1 == 3 or c2 == 3:
        return True

    player_choose_location_nums = [i[1] for i in player_choose_location]
    player_choose_location_letters = [i[0] for i in player_choose_location]
      
    for i in player_choose_location_nums:
        if player_choose_location_nums.count(i) == 3:
            return True
        
    for j in player_choose_location_letters:
        if player_choose_location_letters.count(j) == 3:
            return True    
       
    return False

def check_win_computer():
    c1 = 0
    c2 = 0

    for x in computer_choose_location:
        if x == 'a1' or x == 'b2' or x == 'c3':
            c1 += 1
   
        if x == 'a3' or x == 'b2' or x == 'c1':
            c2 += 1

    if c1 == 3 or c2 == 3:
        return True

    computer_choose_location_nums = [i[1] for i in computer_choose_location]
    computer_choose_location_letters = [i[0] for i in computer_choose_location]
      
    for i in computer_choose_location_nums:
        if computer_choose_location_nums.count(i) == 3:
            return True
        
    for j in computer_choose_location_letters:
        if computer_choose_location_letters.count(j) == 3:
            return True    
       
    return False


def main():
    while True:
        if not(check_win_player() or check_win_computer()): 
            print(locatin_on_board_player())
            print(locatin_on_board_computer()) if not(check_win_player()) else ""
        
        elif check_win_player(): 
            print('You win!')
            break
        
        elif check_win_player2():
            print('Computer win!')
            break
        
        else:
            print('Draw!')
            break

if __name__ == '__main__':
    main()
#work!