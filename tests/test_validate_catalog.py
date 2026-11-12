import csv
from pathlib import Path
from src.ingestion.validate_catalog import (
    EXPECTED_COLUMNS,
    validate_columns,
    validate_status,
    validate_required_fields,
    validate_cover_path,
    find_duplicate_ids,
    validate_catalog,
)


def test_valid_catalog_columns():
    """The expected CSV columns should pass validation."""
    assert validate_columns(EXPECTED_COLUMNS.copy()) is True


def test_invalid_catalog_columns():
    """Columns in the wrong order should fail validation."""
    invalid_columns = EXPECTED_COLUMNS.copy()

    invalid_columns[0], invalid_columns[1] = (
        invalid_columns[1],
        invalid_columns[0],
    )

    assert validate_columns(invalid_columns) is False

def test_valid_verification_statuses():
    """All approved verification statuses should pass."""
    for status in ["verified", "pending", "uncertain"]:
        assert validate_status(status) is True


def test_invalid_verification_statuses():
    """Unapproved statuses should fail validation."""
    for status in ["PENDING", "unknown", ""]:
        assert validate_status(status) is False

def test_valid_required_fields():
    """A complete record should have no missing required fields."""
    record = {
        "comic_id": "CV0001",
        "title": "The New Teen Titans",
        "issue_number": "25",
        "publisher": "DC Comics",
        "cover_image_path": "data/raw/covers/CV0001_front.jpg",
        "metadata_source": "Physical front cover and interior indicia",
    }

    assert validate_required_fields(record) == []


def test_missing_required_field():
    """A record missing its publisher should be rejected."""
    record = {
        "comic_id": "CV0001",
        "title": "The New Teen Titans",
        "issue_number": "25",
        "publisher": "",
        "cover_image_path": "data/raw/covers/CV0001_front.jpg",
        "metadata_source": "Physical front cover and interior indicia",
    }

    assert validate_required_fields(record) == ["publisher"]

def test_existing_cover_image(tmp_path):
    """An existing cover image path should pass."""
    cover_file = tmp_path / "CV0001_front.jpg"
    cover_file.touch()

    record = {
        "cover_image_path": "CV0001_front.jpg"
    }

    assert validate_cover_path(record, tmp_path) is True


def test_missing_cover_image(tmp_path):
    """A nonexistent cover image path should fail."""
    record = {
        "cover_image_path": "CV9999_front.jpg"
    }

    assert validate_cover_path(record, tmp_path) is False

def test_unique_comic_ids():
    """Unique comic IDs should produce no duplicates."""
    records = [
        {"comic_id": "CV0001"},
        {"comic_id": "CV0002"},
        {"comic_id": "CV0003"},
    ]

    assert find_duplicate_ids(records) == []


def test_duplicate_comic_ids():
    """Repeated comic IDs should be detected."""
    records = [
        {"comic_id": "CV0001"},
        {"comic_id": "CV0002"},
        {"comic_id": "CV0001"},
    ]

    assert find_duplicate_ids(records) == ["CV0001"]

def test_valid_catalog_integration(tmp_path):
    """A valid catalog should pass all integrated checks."""

    project_root = Path(__file__).resolve().parents[1]
    source_path = (
        project_root / "data/raw/metadata/comic_catalog_pilot.csv"
    )

    with source_path.open(
        encoding="utf-8-sig", newline=""
    ) as source_file:
        reader = csv.DictReader(source_file)
        records = list(reader)

    test_path = tmp_path / "valid_catalog.csv"

    with test_path.open(
        "w", encoding="utf-8", newline=""
    ) as test_file:
        writer = csv.DictWriter(
            test_file,
            fieldnames=EXPECTED_COLUMNS,
        )
        writer.writeheader()
        writer.writerows(records)

    result = validate_catalog(test_path)

    assert result["valid"] is True
    assert result["record_count"] == len(records)
    assert result["errors"] == []

