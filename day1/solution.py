with open("./input.txt", "r", encoding="utf-8") as file:
  init = 50
  count = 0
  for line in file:
    if line[0] == 'L':
      init -= (int(line[1:]) % 100)
      init = init if init >= 0 else (100 + init)
    else:
      init = ((init + int(line[1:])) % 100)
    if (init % 100) == 0:
      count += 1
  print(f'result: {count}')
