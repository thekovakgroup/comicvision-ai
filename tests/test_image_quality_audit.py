
"""Regression tests for the Milestone 03 image-quality audit."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = (
    PROJECT_ROOT
    / "reports"
    / "milestone_03_image_quality_audit.csv"
)


def test_image_quality_audit():
    """Verify the saved image-quality audit artifact."""

    assert AUDIT_PATH.is_file(), "Image audit CSV is missing"

    audit = pd.read_csv(AUDIT_PATH)

    assert len(audit) == 20, "Expected 20 comic records"

    assert audit["comic_id"].is_unique, (
        "Duplicate comic IDs detected"
    )

    expected_statuses = {
        "preliminary_pass": 17,
        "review_recommended": 3,
    }

    actual_statuses = (
        audit["visual_review_status"]
        .value_counts()
        .to_dict()
    )

    assert actual_statuses == expected_statuses, (
        f"Unexpected review status counts: {actual_statuses}"
    )
