import numpy as np

def parse(filename):
  with open(filename, 'r') as file:
    data = file.read()
    jagged_data = [block.split('\n') for block in data.split('\n\n')]
    max_length = max([len(x) for x in jagged_data])
    squared_data = [inventory+[0]*(max_length-len(inventory)) for inventory in jagged_data]
    return np.array(squared_data, dtype=np.int64)

def part_1(data):
  return np.max(np.sum(data, 1))

def part_2(data):
  totals = list(np.sum(data, 1))
  count = 0
  for _ in range(3):
    top = max(totals)
    count += top
    totals.remove(top)
  return count

if __name__ == '__main__': 
  data = parse('day-1/input.txt')
  print('part 1:')
  print(f'Highest elf load is {part_1(data)} Calories')
  print('part 2:')
  print(f'Combined top 3 elf loads is {part_2(data)} Calories')
