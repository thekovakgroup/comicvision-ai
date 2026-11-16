# ComicVision AI — Milestone 03 Dataset Suitability Report

**Project:** ComicVision AI
**Milestone:** 03 — Data Audit and Exploratory Data Analysis
**Dataset:** 20-comic pilot collection
**Status:** Draft — Pending final reproducibility and acceptance checks

## 1. Executive Summary

The ComicVision AI pilot dataset contains 20 physically owned comic books with verified core bibliographic metadata and corresponding cover photographs.

The dataset is suitable for exploratory data analysis, computer vision pipeline development, image similarity experiments, and initial clustering research.

However, the limited sample size, publisher and era imbalance, and missing genre and description fields prevent reliable supervised classification and text-based modeling at this stage.

**Recommendation:** Accept the dataset for continued pilot experimentation, subject to final Milestone 03 validation. Do not treat pilot model performance as evidence of production readiness.

## 2. Dataset Overview

| Metric | Result |
|---|---|
| Total comics | 20 |
| Original metadata columns | 12 |
| Duplicate records | 0 |
| Duplicate comic IDs | 0 |
| Readable cover images | 20 |
| Standardized publisher groups | 5 |
| Publication decades | 3 |

The original metadata is preserved. Standardized publisher groups and publication decades were created as additional analytical features in the EDA notebook.

## 3. Metadata Quality Assessment

The dataset contains 42 missing values across 240 original metadata cells, representing 17.5% missingness.

| Field | Missing values | Missing percentage |
|---|---:|---:|
| issue_date | 2 | 10% |
| genre_tags | 20 | 100% |
| description | 20 | 100% |
| Other nine fields | 0 | 0% |

The two missing issue dates reflect unresolved month-level information. Publication years remain available for all 20 records.

Genre labels and descriptions require future metadata enrichment.

Missing values must not be replaced with unsupported guesses.

## 4. Publisher Distribution

| Standardized group | Comics | Share |
|---|---:|---:|
| Marvel | 11 | 55% |
| DC | 4 | 20% |
| Western Publishing | 2 | 10% |
| Dark Horse | 2 | 10% |
| Pied Piper | 1 | 5% |

The original seven publisher labels were consolidated into five analytical groups.

Publisher-group normalization is provisional and does not replace historical publisher or imprint attribution.

The dataset exhibits substantial publisher imbalance.

## 5. Publication-Year and Era Distribution

The collection spans publication years 1978 through 1997.

| Decade | Comics | Share |
|---|---:|---:|
| 1970s | 4 | 20% |
| 1980s | 13 | 65% |
| 1990s | 3 | 15% |

The dataset is concentrated in the 1980s, creating an era imbalance that must be considered during model development and evaluation.

## 6. Image Quality Assessment

All 20 cover images were successfully opened and inspected.

| Metric | Result |
|---|---|
| JPEG images | 20 |
| RGB images | 20 |
| Portrait-oriented images | 20 |
| Average resolution | 10.747 MP |
| Average aspect ratio | 0.680 |
| Aspect-ratio IQR outliers | 0 |
| Resolution IQR outliers | 2 |

**Resolution outliers:** CV0001 and CV0002.

These outliers are not automatically considered defective images.

### Preliminary Visual Review

17 images received preliminary-pass annotations, and three were flagged for further inspection:

- CV0002 — Possible reflections and reduced contrast.
- CV0006 — Possible glare near the lower cover.
- CV0013 — Possible fading or reduced contrast.

All three images remain usable for pilot experimentation. Full-resolution inspection may be needed before final image-quality clearance.

## 7. Machine Learning Suitability

| Capability | Assessment |
|---|---|
| Image feature extraction | Suitable for pilot experimentation |
| Image similarity search | Suitable for pilot experimentation |
| Unsupervised clustering | Suitable for pilot experimentation |
| Publisher classification | Limited prototype only |
| Publication-decade classification | Limited prototype only |
| Genre classification | Not ready; labels unavailable |
| Description-based NLP | Not ready; text unavailable |
| Multimodal recommendations | Partially ready; text enrichment required |

The pilot supports pipeline development and technical feasibility testing, not reliable estimates of model generalization.

## 8. Recommended Next Steps

1. Preserve all original cover photographs and bibliographic metadata.
2. Expand the collection toward the planned 100-comic dataset.
3. Enrich genre and description fields using documented, verifiable sources.
4. Preserve historical publisher attribution while maintaining standardized analytical groups.
5. Use aspect-ratio-preserving image resizing and retain original high-resolution files.
6. Review flagged cover photographs before applying corrective preprocessing.
7. Implement leakage-aware evaluation and account for publisher and era imbalance.
8. Declare project dependencies and validate notebook reproducibility.

## 9. Conclusion

The 20-comic pilot dataset is suitable for continuing ComicVision AI's experimental development.

The primary limitations are sample size, class imbalance, and missing semantic metadata rather than missing or unreadable cover images.

**Milestone 03 remains open** until the report, notebook reproducibility, project dependencies, and final acceptance checks are verified.

---

**Supporting artifact:** `reports/milestone_03_image_quality_audit.csv`
**EDA notebook:** `notebooks/01_data_audit_eda.ipynb`