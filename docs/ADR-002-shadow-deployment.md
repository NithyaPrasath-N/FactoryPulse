# ADR-002: Shadow Deployment for Model Evaluation

**Status:** Accepted

## Context

Promoting a new model to production carries risk.

## Decision

- The production model drives all decisions and alerts.
- The staging model scores every request alongside production.
- Staging predictions are logged but never acted upon.
- The disagreement rate is tracked, and a high disagreement triggers investigation.
- Promotion happens only after the shadow period proves that the staging model is equivalent to or better than the production model.

## Consequences

- There is double compute cost during the shadow period, which is acceptable for safety-critical systems.
- Careful bookkeeping is required to ensure shadow predictions never leak into alerts.