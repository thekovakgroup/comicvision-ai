# ComicVision AI

**An AI-powered comic book cataloging, classification, recommendation, and multimodal visual search platform.**

**Project Status:** In Development — Milestone 01 of 12

## Project Overview

ComicVision AI is an end-to-end machine learning and deep learning portfolio project built around a personal collection of 100+ physical comic books.

The project explores how artificial intelligence can help collectors digitize their collections, organize comic metadata, identify visual similarities, discover related titles, and search across text and images.

The initial development phase focuses on 20 physical comics before expanding to the complete 100+ comic collection.

## Project Objectives

- Build a structured and validated comic book dataset.
- Explore computer vision and OCR-assisted cataloging.
- Apply unsupervised learning to identify similarities and clusters.
- Develop content-based comic book recommendations.
- Experiment with supervised classification.
- Compare traditional machine learning with deep learning and transfer learning.
- Implement multimodal retrieval using image and text embeddings.
- Build a functional application with API endpoints.
- Demonstrate MLOps, testing, containerization, and deployment.

## Planned Features

| Feature | Description | Status |
|---|---|---|
| Comic Catalog | Organize physical comics and their metadata | Planned |
| OCR-Assisted Entry | Extract candidate information from photographed covers | Planned |
| Visual Clustering | Group visually or semantically similar comics | Planned |
| Recommendation Engine | Suggest related comics based on content similarity | Planned |
| Classification | Predict supported comic attributes where data permits | Planned |
| Image Search | Find visually similar comics | Planned |
| Multimodal Search | Combine text and image representations | Planned |
| Web Application | Interactive collection exploration | Planned |
| Model API | Expose model inference and retrieval endpoints | Planned |

## Technology Stack

**Language and development**
- Python 3.11
- VS Code
- Git and GitHub
- Jupyter Notebook

**Data science and machine learning**
- pandas and NumPy
- Matplotlib
- scikit-learn

**Deep learning and multimodal AI**
- PyTorch
- Pretrained computer vision models
- CLIP
- Sentence Transformers

**Application and MLOps**
- FastAPI
- Streamlit
- MLflow
- Docker
- GitHub Actions

These technologies are planned for implementation across the roadmap. Their inclusion does not imply that every dependency has already been installed.

## Data Collection Strategy

The project uses an initial collection of 100+ physical comic books.

**Pilot dataset:** 20 comics
**Target initial dataset:** 100+ comics

Each comic record will be associated with a unique identifier, available bibliographic metadata, and a reference to its photographed cover.

Potential metadata includes:
- Title
- Series
- Issue number
- Publisher
- Publication year
- Genre or category
- Cover image reference
- Additional verified attributes

The final metadata schema and photography standards will be established during the foundation and acquisition milestones.

### Dataset Limitations

A collection of 100+ comics is relatively small for training complex deep learning models from scratch.

The project will therefore emphasize pretrained models, transfer learning, interpretable baselines, appropriate validation, and transparent reporting of limitations.

## Twelve-Milestone Roadmap

| Milestone | Focus | Status |
|---|---|---|
| 01 | Project Foundation | In Progress |
| 02 | Physical Data Acquisition | Not Started |
| 03 | Data Audit and EDA | Not Started |
| 04 | Preprocessing and Baselines | Not Started |
| 05 | Unsupervised Clustering | Not Started |
| 06 | Recommendation Engine | Not Started |
| 07 | Supervised Classification | Not Started |
| 08 | Deep Learning and Transfer Learning | Not Started |
| 09 | Multimodal Retrieval | Not Started |
| 10 | Model API and Application | Not Started |
| 11 | MLOps, Security, and Deployment | Not Started |
| 12 | Final Evaluation and Portfolio | Not Started |

Detailed milestone progress is maintained in `docs/MILESTONE_TRACKER.md`.

## Repository Structure

```text
comicvision-ai/
├── .github/
│   └── workflows/
├── app/
│   ├── api/
│   └── frontend/
├── configs/
├── data/
│   ├── raw/
│   │   ├── covers/
│   │   └── metadata/
│   ├── interim/
│   └── processed/
├── docs/
│   ├── PROJECT_MASTER.md
│   ├── MILESTONE_TRACKER.md
│   └── SESSION_HANDOFF.md
├── models/
├── notebooks/
├── reports/
│   └── figures/
├── src/
│   ├── ingestion/
│   ├── preprocessing/
│   ├── features/
│   ├── models/
│   ├── retrieval/
│   └── evaluation/
├── tests/
├── .gitignore
└── README.md
```

The structure will evolve as features and infrastructure are implemented.

## Local Development Setup

**Environment:** Windows, PowerShell, Python 3.11.

The following commands describe the intended setup process.

Create a virtual environment:

```powershell
py -3.11 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Verify the interpreter:

```powershell
python --version
```

Dependency installation and application startup instructions will be added after the relevant project configuration and application components have been implemented.

## Evaluation Principles

ComicVision AI will prioritize reproducibility and transparent evaluation.

Key principles include:

- Avoiding data leakage between training and evaluation.
- Comparing models against meaningful baselines.
- Selecting metrics appropriate to each ML task.
- Evaluating recommendation and retrieval relevance.
- Documenting failure cases and dataset limitations.
- Distinguishing measured performance from expected capabilities.

## Responsible AI and Copyright

ComicVision AI is intended as an educational and portfolio project.

Comic book covers and other creative works may be protected by copyright. Public distribution of source images, metadata, and model outputs will be evaluated before deployment.

OCR-extracted information will be treated as candidate metadata requiring validation rather than automatically trusted ground truth.

## Project Documentation

- **Project Master:** `docs/PROJECT_MASTER.md`
- **Milestone Tracker:** `docs/MILESTONE_TRACKER.md`
- **Session Handoff:** `docs/SESSION_HANDOFF.md`

These documents define the project scope, verified progress, and continuity procedures.

## Current Development Status

Milestone 01 is underway.

The dedicated Python virtual environment, local Git repository, directory structure, and three continuity documents have been established.

The README, project configuration, initial notebook, GitHub remote, and first verified commit remain part of the foundation milestone.

## Future Enhancements

Potential extensions include expanded collection support, improved metadata enrichment, more advanced visual retrieval, and collector-oriented application features.

These enhancements are deferred until the initial 12-milestone roadmap has been completed and evaluated.

---

**ComicVision AI**
Machine Learning • Deep Learning • Computer Vision • Multimodal AI • MLOps

Developed as a practical, end-to-end AI engineering portfolio project.