def test_invalid_status_catalog_integration(tmp_path):
    """The complete validator should reject an invalid status."""

    project_root = Path(__file__).resolve().parents[1]
    source_path = (
        project_root / "data/raw/metadata/comic_catalog_pilot.csv"
    )

    with source_path.open(
        encoding="utf-8-sig", newline=""
    ) as source_file:
        reader = csv.DictReader(source_file)
        records = list(reader)

    # Deliberately introduce an invalid status.
    records[0]["verification_status"] = "PENDING"

    test_path = tmp_path / "invalid_status_catalog.csv"

    with test_path.open(
        "w", encoding="utf-8", newline=""
    ) as test_file:
        writer = csv.DictWriter(
            test_file,
            fieldnames=EXPECTED_COLUMNS,
        )
        writer.writeheader()
        writer.writerows(records)

    result = validate_catalog(test_path)

    assert result["valid"] is False
    assert result["record_count"] == len(records)
    assert (
        "CV0001: Invalid verification status: 'PENDING'"
        in result["errors"]
    )

def test_missing_cover_catalog_integration(tmp_path):
    """The complete validator should reject a missing cover."""

    project_root = Path(__file__).resolve().parents[1]
    source_path = (
        project_root / "data/raw/metadata/comic_catalog_pilot.csv"
    )

    with source_path.open(
        encoding="utf-8-sig", newline=""
    ) as source_file:
        reader = csv.DictReader(source_file)
        records = list(reader)

    # Deliberately reference a nonexistent cover image.
    records[0]["cover_image_path"] = (
        "data/raw/covers/CV9999_front.jpg"
    )

    test_path = tmp_path / "missing_cover_catalog.csv"

    with test_path.open(
        "w", encoding="utf-8", newline=""
    ) as test_file:
        writer = csv.DictWriter(
            test_file,
            fieldnames=EXPECTED_COLUMNS,
        )
        writer.writeheader()
        writer.writerows(records)

    result = validate_catalog(test_path)

    assert result["valid"] is False
    assert result["record_count"] == len(records)
    assert (
        "CV0001: Cover image file not found."
        in result["errors"]
    )

def test_duplicate_ids_catalog_integration(tmp_path):
    """The complete validator should reject duplicate comic IDs."""

    project_root = Path(__file__).resolve().parents[1]
    source_path = (
        project_root / "data/raw/metadata/comic_catalog_pilot.csv"
    )

    with source_path.open(
        encoding="utf-8-sig", newline=""
    ) as source_file:
        reader = csv.DictReader(source_file)
        records = list(reader)

    # Add a second record with the same comic ID.
    records.append(records[0].copy())

    test_path = tmp_path / "duplicate_ids_catalog.csv"

    with test_path.open(
        "w", encoding="utf-8", newline=""
    ) as test_file:
        writer = csv.DictWriter(
            test_file,
            fieldnames=EXPECTED_COLUMNS,
        )
        writer.writeheader()
        writer.writerows(records)

    result = validate_catalog(test_path)

    assert result["valid"] is False
    assert result["record_count"] == len(records)
    assert (
        "Duplicate comic ID detected: CV0001"
        in result["errors"]
    )

def test_missing_publisher_catalog_integration(tmp_path):
    """The complete validator should reject a missing publisher."""

    project_root = Path(__file__).resolve().parents[1]
    source_path = (
        project_root / "data/raw/metadata/comic_catalog_pilot.csv"
    )

    with source_path.open(
        encoding="utf-8-sig", newline=""
    ) as source_file:
        reader = csv.DictReader(source_file)
        records = list(reader)

    # Deliberately remove the publisher.
    records[0]["publisher"] = ""

    test_path = tmp_path / "missing_publisher_catalog.csv"

    with test_path.open(
        "w", encoding="utf-8", newline=""
    ) as test_file:
        writer = csv.DictWriter(
            test_file,
            fieldnames=EXPECTED_COLUMNS,
        )
        writer.writeheader()
        writer.writerows(records)

    result = validate_catalog(test_path)

    assert result["valid"] is False
    assert result["record_count"] == len(records)
    assert (
        "CV0001: Missing required fields: publisher"
        in result["errors"]
    )

def test_invalid_columns_catalog_integration(tmp_path):
    """The complete validator should reject incorrect CSV columns."""

    test_path = tmp_path / "invalid_columns_catalog.csv"

    invalid_columns = EXPECTED_COLUMNS.copy()

    # Swap the first two column names.
    invalid_columns[0], invalid_columns[1] = (
        invalid_columns[1],
        invalid_columns[0],
    )

    with test_path.open(
        "w", encoding="utf-8", newline=""
    ) as test_file:
        writer = csv.writer(test_file)
        writer.writerow(invalid_columns)

    result = validate_catalog(test_path)

    assert result["valid"] is False
    assert (
        "CSV column structure does not match specification."
        in result["errors"]
    )

