# FactoryPulse Architecture

## Data Flow

- The simulator replays C-MAPSS and IMS data over MQTT at a configurable speed.
- Ingestion validates the schema, physical range, and timestamp monotonicity before writing to TimescaleDB.
- Failures are sent to the dead-letter table for investigation.
- The feature pipeline computes windowed features such as rolling statistics, FFT, and domain-specific features.
- These features are materialized into the feature table and cached in Redis.
- Offline ML training builds anomaly detection, remaining useful life (RUL), and classifier models.
- All experiments are tracked in MLflow.
- The inference service loads the production model from MLflow, reads features from Redis, and scores in real time.
- A staging model runs in shadow mode for comparison.
- The alert engine applies hysteresis thresholds, deduplicates alerts, computes composite health scores, and dispatches webhooks.
- Copilot (LangGraph) classifies user intent, plans tool calls (up to six), assembles evidence, drafts responses, and verifies groundedness.
- The console (Streamlit) renders the fleet grid, machine detail view, alert queue, copilot chat, and drift dashboard.

## Key Decisions

- The feature pipeline is serialized with models to prevent training and serving skew.
- Shadow deployment allows staging models to score live traffic without risk.
- Hysteresis alerting opens alerts at a high threshold and closes them at a lower threshold.
- Grounded generation uses embedding similarity and natural language inference verification.


