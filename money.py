#!/usr/bin/python

(SINGULAR,PLURAL) = (0,1) # indices for coins[x]

# mapping of value of coins to tuple providing English name for a single
# of multiple coins of that value

coins = {
  1:   ('penny', 'pennies'),
  2:   ('2p piece','2p pieces'),
  5:   ('5p piece','5p pieces'),
  10:  ('10p piece','10p pieces'),
  20:  ('20p piece','20p pieces'),
  50:  ('50p piece','50p pieces'),
  100: ('pound coin','pound coins'),
  }

coin_values = coins.keys() # get a list of coin values
coin_values.sort() # sort into ascending order

def make_from(amount,coin_values):
  """Returns list of lists of solutions for making amount with coins.
     Coins must be sorted in assending order. Each element in the 
     result is a (coin_value, number_of_coins) pair"""
  
  all_solutions = []

  if not coin_values:
      return []

  coin_value = coin_values[0]

  if coin_value > amount:
      return []

  coin_values = coin_values[1:]

  max = amount / coin_value

  # look for a solution for every number of coins from 0 to max
  for number_of_coins in range(max + 1):
      remaining = amount - coin_value * number_of_coins
      if remaining == 0: # found a solution
          all_solutions.append([(coin_value, number_of_coins)])
      else: # look for solutions using other coins
          solutions_for_number = make_from(remaining, coin_values)
          for solution in solutions_for_number:
            solution.insert(0,(coin_value, number_of_coins))
            all_solutions.append(solution)
                              
  return all_solutions


if __name__ == '__main__':
    # find combinations of coin values that can make 100 pennies (1 UK pound)
    results = make_from(100, coin_values)

    # print the results
    print "%d solutions found" % len(results)

    n_result = 1
    for result in results:
      s = []
      for (value,number) in result:
        if number == 1:
          s.append("%d %s" % (number, coins[value][SINGULAR]))
        elif number > 1:
          s.append("%d %s" % (number, coins[value][PLURAL]))
      print "%d: %s" % (n_result, ', '.join(s))
      n_result+=1
