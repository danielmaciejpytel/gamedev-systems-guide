"""Camera mathematics. Angles in degrees, time in seconds.

Educational examples independent of engine APIs.
"""
import math
from dataclasses import dataclass


def require_finite(*values):
    if not all(math.isfinite(value) for value in values):
        raise ValueError('Values must be finite')


def horizontal_to_vertical(horizontal_degrees, aspect):
    require_finite(horizontal_degrees, aspect)
    if not 0 < horizontal_degrees < 180 or aspect <= 0:
        raise ValueError('FOV must be strictly between 0 and 180; aspect must be positive')
    half_angle = math.radians(horizontal_degrees) / 2
    return math.degrees(2 * math.atan(math.tan(half_angle) / aspect))


def exponential_follow(current, target, response, dt):
    require_finite(current, target, response, dt)
    if response < 0 or dt < 0:
        raise ValueError('Response and dt must be nonnegative')
    alpha = -math.expm1(-response * dt)
    return current + (target - current) * alpha


def wrap_degrees(angle):
    require_finite(angle)
    return (angle + 180) % 360 - 180


def focus_range(distance, outer_near, inner_near, inner_far, outer_far):
    require_finite(distance, outer_near, inner_near, inner_far, outer_far)
    if not (distance >= 0 and 0 <= inner_near <= outer_near
            and 0 <= inner_far <= outer_far):
        raise ValueError('Invalid distance or offset ordering')
    return (max(0, distance - outer_near), max(0, distance - inner_near),
            distance + inner_far, distance + outer_far)


@dataclass
class ScalarTransition:
    """Fixed-duration ease-out. An identical target does not restart the timer."""
    current: float
    target: float = None
    start: float = None
    duration: float = 0.0
    elapsed: float = 0.0

    def __post_init__(self):
        require_finite(self.current)
        self.target = self.current
        self.start = self.current

    def request(self, target, duration):
        require_finite(target, duration)
        if duration < 0:
            raise ValueError('Duration must be nonnegative')
        # duration == 0 explicitly requests an immediate assignment.
        if duration == 0:
            self.current = self.target = self.start = target
            self.duration = self.elapsed = 0.0
            return
        if target == self.target:
            return
        self.start, self.target = self.current, target
        self.duration, self.elapsed = duration, 0.0

    def update(self, dt):
        require_finite(dt)
        if dt < 0:
            raise ValueError('dt must be nonnegative')
        if self.duration == 0:
            return self.current
        self.elapsed = min(self.duration, self.elapsed + dt)
        t = self.elapsed / self.duration
        self.current = self.start + (self.target - self.start) * t * (2 - t)
        return self.current
