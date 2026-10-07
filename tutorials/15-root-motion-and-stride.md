# Root motion, target alignment, and stride length

## Separate base motion and correction
Extract root motion from the clip, transform it into world space, and calculate a separate correction toward the target. This lets you limit correction without destroying the animation's character.

```text
animatedDeltaWorld = actorRotation * animatedDeltaLocal
correction = clampLength(targetError, correctionSpeed * dt)
proposedDelta = animatedDeltaWorld + correction
actualDelta = characterCollision.solve(proposedDelta)
```

This is displacement pseudocode; compose rotations using the appropriate transform operation. After collision resolution, use actual movement for further foot adjustment.

## Stride scale
The ratio of actual movement length to animated movement length helps select stride correction. Use an explicit fallback for a small denominator rather than dividing by almost zero. Constrain the result to a reasonable range and account for the supporting leg.

Scaling XYZ also changes vertical movement. If the goal is only to adjust stride length along the ground, scale horizontal components separately. Control playback rate independently.

## Event target
Aligning a contact, such as a hand reaching a handle, requires the time to a specific marker. A missing marker should disable correction or use a documented fallback. Zero should not pretend that the event was successfully found.

## Check in game
Approach the target from different distances, block movement with collision, and remove the contact marker. Observe foot sliding, root discontinuities, and contact timing.

---

[Table of contents](../README.md) | [Previous tutorial](14-damping-and-springs.md) | [Next tutorial](16-floor-ik.md)
