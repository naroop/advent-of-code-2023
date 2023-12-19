with open('./test-data.txt', 'r') as file:
  test_lines = [line.strip() for line in file.readlines()]
with open('./data.txt', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

def part_one(lines):
  total_points = 0

  for line in lines:
    winning_nums, my_nums = [nums.strip().replace('  ', ' ').split(' ') for nums in line.split(':')[1].split('|')]
    count = 0

    for num in my_nums:
      if num in winning_nums:
        count += 1

    if count:
      total_points += pow(2, count - 1)
    
  print(f'\tAnswer: {total_points}\n')

from collections import defaultdict

def part_two(lines):
  card_win_counts = defaultdict(lambda: 0)

  for i, line in enumerate(lines):
    winning_nums, my_nums = [nums.strip().replace('  ', ' ').split(' ') for nums in line.split(':')[1].split('|')]

    for num in my_nums:
      if num in winning_nums:
        card_win_counts[i] += 1

  card_nums = [i for i in range(len(lines))]
  for card_num in card_nums:
    for i in range(card_num + 1, card_num + card_win_counts[card_num] + 1):
      card_nums.append(i)


  print(f'\tAnswer: {len(card_nums)}\n')
  

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