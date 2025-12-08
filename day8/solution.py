import math


def distance_in_3d(point1, point2):
  x1, y1, z1 = map(int, point1.split(","))
  x2, y2, z2 = map(int, point2.split(","))

  return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def get_distance_dict_sort_by_distance_asc(positions):
  distance_dict = {}
  for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
      distance_dict[(positions[i], positions[j])] = distance_in_3d(positions[i], positions[j])
  return dict(sorted(distance_dict.items(), key=lambda item: item[1]))


def connect_circuits(distance_dict, connect_count=None):
  circuits = []
  distance_dict = list(distance_dict)[:connect_count] if connect_count is not None else distance_dict
  for point1, point2 in distance_dict:
    idx1 = idx2 = None
    for i, circuit in enumerate(circuits):
      if point1 in circuit:
        idx1 = i
      if point2 in circuit:
        idx2 = i
    if idx1 is not None and idx2 is not None:
      if idx1 != idx2:
        circuits[idx1].update(circuits[idx2])
        del circuits[idx2]
    elif idx1 is not None:
      circuits[idx1].add(point2)
    elif idx2 is not None:
      circuits[idx2].add(point1)
    else:
      circuits.append({point1, point2})

  return circuits


def part1():
  with open("input.txt", "r", encoding="utf-8") as file:
    positions = []
    for line in file:
      positions.append(line.strip())
    distance_dict = get_distance_dict_sort_by_distance_asc(positions)
    circuits = connect_circuits(distance_dict, 1000)
    circuits = sorted(circuits, key=len, reverse=True)
    product = math.prod(len(s) for s in circuits[:3])
    print(f"part1 result: {product}")


def find_last_connect_that_form_a_single_circuit(distance_dict, point_count_total):
  circuits = []
  for point1, point2 in list(distance_dict):
    idx1 = idx2 = None
    for i, circuit in enumerate(circuits):
      if point1 in circuit:
        idx1 = i
      if point2 in circuit:
        idx2 = i
    if idx1 is not None and idx2 is not None:
      if idx1 != idx2:
        circuits[idx1].update(circuits[idx2])
        del circuits[idx2]
    elif idx1 is not None:
      circuits[idx1].add(point2)
    elif idx2 is not None:
      circuits[idx2].add(point1)
    else:
      circuits.append({point1, point2})
    if len(circuits) == 1 and len(circuits[0]) == point_count_total:
      return (point1, point2)
  return None


def part2():
  with open("input.txt", "r", encoding="utf-8") as file:
    positions = []
    for line in file:
      positions.append(line.strip())
    distance_dict = get_distance_dict_sort_by_distance_asc(positions)
    point1, point2 = find_last_connect_that_form_a_single_circuit(distance_dict, len(positions))
    point1_x = int(point1.split(",")[0])
    point2_x = int(point2.split(",")[0])
    print(f"part2 result: {point1_x * point2_x}")


part1()
part2()
