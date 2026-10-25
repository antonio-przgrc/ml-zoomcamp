# Machine Learning Zoomcamp

My notes, homework and projects from the [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) by [DataTalks.Club](https://datatalks.club): a free, hands-on course on building, evaluating and deploying machine learning systems.

**Stack:** Python · NumPy · pandas · scikit-learn · XGBoost · TensorFlow · PyTorch · FastAPI · Docker · AWS Lambda · Kubernetes

## Projects

| Project | Description | Stack | Repo |
| --- | --- | --- | --- |
| Midterm | – | – | – |
| Capstone 1 | – | – | – |
| Capstone 2 | – | – | – |

Details in [`projects/`](projects/).

## Progress

✅ done · 🟡 in progress · ⬜ not started

| # | Module | Folder | Status |
| --- | --- | --- | --- |
| 1 | Introduction to Machine Learning | [01-intro/](01-intro/) | ⬜ |
| 2 | Machine Learning for Regression | [02-regression/](02-regression/) | ⬜ |
| 3 | Machine Learning for Classification | [03-classification/](03-classification/) | ⬜ |
| 4 | Evaluation Metrics for Classification | [04-evaluation/](04-evaluation/) | ⬜ |
| 5 | Deploying Machine Learning Models | [05-deployment/](05-deployment/) | ⬜ |
| 6 | Decision Trees and Ensemble Learning | [06-trees/](06-trees/) | ⬜ |
| – | **Midterm project** | | ⬜ |
| 8 | Neural Networks and Deep Learning | [08-deep-learning/](08-deep-learning/) | ⬜ |
| 9 | Serverless Deep Learning | [09-serverless/](09-serverless/) | ⬜ |
| 10 | Kubernetes and TensorFlow Serving | [10-kubernetes/](10-kubernetes/) | ⬜ |
| – | **Capstone project 1** | | ⬜ |
| – | **Capstone project 2** | | ⬜ |

The course has no module 7; the numbering follows the official repository.

## Repository structure

```
├── 01-intro/            # notebook with notes and homework for each module
├── 02-regression/
├── ...
├── 10-kubernetes/
├── projects/            # index of project repositories + README template
├── data/                # local datasets (not committed)
└── pyproject.toml
```

## Setup

Dependencies are managed with [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/<your-user>/ml-zoomcamp.git
cd ml-zoomcamp
uv sync                 # modules 1-6
uv sync --group dl      # adds TensorFlow and PyTorch for modules 8-10
uv run jupyter lab
```

## Learning in public

Posts I wrote along the way:

- –

## About me

Antonio Pérez García · [LinkedIn](#) · [GitHub](#)
