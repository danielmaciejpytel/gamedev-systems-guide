# Parameter smoothing and partial updates

## Problem
An FOV transition never reaches its target because the setter restarts it every frame.

## Solution
Start a transition when the target changes. Store the start value, target, duration, and progress. For zero duration, apply the target immediately.

```text
if requestedTarget != target:
    start = current
    target = requestedTarget
    elapsed = 0
t = clamp(elapsed / duration, 0, 1)
current = lerp(start, target, t * (2 - t))
```

Float comparisons may require a tolerance or request identifier. If the target genuinely moves every frame, use a tracking filter instead of repeatedly restarting a transition with a fixed duration.

## Two weights
Composing `lerp(base, lerp(base, sceneValue, sceneWeight), overrideWeight)` gives `base + sceneWeight * overrideWeight * (sceneValue - base)`. A weight of 0.5 in both places produces a total influence of 0.25.

## Patch and reset
An event with optional fields should update only supplied values. A missing field does not mean zero. Define a separate reset command and a snapshot of the base state. Distinguish storing state, marking it dirty, and sending it to the animation consumer.

## Check in game
Repeat an identical request for a second, send a patch containing only zoom, and interrupt a transition with a new target. FOV should remain predictable.

---

[Table of contents](../README.md) | [Previous tutorial](05-fov-and-projection.md) | [Next tutorial](07-depth-of-field.md)
