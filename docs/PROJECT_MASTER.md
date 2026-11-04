# ComicVision AI — Project Master

**Version:** 1.0
**Status:** Active Development
**Current Milestone:** 01 — Project Foundation
**Project Type:** Computer Vision, Machine Learning, Deep Learning, NLP, and Multimodal AI

## 1. Project Vision

Build an AI-powered comic book cataloging, classification, visual search, and recommendation application using an initial collection of 100 physical comic books.

**Mission:** Scan. Identify. Analyze. Discover.

## 2. Primary Objectives

1. Strengthen Python, machine learning, neural network, and deep learning skills.
2. Build an employer-ready technical portfolio project.
3. Develop and deploy a functioning AI application.
4. Demonstrate reproducible ML experiments, software engineering, and MLOps practices.

## 3. Core Capabilities

1. **Physical Comic Digitization:** Photograph covers, extract candidate metadata using OCR, and verify catalog records.
2. **Comic Classification:** Predict supported attributes such as publisher, publication era, or broad genre.
3. **Clustering:** Discover groups using image and text features.
4. **Recommendation Engine:** Recommend similar comics using content-based similarity.
5. **Computer Vision and Multimodal Search:** Search using cover images, text descriptions, or combined features.
6. **Deployable Application:** Provide an interactive interface, prediction APIs, tests, and containerized deployment.

## 4. Dataset Strategy

- Initial collection: 100 physical comic books.
- Pilot dataset: 20 comics.
- Capture: Original cover photographs.
- Metadata: Unique ID, title, issue number, publisher, publication date, genre tags, and available descriptions.
- Quality controls: Duplicate checks, missing-value audits, image validation, and human verification.
- Dataset expansion: Allowed when evaluation shows insufficient coverage.
- Data leakage: Related images and duplicate editions must not cross evaluation boundaries.

## 5. Technology Stack

- Language: Python 3.11
- Development: VS Code, Jupyter, PowerShell
- Data: pandas, NumPy, Pillow, OpenCV
- Machine Learning: scikit-learn
- Deep Learning: PyTorch, torchvision
- NLP: sentence-transformers, Hugging Face Transformers
- Multimodal Models: Pretrained CLIP-style encoders
- Similarity Search: Cosine similarity, FAISS when appropriate
- Experiment Tracking: MLflow
- Backend: FastAPI, Pydantic
- Frontend: Streamlit
- Deployment: Docker, GitHub Actions, suitable cloud hosting
- Version Control: Git and GitHub

## 6. Twelve-Milestone Roadmap

| Milestone | Name |
|---|---|
| 01 | Project Foundation |
| 02 | Physical Data Acquisition |
| 03 | Data Audit and EDA |
| 04 | Preprocessing and Baselines |
| 05 | Unsupervised Clustering |
| 06 | Recommendation Engine |
| 07 | Supervised Classification |
| 08 | Deep Learning and Transfer Learning |
| 09 | Multimodal Retrieval |
| 10 | Model API and Application |
| 11 | MLOps, Security, and Deployment |
| 12 | Final Evaluation and Portfolio |

## 7. Evaluation Principles

- Establish reproducible baselines before introducing complex models.
- Use appropriate metrics for each ML task.
- Compare traditional ML and deep learning approaches fairly.
- Evaluate recommendation quality using human-reviewed relevance judgments.
- Document limitations arising from the initial 100-comic dataset.
- Do not invent model performance or claim unsupported accuracy.
- Maintain a final evaluation set that is not used for model selection.

## 8. Development Workflow

Use an instructor-led approach:

1. Explain the concept and its purpose.
2. Provide one executable command, code cell, or action at a time.
3. Wait for actual output before advancing.
4. Verify results and troubleshoot errors.
5. Include learner-oriented notebooks and exercises.
6. Document technical decisions and evaluation results.
7. Commit verified milestone deliverables to GitHub.

## 9. Project Continuity

Maintain the following documents:

- `docs/PROJECT_MASTER.md` — Project requirements and architectural decisions.
- `docs/MILESTONE_TRACKER.md` — Milestone status and acceptance criteria.
- `docs/SESSION_HANDOFF.md` — Verified state and next action.

Start a new ChatGPT conversation after approximately three completed milestones.

Before switching conversations:

1. Update all three documents.
2. Verify Git status and relevant tests.
3. Commit and push documentation and completed deliverables.
4. Generate a compact handoff prompt.
5. Resume from the documented next action.

## 10. Deferred Features

- Comic market-price prediction.
- Popularity prediction without reliable historical labels.
- Full comic-dialogue extraction and NLP.
- Generative comic artwork.
- Training large neural networks from scratch.
- Generative AI assistant, until retrieval quality is established.

## 11. Project Completion Criteria

ComicVision AI is complete when:

- The 100-comic collection is cataloged and validated.
- Traditional ML and deep learning experiments are reproducible.
- Search and recommendation performance is evaluated.
- The application exposes functional APIs and a usable interface.
- Automated tests and deployment checks pass.
- The project includes technical documentation and an employer-facing demonstration.

---

**Document owner:** ComicVision AI Project
**Last reviewed:** November 4, 2026
**Next review:** Milestone 01 completion