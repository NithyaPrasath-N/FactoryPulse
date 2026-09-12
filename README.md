# 🏭 FactoryPulse

### Real-Time Predictive Maintenance & Equipment Intelligence Platform

FactoryPulse is an **Industrial AI platform** that monitors machine telemetry, detects anomalies, predicts **Remaining Useful Life (RUL)**, identifies potential failure modes, and provides an **AI-powered maintenance copilot** using RAG.

The system uses public predictive-maintenance datasets and a telemetry simulator to reproduce real-time factory conditions without requiring physical equipment.

---

## 🚀 Features

* 📡 Real-time sensor telemetry using **MQTT/HTTP**
* 🔍 Anomaly detection using **LSTM Autoencoder + Isolation Forest**
* 📉 RUL prediction using a **Transformer**
* 🏷️ Failure-mode classification using **LightGBM**
* 🌡️ Thermal hotspot detection using **OpenCV**
* ❤️ Machine health score and intelligent alerting
* 🤖 **LangGraph maintenance copilot**
* 📚 RAG over manuals, fault codes, and maintenance logs
* 🔎 Hybrid retrieval with **Qdrant**
* 📝 AI-generated maintenance work-order drafts
* 📊 Streamlit monitoring dashboard
* 🧪 ML experiment tracking with **MLflow + DVC**
* 📈 Prometheus monitoring and model-drift detection
* 🔐 JWT authentication and role-based access
* 🐳 Fully containerized with Docker

---

## 🧠 Architecture

```text
Sensors / Simulator
        ↓
   MQTT / HTTP
        ↓
 Ingestion Service
        ↓
   TimescaleDB
        ↓
 Feature Pipeline
        ↓
 ┌───────────────┬────────────────┐
 ↓               ↓                ↓
Anomaly        RUL Model      Failure Model
Detection      Transformer      LightGBM
 ↓               ↓                ↓
 └───────────────┴────────────────┘
                 ↓
          Health & Alert Engine
                 ↓
        ┌────────┴─────────┐
        ↓                  ↓
   Streamlit          AI Copilot
   Dashboard          LangGraph
                           ↓
                    Qdrant RAG
                           ↓
                Maintenance Guidance
```

---

## 🤖 AI Components

### Anomaly Detection

An **LSTM Autoencoder** learns normal machine behavior. Reconstruction error is combined with **Isolation Forest** to identify abnormal patterns.

### RUL Prediction

A **PyTorch Transformer Encoder** predicts the remaining useful life of equipment. **XGBoost** is used as a baseline.

### Failure Classification

**LightGBM** predicts failure modes such as:

* Tool wear
* Heat dissipation failure
* Power failure
* Overstrain failure

### Thermal Intelligence

An OpenCV pipeline detects abnormal thermal hotspots and combines the thermal anomaly score with sensor-based machine health.

### Maintenance Copilot

The LangGraph agent combines:

```text
Live ML Results
      +
Machine History
      +
Equipment Manuals
      +
Fault Codes
      ↓
     RAG
      ↓
Maintenance Recommendation
```

The copilot provides citations and performs a groundedness check to reduce unsupported answers.

---

## 📊 Dataset

FactoryPulse can be developed entirely using public datasets:

* **NASA C-MAPSS** — RUL prediction
* **NASA IMS Bearing Dataset** — bearing degradation/anomaly detection
* **AI4I 2020 Predictive Maintenance Dataset** — failure classification

A simulator replays processed data as real-time machine telemetry.

---

## 🛠️ Tech Stack

| Category        | Technologies                             |
| --------------- | ---------------------------------------- |
| Backend         | Python, FastAPI, Pydantic                |
| Database        | PostgreSQL, TimescaleDB                  |
| Streaming       | MQTT, HTTP                               |
| Cache           | Redis                                    |
| ML              | PyTorch, Scikit-learn, XGBoost, LightGBM |
| Computer Vision | OpenCV                                   |
| GenAI           | LangGraph, LangChain, Qdrant             |
| MLOps           | MLflow, DVC                              |
| Dashboard       | Streamlit, Plotly                        |
| Monitoring      | Prometheus                               |
| Deployment      | Docker, Docker Compose                   |
| Testing         | Pytest                                   |

---

## 📁 Project Structure

```text
factorypulse/
├── services/
│   ├── simulator/
│   ├── ingestion/
│   ├── feature_pipeline/
│   ├── inference/
│   ├── alert_engine/
│   └── copilot/
├── ml/
│   ├── anomaly_detection/
│   ├── rul_prediction/
│   ├── failure_classification/
│   └── thermal_detection/
├── dashboard/
├── rag/
├── database/
├── tests/
├── docs/
├── docker-compose.yml
├── dvc.yaml
├── .env.example
└── README.md
```

---

## ⚡ Performance Targets

* **200+ messages/sec** ingestion load
* **<150 ms** inference p95 latency
* **<5 sec** sensor-to-alert latency
* **<3 sec** copilot first-token latency
* **80%+** unit-test coverage

---

## ▶️ Quick Start

```bash
git clone https://github.com/<username>/factorypulse.git
cd factorypulse

cp .env.example .env

docker compose up -d
```

Train the ML pipeline:

```bash
dvc repro
```

Run the dashboard:

```bash
streamlit run dashboard/streamlit_app/app.py
```

Run tests:

```bash
pytest
```

---

## 🎯 Project Goal

FactoryPulse demonstrates an end-to-end approach to **predictive maintenance**, combining:

**Real-Time Data → ML → Computer Vision → MLOps → RAG → Agentic AI → Actionable Maintenance**

> Built as an engineering/research prototype using public datasets and simulated industrial telemetry. It is not intended to replace safety-critical industrial systems without proper validation.
