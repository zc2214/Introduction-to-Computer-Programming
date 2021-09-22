#main program
def main():
    wall_space = int(input('How many square feet of wall space to be painted?\n> '))
    paint_price = int(input('Price of paint per gallon?\n> '))

    paint_volume = calculate_paint_volume(wall_space)
    labor_hours = calculate_labor_hours(wall_space)
    paint_cost = calculate_paint_cost(paint_volume, paint_price)
    labor_cost = calculate_labor_cost(labor_hours)
    cost = total_cost(paint_cost, labor_cost)

#def functions
def calculate_paint_volume(walls):
    volume = walls / 112     #volume in gallons
    print(volume,'gallons of paint required')
    return volume

def calculate_labor_hours(walls):
    hours = 8 * walls / 112
    print(hours,'hours of labor required')
    return hours

def calculate_paint_cost(volume, price):
    cost = volume * price
    print('The paint cost is: $' + str(cost))
    return cost

def calculate_labor_cost(hours):
    cost = 35 * hours
    print('The labor cost is: $' + str(cost))
    return cost

def total_cost(paint, labor):
    cost = paint + labor
    print('The total cost is: $' + str(cost))
    return cost


#program
main()
