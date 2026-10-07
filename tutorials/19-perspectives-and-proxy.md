# Switching perspective and blending the full view

## States
Distinguish requested, target, and actually active perspectives. A change may wait for an asset, scene completion, or character-model visibility.

```text
requestedMode -> policy -> targetMode -> readiness -> activeMode
```

## Proxy
Activate an intermediate view during the transition. Interpolate position, rotation using Slerp, and explicitly selected optical parameters. A proxy that only blends transforms does not automatically blend FOV or DOF.

When the player reverses a transition, use the current output as the new starting point. Do not return to the old start pose. Handle missing participants, including losing one during a transition. Check collision for the intermediate position as well so the camera path does not cut through the vehicle body.

## Character representation
A first-person camera may hide the head while a third-person camera needs it. Prepare the representation before activating the view. Hide it at the appropriate moment when returning.

## Time type
```cpp
const float transitionSeconds = enteringFirstPerson ? 0.0f : configuredSeconds;
```

Storing a duration in `bool` converts every nonzero value to true. Converting it back yields 1 instead of, for example, 0.3. Include units in names and enable conversion warnings.

## Check in game
Switch modes rapidly, during streaming, and close to the vehicle. Track the active view, optics, and head visibility.

---

[Table of contents](../README.md) | [Previous tutorial](18-vehicle-camera.md) | [Next tutorial](20-configuration-and-debugging.md)
