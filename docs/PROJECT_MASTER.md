# ComicVision AI - Project Master

**Version:** 1.2
**Last Updated:** November 17, 2026
**Current Milestone:** 04 - Preprocessing and Baselines
**Overall Status:** In Progress
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
- Metadata: Unique ID, title, issue number, publisher, issue date (YYYY-MM), publication year (YYYY), genre tags, and available descriptions.
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

## 9A. Milestone 02 — Verified Implementation Progress

**Status:** In Progress
**Checkpoint Date:** November 10, 2026
**Development Branch:** `milestone-02-data-acquisition`
**Latest Verified Commit:** `413a5e1`

### Data Acquisition

- Defined a 12-column comic metadata schema.
- Established a 20-comic pilot target from the physical collection.
- Created the pilot metadata catalog.
- Recorded the first comic: `CV0001`, The New Teen Titans #25.
- Verified the first cover image locally using Pillow.
- Established human verification and metadata provenance requirements.

### Catalog Validation

Implemented `src/ingestion/validate_catalog.py` with:

- CSV column structure validation.
- Required metadata field validation.
- Verification status validation.
- Cover image path existence checks.
- Duplicate comic ID detection.
- Empty catalog rejection.

### Automated Testing

- Test file: `tests/test_validate_catalog.py`
- Unit tests: 10 passing.
- Integration tests: 7 passing.
- Total: 17 passing.
- Latest verified regression result: 17 passed, 0 failed.

### Version Control

- Validator and automated tests committed as `413a5e1`.
- Development branch pushed to GitHub.
- Local branch and recorded upstream verified synchronized.
- Changes have not been merged into `main`.

### Remaining Milestone 02 Work

- Expand the pilot catalog toward 20 verified comics.
- Strengthen metadata format and image-quality validation.
- Complete the acquisition quality review.
- Update the milestone tracker and session handoff.
- Confirm Milestone 02 acceptance criteria before closure.

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

**Document owner:** ComicVision AI Project
**Last reviewed:** November 16, 2026
**Next review:** Milestone 03 closeout completion and Milestone 04 kickoff

## Milestone 02 - Verified Pilot Dataset

- The 20-comic pilot catalog has completed core metadata verification.
- All 20 records are marked verified.
- CV0008 and CV0014 retain intentionally unresolved publication months.
- Verification does not imply physical-edition authentication.
- Final CSV validation passed.
- Final regression suite: 29 tests passed.
- Next phase: Milestone 03 under the established roadmap.

## Milestone 03 - Data Audit and EDA

**Status:** Completed
**Checkpoint Date:** November 16, 2026
**Development Branch:** `milestone-03-data-audit-eda`
**Verified Commit:** `dca1550` — `feat: complete milestone 03 data audit and EDA`
**Remote:** `origin/milestone-03-data-audit-eda`
**Branch State:** Implementation commit `dca1550` was clean and synchronized before documentation edits; closeout documentation is now saved locally and pending diff review, commit, and push. Fast-forward merge into `main` is available.

### Verified Findings

- Pilot catalog: 20 comics; 12 original metadata columns; 0 duplicate records.
- All 20 cover images are readable RGB portrait JPEGs.
- Missing issue dates: 2; missing genre labels: 20; missing descriptions: 20.
- Five standardized publisher groups and three publication decades.
- Resolution outliers: CV0001 and CV0002.
- Visual review recommended for CV0002, CV0006, and CV0013.
- Image feature extraction, similarity retrieval, and clustering are suitable for pilot experiments.
- Publisher and era classification remain limited by dataset size and imbalance.
- Genre classification, description-based NLP, and full multimodal experiments require metadata enrichment.

### Deliverables and Validation

- `notebooks/01_data_audit_eda.ipynb`
- `reports/milestone_03_image_quality_audit.csv`
- `reports/milestone_03_dataset_suitability_report.md`
- `tests/test_image_quality_audit.py`
- Updated `pyproject.toml`
- Notebook fresh-kernel execution: PASS.
- CSV round-trip and dependency consistency: PASS.
- Regression tests: 30 passed, 0 failed.

### Open Project Risks

- The pilot contains 20 of the 100 target comics; 80 remain to be acquired.
- The dataset is too small for reliable supervised performance claims.
- Publisher and era classes are imbalanced.
- CV0002, CV0006, and CV0013 still need visual review.
- Genre and description fields need enrichment before related NLP and supervised work.
- The Milestone 03 feature branch has not yet been merged into `main`.

### Next Action

Begin Milestone 04 — Preprocessing and Baselines.

### Verified Dataset

- Pilot catalog: 20 comics.
- Original metadata columns: 12.
- Unique comic IDs: 20.
- Duplicate records: 0.
- Readable cover images: 20.
- Full collection target: 100 comics (outstanding).

### Metadata Audit

- Missing issue dates: 2.
- Missing genre labels: 20.
- Missing descriptions: 20.
- Standardized publisher groups: 5.
- Publication decades represented: 3.
- Publisher and decade distributions analyzed.

### Image Quality Assessment

- All 20 JPEG covers successfully inspected.
- All images use RGB color mode.
- All images have portrait orientation.
- Resolution outliers: CV0001 and CV0002.
- Images recommended for further visual review:
  CV0002, CV0006, and CV0013.
- Image-quality audit exported and validated.

### Machine Learning Readiness

Suitable for pilot experimentation:

- Image feature extraction.
- Image similarity search.
- Unsupervised clustering.

Limited by dataset size and imbalance:

- Publisher classification.
- Publication-decade classification.

Requires metadata enrichment:

- Genre classification.
- Description-based NLP.
- Full multimodal recommendation experiments.

### Verified Engineering Deliverables

- `notebooks/01_data_audit_eda.ipynb`
- `reports/milestone_03_image_quality_audit.csv`
- `reports/milestone_03_dataset_suitability_report.md`
- `tests/test_image_quality_audit.py`
- Updated runtime dependencies in `pyproject.toml`.

### Validation Results

- Notebook execution from fresh kernel: PASS.
- CSV round-trip validation: PASS.
- Dependency consistency: PASS.
- Automated regression tests: 30 passed, 0 failed.

### Remaining Acceptance Tasks

- [x] Complete and review the closeout documentation.
- [x] Review the diff and check whitespace.
- [x] Commit and push the documentation closeout on the feature branch.
- [x] Fast-forward `main` locally.
- [x] Commit and push the final post-merge status update.
- [x] Confirm clean synchronization, then mark Milestone 03 complete and authorize Milestone 04.

### Milestone 04 — Preprocessing and Baselines

- Use a reproducible 16/4 split by comic ID with random seed 42. Fit
  learned preprocessing on the training split only and reserve the
  four holdout comics for later evaluation.
- Use title-only TF-IDF for the pilot text baseline because genre and
  description fields are empty. Compare default tokenization with
  English stop-word removal on training titles.
- Use whole-cover and quadrant mean RGB as visual baselines. Quadrant
  RGB preserves coarse color location and provides 12 features per
  cover for exploratory similarity and clustering.
- Treat the similarity rankings as exploratory. Human relevance
  judgments are needed to assess recommendation quality.
