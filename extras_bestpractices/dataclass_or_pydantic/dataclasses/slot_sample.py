from dataclasses import dataclass

"""
    - Slots can be used to make classes faster and use less memory. Data classes have no explicit syntax for working with slots, but 
    the normal way of creating slots works for data classes as well. (They really are just regular classes!)
"""


@dataclass()
class SimplePosition:
    __slots__ = ["name", "lon", "lat"]
    name: str
    lon: float
    lat: float


slot1 = SimplePosition("oslo", 19.5, 78.8)
print(slot1)

