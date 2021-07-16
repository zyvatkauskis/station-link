from typing import List, Optional
import math
from link_station.inputs import Station, Coordinates


def get_distance_between_coordinates(station: Station, device: Coordinates) -> float:
    """
    Get distance from station to device.
    """
    return math.sqrt((station.x - device.x) ** 2 + (station.y - device.y) ** 2)


def get_power(station: Station, device: Coordinates) -> float:
    """
    Get power for given device.
    """
    distance = get_distance_between_coordinates(station, device)
    return (station.reach - distance) ** 2 if distance < station.reach else 0


def best_link_station_with_power(
    best_station: Station, device: Coordinates, power: Optional[float]
) -> str:
    if not power:
        return f'No link station within reach for point {device.x},{device.y}\n'
    return (
        f'Best link station for point {device.x},{device.y} is '
        f'{best_station.x},{best_station.y} with power {power}\n'
    )


def get_best_link_station_with_power(
    link_stations: List[Station], device: Coordinates
) -> str:
    """
    Get link station with most power for this device.
    """
    best_power = 0
    best_station = None
    for station in link_stations:
        power = get_power(station, device)
        if power > best_power:
            best_station = station
            best_power = power

    return best_link_station_with_power(best_station, device, best_power)
