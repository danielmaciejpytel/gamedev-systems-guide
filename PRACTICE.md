# In-engine practice plan

Build a small test scene and work through these exercises in order.

| Exercise | Expected result | Evidence |
|---|---|---|
| One camera owner | No doubled yaw or overwritten transform | Owner and angle logs |
| FOV across aspect ratios | Preserve the selected FOV axis | Screenshots of the same scene |
| Repeated transition request | Reach the target within the specified duration | Value-over-time plot |
| DOF target disappears | Controlled fallback | Recording and provider log |
| Walk/run blending | No duplicate footsteps | Event log and audio playback |
| Movement against a wall | Animation matches actual motion | Desired and actual speed |
| Stairs and a platform | Stable supporting foot | Trace and IK visualization |
| Camera near an obstacle | No clipping and a smooth return | Boom recording |
| Rapid transition reversal | Continuous view and optics | Active-perspective log |
| Scene interruption | Restore correct controls | Lock and snapshot logs |

Repeat exercises at different frame rates, during pause, and in slow motion. Include missing assets, teleportation, and configuration changes at runtime. Separate mathematical test results from integration evidence and player feedback on feel.
