
# Milestone 02 — OCR-Assisted Metadata Experiment

**Date:** November 15, 2026  
**Status:** Initial single-cover experiment completed  
**Sample:** CV0001 — The New Teen Titans #25

## Objective

Evaluate whether Tesseract OCR can extract useful
comic-book metadata from original cover photographs.

## Environment

- Python 3.11.9
- pytesseract 0.3.13
- Tesseract OCR 5.4.0
- Pillow image processing
- Windows development environment

## Experiment 1 — Full Cover

Input: CV0001_front.jpg

Configuration:
- Full-resolution RGB image
- Tesseract PSM 11
- English language

Observations:
- Large quantity of nonmeaningful text and symbols.
- Some recognizable dialogue.
- Poor extraction of structured catalog metadata.

## Experiment 2 — Upper Cover

Input: CV0001_front.jpg

Configuration:
- Top 35% of image
- Grayscale conversion
- Contrast enhancement: 1.5x
- Tesseract PSM 6
- English language

Detected candidates:
- Issue number: No.25
- Issue month: NOV.
- Text fragment: THE DEADLY
- Dialogue fragment: SURRENDER

## Catalog Comparison

| Field | Catalog | OCR result | Assessment |
|---|---|---|---|
| Title | The New Teen Titans | THE DEADLY | Not matched |
| Issue | 25 | No.25 | Match |
| Publisher | DC Comics | Not detected | Missing |
| Issue date | 1982-11 | NOV. | Month matches; year missing |
| Publication year | 1982 | Not detected | Missing |

Catalog verification status: pending.

## Findings

The upper-cover approach produced less OCR noise
and extracted two matching metadata candidates.

The experiments changed multiple preprocessing
settings simultaneously, so the contribution of
each individual setting remains unknown.

The results do not establish overall OCR accuracy
or independently verify catalog metadata.

## Recommendation

Use OCR as a metadata-assistance tool rather than
an authoritative metadata source.

Retain original photographs, require human review,
and independently verify historical metadata.

## Next Steps

1. Verify this experiment report.
2. Evaluate whether further OCR trials are useful.
3. Continue metadata verification.
4. Complete the Milestone 02 dataset validation report.
