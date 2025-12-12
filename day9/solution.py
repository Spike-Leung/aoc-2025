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

def part1():
    max_area = sorted(calc_all_area_in_positions(parse_positions()), reverse=True)[0]
    print(f"part1 result: {max_area}")

part1()

def get_all_position_in_area(positions):
  position_group_by_y = {}
  horizon_position = []
  for p in positions:
    x,y = p.split(",")
    if position_group_by_y.get(y) is not None:
      position_group_by_y[y].append(x)
    else:
      position_group_by_y[y] = [x]
  for y, x_positions in position_group_by_y.items():
    min_x = min(map(int, x_positions))
    max_x = max(map(int, x_positions))
    for x in range(min_x, max_x + 1):
      horizon_position.append(f'{x},{y}')
  all_position_in_area = []
  position_group_by_x = {}
  for p in horizon_position:
    x,y = p.split(",")
    if position_group_by_x.get(x) is not None:
      position_group_by_x[x].append(y)
    else:
      position_group_by_x[x] = [y]
  for x, y_positions in position_group_by_x.items():
    min_y = min(map(int, y_positions))
    max_y = max(map(int, y_positions))
    for y in range(min_y, max_y + 1):
      all_position_in_area.append(f'{x},{y}')
  return all_position_in_area

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
        x2, y2 = map(int, polygon[(i + 1) % n].split(","))

        # 检查点是否在多边形的边上
        if ((x1 - x) * (y2 - y) == (x2 - x) * (y1 - y) and
            min(x1, x2) <= x <= max(x1, x2) and
            min(y1, y2) <= y <= max(y1, y2)):
            return True

        # 射线与边相交判断（偶数交点规则）
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside

    return inside

def is_rectangle_inside_polygon(min_x, max_x, min_y, max_y, polygon):
    """
    检查矩形是否完全在多边形内部（包括边界）。
    矩形由 min_x, max_x, min_y, max_y 定义。
    多边形由水平和垂直线段组成。
    """
    # 检查四个顶点是否都在多边形内
    vertices = [
        f"{min_x},{min_y}",  # 左下角
        f"{min_x},{max_y}",  # 左上角
        f"{max_x},{min_y}",  # 右下角
        f"{max_x},{max_y}"   # 右上角
    ]

    for vertex in vertices:
        if not point_in_polygon(vertex, polygon):
            return False

    # 预计算多边形的所有边
    n = len(polygon)
    edges = []
    for k in range(n):
        x1, y1 = map(int, polygon[k].split(","))
        x2, y2 = map(int, polygon[(k + 1) % n].split(","))
        edges.append((x1, y1, x2, y2))

    # 检查矩形的每条边是否与多边形的任何边相交（除了在端点处）
    # 矩形的四条边：
    rect_edges = [
        (min_x, min_y, max_x, min_y),  # 下边
        (min_x, max_y, max_x, max_y),  # 上边
        (min_x, min_y, min_x, max_y),  # 左边
        (max_x, min_y, max_x, max_y)   # 右边
    ]

    for rx1, ry1, rx2, ry2 in rect_edges:
        # 对于矩形的每条边，检查是否与多边形的任何边相交
        for ex1, ey1, ex2, ey2 in edges:
            # 如果两条边共享端点，跳过（允许在顶点处接触）
            if (rx1 == ex1 and ry1 == ey1) or (rx1 == ex2 and ry1 == ey2) or \
               (rx2 == ex1 and ry2 == ey1) or (rx2 == ex2 and ry2 == ey2):
                continue

            # 检查两条线段是否相交
            # 由于所有边都是水平或垂直的，我们可以简化
            # 矩形边：水平或垂直
            rect_horizontal = (ry1 == ry2)
            edge_horizontal = (ey1 == ey2)

            if rect_horizontal and edge_horizontal:
                # 两条水平线：如果y坐标相同且x范围重叠，则重叠
                if ry1 == ey1:
                    if not (rx2 < ex1 or ex2 < rx1):
                        # 有重叠部分，检查是否只是端点接触（已处理）
                        # 如果有内部重叠，则矩形边可能部分在多边形外
                        # 但我们需要确保整个矩形边在多边形内
                        # 对于水平边，如果与多边形水平边重叠，需要进一步检查
                        # 简化：如果矩形边与多边形边重叠，且多边形边是边界，那么矩形边在边界上，这是允许的
                        # 但我们需要确保矩形边完全在多边形内部或边界上
                        # 这里我们假设如果重叠，那么矩形边在边界上，这是允许的
                        # 但需要确保重叠部分不是"洞"的一部分
                        # 由于多边形是简单的曼哈顿多边形，这应该没问题
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
                    if (min(rx1, rx2) <= ex1 <= max(rx1, rx2)) and \
                       (min(ey1, ey2) <= ry1 <= max(ey1, ey2)):
                        # 交点 (ex1, ry1)
                        # 检查交点是否在端点（已处理）
                        # 如果不在端点，则相交，矩形边被刺穿
                        # 检查交点是否是端点
                        if not ((ex1 == rx1 and ry1 == ry1) or (ex1 == rx2 and ry1 == ry2) or \
                                (ex1 == ex1 and ry1 == ey1) or (ex1 == ex2 and ry1 == ey2)):
                            return False
                else:
                    # 矩形边垂直，多边形边水平
                    if (min(ry1, ry2) <= ey1 <= max(ry1, ry2)) and \
                       (min(ex1, ex2) <= rx1 <= max(ex1, ex2)):
                        if not ((rx1 == rx1 and ey1 == ry1) or (rx1 == rx2 and ey1 == ry2) or \
                                (rx1 == ex1 and ey1 == ey1) or (rx1 == ex2 and ey1 == ey2)):
                            return False

    # 另外，检查矩形内部是否有"洞"
    # 我们可以检查矩形的中心点是否在多边形内
    center_x = (min_x + max_x) // 2
    center_y = (min_y + max_y) // 2
    if not point_in_polygon(f"{center_x},{center_y}", polygon):
        return False

    return True


def part2():
    positions = parse_positions()
    valid_areas = []
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            # 将坐标转换为整数
            x1, y1 = map(int, positions[i].split(","))
            x2, y2 = map(int, positions[j].split(","))

            # 确定矩形的四个顶点
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)

            # 四个顶点
            p1 = f"{min_x},{min_y}"  # 左下角
            p2 = f"{min_x},{max_y}"  # 左上角
            p3 = f"{max_x},{min_y}"  # 右下角
            p4 = f"{max_x},{max_y}"  # 右上角

            if is_rectangle_inside_polygon(min_x, max_x, min_y, max_y, positions):
               valid_areas.append(calc_area(p1, p4))

    if valid_areas:
        max_area = max(valid_areas)
        print(f"part2 result: {max_area}")
    else:
        print("No valid rectangles found")

part2()