def test_empty_catalog_integration(tmp_path):
    """The complete validator should reject an empty catalog."""

    test_path = tmp_path / "empty_catalog.csv"

    # Create a CSV with the correct header but no comic records.
    with test_path.open(
        "w", encoding="utf-8", newline=""
    ) as test_file:
        writer = csv.writer(test_file)
        writer.writerow(EXPECTED_COLUMNS)

    result = validate_catalog(test_path)

    assert result["valid"] is False
    assert result["record_count"] == 0
    assert "Comic catalog contains no records." in result["errors"]

def test_valid_comic_id_format():
    """Comic IDs must use CV followed by four digits."""
    from src.ingestion.validate_catalog import validate_comic_id

    assert validate_comic_id("CV0001") is True
    assert validate_comic_id("CV0123") is True
    assert validate_comic_id("CV9999") is True

def test_invalid_comic_id_format():
    """Reject comic IDs that do not follow the required format."""
    from src.ingestion.validate_catalog import validate_comic_id

    assert validate_comic_id("CV1") is False
    assert validate_comic_id("CV12345") is False
    assert validate_comic_id("cv0001") is False
    assert validate_comic_id("COMIC0001") is False
    assert validate_comic_id("CVABCD") is False
    assert validate_comic_id("") is False

def test_invalid_comic_id_catalog_integration(tmp_path):
    """Reject a catalog containing an invalid comic ID."""
    import csv

    from src.ingestion.validate_catalog import (
        EXPECTED_COLUMNS,
        validate_catalog,
    )

    source_path = (
        Path(__file__).resolve().parents[1]
        / "data/raw/metadata/comic_catalog_pilot.csv"
    )

    with source_path.open(encoding="utf-8-sig", newline="") as file:
        record = next(csv.DictReader(file))

    record["comic_id"] = "INVALID123"

    test_csv = tmp_path / "invalid_comic_id.csv"

    with test_csv.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=EXPECTED_COLUMNS)
        writer.writeheader()
        writer.writerow(record)

    result = validate_catalog(test_csv)

    assert result["valid"] is False
    assert any(
        "Invalid comic ID" in error
        for error in result["errors"]
    )

def test_valid_publication_year():
    """Accept publication years from 1800 through the current year."""
    from datetime import date

    from src.ingestion.validate_catalog import validate_publication_year

    assert validate_publication_year("") is True
    assert validate_publication_year("1800") is True
    assert validate_publication_year("1895") is True
    assert validate_publication_year("1938") is True
    assert validate_publication_year("1982") is True
    assert validate_publication_year(str(date.today().year)) is True

def test_invalid_publication_year():
    """Reject invalid, implausible, and future publication years."""
    from datetime import date

    from src.ingestion.validate_catalog import validate_publication_year

    assert validate_publication_year("0001") is False
    assert validate_publication_year("1799") is False
    assert validate_publication_year("0000") is False

    assert validate_publication_year("19AB") is False
    assert validate_publication_year("19822") is False
    assert validate_publication_year("82") is False

    future_year = str(date.today().year + 1)
    assert validate_publication_year(future_year) is False

    assert validate_publication_year(None) is False
    assert validate_publication_year(1982) is False

def test_invalid_publication_year_catalog_integration(tmp_path):
    """Reject a catalog containing an invalid publication year."""
    import csv

    from src.ingestion.validate_catalog import (
        EXPECTED_COLUMNS,
        validate_catalog,
    )

    source_path = (
        Path(__file__).resolve().parents[1]
        / "data/raw/metadata/comic_catalog_pilot.csv"
    )

    with source_path.open(encoding="utf-8-sig", newline="") as file:
        record = next(csv.DictReader(file))

    record["publication_year"] = "1799"

    test_csv = tmp_path / "invalid_publication_year.csv"

    with test_csv.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=EXPECTED_COLUMNS)
        writer.writeheader()
        writer.writerow(record)

    result = validate_catalog(test_csv)

    assert result["valid"] is False
    assert any(
        "Invalid publication year" in error
        for error in result["errors"]
    )

