# Rigs, reflection, and stable data contracts

## Problem
Renaming a bone or field can break a graph even when its data type and the model's appearance stay the same.

## Validate before use
The example solver requires `ViewPivot`, `ChestAnchor`, `ViewAim`, and `MotionRoot`. Check that every index exists before reading parents. Then validate the relationship `ViewAim -> ViewPivot -> ChestAnchor`.

```text
indices = resolveRequiredBones(rig)
if anyMissing(indices):
    return DisabledSolver("missing bone")
if parent(indices.viewAim) != indices.viewPivot:
    return DisabledSolver("invalid hierarchy")
```

An error state must block both updating and sampling. Setting `initialized = false` provides no protection if nobody checks it.

## API and serialization
A public native method is not necessarily available to scripts. Reflection, editor visibility, and write access are separate contracts. Register APIs deliberately and provide migration of serialized graphs and data when names change.

Initialize every field of an animation data packet. Assertions help during development, but runtime input validation should work independently of build configuration.

## Check in game
Remove a required bone, change its parent, and load an older asset. Expect a clear message and a safe fallback pose. An identical memory layout cannot repair incompatible names.

---

[Table of contents](../README.md) | [Previous tutorial](08-camera-motion-and-comfort.md) | [Next tutorial](10-locomotion.md)
