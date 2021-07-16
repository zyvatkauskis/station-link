from mock import Mock, call
import pytest
from link_station.manager import (
    get_distance_between_coordinates,
    get_power,
    best_link_station_with_power,
    get_best_link_station_with_power,
)
from link_station.inputs import Station, Coordinates


def coordinates_fixtures():
    return [
        (
            Station(20, 20, 0),
            Coordinates(21, 21),
            1.4142135623730951,
        ),
        (
            Station(4, 2, 0),
            Coordinates(6, 5),
            3.605551275463989,
        ),
        (
            Station(8, 0, 0),
            Coordinates(3, 6),
            7.810249675906654,
        ),
    ]


@pytest.mark.parametrize('test_c1,test_c2,expected', coordinates_fixtures())
def test_get_distance_between_coordinates(test_c1, test_c2, expected):
    assert get_distance_between_coordinates(test_c1, test_c2) == expected


def test_get_power(mocker):
    station_coordinates = Station(x=10, y=10, reach=5)
    device_coordinates = Coordinates(x=12, y=12)

    get_distance_between_coordinates_mock = Mock()
    get_distance_between_coordinates_mock.return_value = 10

    mocker.patch(
        'link_station.manager.get_distance_between_coordinates',
        get_distance_between_coordinates_mock,
    )

    actual_value = get_power(station_coordinates, device_coordinates)

    get_distance_between_coordinates_mock.assert_called_with(
        station_coordinates, device_coordinates
    )
    assert actual_value == 0

    get_distance_between_coordinates_mock.return_value = 2

    actual_value = get_power(station_coordinates, device_coordinates)
    assert actual_value == 9


def best_link_fixtures():
    return [
        (
            Station(x=2, y=1, reach=12),
            Coordinates(x=4, y=5),
            50,
            'Best link station for point 4,5 is 2,1 with power 50\n',
        ),
        (
            Station(x=33, y=3, reach=5),
            Coordinates(x=5, y=6),
            None,
            'No link station within reach for point 5,6\n',
        ),
    ]


@pytest.mark.parametrize('station,coordinates,power,expected', best_link_fixtures())
def test_best_link_station_with_power(station, coordinates, power, expected):
    assert best_link_station_with_power(station, coordinates, power) == expected


def test_get_best_link_station_with_power(mocker):
    link_stations = [Station(x=33, y=3, reach=5), Station(x=5, y=6, reach=1)]
    device = Coordinates(x=2, y=6)
    get_power_mock = Mock()
    get_power_mock.return_value = 100

    best_link_station_with_power_mock = Mock()
    best_link_station_with_power_mock.return_value = 'success'

    mocker.patch('link_station.manager.get_power', get_power_mock)
    mocker.patch(
        'link_station.manager.best_link_station_with_power',
        best_link_station_with_power_mock,
    )

    actual_value = get_best_link_station_with_power(link_stations, device)

    get_power_mock.assert_has_calls(
        [
            call(Station(x=33, y=3, reach=5), Coordinates(x=2, y=6)),
            call(Station(x=5, y=6, reach=1), Coordinates(x=2, y=6)),
        ]
    )
    best_link_station_with_power_mock.assert_called_with(
        Station(x=33, y=3, reach=5), Coordinates(x=2, y=6), 100
    )

    assert actual_value == 'success'