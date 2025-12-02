with open('input.txt', 'r', encoding='utf-8') as f:
  input = f.read()
  invalidIds = []
  for idRange in input.split(','):
    rangeStart, rangeEnd = idRange.split('-')
    rangeStart = int(rangeStart)
    rangeEnd = int(rangeEnd)
    for id in range(rangeStart, rangeEnd + 1):
      id = str(id)
      idLength = len(id)
      if idLength % 2 == 0:
        before = id[0: idLength // 2]
        after = id[idLength // 2:]
        if before == after:
          invalidIds.append(int(id))
  print(f'part1 result: {sum(invalidIds)}')

with open('input.txt', 'r', encoding='utf-8') as f:
  input = f.read()
  invalidIds = []
  for idRange in input.split(','):
    rangeStart, rangeEnd = idRange.split('-')
    rangeStart = int(rangeStart)
    rangeEnd = int(rangeEnd)
    for id in range(rangeStart, rangeEnd + 1):
      id = str(id)
      idLength = len(id)
      halfIdLength = idLength // 2
      for step in range(1, halfIdLength + 1):
        initSubStr = id[0:step]
        match = True
        for index in range(step, idLength, step):
          compareSubStr = id[index: index + step]
          if initSubStr != compareSubStr:
            match = False
        if match:
          invalidIds.append(int(id))
          break
  print(f'part2 result: {sum(invalidIds)}')
