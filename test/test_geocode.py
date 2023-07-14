import unittest

import pytest

from iheat import _address2latlon


class TestAddress2LatLon(unittest.TestCase):
    def test_address2latlon(self):
        address = "Berlin"
        expected_lat, expected_lon = 52.5170365, 13.3888599
        lat, lon = _address2latlon(address)
        self.assertAlmostEqual(lat, expected_lat, places=4)
        self.assertAlmostEqual(lon, expected_lon, places=4)

    def test_address2latlon_edge_case(self):
        address = "Nonexistent Address"
        with pytest.raises(Exception):
            _address2latlon(address)


if __name__ == "__main__":
    unittest.main()
