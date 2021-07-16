from dataclasses import dataclass
from typing import Union


@dataclass
class Coordinates:
    """
    A Class for stooring x and y coordinates
    """

    x: Union[float, int]
    y: Union[float, int]


@dataclass
class Station(Coordinates):
    """
    A Class for stooring stations coordinates and reach
    """

    reach: Union[float, int]