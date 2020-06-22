import os
import time

# Welcome Screen
tab = "\t\t\t\t\t"
os.system("cls")
for i in range(3):
    print(tab + "*"*34)
    
print(tab + "**  " + "XO"*13 + "  **")
print(tab + "**  " + "~"*len("| Welcome to TIC TAC TOE |") + "  **")
print(tab + "**  | " + "TIC TAC TOE".center(22) + " |  **")
print(tab + "**  " + "~"*len("| Welcome to TIC TAC TOE |") + "  **")
print(tab + "**  " + "XO"*13 + "  **")

for i in range(3):
    print(tab + "*"*34)
    
input("\n"+tab+"Press Enter to Start".center(26))
os.system('cls')

#initial board values
positions = ['1','2','3','4','5','6','7','8','9']
def board(pos , state):
    '''  Decide state of board and calls pboard()
    Parameters
    ----------
    pos : list
        Board values
    state : int
        initial board or current board
    Returns
    -------
    None.'''
    
    if state == 0:
        os.system('cls')
        print(tab+"Initial Board".center(31)+"\n")
        pboard(pos)
    else:
        os.system('cls')
        print(tab+"Current Board".center(31)+"\n")
        pboard(pos)

def pboard(values):
    '''  Prints the board with given board values.
    Parameters
    ----------
    values : list
        Board values
    Returns
    -------
    None.'''
    
    print(tab+"-"*31)
    print(tab+"|         "*3+"|")
    print(tab+"|    "+values[0] +"    |    "+values[1]+"    |    "+values[2]+"    |" )
    print(tab+"|         "*3+"|")
    print(tab+"-"*31)
    print(tab+"|         "*3+"|")
    print(tab+"|    "+values[3] +"    |    "+values[4]+"    |    "+values[5]+"    |" )
    print(tab+"|         "*3+"|")
    print(tab+"-"*31)
    print(tab+"|         "*3+"|")
    print(tab+"|    "+values[6] +"    |    "+values[7]+"    |    "+values[8]+"    |" )
    print(tab+"|         "*3+"|")
    print(tab+"-"*31)
        
def validate(pos,s):
        '''  validates conditions for winning.
        Parameters
        ----------
        pos : list
            Board values.
        s : character
            'X' or 'O'
        Returns
        -------
        bool
            True for win otherwise False.'''
        combinations = [[0,1,2],[3,4,5],[6,7,8]
                        ,[0,3,6],[1,4,7],[2,5,8]
                        ,[0,4,8],[2,4,6]]
        for comb in combinations:
            if pos[comb[0]] == s and pos[comb[1]]== s and pos[comb[2]]== s:
                    return True
        return False
    

def symbols(p1,p2):
    '''  Prints Symbols assigned for players.
    Parameters
    ----------
    p1 : String
        Player 1 Name.
    p2 : String
        Player 2 Name.
    Returns
    -------
    None.'''
    
    print("  "+p1 + " your symbol --> X\n")
    print("  "+p2 + " your symbol --> O\n\n")
    print("  (Enter position in between 1 to 9)\n\n")
    

def validate_input(pos):
    ''' Validates user position input.
    Parameters
    ----------
    pos : list
        Board values.
    Returns
    -------
    bool
        True if right , False if wrong.'''
        
    if(pos.isdigit() == False):
        print("  Invalid Choice!!")
        time.sleep(0.8)
        return False
    elif(int(pos) < 0 or int(pos) > 9):
        print("  Choice out of range !!")
        time.sleep(0.8)
        return False
    elif positions[int(pos)-1] == 'X' or positions[int(pos)-1] == 'O':
        print('  Position already taken!')
        time.sleep(0.8)
        return False
    return True

def p1chance():
    '''  takes player1 input and call validate_input().
    Returns
    -------
    result : bool
        True if player1 is winner , otherwise false. '''
        
    global positions
    board(positions,1)
    symbols(p1,p2)
    pos = input("  "+p1+" your position : ")
    while(validate_input(pos)==False):
        board(positions,1)
        symbols(p1,p2)
        pos = input("  "+p1+" your position : ")
    pos = int(pos)
    positions[pos-1] = 'X'
    board(positions,1)
    result = validate(positions , 'X')
    return result

def p2chance():
    '''  takes player2 input and call validate_input().
    Returns
    -------
    result : bool
        True if player2 is winner , otherwise false.'''
        
    global positions
    board(positions,1)
    symbols(p1,p2)
    pos = input("  "+p2+" your position : ")
    while(validate_input(pos)==False):
         board(positions,1)
         symbols(p1,p2)
         pos = input("  "+p2+" your position : ")
    pos = int(pos)
    positions[pos-1] = 'O'
    board(positions,1)
    result = validate(positions , 'O')
    return result
        

# input player1 name and validate it.
board(positions,0)
p1 = input("  Player1 Name : ")
while(p1.isalpha()==False):
    print("  Please enter a valid name !")
    time.sleep(0.8)
    board(positions,0)
    p1 = input("  Player1 Name : ")
    
# input player1 name and validate it.
board(positions,0)
p2 = input("  Player2 Name : ")
while(p2.isalpha()==False):
    print("  Please enter a valid name !")
    time.sleep(0.8)
    board(positions,0)
    p2 = input("  Player2 Name : ")


positions = [' ']*9

#Game Starts .....
while(True):
    if ' ' in positions:
        res = p1chance()
        if(res):
            print("\n\n"+tab +("Woah , " + p1 +" you won !!!").center(31))
            break
    else:
        print("\n"+tab+("Match Tied !!!").center(31))
        break

    if ' ' in positions:  
        res = p2chance()
        if(res):
            print("\n\n"+tab + ("Woah , " + p2 +" you won !!!").center(31))
            break
    else:
        print("\n"+tab+("Match Tied !!!").center(31))
        break

exit()

