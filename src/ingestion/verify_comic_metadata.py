
"""Generate read-only metadata verification worksheets for ComicVision AI."""

import argparse
import csv
from pathlib import Path


CATALOG = Path("data/raw/metadata/comic_catalog_pilot.csv")


def load_catalog():
    """Load comic metadata and check for duplicate IDs."""
    with CATALOG.open("r", encoding="utf-8-sig", newline="") as file:
        records = list(csv.DictReader(file))

    ids = [row["comic_id"] for row in records]

    assert len(ids) == len(set(ids)), "Duplicate comic IDs detected"

    return records


def select_batch(records, start_id, batch_size):
    """Select consecutive records beginning with the requested comic ID."""
    if batch_size < 1:
        raise ValueError("Batch size must be at least 1")

    for index, record in enumerate(records):
        if record["comic_id"] == start_id:
            return records[index:index + batch_size]

    raise ValueError(f"Comic ID not found: {start_id}")


def display_worksheet(batch):
    """Print metadata and inspection fields for each comic."""
    print("=== COMICVISION AI BATCH INSPECTION ===")
    print(f"Batch records: {len(batch)}")
    print()

    missing_covers = 0

    for record in batch:
        cover = Path(record["cover_image_path"])
        cover_exists = cover.is_file()

        if not cover_exists:
            missing_covers += 1

        print(
            f"{record['comic_id']} | "
            f"{record['title']} #{record['issue_number']}"
        )
        print(f"  Publisher: {record['publisher']}")
        print(f"  Cover date: {record['issue_date'] or 'Not recorded'}")
        print(f"  Cover file: {'FOUND' if cover_exists else 'MISSING'}")
        print(f"  Verification status: {record['verification_status']}")
        print(f"  Notes: {record.get('notes', '')}")
        print()
        print("  PHYSICAL INSPECTION")
        print("  Issue number: [ ] Confirmed [ ] Mismatch [ ] Unclear")
        print("  Cover date:   [ ] Confirmed [ ] Mismatch [ ] Unclear")
        print("  Cover price:  [ ] Confirmed [ ] Mismatch [ ] Unclear")
        print("  Indicia:      [ ] Confirmed [ ] Mismatch [ ] Unclear")
        print()
        print("  HISTORICAL VERIFICATION")
        print("  Publisher:    [ ] Confirmed [ ] Mismatch [ ] Pending")
        print("  Reference:    [ ] Confirmed [ ] Mismatch [ ] Pending")
        print("-" * 60)

    print()
    print(f"Missing cover files: {missing_covers}")
    print("CSV modifications: NONE")
    print("Verification status changes: NONE")
    print("RESULT: WORKSHEET GENERATED")


def main():
    """Parse command-line options and generate the worksheet."""
    parser = argparse.ArgumentParser(
        description="ComicVision AI batch metadata verification"
    )

    parser.add_argument(
        "--start",
        default="CV0002",
        help="First comic ID in the batch",
    )

    parser.add_argument(
        "--batch-size",
        type=int,
        default=5,
        help="Number of comics to inspect",
    )

    args = parser.parse_args()

    records = load_catalog()
    batch = select_batch(records, args.start, args.batch_size)

    display_worksheet(batch)


if __name__ == "__main__":
    main()
