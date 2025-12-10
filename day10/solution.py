def combinations(list, count):
    result = []
    def backtrack(start, current):
        if len(current) == count:
            result.append(current.copy())
            return
        for i in range(start, len(list)):
            current.append(list[i])
            backtrack(i + 1, current)
            current.pop()
    backtrack(0, [])
    return result

def find_fewest_button_presses_match_light_diagram(light_diagram, button_wiring_schematics):
  # [.#.#] -> .#.#
  fewest_button_presses = 0
  light_diagram = light_diagram[1:-1]
  found = False
  for i in range(1, len(button_wiring_schematics)+1):
    for combination in combinations(button_wiring_schematics, i):
      state = ['.']*len(light_diagram)
      for button_wiring_schematic in combination:
        for index in map(int, button_wiring_schematic[1:-1].split(",")):
          if state[index] is None or state[index] == '.':
            state[index] = '#'
          elif state[index] == '#':
            state[index] = '.'
        if ''.join(state) == light_diagram:
          fewest_button_presses += i
          found = True
          break
      if found:
        break
    if found:
      break
  return fewest_button_presses


def part1():
  with open("input.txt", "r", encoding="utf-8") as file:
    data = []
    fewest_button_presses = 0
    for line in file:
      light_diagram, *button_wiring_schematics, _ = line.strip().split()
      fewest_button_presses += find_fewest_button_presses_match_light_diagram(light_diagram, button_wiring_schematics)
    print(f'part1 result: {fewest_button_presses}')

part1()

def find_fewest_button_presses_match_joltage_requirements(joltage_requirements, button_wiring_schematics):
  fewest_button_presses = 0

  # if all joltage equal 0, end
  # if button_wiring_schematics's len equal 0, end
  is_all_joltage_equal_zero = True
  zero_joltage_index = []
  not_zero_joltage_index = []
  for i in range(len(joltage_requirements)):
    if joltage_requirements[i] != 0:
      not_zero_joltage_index.append(i)
      is_all_joltage_equal_zero = False
    else:
      zero_joltage_index.append(i)

  if is_all_joltage_equal_zero:
    return 0

  valid_button_wiring_schematics = []
  for i in button_wiring_schematics:
    valid = True
    for j in map(int, i[1:-1].split(",")):
      if j in zero_joltage_index:
        valid = False
    if valid:
      valid_button_wiring_schematics.append(i)

  if len(valid_button_wiring_schematics) == 0:
    return -1

  print('********************')
  print(f'not_zero_joltage_index:{not_zero_joltage_index}, zero_joltage_index:{zero_joltage_index}, valid_button_wiring_schematics:{valid_button_wiring_schematics}')
  for i in not_zero_joltage_index:
    is_contain_not_zero_joltage_index = False
    for j in valid_button_wiring_schematics:
      if i in map(int, j[1:-1].split(",")):
        is_contain_not_zero_joltage_index = True
    if not is_contain_not_zero_joltage_index:
      return -1

  # merge same joltage
  joltage_and_index_dict = {}
  for i in range(len(joltage_requirements)):
    if joltage_and_index_dict.get(joltage_requirements[i]) is not None:
      joltage_and_index_dict[joltage_requirements[i]].append(i)
    else:
      joltage_and_index_dict[joltage_requirements[i]] = [i]

  # find the minimum joltage, maybe a list
  minimum_joltage = None
  for joltage in joltage_requirements:
    if int(joltage) == 0:
      continue
    if minimum_joltage is None:
      minimum_joltage = joltage
    elif int(joltage) < int(minimum_joltage):
      minimum_joltage = joltage

  minimum_joltage_indexs = joltage_and_index_dict[minimum_joltage]

  button_wiring_schematics_contains_minimum_joltage_index = []
  # find button_wiring_schematics which contains minimum_joltage_index
  for minimum_joltage_index in minimum_joltage_indexs:
    for button_wiring_schematic in valid_button_wiring_schematics:
      if minimum_joltage_index in map(int, button_wiring_schematic[1:-1].split(",")):
        button_wiring_schematics_contains_minimum_joltage_index.append(button_wiring_schematic)

  print(f'button_wiring_schematics_contains_minimum_joltage_index:{button_wiring_schematics_contains_minimum_joltage_index:}')
  result = []
  # press the button with minimum_joltage times
  for i in button_wiring_schematics_contains_minimum_joltage_index:
    indexs = map(int, i[1:-1].split(","))
    joltage_requirements_after_pressed = joltage_requirements.copy()
    print('>>>>>>>>>>>>>>>>>>>>')
    print(f'i:{i}')
    print(f'joltage_requirements_after_pressed before: {joltage_requirements_after_pressed}')
    for j in indexs:
      joltage_requirements_after_pressed[j] -= minimum_joltage
    print(f'joltage_requirements_after_pressed after: {joltage_requirements_after_pressed}')
    next_button_presses = find_fewest_button_presses_match_joltage_requirements(joltage_requirements_after_pressed, valid_button_wiring_schematics)
    print(f'next_button_presses:{next_button_presses}')
    if next_button_presses != -1:
      result.append(minimum_joltage + next_button_presses)
  if len(result) > 0:
    return min(result)
  else:
    return -1

def part2():
  with open("example.txt", "r", encoding="utf-8") as file:
    fewest_button_presses = 0
    for line in file:
      light_diagram, *button_wiring_schematics, joltage_requirements = line.strip().split()
      print('--------------------')
      print(line)
      press = find_fewest_button_presses_match_joltage_requirements(list(map(int, joltage_requirements[1:-1].split(","))), button_wiring_schematics)
      print(f'press:{press}')
      fewest_button_presses += press
    print(f'part2 result: {fewest_button_presses}')

part2()
