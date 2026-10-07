# Who actually controls the camera?

## Problem
The camera rotates correctly for one frame, then snaps back. Multiple systems may be writing the same output: player input, animation, scene scripting, and the vehicle camera.

## Build the data flow
Separate `LookController`, which collects intent, `ViewState`, which stores state, `ViewPoseSolver`, which resolves the pose, and `RenderView`, which sends the result to the renderer. A camera object in the scene is not necessarily the active view. Give activation to `ViewDirector`, which selects an owner using explicit priorities.

```text
device -> LookController -> ViewState -> ViewPoseSolver -> RenderView
                                ^
                     scene / vehicle / assistance
```

For a camera driven by the skeleton, change the solver input instead of a transform that animation will overwrite. Decide whether horizontal rotation belongs to the body or the local view. Applying the full delta in both places doubles the turn.

```text
if freeBodyHeading:
    actor.yaw += look.yaw
    view.localYawDelta = 0
else:
    view.localYawDelta = look.yaw
view.localPitchDelta = look.pitch
```

## Check in game
Display the active owner, yaw source, and final yaw. Test turning, entering a vehicle, and returning from a scene. Every frame should have an unambiguous owner of the final view.

---

[Table of contents](../README.md) | [Next tutorial](02-input-and-time.md)
