# Scenes, request queues, and returning control

## Problem
A scene leaves FOV changed or look input locked. Camera takeover lacks a complete lifecycle.

## Control transaction
On entry, capture the base state: view owner, optics, limits, procedural weights, and locks. Give the takeover an identifier so an old scene's completion cannot release a lock owned by a newer scene.

```text
token = director.acquire(ScenePriority)
snapshot = captureViewState()
playScene(token)
blendBackToGameplay(token, snapshot)
director.release(token)
```

A snapshot need not restore every old value unconditionally. A comfort setting changed by the player during the scene should usually survive. Define which fields belong to the scene and which belong to the user.

## Queue and streaming
An activation request does not mean the camera is immediately ready. Process the queue at a defined frame stage. Deduplicate requests and provide cancellation, a timeout, and retries for assets that are not yet ready.

A change lock should specify whether it covers activation, optics, and movement. Marking a camera cut is a separate decision that may reset renderer history.

## Check in game
Interrupt a scene, seek its timeline, disable an actor after streaming, and start a second scene before the first ends. After returning control, check the body, camera, and input locks.

---

[Table of contents](../README.md) | [Previous tutorial](16-floor-ik.md) | [Next tutorial](18-vehicle-camera.md)
