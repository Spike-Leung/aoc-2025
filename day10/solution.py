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

def part1():
  with open("input.txt", "r", encoding="utf-8") as file:
    data = []
    fewest_button_presses = 0
    for line in file:
      light_diagram, *button_wiring_schematics, joltage_requirements = line.strip().split()
      light_diagram = light_diagram[1:-1]
      button_wiring_schematics_len = len(button_wiring_schematics)

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

    print(f'part1 result: {fewest_button_presses}')

part1()