def test_valid_publication_date():
    """Accept empty dates and valid calendar dates."""
    from src.ingestion.validate_catalog import validate_publication_date

    assert validate_publication_date("") is True
    assert validate_publication_date("1800-01-01") is True
    assert validate_publication_date("1895-05-05") is True
    assert validate_publication_date("1982-11-01") is True
    assert validate_publication_date("2000-02-29") is True

def test_invalid_publication_date():
    """Reject malformed, impossible, and out-of-range dates."""
    from datetime import date

    from src.ingestion.validate_catalog import validate_publication_date

    # Dates outside the approved range
    assert validate_publication_date("1799-12-31") is False
    assert validate_publication_date("0000-01-01") is False

    future_date = date.fromordinal(date.today().toordinal() + 1)
    assert validate_publication_date(future_date.isoformat()) is False

    # Invalid calendar dates
    assert validate_publication_date("1982-13-01") is False
    assert validate_publication_date("1982-02-30") is False
    assert validate_publication_date("1900-02-29") is False

    # Incorrect formats
    assert validate_publication_date("11/01/1982") is False
    assert validate_publication_date("1982-1-01") is False
    assert validate_publication_date("19821101") is False
    assert validate_publication_date("1982-AB-01") is False

    # Incorrect data types
    assert validate_publication_date(None) is False
    assert validate_publication_date(1982) is False

def test_invalid_publication_date_catalog_integration(tmp_path):
    """Reject a catalog containing an invalid publication date."""
    import csv

    from src.ingestion.validate_catalog import (
        EXPECTED_COLUMNS,
        validate_catalog,
    )

    source_path = (
        Path(__file__).resolve().parents[1]
        / "data/raw/metadata/comic_catalog_pilot.csv"
    )

    with source_path.open(encoding="utf-8-sig", newline="") as file:
        record = next(csv.DictReader(file))

    record["publication_date"] = "1982-02-30"

    test_csv = tmp_path / "invalid_publication_date.csv"

    with test_csv.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=EXPECTED_COLUMNS)
        writer.writeheader()
        writer.writerow(record)

    result = validate_catalog(test_csv)

    assert result["valid"] is False
    assert any(
        "Invalid publication date" in error
        for error in result["errors"]
    )

def test_publication_date_year_mismatch(tmp_path):
    """Reject a catalog when publication date and year disagree."""
    import csv

    from src.ingestion.validate_catalog import (
        EXPECTED_COLUMNS,
        validate_catalog,
    )

    source_path = (
        Path(__file__).resolve().parents[1]
        / "data/raw/metadata/comic_catalog_pilot.csv"
    )

    with source_path.open(encoding="utf-8-sig", newline="") as file:
        record = next(csv.DictReader(file))

    # Both values are individually valid, but they disagree.
    record["publication_date"] = "1982-11-01"
    record["publication_year"] = "1983"

    test_csv = tmp_path / "publication_date_year_mismatch.csv"

    with test_csv.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=EXPECTED_COLUMNS)
        writer.writeheader()
        writer.writerow(record)

    result = validate_catalog(test_csv)

    assert result["valid"] is False
    assert any(
        "Publication date/year mismatch" in error
        for error in result["errors"]
    )

def test_valid_publication_date_year_combinations(tmp_path):
    """Accept matching dates and optional publication fields."""
    import csv

    from src.ingestion.validate_catalog import (
        EXPECTED_COLUMNS,
        validate_catalog,
    )

    source_path = (
        Path(__file__).resolve().parents[1]
        / "data/raw/metadata/comic_catalog_pilot.csv"
    )

    with source_path.open(encoding="utf-8-sig", newline="") as file:
        original_record = next(csv.DictReader(file))

    valid_combinations = [
        ("1982-11-01", "1982"),
        ("1982-11-01", ""),
        ("", "1982"),
        ("", ""),
    ]

    for index, (publication_date, publication_year) in enumerate(
        valid_combinations
    ):
        record = original_record.copy()
        record["publication_date"] = publication_date
        record["publication_year"] = publication_year

        test_csv = tmp_path / f"valid_publication_{index}.csv"

        with test_csv.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=EXPECTED_COLUMNS)
            writer.writeheader()
            writer.writerow(record)

        result = validate_catalog(test_csv)

        assert result["valid"] is True, (
            f"Rejected valid combination: "
            f"date={publication_date!r}, "
            f"year={publication_year!r}, "
            f"errors={result['errors']}"
        )
