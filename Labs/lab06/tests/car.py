test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.model
          'Model S'
          >>> hilfingers_car.gas = 10
          >>> hilfingers_car.drive()
          'Tesla Model S goes vroom!'
          >>> hilfingers_car.drive()
          'Tesla Model S cannot drive!'
          >>> hilfingers_car.fill_gas()
          Your car is full.
          >>> hilfingers_car.gas
          30
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> Car.headlights
          2
          >>> hilfingers_car.headlights
          2
          >>> Car.headlights = 3
          >>> hilfingers_car.headlights
          3
          >>> hilfingers_car.headlights = 2
          >>> Car.headlights
          3
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.wheels = 2
          >>> hilfingers_car.wheels
          2
          >>> Car.num_wheels
          4
          >>> hilfingers_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          'Tesla Model S cannot drive!'
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          >>> Car.drive(hilfingers_car) # Type Error if an error occurs and Nothing if nothing is displayed
          'Tesla Model S cannot drive!'
          >>> MonsterTruck.drive(hilfingers_car) # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = MonsterTruck('Monster', 'Batmobile')
          >>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          'Monster Batmobile goes vroom!'
          >>> MonsterTruck.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          'Monster Batmobile goes vroom!'
          >>> Car.rev(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> class FoodTruck(MonsterTruck):
          ...    delicious = 'meh'
          ...    def serve(self):
          ...        if FoodTruck.size == 'delicious':
          ...            print('Yum!')
          ...        if self.food != 'Tacos':
          ...            return 'But no tacos...'
          ...        else:
          ...            return 'Mmm!'
          >>> taco_truck = FoodTruck('Tacos', 'Truck')
          >>> taco_truck.food = 'Guacamole'
          >>> taco_truck.serve() # Type Error if an error occurs and Nothing if nothing is displayed
          'But no tacos...'
          >>> taco_truck.food = taco_truck.make
          >>> FoodTruck.size = taco_truck.delicious
          >>> taco_truck.serve() # Type Error if an error occurs and Nothing if nothing is displayed
          'Mmm!'
          >>> taco_truck.size = 'delicious'
          >>> taco_truck.serve() # Type Error if an error occurs and Nothing if nothing is displayed
          'Mmm!'
          >>> FoodTruck.pop_tire() # Type Error if an error occurs and Nothing if nothing is displayed
          Error
          >>> FoodTruck.pop_tire(taco_truck) # Type Error if an error occurs and Nothing if nothing is displayed
          Nothing
          >>> taco_truck.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          Vroom! This Monster Truck is huge!
          'Tacos Truck cannot drive!'
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
