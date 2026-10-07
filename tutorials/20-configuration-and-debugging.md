# Configuration, caches, and evidence of correct behavior

## Configuration
A parameter set may be cached. Selecting the same name again need not refresh its data. Use a generation identifier or an explicit `reload`, and handle a missing set with a documented error or base preset.

```text
if active.name != requested.name or active.revision != requested.revision:
    validate(requested)
    active = buildRuntimeParameters(requested)
```

Define units, ranges, and defaults. A weight used as a logical threshold is not a continuous blend. If a field behaves as a binary switch, use a name and type that describe that behavior.

## Debugger
Show input intent, state before constraints, procedural contributions, active preset, owner, and renderer output. Reading a field or having a setter does not prove the final solver uses it. Trace the path to its consumer.

## Verification plan
Check data validation, mathematical tests, graph integration, and runtime behavior. A passing FOV conversion test does not confirm camera comfort in a finished scene.

Test pause, extreme time steps, missing assets, rig changes, teleportation, and interrupted transitions. Repeat scenarios on the target platform in a release build. Debug features and comments are not evidence that a feature works in the player's build.

## Final exercise
Build a small scene with a character, stairs, a vehicle, and a short dialogue sequence. Connect the mechanisms from the previous chapters. Write down expected behavior and compare it with a recording and a log of active systems.

---

[Table of contents](../README.md) | [Previous tutorial](19-perspectives-and-proxy.md)
