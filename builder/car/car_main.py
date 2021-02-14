from car_director import CarDirector
from sports_car_builder import SportsCarBuilder

def car_main():
    c = CarDirector()
    c.build_car(SportsCarBuilder())
    print(c.car)


if __name__ == "__main__":
    car_main()