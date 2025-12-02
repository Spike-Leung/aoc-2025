# part1
with open("./input.txt", "r", encoding="utf-8") as file:
  currentPoint = 50
  count = 0
  for line in file:
    move = int(line[1:])
    if line[0] == 'L':
      currentPoint -= (move % 100)
      currentPoint = currentPoint if currentPoint >= 0 else (100 + currentPoint)
    else:
      currentPoint = ((currentPoint + move) % 100)
    if (currentPoint % 100) == 0:
      count += 1
  print(f'part1 result: {count}')

#part2
with open("./input.txt", "r", encoding="utf-8") as file:
  currentPoint = 50
  count = 0
  for line in file:
    move = int(line[1:])
    count += int(move / 100)
    if (line[0] == 'L'):
      prevPoint = currentPoint
      currentPoint -= (move % 100)
      currentPoint = currentPoint if currentPoint >= 0 else (100 + currentPoint)

      if currentPoint > prevPoint:
        count += 1
    else:
      prevPoint = currentPoint
      currentPoint = ((currentPoint + move) % 100)

      if currentPoint < prevPoint:
        count += 1
  print(f'part2 result: {count}')
