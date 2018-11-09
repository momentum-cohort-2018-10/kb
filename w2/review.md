# W2 Review

- Modules
- Testing
- Objects
- Classes
- Pipenv


## Why classes instead of functions?

- data we need to find the next step on our path
  - elevation map data
  - current location that the "person" is

```py
def find_path(elevation_map_data, starting_location):
    """
    elevation_map_data - list of lists
    starting_location - (x, y) tuple

    continually call find_next_step(elevation_map_data, current_location)
    """

    path = [starting_location]
    current_location = starting_location

    while current_location[0] < len(elevation_map_data[0]):
      next_location = find_next_step(elevation_map_data, current_location)
      path.append(next_location)

    return path    
```

```py
class Pathfinder:
    def __init__(self, elevation_map: ElevationMap, starting_location):
        self.elevation_map = elevation_map
        self.current_location = starting_location
        self.path = [self.current_location]

    def find_path(self):
        while self.current_location[0] < self.elevation_map.get_width():
            self.path.append(self.find_next_step())

        return self.path

    def find_next_step(self):
        pass