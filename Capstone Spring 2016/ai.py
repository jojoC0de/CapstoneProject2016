#! /usr/bin/python

## \file  ai.py
#  \brief handles all functions related to the ai
#  \author John Stone
#  \date 2016
#  \version 1.0.1
#
    
import random, fight
random.seed()

## chooses a random move for the boss to use 
def ai_choose_random():
   move = random.randint(20, 23)

   return move

## function that is called to run the ai and allow it to make an informed
## guess on what the Player will use, and then with that guess, choose the
## best move against that. However, ~30% of the time, the ai will choose a random
## move 
def ai_choose_updated(move_prob, prev_moves, frequencies):
   move = parse_data(move_prob,prev_moves,frequencies)
   move = make_decision(move)
   return move

## function that is called within the main file.
## this function executes a certain ai strategy type given the iteration number
## that can be changed from within the options menu
def ai_choose_options(move_prob, prev_moves, frequencies, iteration):

   move = ai_choose_random()
   if iteration != 0:
      if iteration == 1:
         move = first_iteration(prev_moves, frequencies)
      elif iteration == 2:
         move = second_iteration(move_prob, frequencies, prev_moves)
      elif iteration == 3:
         move = third_iteration(move_prob, frequencies, prev_moves)
      elif iteration == 4:
         move = fourth_iteration(move_prob, frequencies, prev_moves)
      elif iteration == 5:
         move = fifth_iteration(move_prob, frequencies, prev_moves)
      elif iteration == 6:
         move = sixth_iteration(move_prob, frequencies, prev_moves)

   move = make_decision(move)
   return move

## Recreation of the first iteration of AI
## This iteration relied almost  completely on recent information,
## but would start to fail fairly early on
def first_iteration(prev_moves, move_prob):
   move = 20
   
   if len(prev_moves) >= 6:
      for i in range(0,6):
         temp = prev_moves[len(prev_moves)-i:len(prev_moves)]
         temp_freq = get_frequency(temp)
         move_prob = update_probabilities_updated(move_prob,temp_freq,1)
   else:
      for i in range(0, len(prev_moves)):
         temp = prev_moves[len(prev_moves)-i:len(prev_moves)]
         temp_freq = get_frequency(temp)
         move_prob = update_probabilities_updated(move_prob,temp_freq,1)
         
   move = get_move(move_prob)
   return move

## Recreation of the second iteration of AI
## This iteration relied on recent and past information,
## but would still fail often
def second_iteration(move_prob, frequencies, prev_moves):
   move_freq = get_frequencies(prev_moves)
   move_prob = get_probabilities_updated(move_prob, move_freq,2)
   move = get_move(move)
   
   return move

## recreation of the third iteration of AI
## Relies on old and new information and chooses a move given its
## likelihood of occurrence
def third_iteration(move_prob, frequencies, prev_moves):
   move_prob = get_probabilities_updated(move_prob, move_freq,3)
   move = get_move(move)
   
   return move

## recreation of the fourth iteration of AI
## The third iteration with randomness thrown in to make it less
## predictable
def fourth_iteration(move_prob, frequencies, prev_moves):
   move_prob = get_probabilities_updated(move_prob, move_freq,4)
   if random.random() > 0.70:
      move = random.randint(20,23)   
   ## build a tree given move_prob. make choice from those values
   else:
      move = get_move(move)
   
   return move


## recreation of the fifth iteration of AI
## Uses both old and new information with even weights, and builds a probability
## tree that it parses, and then returns the move it thinks the player will choose
## Has randomness thrown in to make it less predictable
def fifth_iteration(move_prob, frequencies, prev_moves):
   if len(prev_moves) == 0:
      move = random.randint(20,23)
   else:
      if random.random() > 0.70:
         move = random.randint(20,23)
         ## build a tree given move_prob. make choice from those values
      else:
         move = parse_tree(move_prob, prev_moves)
   return move

## recreation of the sixth iteration of AI
## This relies on old and new information, but weights itself such that new
## information is worth more than old information
def sixth_iteration(move_prob, frequencies, prev_moves):
   move = parse_data(move_prob,prev_moves,frequencies)
   return move

