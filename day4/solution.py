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
    for column in range(0, cols):
      rolls_of_paper_adjacent = 0
      if grid[row][column] == '.': continue
      for dr, dc in directions:
        r, c = row + dr, column + dc
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '@':
          rolls_of_paper_adjacent += 1
      if rolls_of_paper_adjacent < 4:
        rolls_of_papar_can_assess += 1
  print(f'part1 result:{rolls_of_papar_can_assess}')
