"""
    1- Comparison
    2- Representation
    3- How to add default values
    4- How data class allow for ordering of objs
    5- How to represent immutable data
    6- How data class handle inheritance
"""
from cmath import sin
from dataclasses import dataclass, field
from math import radians, cos, asin, sqrt

"""
    A data class is a regular Python class. 
    The only thing that sets it apart is that it has basic data model methods like 
    .__init__(), .__repr__(), and .__eq__() implemented for you.
    
    1- Dataclass requires type hint, we can use Any
    2- The metadata (and other information about a field) can be retrieved using the fields() function
"""


@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={"unit": "degrees"})
    lat: float = field(default=0.0, metadata={"unit": "degrees"})

    def distance_of(self, other):
        r = 6371  # Earth radius in km
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)

        h = (
            sin((phi_2 - phi_1) / 2) ** 2 + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2
        )

        return 2 * r * asin(sqrt(h))


@dataclass
class Capital(Position):
    country: str = field(default="Norway", metadata="capital_of_a_country")


ha_noi = Capital(name="HaNoi", country="VietNam", lat=40.0)
print(ha_noi)


# oslo = Position("Oslo", 10.8, 59.9)
# vancouver = Position("Vancouver", -123.1, 49.3)
# print(oslo.distance_of(vancouver))
#
# null_island = Position("Null Island")
# print(null_island)




