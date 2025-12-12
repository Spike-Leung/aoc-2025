def part1():
  with open("input.txt", "r", encoding="utf-8") as file:
    blocks = file.read().split('\n\n')
    gifts = blocks[:-1]
    gift_size = {}
    for i in range(len(gifts)):
      gift_size[i] = 0
      for j in gifts[i]:
        if j == '#':
          gift_size[i] += 1

    area_fit_count = 0
    tree_areas = blocks[-1]
    for tree in tree_areas.splitlines():
      print(tree)
      area_str, index = tree.split(":")
      area_x, area_y = list(map(int, area_str.split("x")))
      area = area_x * area_y
      index_list = list(map(int, index.split()))
      gift_area = 0
      for i in range(len(index_list)):
        gift_area += gift_size[i] * index_list[i]
      if area >= gift_area:
        area_fit_count += 1
    print(f'result: {area_fit_count}')

part1()
