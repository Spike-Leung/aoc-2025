from shapely.geometry import Polygon

def calc_area(position1, position2):
  x1, y1 = map(int, position1.split(","))
  x2, y2 = map(int, position2.split(","))
  return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def parse_positions():
  with open("input.txt", "r", encoding="utf-8") as file:
    positions = []
    for line in file:
      positions.append(line.strip())
    return positions


def calc_all_area_in_positions(positions):
  areas = []
  for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
      areas.append(calc_area(positions[i], positions[j]))
  return areas


def point_in_polygon(point, polygon):
  """
  使用射线法判断点是否在多边形内部（包括边界）。
  point: (x, y) 元组
  polygon: 顶点列表，顺序连接形成封闭多边形（顺时针或逆时针均可）
  """
  x, y = map(int, point.split(","))
  n = len(polygon)
  inside = False
  for i in range(n):
    x1, y1 = map(int, polygon[i].split(","))
    # 通过 % n 使得最后一个点可以闭环
    x2, y2 = map(int, polygon[(i + 1) % n].split(","))

    # 检查点是否在多边形的边上，两条直线斜率相同，且 x，y 范围相同
    if (
      (x1 - x) * (y2 - y) == (x2 - x) * (y1 - y) and min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)
    ):
      return True

    """
        射线与边相交判断（偶数交点规则），一条向右的射线，判断交点数量

        (y1 > y) != (y2 > y)

        - 忽略了不相交的情况
        - 忽略了水平边，当是水平边是 y = y1 = y2 ，返回 False
        - 当交点是顶点时，忽略上顶点，只考虑下顶点，避免重复判断
        """
    if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
      # 每次存在相交点都是奇偶变化，对应在轮廓内/外
      inside = not inside

  return inside


def is_rectangle_inside_polygon(point1, point2, polygon):
  """
  检查矩形是否完全在多边形内部（包括边界）。
  矩形由 min_x, max_x, min_y, max_y 定义。
  多边形由水平和垂直线段组成。
  """
  x1, y1 = map(int, point1.split(","))
  x2, y2 = map(int, point2.split(","))

  min_x = min(x1, x2)
  max_x = max(x1, x2)
  min_y = min(y1, y2)
  max_y = max(y1, y2)

  # 检查四个顶点是否都在多边形内
  vertices = [
    f"{min_x},{min_y}",  # 左下角
    f"{min_x},{max_y}",  # 左上角
    f"{max_x},{min_y}",  # 右下角
    f"{max_x},{max_y}",  # 右上角
  ]

  for vertex in vertices:
    if not point_in_polygon(vertex, polygon):
      return False

  n = len(polygon)
  edges = []
  for k in range(n):
    x1, y1 = map(int, polygon[k].split(","))
    x2, y2 = map(int, polygon[(k + 1) % n].split(","))
    edges.append((x1, y1, x2, y2))

  # 检查矩形的每条边是否与多边形的任何边相交（除了在端点处）
  # 矩形的四条边：
  rect_edges = [
    (min_x, max_y, max_x, max_y),  # 上边
    (min_x, min_y, max_x, min_y),  # 下边
    (min_x, min_y, min_x, max_y),  # 左边
    (max_x, min_y, max_x, max_y),  # 右边
  ]

  for rx1, ry1, rx2, ry2 in rect_edges:
    # 对于矩形的每条边，检查是否与多边形的任何边相交
    for ex1, ey1, ex2, ey2 in edges:
      # 如果两条边共享端点，跳过（允许在顶点处接触）
      if (
        (rx1 == ex1 and ry1 == ey1)
        or (rx1 == ex2 and ry1 == ey2)
        or (rx2 == ex1 and ry2 == ey1)
        or (rx2 == ex2 and ry2 == ey2)
      ):
        continue

      # 检查两条线段是否相交
      # 由于所有边都是水平或垂直的，我们可以简化
      # 矩形边：水平或垂直
      rect_horizontal = ry1 == ry2
      edge_horizontal = ey1 == ey2

      if rect_horizontal and edge_horizontal:
        # 两条水平线：如果y坐标相同且x范围重叠，则重叠
        if ry1 == ey1:
          if not (rx2 < ex1 or ex2 < rx1):
            pass
      elif not rect_horizontal and not edge_horizontal:
        # 两条垂直线：如果x坐标相同且y范围重叠
        if rx1 == ex1:
          if not (ry2 < ey1 or ey2 < ry1):
            pass
      else:
        # 一条水平，一条垂直：检查交点
        if rect_horizontal:
          # 矩形边水平，多边形边垂直
          if (min(rx1, rx2) <= ex1 <= max(rx1, rx2)) and (min(ey1, ey2) <= ry1 <= max(ey1, ey2)):
            # 交点 (ex1, ry1)
            # 检查交点是否在端点（已处理）
            # 如果不在端点，则相交，矩形边被刺穿
            # 检查交点是否是端点
            if not (
              (ex1 == rx1 and ry1 == ry1)
              or (ex1 == rx2 and ry1 == ry2)
              or (ex1 == ex1 and ry1 == ey1)
              or (ex1 == ex2 and ry1 == ey2)
            ):
              return False
        else:
          # 矩形边垂直，多边形边水平
          if (min(ry1, ry2) <= ey1 <= max(ry1, ry2)) and (min(ex1, ex2) <= rx1 <= max(ex1, ex2)):
            if not (
              (rx1 == rx1 and ey1 == ry1)
              or (rx1 == rx2 and ey1 == ry2)
              or (rx1 == ex1 and ey1 == ey1)
              or (rx1 == ex2 and ey1 == ey2)
            ):
              return False

  # 另外，检查矩形内部是否有"洞"
  # 我们可以检查矩形的中心点是否在多边形内
  center_x = (min_x + max_x) // 2
  center_y = (min_y + max_y) // 2
  if not point_in_polygon(f"{center_x},{center_y}", polygon):
    return False

  return True


def part1():
  max_area = sorted(calc_all_area_in_positions(parse_positions()), reverse=True)[0]
  print(f"part1 result: {max_area}")

def part2():
  positions = parse_positions()
  valid_areas = []
  for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
      if is_rectangle_inside_polygon(positions[i], positions[j], positions):
        valid_areas.append(calc_area(positions[i], positions[j]))
  print(f"part2 result: {max(valid_areas)}")

def poly_rectangle_area(x1: int, y1: int, x2: int, y2: int) -> Polygon:
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    return Polygon([(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)])

def area_size(x1: int, y1: int, x2: int, y2: int) -> int:
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

def part2_with_Polygon():
    positions = parse_positions()
    data = [tuple(int(i) for i in p.split(",")) for p in positions]
    largest = 0
    poly_area = Polygon(data)
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            x1, y1 = data[i]
            x2, y2 = data[j]
            rectangle = poly_rectangle_area(x1, y1, x2, y2)
            if rectangle.within(poly_area):
                area = area_size(x1, y1, x2, y2)
                if area > largest:
                    largest = area
    print(f"part2 result: {largest}")

part1()
# part2()
part2_with_Polygon()
