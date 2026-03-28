# Invariant

No valid decision record -> no state mutation.

## Definition

A mutation is any change to system state.

A valid decision record must be:

- present
- unexpired
- correctly scoped (action, object, environment match)
- signature valid (HMAC-SHA256)
- nonce unused

If any condition fails, mutation does not occur.
