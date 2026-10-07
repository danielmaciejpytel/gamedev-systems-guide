# Animation selection tables, wildcards, and fallback

## Problem
A general rule captures a case that has its own specific clip.

## Explicit matching policy
In a "first match wins" table, ordering is part of the logic:

```text
action      stance      clip
vault       crouched    vault_low
vault       *           vault_default
*           *           idle_safe
```

Place specific rules before general ones. Alternatively, rank specificity and define how ties are resolved. Do not accidentally mix both policies.

## Schema and fallback
Validate input counts and named columns. Do not rely on a comment that describes a different order than the parser. Distinguish no matching rule, a missing clip, and a clip not yet ready after streaming.

Fallback may be a platform choice, a quality alternative, or a recovery asset. Document when it is selected. If a node selects a clip at activation, changing inputs during Update will not automatically trigger another search.

## Cache
A cache should track database and asset generations. After hot reload, refresh the result or explicitly require reactivation. Otherwise, the editor displays the new table while runtime uses the old wrapper.

## Check in game
Test a shadowed rule, an incorrect input count, a missing asset, and a table changed during playback. The debugger should show the selected row and the reason for fallback.

---

[Table of contents](../README.md) | [Previous tutorial](10-locomotion.md) | [Next tutorial](12-clips-blending-and-events.md)
