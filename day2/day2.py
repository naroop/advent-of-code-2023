with open('./day2.txt', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

bag_max = { 'red': 12, 'green': 13, 'blue': 14 }

def part_one():
  games = []
  # games = [
  #   game_number
  #   for line in lines
  #   for game_number in [int(line.split(':')[0][5:])]
  #   if all(
  #       all(int(count) <= bag_max[color] for count, color in [color_count.strip().split(' ') for color_count in handfull.split(',')])
  #       for handfull in line.split(':')[1].split(';')
  #   )
  # ]
  for line in lines:
    game_number = int(line.split(':')[0][5:])
    valid = True

    for handfull in line.split(':')[1].split(';'):
      if not valid:
        break

      for color_count in handfull.split(','):
        count, color = color_count.strip().split(' ')
        if int(count) > bag_max[color]:
          valid = False
          break

    if valid:
      games.append(game_number)

  print(f'Answer is: {sum(games)}')
    
from collections import defaultdict
from functools import reduce
import operator

def part_two():
  powers = []

  for line in lines:
    max_colors = defaultdict(lambda: 0)

    for handfull in line.split(':')[1].split(';'):
      for color_count in handfull.split(','):
        count, color = color_count.strip().split(' ')
        if int(count) > max_colors[color]:
          max_colors[color] = int(count)

    powers.append(reduce(operator.mul, max_colors.values(), 1))

  print(f'Answer is: {sum(powers)}')
  

print('--- Part One ---')
part_one()
print('--- Part Two ---')
part_two()