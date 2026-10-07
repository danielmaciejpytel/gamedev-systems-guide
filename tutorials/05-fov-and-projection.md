# FOV: horizontal, vertical, and aspect ratio

## Problem
The number in the settings may not use the convention expected by the camera. One can represent horizontal FOV and the other vertical FOV.

For `aspect = width / height`:

```text
vertical = 2 * atan(tan(horizontal / 2) / aspect)
horizontal = 2 * atan(tan(vertical / 2) * aspect)
```

Trigonometric functions use radians. Convert the result to degrees afterward. Avoid hidden offsets in the user setting; if calibration is required, name and explain it in the configuration.

## Implementation
Choose one internal convention, such as vertical FOV. Accept only finite values strictly between 0 and 180 degrees, and positive aspect ratios. An editor slider's range does not protect a setter called from code.

The runnable example is in [camera_math.py](../examples/camera_math.py). The `horizontal_to_vertical` function performs the conversion and validates its arguments.

## Body and weapon
A wider frame can reveal shoulders and arms. Treat camera position compensation relative to the body as a separate system with limited influence. Keep projection settings distinct from transform offsets. A separate weapon projection requires explicit clipping-plane and rendering configuration.

## Check in game
Change aspect ratio while keeping vertical FOV fixed, then while keeping horizontal FOV fixed. Each approach preserves a different part of the frame. Check aiming, body visibility, and weapon clipping.

---

[Table of contents](../README.md) | [Previous tutorial](04-soft-rotation-limits.md) | [Next tutorial](06-parameter-blending.md)
