
# ComicVision AI — Comic Data Acquisition Specification

**Version:** 1.0
**Status:** Draft — Pending Validation
**Project:** ComicVision AI
**Pilot Target:** 20 physical comics
**Full Collection Target:** 100+ physical comics

## 1. Purpose

Establish a consistent, reproducible process for photographing,
identifying, cataloging, and validating physical comic books.

The resulting dataset will support computer vision, classification,
clustering, recommendations, and multimodal retrieval.

## 2. Collection Strategy

- Begin with 20 unique physical comics.
- Validate the acquisition workflow before expanding.
- Expand to 100+ unique comic records.
- Retain original photographs without destructive edits.
- Record uncertain metadata explicitly rather than guessing.

## 3. Cover Photography Standards

- Photograph the complete front cover.
- Use even lighting and avoid glare or harsh shadows.
- Place comics on a clean, neutral background.
- Keep the camera approximately parallel to the cover.
- Ensure titles, issue numbers, and publisher marks are legible.
- Avoid fingers or other objects obscuring the cover.
- Retain the highest-quality original image available.
- Use JPEG or PNG format.
- Aim for at least 1500 pixels on the image's longest side.
- Record exceptions when image quality requirements cannot be met.

## 4. Image Naming and Storage

Assign every physical comic a stable identifier:

CV0001, CV0002, CV0003, and so on.

Example filename:

CV0001_front.jpg

Store original cover photographs in:

data/raw/covers/

Do not rename an identifier after it has been assigned.

## 5. Metadata Schema

Create one catalog record per physical comic.

| Field | Required | Description |
|---|---|---|
| comic_id | Yes | Stable unique identifier |
| title | Yes | Comic title |
| issue_number | Yes | Issue identifier, stored as text |
| publisher | Yes | Publisher name |
| publication_date | No | Verified date in YYYY-MM-DD format |
| publication_year | No | Verified publication year |
| genre_tags | No | One or more supported genre labels |
| description | No | Verified synopsis or description |
| cover_image_path | Yes | Relative path to original image |
| metadata_source | Yes | Source used to verify metadata |
| verification_status | Yes | verified, pending, or uncertain |
| notes | No | Exceptions or additional context |

Unknown required metadata must be flagged for review rather
than invented.

## 6. Metadata Verification

- Use the physical cover and indicia when available.
- Use reputable comic databases for supplementary verification.
- Treat OCR output as a candidate, not verified ground truth.
- Review OCR-extracted titles and issue numbers manually.
- Record the source of verified information.
- Preserve uncertainty when sources disagree.

## 7. Data Quality Checks

Validate that:

1. Every comic has a unique comic_id.
2. Every catalog record references an existing cover image.
3. Images can be opened successfully.
4. Required metadata fields are populated or flagged.
5. Duplicate physical records are identified.
6. Publication years and dates are plausible.
7. Original images remain unchanged.
8. Verification status uses approved values.

## 8. Pilot Acceptance Criteria

The 20-comic pilot is accepted when:

- 20 distinct physical comics are cataloged.
- Every record has a stable identifier.
- Every record references a valid original cover image.
- Metadata verification status is documented.
- Missing and uncertain values are identified.
- A dataset validation report is produced.

## 9. Full Collection Acceptance Criteria

Milestone 02 is complete when:

- 100+ unique physical comic records are cataloged.
- Every record has a valid cover image reference.
- Data quality checks have been executed.
- OCR-assisted extraction has been evaluated.
- The final dataset validation report is documented.

## 10. Data Handling and Reproducibility

- Keep original photographs in data/raw/covers/.
- Store raw metadata separately from processed datasets.
- Do not overwrite original photographs during preprocessing.
- Keep private collection details out of public repositories.
- Document acquisition exceptions and corrections.
- Use consistent identifiers across all project artifacts.
- Respect copyright when sharing comic cover images.

## 11. Initial Implementation Plan

1. Select 20 unique physical comics from the existing collection. Include a variety of publishers, publication eras, and genres where available. Publisher diversity is encouraged but not required. Record the actual distribution and assess class imbalance before supervised modeling.
2. Photograph their front covers.
3. Assign stable comic identifiers.
4. Create the initial metadata catalog.
5. Verify metadata against reliable sources.
6. Run automated validation.
7. Review results before expanding to 100+ comics.