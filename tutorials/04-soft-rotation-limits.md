# Soft rotation limits and return to center

## Goal
A hard clamp stops the camera abruptly. A soft zone attenuates outward motion before the boundary and can gently return the view to its allowed range.

```text
distanceToEdge = maxYaw - yaw
outwardScale = smoothstep(0, softMargin, distanceToEdge)
if inputYaw > 0:
    inputYaw *= outwardScale
```

Here, `smoothstep` is an illustrative curve choice. Handle the left boundary symmetrically. Movement toward the center should remain responsive. Limit the soft zone to half the available range; for a zero range, lock the axis without dividing by zero.

Separate angle limits, input damping, and return speed. This lets a designer create a soft stop without strong autocentering. When changing limits at runtime, smooth them and handle a current angle outside the new range.

## Aspect ratio
Changing aspect ratio changes the visible area. If look limits protect a scene's framing, derive them from the actual projection. Approximating horizontal FOV as `verticalFov * aspect` is not an exact perspective conversion.

## Check in game
Hold the stick at the boundary, reverse direction, and narrow the range during motion. Compare 16:9 with an ultrawide display. Evaluate control feel and framing.

---

[Table of contents](../README.md) | [Previous tutorial](03-angles-limits-and-resets.md) | [Next tutorial](05-fov-and-projection.md)
