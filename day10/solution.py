import re
from z3 import Int, Optimize, sat

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


def parse_line(line):
    """从一行中解析操作列表和目标数组，忽略开头的方括号部分"""
    line = re.sub(r'^\[.*?\]\s*', '', line).strip()
    tokens = re.findall(r'\([^)]+\)|\{[^}]+\}', line)
    ops = []
    target = None
    for tok in tokens:
        if tok.startswith('('):
            indices = list(map(int, tok[1:-1].split(',')))
            ops.append(indices)
        elif tok.startswith('{'):
            target = list(map(int, tok[1:-1].split(',')))
    return ops, target

def min_operations_z3(ops, target):
    """使用 Z3 求解最小操作次数，返回整数最优值（若无解返回 None）"""
    n = len(ops)           # 操作数量
    m = len(target)        # 索引数量

    # 创建变量
    vars = [Int(f'x{i}') for i in range(n)]

    opt = Optimize()
    # 变量非负约束
    for v in vars:
        opt.add(v >= 0)

    # 每个索引的等式约束
    for i in range(m):
        coeff_sum = sum(vars[j] for j in range(n) if i in ops[j])
        opt.add(coeff_sum == target[i])

    # 最小化总操作次数
    total = sum(vars)
    opt.minimize(total)

    if opt.check() == sat:
        model = opt.model()
        return model.evaluate(total).as_long()
    else:
        return None

def part2():
    with open("input.txt", "r", encoding="utf-8") as file:
      ans = 0
      for line in file:
        ops, target = parse_line(line)
        ans += min_operations_z3(ops, target)
      print(f'part2 result: {ans}')

part2()
