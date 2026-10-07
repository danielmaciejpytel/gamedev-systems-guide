# Damping, interpolation, and springs

## Choose the mechanism for the goal
A lerp with a fixed weight per frame changes its response with FPS. Exponential damping uses:

```text
alpha = 1 - exp(-response * dt)
value += (target - value) * alpha
```

A constant rate limits maximum change per second. A spring also stores velocity and can produce inertia or oscillation. These mechanisms are not interchangeable.

## Spring
An example semi-implicit integrator:

```text
acceleration = (stiffness * (target - value) - damping * velocity) / mass
velocity += acceleration * step
value += velocity * step
```

Require positive mass and nonnegative damping and stiffness. Split a large `dt` into small substeps, but cap the cost after a frame hitch. Parameters and integration method jointly determine stability. Critical damping for the continuous model is `2 * sqrt(stiffness * mass)`; the discrete integrator still needs testing.

## Angles
Choose the shortest angular difference by wrapping around zero. For quaternions, use rotation interpolation and remember that `q` and `-q` describe the same orientation.

## Check in game
Apply a step change, sinusoidal target motion, and a frame hitch. Compare settling time and overshoot at different frame rates. The Python example includes `exponential_follow`.

---

[Table of contents](../README.md) | [Previous tutorial](13-state-machines-and-inertialization.md) | [Next tutorial](15-root-motion-and-stride.md)
