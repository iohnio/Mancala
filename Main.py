CUP_AMOUNT = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]


def get_player():
  """                                                                                                                                       
  A function to recieve the players' names.                                                                          
  :return: The names of both players from the input.   
  """
  player1 = input("Player 1 please tell me your name: ")
  player2 = input("Player 2 please tell me your name: ")
  return player1, player2


def short_name(name):
  """
  A helper function to adjust the amount of letters in a name so the board is printed correctly.
  :param name: the name of the player to determine if it should be truncated, extended, or unchanged.
  """
  if len(name) > 6:
    return name[:6]
  elif len(name) < 6:
    return name + " "*(6-len(name))
  else:
    return name

  
def initialize_game():
  """
  A function to call both the get_player and short_name functions.
  :return: The updated names of both players.
  """
  player1, player2 = get_player()
  player1 = short_name(player1)
  player2 = short_name(player2)
  return player1, player2


def format_mancala_board(CUP_AMOUNT):
  """
  A helper function to adjust the spaces in a number if it becomes double digits so the board is printed correctly.
  :param name CUP_AMOUNT: A list of numbers to change their format
  :return: A new list of updated numbers
  """
  formatted_cups = []
  for i in range(len(CUP_AMOUNT)):
      if i in (0, 7):
        if CUP_AMOUNT[i] < 10:
          formatted_cups.append(f"{CUP_AMOUNT[i]} ")
        else:
            formatted_cups.append(f"{CUP_AMOUNT[i]}")
      else:
          if CUP_AMOUNT[i] < 10:
            formatted_cups.append(f" {CUP_AMOUNT[i]}")
          else:
              formatted_cups.append(f"{CUP_AMOUNT[i]}")
  return formatted_cups


def draw_board(CUP_AMOUNT, player1, player2):
  """
  A function to draw the mancala board including the players' names and stones. 
  :param CUP_AMOUNT: A list of numbers representing the amount of stones in each cup. 
  :param player1: The name of player1 to print on the mancala board. 
  :param player2: The name of player2 to print on the mancala board.
  """
  formatted_cups = format_mancala_board(CUP_AMOUNT)
  board = [
      "*********************************************************",
      "*      *Cup   *Cup   *Cup   *Cup   *Cup   *Cup   *      *",
      "*      *     1*     2*     3*     4*     5*     6*      *",
      "*      *Stones*Stones*Stones*Stones*Stones*Stones*      *",
      f"*{player2}*    {formatted_cups[1]}*    {formatted_cups[2]}*    {formatted_cups[3]}*    {formatted_cups[4]}*    {formatted_cups[5]}*    {formatted_cups[6]}*{player1}*",
      "*      *      *      *      *      *      *      *      *",
      "*      *******************************************      *",
      "*      *Cup   *Cup   *Cup   *Cup   *Cup   *Cup   *      *",
      "*Stones*    13*    12*    11*    10*     9*     8*Stones*",
      f"*{formatted_cups[0]}    *Stones*Stones*Stones*Stones*Stones*Stones*{formatted_cups[7]}    *",
      f"*      *    {formatted_cups[13]}*    {formatted_cups[12]}*    {formatted_cups[11]}*    {formatted_cups[10]}*    {formatted_cups[9]}*    {formatted_cups[8]}*      *",
      "*      *      *      *      *      *      *      *      *",
      "*********************************************************"
  ]

  for row in board:
      print(row)
      

def take_turn(player, game_cups, CUP_AMOUNT):
  """
  A function that handles a player's turn by distributing stones in the cups according to the game rules.
  :param player: To determine which player takes the turn.
  :param game_cups: The player's input of how many stones they want to move.
  :param CUP_AMOUNT: A list of numbers representing the amount of stones in each cup.
  """ 
  if player == player1 or player == player2:
      if (1 <= game_cups <= 6 or 8 <= game_cups <= 13) and CUP_AMOUNT[game_cups] != 0:
          stones_to_distribute = CUP_AMOUNT[game_cups]
          CUP_AMOUNT[game_cups] = 0
          last_cup = 0

          # Distributes the stones in a clockwise manner
          for i in range(stones_to_distribute):
              game_cups = (game_cups + 1) % 14
              CUP_AMOUNT[game_cups] += 1
              
          # Checks if the last stone was placed in the player's mancala
          last_cup = game_cups
          if last_cup == 0 or last_cup == 7:
            print("Your last stone landed in a mancala.")
            print("Go again please...")
            draw_board(CUP_AMOUNT, player1, player2)
            if check_clear(CUP_AMOUNT, 1, 6) == 0 or check_clear(CUP_AMOUNT, 8, 13) == 0:
              playing = False
            else:
                moves = int(input(f"{player.strip()} What cup do you want to move? "))
                take_turn(player, moves, CUP_AMOUNT)
                
      # Checks if the player chose a mancala 
      elif game_cups == 0 or game_cups == 7:
          print("You cannot move stones out of the mancala.")
          print("Go again please...")
          draw_board(CUP_AMOUNT, player1, player2)
          moves = int(input(f"{player.strip()} What cup do you want to move? "))
          take_turn(player, moves, CUP_AMOUNT)

      # Checks if the player chose an empty cup    
      else:
          print("There are no stones in that cup.")
          print("Go again please...")
          draw_board(CUP_AMOUNT, player1, player2)
          moves = int(input(f"{player.strip()} What cup do you want to move? "))
          take_turn(player, moves, CUP_AMOUNT)


def check_clear(CUP_AMOUNT, start, end):
  """
  A helper function that calculates the total amount of stones in a row.
  :param CUP_AMOUNT: A list of numbers representing the amount of stones in each cup.
  :param start: The start of a row to count.
  :param end: The end of a row to stop counting.
  :return: The total stone count in a row.
  """ 
  total = 0
  for i in range(start, end + 1):
      total += CUP_AMOUNT[i]
  return total


def determine_winner(player1_score, player2_score):
  """
  A helper function that compares the players' scores to determine a winner.
  :param player1_score: The amount of stones in player1's mancala.
  :param player2_score: The amount of stones in player2's mancala.
  """ 
  if player1_score > player2_score:
      print(f"{player1.strip()} is the winner")
  elif player1_score < player2_score:
      print(f"{player2.strip()} is the winner")
  else:
      print("It's a tie!")


def run_game(player1,player2):
  """
  A function that starts the game with player1 and continues to switch turns until there is a winner.
  :param player1: The name of player1 for the draw_board function and to switch turns.
  :param player2: The name of player2 for the draw_board function and to switch turns.
  """
  playing = True
  current_player = player1
  while playing:

    draw_board(CUP_AMOUNT, player1, player2)
    valid_move = False
    while not valid_move:
        moves = int(input(f"{current_player.strip()} What cup do you want to move? "))
        take_turn(current_player, moves, CUP_AMOUNT)
        valid_move = True

    # Checks the first and second rows to end the game if one is empty   
    if check_clear(CUP_AMOUNT, 1, 6) == 0 or check_clear(CUP_AMOUNT, 8, 13) == 0:
      playing = False

    # Checks to switch turns
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

  # Determines the winner based on the number of stones in the mancalas
  player1_score = CUP_AMOUNT[7]
  player2_score = CUP_AMOUNT[0]
  determine_winner(player1_score, player2_score)      

  
if __name__ == "__main__":
  player1, player2 = initialize_game()
  run_game(player1, player2)
