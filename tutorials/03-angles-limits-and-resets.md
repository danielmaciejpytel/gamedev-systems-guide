# Predictable angles, corrections, and resets

## Model
Keep the player angle separate from the correction angle. Name the output `finalYaw` so a consumer does not add the correction a second time.

```text
playerYaw = clamp(wrap(playerYaw + inputYaw), minYaw, maxYaw)
correctionYaw += externalYaw
finalYaw = playerYaw + correctionYaw
```

This model constrains input but lets corrections exceed the range. If you need an absolute safety boundary, constrain the sum as well. Decide explicitly whether an orientation override bypasses the normal limits.

## Proportional reset
The reset `x *= max(0, 1 - speed * dt)` slows near zero. A constant-speed reset, `moveTowards(x, 0, degreesPerSecond * dt)`, responds differently. The exponential version, `x *= exp(-speed * dt)`, preserves the same decay rate across different time steps. Use a small completion threshold if you need an exact zero.

## Commands within one frame
If orientation can only be forced once per frame, define the policy: first request, last request, or highest priority. Do not hide it in incidental call order. Collect requests and resolve them before updating the pose.

## Check in game
Apply a correction beyond the range, reset while input is active, and submit two forced orientations in one frame. Observe player angle, correction, and output separately. Test crossing the -180/180-degree boundary.

---

[Table of contents](../README.md) | [Previous tutorial](02-input-and-time.md) | [Next tutorial](04-soft-rotation-limits.md)
