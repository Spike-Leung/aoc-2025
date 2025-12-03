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

def findBestNumber(str, count):
  if count == 0:
    return ''

  start = 0
  end = len(str) - count + 1
  searchStr = str[start:end]
  bestNumber = sorted(list(searchStr), reverse=True)[0]
  bestNumberIndex = str.find(bestNumber)

  return bestNumber + findBestNumber(str[bestNumberIndex+1:], count - 1)

#part2
with open("input.txt", 'r', encoding="utf-8") as file:
  total = 0
  for line in file:
    line = line.strip()
    total += int(findBestNumber(line, 12))
  print(f'part2 result: {total}')
