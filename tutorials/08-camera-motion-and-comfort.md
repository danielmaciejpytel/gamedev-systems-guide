# Camera motion layers and player comfort

## Problem
Disabling one multiplier does not remove all view motion. Animated sway, parallax, recoil, procedural vehicle response, and scenes have separate sources.

## Design
Define separate channels: `bodyMotion`, `lookOffset`, `weaponKick`, `vehicleMotion`, and `sceneMotion`. Each should have its own weight, space, and composition stage.

```text
vehicleContribution = vehiclePose * vehicleModeWeight * comfortVehicleWeight
```

Zeroing either weight removes this contribution without affecting other channels. Do not label a single field "disable all motion" when it only controls parallax.

## Spaces
A sideways offset relative to the camera differs from one relative to the chest or trajectory. Transform the vector through the appropriate space. Document the axis convention and transform multiplication order.

## Comfort options
Expose independent controls for sway, roll, shake, and blur. Motion used to communicate a hit can partly be replaced by sound, HUD feedback, and weapon animation. Sudden FOV changes also affect perceived motion.

## Check in game
Disable channels individually. Test walking, sprinting, looking down, a vehicle collision, and a scene. Record each channel's contribution before composition so diagnosis does not rely on guessing.

---

[Table of contents](../README.md) | [Previous tutorial](07-depth-of-field.md) | [Next tutorial](09-rigs-and-data-contracts.md)
