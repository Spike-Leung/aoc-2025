#part1
with open('input.txt', 'r', encoding='utf-8') as file:
  grid = []
  for line in file:
    grid.append(line.strip())
  rows, cols = len(grid), len(grid[0])
  directions = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),         (0, 1),
                (1, -1),  (1, 0), (1, 1)]
  rolls_of_papar_can_assess = 0
  for row in range(0, rows):
    for col in range(0, cols):
      rolls_of_paper_adjacent = 0
      if grid[row][col] == '.': continue
      for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '@':
          rolls_of_paper_adjacent += 1
      if rolls_of_paper_adjacent < 4:
        rolls_of_papar_can_assess += 1
  print(f'part1 result:{rolls_of_papar_can_assess}')

def get_rolls_of_paper_can_remove(grid):
  rows, cols = len(grid), len(grid[0])
  directions = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),         (0, 1),
                (1, -1),  (1, 0), (1, 1)]
  rolls_of_paper_can_remove = []
  for row in range(0, rows):
    for col in range(0, cols):
      rolls_of_paper_adjacent = 0
      if grid[row][col] == '.': continue
      for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '@':
          rolls_of_paper_adjacent += 1
      if rolls_of_paper_adjacent < 4:
        rolls_of_paper_can_remove.append((row, col))
  return rolls_of_paper_can_remove

def count_rolls_of_paper_can_remove(grid):
  total_roll_of_papar_can_remove = 0
  rolls_of_paper_can_remove = get_rolls_of_paper_can_remove(grid)
  rolls_of_paper_can_remove_count = len(rolls_of_paper_can_remove)

  if rolls_of_paper_can_remove_count == 0:
    return 0

  if rolls_of_paper_can_remove_count > 0:
    total_roll_of_papar_can_remove += rolls_of_paper_can_remove_count
    for r, c in rolls_of_paper_can_remove:
      grid[r] = grid[r][:c] + '.' + grid[r][c+1:]
    return total_roll_of_papar_can_remove + count_rolls_of_paper_can_remove(grid)

#part2
with open('input.txt', 'r', encoding='utf-8') as file:
  grid = []
  for line in file:
    grid.append(line.strip())
  print(f'part2 result: {count_rolls_of_paper_can_remove(grid)}')
