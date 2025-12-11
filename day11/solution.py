def init_device_dict():
  graph = {}
  with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
      key, childs = line.strip().split(":")
      graph[key] = childs.strip().split()
  return graph

def count_path_to_out(graph, start):
  if start == 'out':
    return 1

  count = 0
  next_paths = graph[start]
  for path in next_paths:
    count += count_path_to_out(graph, path)
  return count

def count_path_to_out_contain_fft_dac(graph, node, seen_fft = False, seen_dac = False, memo = None):
  if memo is None:
    memo = {}
  key = (node, seen_fft, seen_dac)
  seen_fft = seen_fft or node == 'fft'
  seen_dac = seen_dac or node == 'dac'

  if key in memo:
    return memo[key]
  if node == 'out':
    memo[key] = 1 if seen_fft and seen_dac else 0
    return memo[key]

  count = 0
  next_paths = graph[node]
  for path in next_paths:
    count += count_path_to_out_contain_fft_dac(graph, path, seen_fft, seen_dac, memo)
  memo[key] = count
  return count

def part1():
  graph = init_device_dict()
  result = count_path_to_out(graph, 'you')
  print(f'part1 result: {result}')

def part2():
  graph = init_device_dict()
  result = count_path_to_out_contain_fft_dac(graph, 'svr')
  print(f'part2 result: {result}')

part1()
part2()
