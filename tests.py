from tictactoe import initial_state, player, actions, result, winner, terminal, utility, minimax

# 1. Initial state is array 3x3 array of None
start1 = initial_state()
assert(all(row.count(None) == 3 for row in start1) and len(start1) == 3)

# 2. player returns correct mark
assert(player(initial_state()) == "X")
statea2 = initial_state()
statea2[0][0] = "X"
assert(player(statea2) == "O")
stateb2 = initial_state()
stateb2[0][0] = "X"
stateb2[1][1] = "O"
stateb2[0][2] = "X"
stateb2[0][1] = "O"
assert(player(stateb2) == "X")

# 3. actions returns list with correct number of moves
assert(len(actions(initial_state())) == 9)
#print(actions(initial_state()))
statea3 = initial_state()
statea3[0][0] = "X"
#print(actions(statea3))
assert(len(actions(statea3)) == 8)
stateb3 = initial_state()
stateb3[0][0] = "X"
stateb3[1][1] = "O"
stateb3[0][2] = "X"
stateb3[0][1] = "O"
#print(actions(stateb3))
assert(len(actions(stateb3)) == 5)

# 4. result works
#print(result(initial_state(), (0, 0)))
state4 = initial_state()
state4[0][0] = "X"
#print(result(state4, (1,1)))
#print(result(result(state4, (1,1)), (0, 2)))

# 5. winner works
    # horizontal
stateh5 = initial_state()
stateh5[1] = ["X", "X", "X"]
stateh5[0] = ["O", "O", None]
assert(winner(stateh5) == "X")
    #vertical
statev5 = initial_state()
statev5[0][1] = "O"
statev5[2][1] = "O"
statev5[1] = ["X", "O", "X"]
assert(winner(statev5) == "O")
    #diagonal left
statedl5 = initial_state()
statedl5[0][0] = "O"
statedl5[2][2] = "O"
statedl5[1] = ["X", "O", "X"]
assert(winner(statedl5) == "O")
    #diagonal right
statedr5 = initial_state()
statedr5[0][2] = "X"
statedr5[2][0] = "X"
statedr5[1] = ["O", "X", "O"]
assert(winner(statedl5) == "O")
assert(winner([["X", "O", "O"],["O", "O", "X"],["X", "X", "O"]]) == None)

# 6. terminal works
assert(terminal(stateh5) == True)
assert(terminal(stateb3) == False)
assert(terminal([["X", "O", "O"],["O", "O", "X"],["X", "X", "O"]]) == True)

# 7. utility works
assert(utility(stateh5) == 1)
assert(utility(stateb3) == 0)
assert(utility(initial_state()) == 0)
assert(utility(statedl5) == -1)
assert(utility([["X", "O", "O"],["O", "O", "X"],["X", "X", "O"]]) == 0)

# 8. minimax works
# print([None, "X", "O"])
# print(["O", "O", "X"])
# print([None, "X", None])
# print(minimax([[None, "X", "O"],["O", "O", "X"],[None, "X", None]]))





print("all assertions passed")