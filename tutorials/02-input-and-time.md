# Input, pause, and different clocks

## Problem
The same sensitivity behaves differently at low frame rates, during slow motion, and while paused.

## Separate the units
A mouse usually supplies displacement accumulated between frames. A stick supplies deflection, which you convert into angular velocity. Do not multiply mouse delta by time again if the backend already provides displacement.

```text
mouseAngle = mouseDelta * degreesPerMouseUnit
stickAngle = stickAxis * degreesPerSecond * realDt
simulationDt = realDt * timeScale
```

Real time suits interface responsiveness and controls during slow motion. Simulation time suits movement in the world. This is a design choice: pause can block gameplay while still allowing rotation of a preview camera.

Handle `dt <= epsilon` before computing `angleDelta / dt`. Replacing every zero with an artificial step can produce a huge velocity. Choose whether to skip the update or keep the previous value.

## Order matters
Document the pipeline: device filtering, aim assistance, look-at, recoil, constraints, and final orientation. Distinguish a correction added to input from a takeover that removes user input.

## Check in game
Replay the same input sequence at 30, 60, and 144 FPS, during pause, and with `timeScale = 0.25`. Compare the final angle and response latency. Document each parameter's units next to its definition.

---

[Table of contents](../README.md) | [Previous tutorial](01-camera-ownership.md) | [Next tutorial](03-angles-limits-and-resets.md)
