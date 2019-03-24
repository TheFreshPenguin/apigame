import unittest
from World import World

class APITest(unittest.TestCase):
    def setUp(self):
        self.sight = 1
        self.start_grid = [
            [(0, 8), (0, 8), (0, 8), (0, 8), (1, 8), (1, 8), (1, 8)],
            [(0, 8), (1, 8), (0, 8), (1, 8), (0, 8), (0, 8), (0, 8)],
            [(0, 8), (0, 8), (0, 8), (0, 8), (0, 8), (0, 8), (0, 8)],
            [(0, 8), (1, 8), (1, 8), (0, 8), (0, 8), (0, 8), (0, 8)],
            [(0, 8), (0, 8), (0, 8), (0, 8), (1, 8), (1, 8), (1, 8)],
            [(1, 8), (0, 8), (1, 8), (0, 8), (0, 8), (0, 8), (0, 8)],
            [(1, 8), (1, 8), (1, 8), (1, 8), (0, 8), (0, 8), (0, 8)],
        ]
        World.generate_world_from_grid(self.start_grid)

    def test_movement(self):
        # expected_grid = [
        #     [(0, 8), (1, 8), (0, 8)],
        #     [(0, 8), (0, 8), (0, 8)],
        #     [(0, 8), (0, 8), (1, 8)],
        # ]
        expected_grid = [
            [(0, 8), (0, 8), (0, 8)],
            [(1, 8), (0, 8), (0, 8)],
            [(0, 8), (0, 8), (1, 8)],
        ]
        expected_grid_left = [
            [(0, 8), (0, 8), (0, 8)],
            [(1, 8), (1, 8), (0, 8)],
            [(0, 8), (0, 8), (0, 8)],
        ]
        new_grid = World.explore_world(-1, self.sight)
        self.assertEqual(new_grid, expected_grid)

        new_grid = World.explore_world(2, self.sight)
        self.assertEqual(new_grid, expected_grid_left)

    def tearDown(self):
        pass
