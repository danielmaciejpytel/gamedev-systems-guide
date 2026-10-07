# Locomotion: intent, actual movement, and stride phase

## Input data
Separate desired, actual, and filtered speed. A character may want to sprint while standing against a wall. Animation based only on intent will show running in place.

```text
horizontalSpeed = length(vec2(velocity.x, velocity.z))
verticalSpeed = velocity.y
desiredSpeed = inputMagnitude * selectedMaxSpeed
```

This example assumes Y is up. Adapt the axes for another engine. The length of a 3D velocity vector includes vertical movement; consider this before using it to select a gait.

## Direction and context
Compute movement direction relative to facing. For a nearly zero vector, retain the previous direction or use an explicit idle state instead of normalizing zero. Separate ground slope, path incline, and turn curvature.

## Planning
Separate starts, loops, and stops. Select transitions with foot phase in mind to avoid a jump in the supporting leg. Playback rate and root-motion displacement scale are different parameters: faster playback does not mean a longer stride.

## Check in game
Test walls, backward movement, strafing, stairs, abrupt stops, and landing. Log intent and actual speed. Good locomotion communicates the player's decision while matching physical movement.

---

[Table of contents](../README.md) | [Previous tutorial](09-rigs-and-data-contracts.md) | [Next tutorial](11-animation-selection.md)
