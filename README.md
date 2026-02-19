# AeroPredict-Proto

![Status](https://img.shields.io/badge/Project-Prototype-blue)
![Phase](https://img.shields.io/badge/Phase-2%20In%20Progress-orange)
![Domain](https://img.shields.io/badge/Domain-Aviation%20PdM-0052CC)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Isolation%20Forest-F7931E?logo=scikitlearn&logoColor=white)
![TinyML](https://img.shields.io/badge/Edge%20AI-TinyML-2E7D32)
![MCU](https://img.shields.io/badge/Target-STM32%20Cortex--M4-03234B)

**Edge-AI for Turbofan Health Monitoring**  
Bridging aircraft maintenance expertise with embedded machine learning for real-time, on-wing diagnostics.

---

## ✈️ Objective

`AeroPredict-Proto` is an end-to-end predictive maintenance prototype designed to detect **early-stage turbofan degradation** using NASA C-MAPSS (FD001) data.

The target outcome is to deploy a lightweight anomaly detection model to an **ARM Cortex-M4 (STM32)** platform, enabling **cloud-independent local inference** and actionable maintenance alerts.

---

## 💼 Why This Project Matters (Recruiter Snapshot)

- Combines **10+ years of aircraft maintenance experience** with practical ML engineering.
- Focuses on **operationally relevant sensors**, not generic feature selection.
- Demonstrates full-stack execution: **data pipeline → model training → edge deployment pathway**.
- Designed for safety-critical workflows where **latency, reliability, and interpretability** matter.

---

## 🛠️ Tech Stack

### Domain & Operations
- Aircraft Systems & Maintenance (FAA/EASA-informed reasoning)

### Data Science & Prototyping
- Python
- Pandas
- Scikit-Learn (`IsolationForest`)
- Marimo

### Embedded & Edge AI
- C/C++
- STM32CubeIDE
- NUCLEO-F302R8
- Edge Impulse / TinyML quantized deployment flow

---

## 📂 Project Structure

```text
AeroPredict-Proto/
├── data/              # Raw NASA C-MAPSS FD001 datasets
├── notebooks/         # Marimo notebooks for EDA and model training
├── firmware/          # STM32CubeIDE project (C/C++ firmware)
├── models/            # Exported TinyML model artifacts (.h / deployment headers)
├── mo_nb.py           # Current marimo prototype notebook/script
├── pyproject.toml
└── README.md
```

---

## 📈 Progress by Phase

### ✅ Phase 1 — Exploratory Data Analysis (Completed)

- Ingested NASA C-MAPSS FD001 (100 engines, single fault mode).
- Isolated critical fuel/pressure-related channels:
	- `s_14`: Core speed
	- `s_11`: HPC outlet pressure
- Visualized trend behavior and established a baseline healthy operating profile.

### 🔄 Phase 2 — Anomaly Detection Model (In Progress)

- Training an `IsolationForest` model in Marimo to detect HPC-related deviations.
- Defining Remaining Useful Life (RUL) targets for maintenance alerting thresholds.
- Evaluating false-positive behavior to keep outputs maintenance-actionable.

### 🚀 Phase 3 — Embedded Pivot (Next)

- **Quantization:** Convert Python-trained model into MCU-ready C/C++ artifacts.
- **Hardware Integration:** Stream simulated sensor data over UART on NUCLEO-F302R8.
- **Local Inference:** Trigger onboard GPIO/LED/interrupt outputs on anomaly detection.

---

## 💡 Maintenance-First Modeling Philosophy

This prototype applies a domain-first approach:

- **Sensor 14 (core speed):** tracked for FMU fatigue signatures and fuel metering instability.
- **Sensor 11 (HPC outlet pressure):** monitored for stall precursor behavior often missed by interval-based checks.

In short: feature selection is grounded in practical engine behavior, not only statistical convenience.

---

## 🚀 How to Run (Development)

### 1) Python / Marimo workflow

```bash
# from repository root
marimo edit mo_nb.py
```

> If you move notebooks into `notebooks/`, use:
>
> `marimo edit notebooks/AeroPredict.py`

### 2) Embedded workflow

1. Open STM32CubeIDE
2. Import the `firmware/` project
3. Build and flash to NUCLEO-F302R8

### 3) Data requirement

Ensure `train_FD001.txt` is present in `data/`.

---

## 🔭 Roadmap Highlights

- Add model export + quantization benchmark results (accuracy/latency/size)
- Integrate UART test harness for repeatable sensor replay
- Add edge-side alert policy with configurable thresholds
- Capture demo video: host-side stream + on-board anomaly trigger

---

## 🤝 Collaboration

If you work in aviation analytics, embedded AI, or predictive maintenance systems, I’d be happy to connect and collaborate.