## Used in the Sixth Iteration
## This takes the most 7 most recent moves used, and this discounts
## and weights the information accordingly.
## It then determines which move is most likely to occur given the 2 probabilities,
## and returns the one that has the highest probability of occurence
def parse_data(move_prob, prev_moves, frequencies):
   move = 20
   temp = prev_moves[len(prev_moves)-7: len(prev_moves)]
   discount = 0.5
   weight_new = 0.6
   weight_old = 0.4
   total = 0
   
   freq = get_frequency(temp)
   prob = get_discounted_probability(temp,freq)
   ##find max of original and of recent moves
   original_move = get_move(move_prob)
   temp = get_move(prob)
   recent_moves = [prob[temp-20]] ##function will be used to get maximum value and index of the value

   if (move_prob[original_move-20]*weight_old) > (prob[temp-20] * weight_new):
      move = original_move
   else:
      move = temp

   return move

## parse tree will look at the top 2 most, or least, likely to occur moves,
## and then randomly choose between them the move the ai thinks the Player will
## use. The reason for this is to avoid the ai using predictable moves and add in some
## randomness.
#### weakness in decision arises when all probabilities are equal
def parse_tree(move_prob, prev_moves):
   move = 20
   moves = [0,0]
   probs = [0,0]
   first = True
   temp = [0,0,0,0]
   lowest_value_index = 0
   index_last_move = prev_moves[len(prev_moves) - 1] - 20

   for i in range(0,4):
      temp[i] = move_prob[i]

   if random.random() <= 0.70:
      for i in range(0,2):
         probs[i] = temp.pop(temp.index(max(temp)))
         moves[i] = move_prob.index(probs[0]) + 20
   else:
      for i in range(0,2):
         probs[i] = temp.pop(temp.index(min(temp)))
         moves[i] = move_prob.index(probs[0]) + 20

   move = random.choice(moves)
   
   return move

## using information the player can access, the ai will choose the best option given this
## information
def make_decision(player_move):
   boss_move = 0

   if player_move == 20:
      boss_move = 21
   elif player_move == 21:
      boss_move = 23
   elif player_move == 22:
      boss_move = 20
   elif player_move == 23:
      boss_move = 22
      
   return boss_move

## the function used to initialize the ai, which is called at the beginning of the program
## the function reads in information from a file and returns that information to be used
## and updated with later function
def ai_init_updated():
   recorded_moves = []
   frequencies = []

   f = open("data.dat")

   for line in f:
      for i, value in enumerate(line.split()):
         frequencies.append(int(value))

   total = frequencies[0] + frequencies[1] + frequencies[2] + frequencies[3]
   probabilities = [float(frequencies[0])/total, float(frequencies[1])/total,
                    float(frequencies[2])/total, float(frequencies[3])/total]
   f.close()
   return (frequencies, probabilities)

## Called whenever the user quits out of the program.
## This function will open a file and write the updated information to be used the next time
## the programis opened.
def file_update(frequency):
   w = open('data.dat','w')
   
   for i in range(0,len(frequency)):
      w.write(str(int(frequency[i])) + ' ')

   w.close()

   return None

## an update to the update_probabilities function that allows for differnent updates
## to occur given the current iteration
def update_probabilities_updated(past_probabilities, frequencies_recent, iteration):
   total = 0
   probabilities = []
   done = False
   #print past_probabilities

   for i in range(0,4):
      if not done:
         for j in range(0,4):
            total += frequencies_recent[j]
         done = True

      probabilities.append((past_probabilities[i] * 0.5) + ((float(frequencies_recent[i])/total) * 0.5))
   if iteration > 2:
      total=0
      for i in range(0,4):
         total+=probabilities[i]

      if total != 0:
         multiplier = 1/total
         #print multiplier
         for i in range(0,4):
            probabilities[i] = probabilities[i] * multiplier
   
   return probabilities

