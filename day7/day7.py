with open('./test-data.txt', 'r') as file:
  test_lines = [line.strip() for line in file.readlines()]
with open('./data.txt', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

from collections import Counter
from functools import reduce
import operator

def part_one(lines) -> str:
  def get_strength(cards):
    counts = Counter(cards).values()
    if 5 in counts:
      return 7 # 5 of a kind
    elif 4 in counts:
      return 6 # 4 of a kind
    elif 3 in counts:
      if 2 in counts:
        return 5 # full house
      return 4 # 3 of a kind
    elif list(counts).count(2) == 2:
      return 3 # two pair
    elif 2 in counts:
      return 2 # one pair
    return 1 # high card

  strengths = {card: i+2 for i, card in enumerate(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'])}
  hands = [{'cards': x, 'bid': int(y), 'strength': get_strength(list(x))} for line in lines for x, y in [line.split(' ')]]
  
  def custom_sort(hand):
    return (hand['strength'],) + tuple(strengths[card] for card in list(hand['cards']))

  sorted_hands = sorted(hands, key=custom_sort)

  return str(reduce(operator.add, [hand['bid'] * (i+1) for i, hand in enumerate(sorted_hands)]))

def part_two(lines) -> str:
  def get_strength(cards):
    counter = Counter(cards)
    counter_vals = counter.values()
    strength = 0

    if 5 in counter_vals:
      strength = 7 # 5 of a kind
    elif 4 in counter_vals:
      strength = 6 # 4 of a kind
    elif 3 in counter_vals:
      if 2 in counter_vals:
        strength = 5 # full house
      else:
        strength = 4 # 3 of a kind
    elif list(counter_vals).count(2) == 2:
      strength = 3 # two pair
    elif 2 in counter_vals:
      strength = 2 # one pair
    else:
      strength = 1 # high card
    
    if counter['J'] > 0:
      match strength:
        case 1: # high card
          if counter['J'] == 1:
            strength = 2 # one pair
        case 2: # one pair
          if counter['J'] == 1 or counter['J'] == 2:
            strength = 4 # 3 of a kind
        case 3: # two pair
          if counter['J'] == 1:
            strength = 5 # full house
          elif counter['J'] == 2:
            strength = 6 # 4 of a kind
        case 4: # 3 of a kind
          if counter['J'] == 1 or counter['J'] == 3:
            strength = 6 # 4 of a kind
        case 5: # full house
          if counter['J'] == 3 or counter['J'] == 2:
            strength = 7 # 5 of a kind
        case 6: # 4 of a kind
          if counter['J'] == 1 or counter['J'] == 4:
            strength = 7 # 5 of a kind
    
    return strength

  strengths = {card: i+2 for i, card in enumerate(['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'])}
  hands = [{'cards': x, 'bid': int(y), 'strength': get_strength(list(x))} for line in lines for x, y in [line.split(' ')]]

  def custom_sort(hand):
    return (hand['strength'],) + tuple(strengths[card] for card in list(hand['cards']))

  sorted_hands = sorted(hands, key=custom_sort)

  return str(reduce(operator.add, [hand['bid'] * (i+1) for i, hand in enumerate(sorted_hands)]))
  

print('--- Part One ---')
print(f'Test: {part_one(test_lines)}')
print(f'Actual: {part_one(lines)}')
print('--- Part Two ---')
print(f'Test: {part_two(test_lines)}')
print(f'Actual: {part_two(lines)}')