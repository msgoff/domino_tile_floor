import time
from random import randint

# keywords:
# domino tile dominos tiles matrix random snake worm snakes worms

# two headed snake AKA domino tile matrix
#
# after each
# complete realization is found, the script PAUSES.  To continue, press any key
# When satisfied, CTRL-C to stop.
#
# For a visual example of what this script accomplishes, see the game
# http://www.snakegame.net/ 
# The output of this script is a matrix of a size defined by two
# parameters, "numrows" by "numcolumns".  A boarder is placed around this
# matrix (the "None000" value) by placing the original matrix into a larger
# matrix of dimension (numrows+2) by (numcolumns+2).  The purpose behind
# this is to allow the user to specify an arbitrary shape other than just
# rectangles.
#
# Now that an arbitrarily shaped empty "matrix" is set up, start filling in
# the matrix with a sequence of integers such that at the end of the
# process the matrix is filled completely.  To start, choose a random
# location for 1.  Next, choose randomly a neighboring location to place 2.  Then
# place 3 next to 2 in a random location.  Each of this random choices has
# a maximum of four possible outcomes (up, down, left, right of the
# previous integer) but sometimes the number of choices is less (only up or
# down since left and right are occupied by integers.  This restriction of
# choices is what makes the code long: the number of choices depends on the
# number of open neighboring elements in the matrix.
#
# In the end, the integers can no longer be incremented as there are no more open neighboring 
# locations.  This is due to either the matrix being filled or the "snake"
# of previous integers has "cut itself off."  (There are open (zero-valued)
# elements, but they are inaccessible due to previous choices.)  Normally
# this realization would then be discarded since it was not filled.
# However, the "snake" could possibly grow from the other end (start at 1
# and decrement).  Thus this decreases the number of realizations one
# discards.
#
# to view previous successfully filled matrices, view
# suc(4,:,:)  # where "4" is the realization number of the matrix.
# other recorded information includes
# num_tries
# num_successes
# times

def print_grid(grid,num_rows):
  for x in range(num_rows+2):
    print(grid[x])

def create_grid_with_boundaries(num_rows,num_columns):
  grid = [[0 for x in range(num_columns+2)] for y in range(num_rows+2)] 

  for indx in range(num_columns+2):
    grid[0][indx]=None
  for indx in range(num_columns+2):
    grid[num_rows+1][indx]=None
  for indx in range(num_rows+2):
    grid[indx][0]=None
  for indx in range(num_rows+2):
    grid[indx][num_columns+1]=None
  return(grid)

def find_starting_location(grid):
  found_xy=False
  while not found_xy:
    x=randint(1,num_rows)
    y=randint(1,num_columns)
    #print("x="+str(x)+", y="+str(y))
    if (grid[x][y]==0):
      found_xy=True
  return x,y
  
def find_next_location(grid,current_x,current_y,watch_evolution):
#  print("finding next location")
#         north
#  west  "value"  east
#         south
  
  west=grid[current_x][current_y-1]
  east=grid[current_x][current_y+1]
  north =grid[current_x-1][current_y]
  south =grid[current_x+1][current_y] # correct
  if (watch_evolution):  
    print_grid(grid,num_rows)
    print("north=              "+str(north))
    print("west="+str(west)+", value="+str(grid[current_x][current_y])+", east="+str(east))
    print("south=           "+str(south))
    print(" ")
  no_remaining_choices=False
  #      0
  #   0  v  0
  #      0
  if ((north==0) and (south==0) and (east==0) and (west==0)):
    coin = randint(0,3)
    if (coin==0):
#      print("4 choices, 0") # south
      next_x=current_x+1
      next_y=current_y
    elif (coin==1):
#      print("4 choices, 1") # north
      next_x=current_x-1
      next_y=current_y
    elif (coin==2):
#      print("4 choices, 2") # east
      next_x=current_x
      next_y=current_y+1
    else: # (coin==3)
