# Project name

One sentence on what this project predicts and who would use it.

## Problem description

What problem is being solved, why it matters, and how the model would be used in practice.

## Dataset

- Source: <!-- link -->
- How to get it: <!-- committed under data/ or download instructions -->

## Project structure

```
├── README.md
├── data/               # dataset or download script
├── notebook.ipynb      # data preparation, EDA, feature importance, model selection
├── train.py            # trains the final model and saves it
├── predict.py          # loads the model and serves it via FastAPI
├── pyproject.toml      # dependencies (uv)
├── uv.lock
└── Dockerfile
```

## EDA

Main findings: target distribution, missing values, feature importance.

## Models

| Model | Parameters tuned | Validation metric |
| --- | --- | --- |
| | | |

Final model and why it was chosen.

## How to run

### Install dependencies

```bash
uv sync
```

### Train the model

```bash
uv run python train.py
```

### Run the service locally

```bash
uv run uvicorn predict:app --host 0.0.0.0 --port 9696
```

### Run with Docker

```bash
docker build -t project-name .
docker run -it --rm -p 9696:9696 project-name
```

### Example request

```bash
curl -X POST http://localhost:9696/predict \
  -H "Content-Type: application/json" \
  -d '{}'
```

## Cloud deployment

URL of the deployed service, or a screenshot/video of it working.
