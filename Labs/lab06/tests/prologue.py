test = {
  'name': 'Prologue',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.color
          'No color yet. You need to paint me.'
          >>> hilfingers_car.paint('black')
          'Tesla Model S is now black'
          >>> hilfingers_car.color
          'black'
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_truck = MonsterTruck('Monster Truck', 'XXL')
          >>> hilfingers_car.size
          'Tiny'
          >>> hilfingers_truck.size
          'Monster'
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
