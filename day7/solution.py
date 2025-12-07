#part1

def replace_char_in_str(str, char, position):
  return str[:position] + char + str[position + 1:]

def part1():
  with open("input.txt", "r", encoding="utf-8") as file:
    diagram = []
    for line in file:
      diagram.append(line.strip())
    # init tachyon beams
    tachyon_beams_start_position = diagram[0].find('S')
    diagram[1] = replace_char_in_str(diagram[1], '|', tachyon_beams_start_position)
    # count tachyon_beam_split_times
    tachyon_beam_split_times = 0
    current_row_index = 2
    for row in diagram[2:]:
      pointCount = len(row)
      for point in range(0, pointCount):
        if diagram[current_row_index - 1][point] == '|':
          if diagram[current_row_index][point] == '^':
            tachyon_beam_split_times += 1
            # beam split to the left side of the spliter
            if point > 0:
              diagram[current_row_index] = replace_char_in_str(diagram[current_row_index], '|', point - 1)
            # beam split to the right side of the spliter
            if point < pointCount - 1:
              diagram[current_row_index] = replace_char_in_str(diagram[current_row_index], '|', point + 1)
          # beam go downward
          else:
            diagram[current_row_index] = replace_char_in_str(diagram[current_row_index], '|', point)

      current_row_index += 1
    print(f'part1 result: {tachyon_beam_split_times}')

part1()

def get_beam_downward_count(diagram, current_row, current_col, memo=None):
    if memo is None:
        memo = {}
    key = (current_row, current_col)
    if key in memo:
        return memo[key]

    if current_row == len(diagram):
        return 0
    elif current_row == len(diagram) - 1:
      return 1
    else:
        current = diagram[current_row][current_col]
        if current == '^':
            res = get_beam_downward_count(diagram, current_row, current_col - 1, memo) + get_beam_downward_count(diagram, current_row, current_col + 1, memo)
        else:
            res = get_beam_downward_count(diagram, current_row + 1, current_col, memo)
        memo[key] = res
        return res

def part2():
  with open("input.txt", "r", encoding="utf-8") as file:
    diagram = []
    for line in file:
      diagram.append(line.strip())
    tachyon_beam_split_timelines = 0
    tachyon_beams_start_position = diagram[0].find('S')
    tachyon_beam_split_timelines = get_beam_downward_count(diagram, 0, tachyon_beams_start_position)

    print(f'part2 result: {tachyon_beam_split_timelines}')

part2()