#      print("4 choices, 3") # west
      next_x=current_x
      next_y=current_y-1
    
  #   0  v  0
  #      0
  elif ((south==0) and (east==0) and (west==0)):
    coin = randint(0,2)
    if (coin==0):
#      print("3 choices V, 0") # south
      next_x=current_x+1
      next_y=current_y    
    elif (coin==1):
#      print("3 choices V, 1") # east
      next_x=current_x
      next_y=current_y+1
    else: #(coin==2):
#      print("3 choices V, 2") # west
      next_x=current_x
      next_y=current_y-1
  #      0
  #   0  v  0
  elif ((north==0) and (east==0) and (west==0)):
    coin = randint(0,2)
    if (coin==0):
#      print("3 choices ^, 0") # north
      next_x=current_x-1
      next_y=current_y  
    elif (coin==1):
#      print("3 choices ^, 1") # east
      next_x=current_x
      next_y=current_y+1
    else: #(coin==2):
#      print("3 choices ^, 2") # west
      next_x=current_x
      next_y=current_y-1
  #      0
  #   0  v
  #      0
  elif ((north==0) and (south==0) and (west==0)):
    coin = randint(0,2)
    if (coin==0):
#      print("3 choices <, 0") # north
      next_x=current_x-1
      next_y=current_y
    elif (coin==1):
#      print("3 choices <, 1") # south
      next_x=current_x+1
      next_y=current_y    
    else: #(coin==2):
#      print("3 choices <, 2") # west
      next_x=current_x
      next_y=current_y-1
  #      0
  #      v  0
  #      0
  elif ((north==0) and (south==0) and (east==0)):
    coin = randint(0,2)
    if (coin==0):
#      print("3 choices >, 0") # north
      next_x=current_x-1
      next_y=current_y
    elif (coin==1):
#      print("3 choices >, 1") # south
      next_x=current_x+1
      next_y=current_y    
    else: #(coin==2):
#      print("3 choices >, 2") # east
      next_x=current_x
      next_y=current_y+1
  #      0
  #      v
  #      0
  elif ((north==0) and (south==0)):
    coin = randint(0,2)
    if (coin==0):
#      print("2 choices over/under, 0") # north
      next_x=current_x-1
      next_y=current_y
    else: #(coin==1):
#      print("2 choices over/under, 1") # south
      next_x=current_x+1
      next_y=current_y    
  #   0  v  0
  elif ((east==0) and (west==0)):
    coin = randint(0,2)
    if (coin==0):
#      print("2 choices side-by-side, 0") # east
      next_x=current_x
      next_y=current_y+1
    else: #(coin==1):
#      print("2 choices side-by-side, 1") # west
      next_x=current_x
      next_y=current_y-1
  #      0
  #   0  v 
  elif ((north==0) and (west==0)):
    coin = randint(0,2)
    if (coin==0):
#      print("2 choices upper-left, 0") # north
      next_x=current_x-1
      next_y=current_y
    else: #(coin==1):
#      print("2 choices upper-left, 1") # west
      next_x=current_x
      next_y=current_y-1
  #      0
  #      v  0
  elif ((north==0) and (east==0)):
    coin = randint(0,2)
    if (coin==0):
#      print("2 choices upper-right, 0") # north
      next_x=current_x-1
      next_y=current_y
    else: #(coin==1):
#      print("2 choices upper-right, 1") # east
      next_x=current_x
      next_y=current_y+1
  #   0  v 
  #      0
  elif ((south==0) and (west==0)):
    coin = randint(0,2)
    if (coin==0):
#      print("2 choices lower-left, 0") # south
      next_x=current_x+1
      next_y=current_y    
    else: #(coin==1):
#      print("2 choices lower-left, 1") # west
      next_x=current_x
      next_y=current_y-1
  #      v  0
  #      0
  elif ((south==0) and (east==0)):
    coin = randint(0,2)
    if (coin==0):
#      print("2 choices lower-right, 0") # south
      next_x=current_x+1
      next_y=current_y    
    else: #(coin==1):
#      print("2 choices lower-right, 1") # east
      next_x=current_x
      next_y=current_y+1
  elif (north==0):
