def main():
    area = int(input('Square feet of wall to paint: '))
    p_1_gal = float(input('Price for 1 gallon of paint: '))

    total_price = total_cost(area, p_1_gal)
    print(total_price)

def calculate_paint_volume(surface):
    volume = surface // 112
    if surface % 112 != 0:
        volume += 1
    return volume

def calculate_labor_hours(surface2):
    return 8 * surface2 / 112

def calculate_paint_cost(s, p_1_g):
    return p_1_g * calculate_paint_volume(s)

def calculate_labor_cost(surf):
    return 35 * calculate_labor_hours(surf)

def total_cost(surface, p_1_gallon):
    return calculate_paint_cost(surface, p_1_gallon) + calculate_labor_cost(surface)


main()
