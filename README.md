# GameDev Systems Guide

Practical tutorials on systems that help build a responsive and coherent game: cameras, animation, locomotion, ground contact, and transitions between gameplay and scenes.

Each tutorial presents a problem, an implementation approach, and an in-game verification scenario. Start with camera ownership when building a complete system. For a specific issue, choose the relevant topic below.

## How to use this guide

The material is engine-independent. Type, bone, field, and asset names are illustrative. Blocks marked `text` are pseudocode that needs an adapter for your engine's units, axes, APIs, and update lifecycle. They are not a ready-made plugin.

The Python examples are standalone and use only the standard library. They demonstrate mathematics and simple mechanisms, rather than simulating a renderer or a complete animation graph.

From the repository root, run:

```sh
python -m unittest discover -s tests -v
```

## Tutorials

- [Who actually controls the camera?](tutorials/01-camera-ownership.md)
- [Input, pause, and different clocks](tutorials/02-input-and-time.md)
- [Predictable angles, corrections, and resets](tutorials/03-angles-limits-and-resets.md)
- [Soft rotation limits and return to center](tutorials/04-soft-rotation-limits.md)
- [FOV: horizontal, vertical, and aspect ratio](tutorials/05-fov-and-projection.md)
- [Parameter smoothing and partial updates](tutorials/06-parameter-blending.md)
- [Depth of field and a dynamic focus target](tutorials/07-depth-of-field.md)
- [Camera motion layers and player comfort](tutorials/08-camera-motion-and-comfort.md)
- [Rigs, reflection, and stable data contracts](tutorials/09-rigs-and-data-contracts.md)
- [Locomotion: intent, actual movement, and stride phase](tutorials/10-locomotion.md)
- [Animation selection tables, wildcards, and fallback](tutorials/11-animation-selection.md)
- [Clip playback, blending, and events](tutorials/12-clips-blending-and-events.md)
- [State machines and smooth transitions through inertialization](tutorials/13-state-machines-and-inertialization.md)
- [Damping, interpolation, and springs](tutorials/14-damping-and-springs.md)
- [Root motion, target alignment, and stride length](tutorials/15-root-motion-and-stride.md)
- [Floor IK and stable ground contact](tutorials/16-floor-ik.md)
- [Scenes, request queues, and returning control](tutorials/17-scenes-and-control-handover.md)
- [Vehicle camera: boom, autocenter, and collision](tutorials/18-vehicle-camera.md)
- [Switching perspective and blending the full view](tutorials/19-perspectives-and-proxy.md)
- [Configuration, caches, and evidence of correct behavior](tutorials/20-configuration-and-debugging.md)

## Examples and exercises

- [Camera mathematics and smoothing](examples/camera_math.py)
- [Behavior tests for the examples](tests/test_camera_math.py)
- [In-engine practice plan](PRACTICE.md)

Smooth cameras, animation, and movement contribute to game quality. Clear goals, level design, sound, balance, and accessibility also require their own iterations and playtests.