#    print("1 choice, north") # north
    next_x=current_x-1
    next_y=current_y
  elif (south==0):
#    print("1 choice, south") # south
    next_x=current_x+1
    next_y=current_y
  elif (east==0):
#    print("1 choice, east") # east
    next_x=current_x
    next_y=current_y+1
  elif (west==0):
#    print("1 choice, west") # west
    next_x=current_x
    next_y=current_y-1
  else:
    no_remaining_choices=True  
    next_x=-1
    next_y=-1
  
  return next_x,next_y,no_remaining_choices

def are_there_zeros_on_grid(grid,num_rows,num_columns):
  for indx in range(num_columns+2):
    for jndx in range(num_rows+2):
      if (grid[jndx][indx]==0):
        return True
  return False
  
# user defined variables
# dimensions of two dimensional grid:
num_rows = 9
num_columns = 9
watch_evolution=False
suppress_display=True
output_max=100

# initialize variables    
num_tries=0
num_successes=0

f=open('results.dat','w')
results_dic={}

start_time_between_successes = time.time()
while True: # search for random space-filling curves in the grid
  num_tries+=1
  start_time_this_iteration = time.time()

  grid=create_grid_with_boundaries(num_rows,num_columns)
  
  start_x,start_y=find_starting_location(grid)
  current_x=start_x
  current_y=start_y
  value=1
  grid[current_x][current_y]=value
  
  increment_head=True
  change_value_by=1
  while increment_head:
    next_x,next_y,no_remaining_choices=find_next_location(grid,current_x,current_y,watch_evolution)
    if no_remaining_choices:
      increment_head=False
      if (watch_evolution):
        print("no remaining locations for head")
    else:
      value+=1
      grid[next_x][next_y]=value
      current_x=next_x
      current_y=next_y
    if (watch_evolution):  
      wait = raw_input("    press enter to continue incrementing head")
  
  if (watch_evolution):
    print("switching to tail exploration")  
  current_x=start_x
  current_y=start_y
  value=0  
  increment_tail=True
  change_value_by=-1
  while increment_tail:
    next_x,next_y,no_remaining_choices=find_next_location(grid,current_x,current_y,watch_evolution)
    if no_remaining_choices:
      increment_tail=False
    else:
      value+=-1
      grid[next_x][next_y]=value
      current_x=next_x
      current_y=next_y
  if (watch_evolution):
    print("no remaining tail locations")
  
  if (num_tries%1000==0 and not suppress_display):
    print("num_tries="+str(num_tries))
    
  if (watch_evolution) and (are_there_zeros_on_grid(grid,num_rows,num_columns)):
    print("this snake does not fill the grid")
    print("num_tries="+str(num_tries))
    elapsed_time = time.time() - start_time_this_iteration     
    print("elapsed time: "+str(elapsed_time)+" seconds")
  if not are_there_zeros_on_grid(grid,num_rows,num_columns):
    if (not suppress_display):
      print("space-filling curve found!")  
      print_grid(grid,num_rows)
    num_successes+=1
    if (not suppress_display):
      print("number of tries: "+str(num_tries))
      print("number of successes: "+str(num_successes))
    elapsed_time = time.time() - start_time_between_successes
    if (not suppress_display):
      print("elapsed time: "+str(elapsed_time)+" seconds")
#    wait = raw_input("    press enter to continue to next grid attempt")
    start_time_between_successes = time.time()
    results_dic[num_successes]=[elapsed_time, num_tries]
    print(str(num_successes)+": "+str(elapsed_time)+" seconds, "+str(num_tries)+" tries")
    num_tries=0

    if (num_successes==output_max):
      for key,val in results_dic.iteritems():
        print(str(val[0]) +" "+ str(val[1]))
        f.write(str(val[0]) +" "+ str(val[1])+"\n")
      f.close()
      break
    
  if (watch_evolution):
    print("grid: ")
    print_grid(grid,num_rows)
    wait = raw_input("    press enter to continue to next grid attempt")
