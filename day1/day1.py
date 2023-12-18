with open('./day1.txt', 'r') as file:
  lines = [line.strip() for line in file.readlines()]

def part_one():
  nums = []

  for line in lines:
    no_letters = ''.join(char for char in line if char.isdigit())
    if len(no_letters) == 1:
      nums.append(int(f'{no_letters}{no_letters}'))
    else:
      nums.append(int(f'{no_letters[0]}{no_letters[len(no_letters) - 1]}'))

  print(f'Answer is: {sum(nums)}')

def part_two():
  nums = []

  numbers_dict = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }
  for line in lines:
    first = -1
    last = -1
    for i in range(1, len(line) + 1):
      chopped = line[0:i]
      
      if chopped[i-1].isdigit():
        first = chopped[i-1]
        break
      
      first = next((numbers_dict[key] for key in numbers_dict if key in chopped), -1)
      if first != -1:
        break

    backwards = line[::-1]
    for i in range(1, len(line) + 1):
      chopped = backwards[0:i]
      
      if chopped[i-1].isdigit():
        last = chopped[i-1]
        break
      
      last = next((numbers_dict[key] for key in numbers_dict if key[::-1] in chopped), -1)
      if last != -1:
        break
    
    nums.append(int(f'{first}{last}'))

  print(f'Answer is: {sum(nums)}')

print('--- Part One ---')
part_one()
print('--- Part Two ---')
part_two()
