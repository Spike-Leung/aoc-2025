with open("input.txt", "r", encoding="utf-8") as file:
  worksheet = []
  grand_total = 0
  for line in file:
    line = line.strip()
    worksheet.append(line.split())
  problem_count = len(worksheet[0])
  for col in range(0, problem_count):
    operator = worksheet[-1][col]
    numbers = []
    for row in worksheet[:-1]:
      numbers.append(int(row[col]))
    if operator == '+':
      grand_total += sum(numbers)
    elif operator == '*':
      product = 1
      for num in numbers:
        product *= num
      grand_total += product
  print(f'part1 result: {grand_total}')
