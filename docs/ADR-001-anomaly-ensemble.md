
# ADR-001: Anomaly Detection Ensemble

**Status:** Accepted

## Context

Single-model approaches miss different failure patterns.

## Decision

Use an ensemble of an LSTM Autoencoder and an Isolation Forest.

- The LSTM Autoencoder is trained on healthy-only data; high reconstruction error indicates an anomaly.
- It captures temporal patterns and gradual degradation.
- The Isolation Forest catches point anomalies and sudden shifts.
- Adaptive thresholds are calibrated per machine instead of using a single static threshold across the fleet.

## Consequences

- Two models must be maintained, but the system covers both gradual and sudden anomalies.
- Inference has higher compute cost, but this remains acceptable given the service-level objective of less than five seconds.