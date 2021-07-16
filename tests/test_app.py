from mock import Mock, call

from link_station.app import run_for_default_data
from link_station.inputs import Station, Coordinates


def test_run_for_default_data(mocker):
    get_best_link_station_with_power_mock = Mock()
    get_best_link_station_with_power_mock.return_value = "test1"
    mocker.patch(
        "link_station.app.get_best_link_station_with_power",
        get_best_link_station_with_power_mock,
    )

    actual_value = run_for_default_data()
    get_best_link_station_with_power_mock.assert_has_calls(
        [
            call(
                [
                    Station(x=0, y=0, reach=10),
                    Station(x=20, y=20, reach=5),
                    Station(x=10, y=0, reach=12),
                ],
                Coordinates(x=0, y=0),
            ),
            call(
                [
                    Station(x=0, y=0, reach=10),
                    Station(x=20, y=20, reach=5),
                    Station(x=10, y=0, reach=12),
                ],
                Coordinates(x=100, y=100),
            ),
            call(
                [
                    Station(x=0, y=0, reach=10),
                    Station(x=20, y=20, reach=5),
                    Station(x=10, y=0, reach=12),
                ],
                Coordinates(x=15, y=10),
            ),
            call(
                [
                    Station(x=0, y=0, reach=10),
                    Station(x=20, y=20, reach=5),
                    Station(x=10, y=0, reach=12),
                ],
                Coordinates(x=18, y=18),
            ),
        ]
    )
    assert actual_value == "test1test1test1test1"
