with open('./test-data.txt', 'r') as file:
  test_lines = [line.strip() for line in file.readlines()]
with open('./data.txt', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

strengths = {card: i+2 for i, card in enumerate(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'])}

from collections import Counter
from functools import reduce
import operator

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

def part_one(lines) -> str:
  hands = [{'cards': x, 'bid': int(y), 'strength': get_strength(list(x))} for line in lines for x, y in [line.split(' ')]]
  
  def custom_sort(hand):
    return (hand['strength'],) + tuple(strengths[card] for card in list(hand['cards']))

  sorted_hands = sorted(hands, key=custom_sort)

  return str(reduce(operator.add, [hand['bid'] * (i+1) for i, hand in enumerate(sorted_hands)]))

def part_two(lines) -> str:
  pass
  

print('--- Part One ---')
print(f'Test: {part_one(test_lines)}')
print(f'Actual: {part_one(lines)}')
print('--- Part Two ---')
print(f'Test: {part_two(test_lines)}')
print(f'Actual: {part_two(lines)}')