## updates the probabiliteis given the probabilities pulled from the file and the frequencies
## of the moves that the Player has used since the program was opened
def update_probabilities(past_probabilities, frequencies_recent):
   total = 0
   probabilities = []
   done = False
   #print past_probabilities

   for i in range(0,4):
      if not done:
         for j in range(0,4):
            total += frequencies_recent[j]
         done = True

      probabilities.append((past_probabilities[i] * 0.5) + ((float(frequencies_recent[i])/total) * 0.5))

   total=0
   for i in range(0,4):
      total+=probabilities[i]

   if total != 0:
      multiplier = 1/total
      #print multiplier
      for i in range(0,4):
         probabilities[i] = probabilities[i] * multiplier
   return probabilities

## updates the frequency of the moves used by the player given the frequency of moves and
## the previous moves
def update_frequencies(move_frequencies, prev_moves):
   move_frequencies[prev_moves[len(prev_moves)-1]-20] += 1
   return move_frequencies

## function that returns the frequency of the moves used given the moves the player has used
def get_frequency(moves_used):
   frequency = [0,0,0,0]

   for i in range(0,len(moves_used)):
      frequency[moves_used[i]-20] += 1

   return frequency

## function that returns the probability of a move given the frequency of occurrence
def get_probability(frequency):
   total = 0
   prob = []
   for i in range(0,4):
      total+= frequency[i]

   for i in range(0,4):
      prob.append(float(frequency[i])/total)

   return prob

## Used in the Fourth Iteration
## Sorts the move_prob in order of maximum to minimum in terms of their position in the list
def get_max(move_prob):
   ## used as a list of places in terms of their 
   prob_list = [0,0,0,0]
   temp = []
   for i in range(0,4):
      index = -1
      if i == 0:
         temp.append(i)
      else:
         if move_prob[i] >= move_prob[temp[0]]:
            temp.insert(0,i)
         elif len(temp) == 2:
            if move_prob[i] >= move_prob[temp[1]]:
               temp.insert(1,i)
            else:
               temp.append(i)
         elif len(temp) == 3:
            if move_prob[i] >= move_prob[temp[1]]:
               temp.insert(1,i)
            elif move_prob[i] >= move_prob[temp[2]]:
               temp.insert(2,i)
            else:
               temp.append(i)
         else:
            temp.append(i)
   return temp

## Used in the Fourth Iteration
## Funtion that parses  the move probability and returns a choice
## based on probability of occurrence 
def get_move(move_prob):
   max_list = get_max(move_prob)
   #print max_list
   max_index = max_list[0]
   if move_prob[0] == move_prob[1]:
      max_index = [max_index,max_list[1]]
      if move_prob[0] == move_prob[2]:
         max_index.append(max_list[2])
         if move_prob[0] == move_prob[3]:
            max_index.append(max_list[3])
      max_index = random.choice(max_index)
   
   return max_index + 20

## Used in the Sixth Iteration
## Create a pseudo-randomly generated set of moves to be used in the case
## that the sixth iteration is being used so it can still make an
## "informed" decision
def create_first_set(move_prob):
   move_set = []

   for i in range(0,7):
      temp = random.random()
      if temp <= move_prob[0]:
         move_set.append(20)
      elif temp > move_prob[0] and temp <= (move_prob[0]+move_prob[1]):
         move_set.append(21)
      elif temp > (move_prob[0]+move_prob[1]) and temp <= (move_prob[0]+move_prob[1]+move_prob[2]):
         move_set.append(22)
      else:
         move_set.append(23)
         
   return move_set

## Used in multiple Iterations
## returns a probability in which new information is weighted and discounted
## depending on how recent it has occurred
def get_discounted_probability(move_set,freq):
   temp = [0,0,0,0]
   for i in range(0,len(move_set)):
      temp[move_set[i]-20] += (float(freq[move_set[i]-20])/len(move_set))/(len(move_set)-i)
      #* float((7-i))/7
   total = temp[0]+temp[1]+temp[2]+temp[3]
   if total !=1:
      multiplier = 1/total
      for i in range(0,4):
         temp[i]*=multiplier
      
   return temp

