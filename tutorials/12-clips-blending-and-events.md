# Clip playback, blending, and events

## Time trimming
After trimming the beginning and end of a clip, its effective duration is `max(0, duration - trimStart - trimEnd)`. Sample events over the same transformed interval used for the pose. Resuming and restarting have different meanings.

## Pose and events
Pose blending can be written as `blend(A, B, weight)`, but footsteps should not be emitted indiscriminately from both clips. One simple policy chooses events from A below a weight of 0.5 and from B otherwise. Another synchronizes shared markers and removes duplicates.

## Phase
Clips with different durations can share a normalized phase:

```text
timeA = phase * durationA
timeB = phase * durationB
```

Blend-space weights can come from barycentric interpolation. Validate duplicate points and zero axis ranges. Missing samples need an explicit result: a reference pose for regular animation, or a neutral delta for additive animation.

## Additive animation
Additive animation describes a difference from a base pose. Define the reference pose and rotation space; a regular clip does not become a valid delta simply by changing a flag.

## Check in game
Blend walk and run clips with different durations. Listen for duplicate footsteps when crossing 0.5. Test looping, seeking, and a large time step that crosses the end of the clip.

---

[Table of contents](../README.md) | [Previous tutorial](11-animation-selection.md) | [Next tutorial](13-state-machines-and-inertialization.md)
