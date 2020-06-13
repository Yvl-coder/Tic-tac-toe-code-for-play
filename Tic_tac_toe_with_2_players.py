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
player1_choose_location = []
player2_choose_location = []
valid_location_board = [i+str(j) for i in 'abc' for j in range(1, 4)]

x_or_o_player1 = input("Player 1: Please choose your shape(capital 'X' or capital 'O'):\n") + ' '
if x_or_o_player1 != 'X ' and x_or_o_player1 != 'O ':
    raise ValueError("enter only capital 'X' or capital 'O'!")
x_or_o_player2 = 'X ' if x_or_o_player1 == 'O ' else 'O '
print('\nPlayer 2 shape is:', x_or_o_player2)

print('\n' + board_show + '\n')


def locatin_on_board_player1():
    global board
    global board_show
    global player1_choose_location
    global valid_location_board
    
    location = input("Player 1: Please enter a location:\n")
    
    if location in valid_location_board: 
        player1_choose_location += [location]
        valid_location_board.remove(location)
        board = board.replace(location, x_or_o_player1)
        board_show = board
    
        for i in valid_location_board:
            board_show = board_show.replace(i, '  ')
        
        return board_show + '\n'
    
    else:
        print('Player 1: You type illegal location or this location used before! Your turn is skip!\n')
        return board_show + '\n'

def locatin_on_board_player2():
    global board
    global board_show
    global player2_choose_location
    global valid_location_board
    
    location = input("Player 2: Please enter a location:\n")
    
    if location in valid_location_board: 
        player2_choose_location += [location]
        valid_location_board.remove(location)
        board = board.replace(location, x_or_o_player2)
        board_show = board
    
        for i in valid_location_board:
            board_show = board_show.replace(i, '  ')
        
        return board_show + '\n'
    
    else:
        print('Player 2: You type illegal location or this location used before! Your turn is skip!\n')
        return board_show + '\n'

def check_win_player1():
    c1 = 0
    c2 = 0
    
    for x in player1_choose_location:
        if x == 'a1' or x == 'b2' or x == 'c3':
            c1 += 1
   
        if x == 'a3' or x == 'b2' or x == 'c1':
            c2 += 1

    if c1 == 3 or c2 == 3:
        return True

    player1_choose_location_nums = [i[1] for i in player1_choose_location]
    player1_choose_location_letters = [i[0] for i in player1_choose_location]
      
    for i in player1_choose_location_nums:
        if player1_choose_location_nums.count(i) == 3:
            return True
        
    for j in player1_choose_location_letters:
        if player1_choose_location_letters.count(j) == 3:
            return True    
       
    return False

def check_win_player2():
    c1 = 0
    c2 = 0
    
    for x in player2_choose_location:
        if x == 'a1' or x == 'b2' or x == 'c3':
            c1 += 1
   
        if x == 'a3' or x == 'b2' or x == 'c1':
            c2 += 1

    if c1 == 3 or c2 == 3:
        return True

    player2_choose_location_nums = [i[1] for i in player2_choose_location]
    player2_choose_location_letters = [i[0] for i in player2_choose_location]
      
    for i in player2_choose_location_nums:
        if player2_choose_location_nums.count(i) == 3:
            return True
        
    for j in player2_choose_location_letters:
        if player2_choose_location_letters.count(j) == 3:
            return True    
       
    return False


def main():
    while True:   
        if not(check_win_player1() or check_win_player2()): 
            print(locatin_on_board_player1())
            print(locatin_on_board_player2()) if not(check_win_player1()) else ""
        
        elif check_win_player1(): 
            print('Player 1 win!')
            break
        
        elif check_win_player2():
            print('Player 2 win!')
            break
        
        else:
            print('Draw!')
            break

if __name__ == '__main__':
    main()
#work!