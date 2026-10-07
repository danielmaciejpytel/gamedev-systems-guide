# Vehicle camera: boom, autocenter, and collision

## Model
Separate the look-at point and camera boom from the final position after collision resolution. A preset defines the intended distance; world geometry may shorten it.

## Collision
Perform a sphere sweep from a safe point near the vehicle to the desired camera position. Filter out the vehicle itself. Separately handle a query that starts inside an obstacle.

```text
allowedDistance = collisionQuery(pivot, desiredPosition, probeRadius)
if allowedDistance < currentDistance:
    currentDistance = allowedDistance
else:
    currentDistance = follow(currentDistance, allowedDistance, returnRate, dt)
```

Immediate shortening prevents movement through walls. A smoothed return reduces camera pumping. Sweep and overlap tests may use different radii because they answer different questions; name the radii separately.

## Autocenter
Wait for a defined interval after manual input, then increase centering strength with vehicle speed. Separate mouse and gamepad settings help achieve the expected feel. Copying vehicle yaw does not require copying pitch and roll.

## Check in game
Reverse near a wall, drive under a bridge, pass a narrow pole, and jump off a ramp. Check that collision shortens the boom immediately and leaving an obstacle does not suddenly push the camera outward.

---

[Table of contents](../README.md) | [Previous tutorial](17-scenes-and-control-handover.md) | [Next tutorial](19-perspectives-and-proxy.md)
