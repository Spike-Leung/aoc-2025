def split_input_data():
  with open("input.txt", "r", encoding="utf-8") as file:
   fresh_id_ranges = []
   fresh_ids = []
   fresh_id_ranges_lines, fresh_ids_lines = file.read().split('\n\n', maxsplit=1)
   for line in fresh_id_ranges_lines.splitlines():
     line = line.strip()
     start,end = line.split('-')
     fresh_id_ranges.append((int(start), int(end)))
   for line in fresh_ids_lines.splitlines():
     line = line.strip()
     fresh_ids.append(int(line))
   return fresh_id_ranges, fresh_ids

def merge_fresh_id_ranges(fresh_id_ranges):
  reversed_sorted_fresh_id_ranges = sorted(fresh_id_ranges, key=lambda x: x[0], reverse=True)
  index = 0
  while index < len(reversed_sorted_fresh_id_ranges):
      start,end = reversed_sorted_fresh_id_ranges[index]

      if index + 1 < len(reversed_sorted_fresh_id_ranges):
        nextStart,nextEnd = reversed_sorted_fresh_id_ranges[index + 1]
        if nextStart <= start <= nextEnd:
          if end > nextEnd:
            reversed_sorted_fresh_id_ranges[index + 1] = (nextStart, end)
          del reversed_sorted_fresh_id_ranges[index]
          continue

      index += 1
  return list(reversed(reversed_sorted_fresh_id_ranges))

def is_fresh_id(fresh_id_ranges, fresh_id):
  left = 0;
  right = len(fresh_id_ranges)

  while left < right:
    mid = int(left + (right - left) / 2)
    rangeStart = fresh_id_ranges[mid][0]

    if rangeStart > fresh_id:
      right = mid
    elif rangeStart == fresh_id:
      left = mid + 1
    elif rangeStart < fresh_id:
      left = mid + 1
  if left - 1 >= 0:
    match_range = fresh_id_ranges[left - 1]
  else:
    match_range = fresh_id_ranges[left]

  return True if match_range[0] <= fresh_id <= match_range[1] else False

def part1():
  fresh_id_ranges, fresh_ids = split_input_data()
  fresh_id_ranges = merge_fresh_id_ranges(fresh_id_ranges)
  fresh_id_count = 0
  for id in fresh_ids:
    if is_fresh_id(fresh_id_ranges, id):
      fresh_id_count += 1
  print(f'part1 result:{fresh_id_count}')

def part2():
  fresh_id_ranges, fresh_ids = split_input_data()
  fresh_id_ranges = merge_fresh_id_ranges(fresh_id_ranges)
  fresh_ingredient_id_count = 0
  for range in fresh_id_ranges:
    fresh_ingredient_id_count += range[1] - range[0] + 1
  print(f'part2 result:{fresh_ingredient_id_count}')

part1()
part2()
