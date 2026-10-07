# Floor IK and stable ground contact

## Pipeline
Sample the base animation first, detect the ground, adjust the pelvis, and then solve leg IK. Decide whether traces use the pose before or after correction to avoid feedback loops.

```text
baseFeet = animatedPose.feet
contacts = traceGround(baseFeet)
pelvisOffset = limitedPelvisCorrection(contacts)
pose = applyPelvisOffset(animatedPose, pelvisOffset)
pose = solveTwoBoneLegs(pose, contacts)
```

## Contact
The surface normal determines foot orientation, but limit the maximum tilt. Smooth contact entry and exit. Lock the supporting foot relative to the ground; on a moving platform, store the point in that platform's space.

The pelvis should help both legs. Limit vertical offset and limb stretching. Not every trace hit is suitable ground: check collision layer, slope, and reach.

## Robustness
Validate bones, segment lengths, and bend direction. A missing hit should reduce IK weight. Teleporting resets the contact cache. At low LOD, trace frequency can be reduced while retaining smooth fading.

## Check in game
Walk over stairs, an edge, a slope, and a moving platform. Test landing and loss of ground contact. Draw traces, contact points, normals, and final IK targets.

---

[Table of contents](../README.md) | [Previous tutorial](15-root-motion-and-stride.md) | [Next tutorial](17-scenes-and-control-handover.md)
