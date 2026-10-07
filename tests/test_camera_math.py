import math
import unittest

from examples.camera_math import (horizontal_to_vertical, exponential_follow,
                                 wrap_degrees, focus_range, ScalarTransition)


class CameraMathTests(unittest.TestCase):
    def test_projection_round_trip(self):
        for aspect in (1, 16/9, 21/9):
            vertical = horizontal_to_vertical(90, aspect)
            horizontal = math.degrees(2 * math.atan(
                math.tan(math.radians(vertical) / 2) * aspect))
            self.assertAlmostEqual(horizontal, 90)

    def test_projection_rejects_invalid_inputs(self):
        for angle, aspect in ((0, 1), (180, 1), (80, 0), (math.nan, 1)):
            with self.assertRaises(ValueError):
                horizontal_to_vertical(angle, aspect)

    def test_damping_is_independent_of_step_partition(self):
        one_step = exponential_follow(0, 10, 4, 1)
        many_steps = 0
        for _ in range(120):
            many_steps = exponential_follow(many_steps, 10, 4, 1/120)
        self.assertAlmostEqual(one_step, many_steps)

    def test_pause_does_not_move_damping(self):
        self.assertEqual(exponential_follow(2, 10, 4, 0), 2)

    def test_angles_cross_boundary(self):
        self.assertEqual(wrap_degrees(181), -179)
        self.assertEqual(wrap_degrees(-181), 179)

    def test_focus_near_camera_is_ordered(self):
        values = focus_range(0.2, 2, 1, 1, 3)
        self.assertEqual(values, tuple(sorted(values)))
        self.assertEqual(values[:2], (0, 0))

    def test_focus_rejects_reversed_offsets(self):
        with self.assertRaises(ValueError):
            focus_range(5, 1, 2, 1, 3)

    def test_identical_requests_complete_on_time(self):
        transition = ScalarTransition(60)
        for _ in range(8):
            transition.request(80, 1)
            transition.update(0.125)
        self.assertEqual(transition.current, 80)

    def test_interrupted_transition_starts_at_current_value(self):
        transition = ScalarTransition(60)
        transition.request(80, 1)
        transition.update(0.5)
        value_at_interrupt = transition.current
        transition.request(50, 1)
        self.assertEqual(transition.update(0), value_at_interrupt)
        self.assertEqual(transition.update(1), 50)

    def test_zero_duration_snaps_even_to_existing_target(self):
        transition = ScalarTransition(60)
        transition.request(80, 1)
        transition.update(0.2)
        transition.request(80, 0)
        self.assertEqual(transition.current, 80)


if __name__ == '__main__':
    unittest.main()
