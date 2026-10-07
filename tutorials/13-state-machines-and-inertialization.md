# State machines and smooth transitions through inertialization

## State rules
Define the default state, transition priorities, and whether a global transition can interrupt a local one. Enter and exit events should occur exactly once. Guard against a transition loop within one frame.

## Inertialization
A regular crossfade evaluates two poses and blends them. Inertialization switches to the new animation and decays an offset from the previous motion, including its velocity.

```text
outputPose = newPose + decayingOffset
```

This is conceptual notation: rotations need a delta quaternion or axis-angle representation rather than matrix addition. Keep previous samples, calculate error and velocity, then decay them with a function that ends smoothly. A simple lerp does not preserve the same velocity continuity.

## Lifecycle
A teleport should reset history so the old pose does not pull the character toward its previous location. Ragdoll and rig changes require separate policies. With LOD restrictions, an active effect may require updates even when animation would normally be skipped.

A zero transition time in the state machine does not necessarily cause a visible snap if smoothing is handled by the next stage.

## Check in game
Interrupt a run start with a stop, teleport during a transition, and change LOD. Evaluate limb velocity discontinuities as well as position.

---

[Table of contents](../README.md) | [Previous tutorial](12-clips-blending-and-events.md) | [Next tutorial](14-damping-and-springs.md)
