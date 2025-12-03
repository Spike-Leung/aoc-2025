#part1
with open("input.txt", 'r', encoding="utf-8") as file:
  total = 0
  for line in file:
    line = line.strip()
    a,b = sorted(list(line), reverse=True)[:2]
    length = len(line)
    aIndex = line.find(a)
    bIndex = line.find(b)

    if aIndex < length - 1:
      total += int(a + sorted(list(line[aIndex+1:]), reverse=True)[0])
    else:
      total += int(b + sorted(list(line[bIndex+1:]), reverse=True)[0])

  print(f'part1 result: {total}')
