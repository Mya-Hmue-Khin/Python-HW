def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('BMW', 'BMW 320i', horsepower = '184 hp', speed = 'around 235 km/h(146 mph)')
print(car)