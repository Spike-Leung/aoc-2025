def calc_operator_result(numbers, operator):
  result = 0
  if operator == '+':
    result += sum(numbers)
  elif operator == '*':
    product = 1
    for num in numbers:
      product *= num
    result += product
  return result

def part1():
  with open("example.txt", "r", encoding="utf-8") as file:
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
      grand_total += calc_operator_result(numbers, operator)
    print(f'part1 result: {grand_total}')

def part2():
  with open("input.txt", "r", encoding="utf-8") as file:
    worksheet = []
    grand_total = 0
    for line in file:
      worksheet.append(line.strip('\n') + ' ')
    valid_numbers = []
    empty_col = 0
    for col in range(0, len(worksheet[0])):
      number = ''
      for row in worksheet[:-1]:
        number += row[col]
      if number.strip() != '':
        valid_numbers.append(int(number.strip()))
      else:
        operator = worksheet[-1][empty_col:col].strip()
        grand_total += calc_operator_result(valid_numbers, operator)
        valid_numbers = []
        empty_col = col
    print(f'part2 result: {grand_total}')
part2()
