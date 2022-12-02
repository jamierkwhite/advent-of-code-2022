import numpy as np

def parse(filename):
  conversions = {'X': -1, 'A': -1, 'Y': 0, 'B': 0, 'Z': 1, 'C': 1}
  with open(filename, 'r') as file:
    return np.array([[conversions[x] for x in line.strip().split(' ')] for line in file.readlines()])

def part_1(data):
  win_scores = (data[:, 1] - data[:, 0] + 1) % 3 * 3
  play_scores = data[:, 1] + 2
  scores = win_scores + play_scores
  return np.sum(scores)

def part_2(data):
  win_scores = (data[:, 1] + 1) * 3
  play_scores = (data[:, 1] + data[:, 0] + 1) % 3 + 1
  scores = win_scores + play_scores
  return np.sum(scores)

if __name__ == '__main__':
  data = parse('day-2/input.txt')

  print(f'Part 1 score: {part_1(data)}')
  print(f'Part 2 score: {part_2(data)}')
