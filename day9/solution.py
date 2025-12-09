def calc_area(position1, position2):
  x1, y1 = map(int, position1.split(","))
  x2, y2 = map(int, position2.split(","))
  return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def part1():
  with open("input.txt", "r", encoding="utf-8") as file:
    positions = []
    for line in file:
      positions.append(line.strip())
    areas = []
    for i in range(len(positions)):
      for j in range(i + 1, len(positions)):
        areas.append(((positions[i], positions[j]), calc_area(positions[i], positions[j])))
    max_area = sorted(areas, key=lambda item: item[1], reverse=True)[0][1]
    print(f"part1 result: {max_area}")


part1()
