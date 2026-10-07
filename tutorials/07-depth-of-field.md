# Depth of field and a dynamic focus target

## Contract
Store distances in one world unit and maintain this relationship:

```text
0 <= nearBlur <= nearFocus <= farFocus <= farBlur
```

The names represent the end of full near blur, the start of the sharp range, the end of the sharp range, and the start of full far blur. Definitions vary by renderer, so adapt the interface accordingly.

## Moving target
Compute the target's distance from the camera, then build the range from offsets:

```text
d = length(targetPosition - cameraPosition)
nearBlur  = max(0, d - outerNearOffset)
nearFocus = max(0, d - innerNearOffset)
farFocus  = d + innerFarOffset
farBlur   = d + outerFarOffset
```

Validate offset ordering and finite values. Decide whether to use Euclidean distance or depth along the view axis; the renderer may expect the latter.

## Missing target
A provider may lose an actor, attachment slot, or component during streaming. Return an explicit missing result. Camera policy can retain the last range, fade out DOF, or restore base settings. Do not choose an arbitrary target.

## Check in game
Move the target through the camera, remove it during a scene, and set its distance close to zero. Check continuity and consistent units. [camera_math.py](../examples/camera_math.py) includes a function that builds an ordered focus range.

---

[Table of contents](../README.md) | [Previous tutorial](06-parameter-blending.md) | [Next tutorial](08-camera-motion-and-comfort.md)
