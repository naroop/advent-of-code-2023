with open('./test-data.txt', 'r') as file:
  test_lines = [line.strip() for line in file.readlines()]
with open('./data.txt', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

from functools import reduce
import operator
def part_one(lines):
  races = [{"time": t, "distance": d} for t, d in zip(list(map(int, lines[0].split()[1:])), list(map(int, lines[1].split()[1:])))]
  ways_to_win = []

  for race in races:
    min_holding_time = 0
    for ms_holding_button in range(1, race['time']):
      if (race['time'] - ms_holding_button) * ms_holding_button > race['distance']:
        min_holding_time = ms_holding_button
        break
    
    max_holding_time = 0
    for ms_holding_button in range(race['time'], min_holding_time, -1):
      if (race['time'] - ms_holding_button) * ms_holding_button > race['distance']:
        max_holding_time = ms_holding_button
        break

    ways_to_win.append(max_holding_time - min_holding_time + 1)
    
  print(f'\tAnswer: {reduce(operator.mul, ways_to_win, 1)}\n')

def part_two(lines):
  race = {"time": int(''.join(lines[0].split()[1:])), "distance": int(''.join(lines[1].split()[1:]))}

  min_holding_time = 0
  for ms_holding_button in range(1, race['time']):
    if (race['time'] - ms_holding_button) * ms_holding_button > race['distance']:
      min_holding_time = ms_holding_button
      break
  
  max_holding_time = 0
  for ms_holding_button in range(race['time'], min_holding_time, -1):
    if (race['time'] - ms_holding_button) * ms_holding_button > race['distance']:
      max_holding_time = ms_holding_button
      break

  print(f'\tAnswer: {max_holding_time - min_holding_time + 1}\n')
  

print('--- Part One ---')
print('Test')
part_one(test_lines)
print('Actual')
part_one(lines)
print('--- Part Two ---')
print('Test')
part_two(test_lines)
print('Actual')
part_two(lines)