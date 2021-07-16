from link_station.inputs import Station, Coordinates
from link_station.manager import get_best_link_station_with_power


def run_for_default_data():
    """Run program for default data"""
    # initialize data
    link_stations = [
        Station(0, 0, 10),
        Station(20, 20, 5),
        Station(10, 0, 12),
    ]
    devices = [
        Coordinates(0, 0),
        Coordinates(100, 100),
        Coordinates(15, 10),
        Coordinates(18, 18),
    ]

    return "".join(
        get_best_link_station_with_power(link_stations, device) for device in devices
    )


if __name__ == "__main__":
    print(run_for_default_data())
