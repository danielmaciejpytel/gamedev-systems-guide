<h1 align="center">GameDev Systems Guide</h1>

<p align="center"><b>Practical systems for responsive, coherent games.</b><br>
Engine-independent tutorials on cameras, animation, locomotion, ground contact and transitions between gameplay and scenes.</p>

<p align="center">
  <img src="https://img.shields.io/badge/type-written_guide-2E86AB?style=for-the-badge&labelColor=1f2937" alt="Written guide">
  <img src="https://img.shields.io/badge/tutorials-20-F6AE2D?style=for-the-badge&labelColor=1f2937" alt="20 tutorials">
  <img src="https://img.shields.io/badge/engine-independent-E4572E?style=for-the-badge&labelColor=1f2937" alt="Engine independent">
  <img src="https://img.shields.io/badge/language-English-2E86AB?style=for-the-badge&labelColor=1f2937" alt="Language: English">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/examples-Python_standard_library-F6AE2D?style=flat-square&labelColor=1f2937" alt="Examples use only the Python standard library">
</p>

<p align="center">
  <a href="README.pl.md">Polski</a> · <b>English</b> ·
  <a href="#start-reading">Start reading</a> ·
  <a href="#tutorials">Tutorials</a> ·
  <a href="#examples-and-practice">Examples and practice</a> ·
  <a href="#running-the-tests">Running the tests</a>
</p>

Each tutorial presents a problem, an implementation approach and an in-game verification scenario. This is a written guide, not a game or a plugin. The tutorials and examples are in English only; `README.pl.md` is a Polish version of this page, not a translation of the guide.

## Start reading

- Building a complete system: start with [Who actually controls the camera?](tutorials/01-camera-ownership.md) and continue in order.
- Chasing a specific problem: pick the matching topic in [Tutorials](#tutorials).
- Want to try things in an engine: use the [in-engine practice plan](PRACTICE.md).

The material is engine-independent. Type, bone, field and asset names are illustrative. Blocks marked `text` are pseudocode that needs an adapter for your engine's units, axes, APIs and update lifecycle. They are not a ready-made plugin.

## Tutorials

Camera:

1. [Who actually controls the camera?](tutorials/01-camera-ownership.md)
2. [Input, pause, and different clocks](tutorials/02-input-and-time.md)
3. [Predictable angles, corrections, and resets](tutorials/03-angles-limits-and-resets.md)
4. [Soft rotation limits and return to center](tutorials/04-soft-rotation-limits.md)
5. [FOV: horizontal, vertical, and aspect ratio](tutorials/05-fov-and-projection.md)
6. [Parameter smoothing and partial updates](tutorials/06-parameter-blending.md)
7. [Depth of field and a dynamic focus target](tutorials/07-depth-of-field.md)
8. [Camera motion layers and player comfort](tutorials/08-camera-motion-and-comfort.md)
9. [Rigs, reflection, and stable data contracts](tutorials/09-rigs-and-data-contracts.md)

Locomotion and animation:

10. [Locomotion: intent, actual movement, and stride phase](tutorials/10-locomotion.md)
11. [Animation selection tables, wildcards, and fallback](tutorials/11-animation-selection.md)
12. [Clip playback, blending, and events](tutorials/12-clips-blending-and-events.md)
13. [State machines and smooth transitions through inertialization](tutorials/13-state-machines-and-inertialization.md)
14. [Damping, interpolation, and springs](tutorials/14-damping-and-springs.md)
15. [Root motion, target alignment, and stride length](tutorials/15-root-motion-and-stride.md)
16. [Floor IK and stable ground contact](tutorials/16-floor-ik.md)

Scenes, vehicles and configuration:

17. [Scenes, request queues, and returning control](tutorials/17-scenes-and-control-handover.md)
18. [Vehicle camera: boom, autocenter, and collision](tutorials/18-vehicle-camera.md)
19. [Switching perspective and blending the full view](tutorials/19-perspectives-and-proxy.md)
20. [Configuration, caches, and evidence of correct behavior](tutorials/20-configuration-and-debugging.md)

## Examples and practice

- **[`examples/camera_math.py`](examples/camera_math.py)** — camera mathematics and smoothing. Standalone, standard library only. It demonstrates the mathematics and simple mechanisms, not a renderer or a complete animation graph.
- **[`tests/test_camera_math.py`](tests/test_camera_math.py)** — behaviour tests for the examples.
- **[`PRACTICE.md`](PRACTICE.md)** — an in-engine practice plan: ten exercises, each with an expected result and the evidence to collect. Repeat them at different frame rates, during pause and in slow motion.

## Running the tests

From the repository root:

```sh
python -m unittest discover -s tests -v
```

Smooth cameras, animation and movement contribute to game quality. Clear goals, level design, sound, balance and accessibility also require their own iterations and playtests.
