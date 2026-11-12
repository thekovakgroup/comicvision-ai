import csv
from pathlib import Path

EXPECTED_COLUMNS = [
    "comic_id",
    "title",
    "issue_number",
    "publisher",
    "publication_date",
    "publication_year",
    "genre_tags",
    "description",
    "cover_image_path",
    "metadata_source",
    "verification_status",
    "notes",
]

def validate_columns(actual_columns):
    """Check whether CSV columns match the expected schema."""
    return actual_columns == EXPECTED_COLUMNS

VALID_STATUSES = {
    "verified",
    "pending",
    "uncertain",
}

def validate_status(status):
    """Check whether a verification status is allowed."""
    return status in VALID_STATUSES

REQUIRED_FIELDS = {
    "comic_id",
    "title",
    "issue_number",
    "publisher",
    "cover_image_path",
    "metadata_source",
}

def validate_required_fields(record):
    """Return the names of required fields that are empty."""
    missing_fields = []

    for field in REQUIRED_FIELDS:
        value = record.get(field, "")

        if not value or not value.strip():
            missing_fields.append(field)

    return missing_fields

def validate_cover_path(record, project_root):
    """Check whether a comic's cover image file exists."""
    cover_path = record.get("cover_image_path", "")

    if not cover_path or not cover_path.strip():
        return False

    full_path = Path(project_root) / cover_path

    return full_path.is_file()

def find_duplicate_ids(records):
    """Return comic IDs that appear more than once."""
    seen = set()
    duplicates = set()

    for record in records:
        comic_id = record.get("comic_id", "").strip()

        if comic_id in seen:
            duplicates.add(comic_id)
        else:
            seen.add(comic_id)

    return sorted(duplicates)

def validate_catalog(csv_path):
    """Read a comic catalog and validate its column structure."""
    with open(csv_path, encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        actual_columns = reader.fieldnames

        if not validate_columns(actual_columns):
            return {
                "valid": False,
                "errors": ["CSV column structure does not match specification."],
            }

        records = list(reader)

    project_root = Path(__file__).resolve().parents[2]
    errors = []

    if not records:
        errors.append("Comic catalog contains no records.")

    for record in records:
        comic_id = record.get("comic_id", "").strip()

        if comic_id and not validate_comic_id(comic_id):
            errors.append(
                f"{comic_id}: Invalid comic ID format."
            )

        publication_year = record.get("publication_year", "")
        publication_date = record.get("publication_date", "")

        if not validate_publication_year(publication_year):
            errors.append(
                f"{comic_id or 'UNKNOWN'}: "
                f"Invalid publication year: {publication_year!r}"
            )

        if not validate_publication_date(publication_date):
            errors.append(
                f"{comic_id or 'UNKNOWN'}: "
                f"Invalid publication date: {publication_date!r}"
            )

        if (
            publication_date
            and publication_year
            and validate_publication_date(publication_date)
            and validate_publication_year(publication_year)
            and publication_date[:4] != publication_year
        ):
            errors.append(
                f"{comic_id or 'UNKNOWN'}: "
                "Publication date/year mismatch."
            )

        missing_fields = validate_required_fields(record)

        if missing_fields:
            errors.append(
                f"{comic_id or 'UNKNOWN'}: Missing required fields: "
                f"{', '.join(sorted(missing_fields))}"
            )

        status = record.get("verification_status", "")

        if not validate_status(status):
            errors.append(
                f"{comic_id or 'UNKNOWN'}: Invalid verification status: "
                f"{status!r}"
            )

        if not validate_cover_path(record, project_root):
            errors.append(
                f"{comic_id or 'UNKNOWN'}: Cover image file not found."
            )

    duplicate_ids = find_duplicate_ids(records)

    for comic_id in duplicate_ids:
        errors.append(
            f"Duplicate comic ID detected: {comic_id}"
        )

    return {
        "valid": len(errors) == 0,
        "record_count": len(records),
        "errors": errors,
    }

def validate_comic_id(comic_id):
    """Check whether a comic ID uses CV followed by four digits."""
    import re

    return re.fullmatch(r"CV[0-9]{4}", comic_id) is not None

def validate_publication_year(year):
    """Validate an optional publication year from 1800 to today."""
    from datetime import date

    if year == "":
        return True

    if not isinstance(year, str):
        return False

    if len(year) != 4 or not year.isascii() or not year.isdecimal():
        return False

    year_number = int(year)

    return 1800 <= year_number <= date.today().year

def validate_publication_date(date_value):
    """Validate an optional publication date from 1800 through today."""
    from datetime import date

    if date_value == "":
        return True

    if not isinstance(date_value, str):
        return False

    if len(date_value) != 10:
        return False

    if date_value[4] != "-" or date_value[7] != "-":
        return False

    year = date_value[:4]
    month = date_value[5:7]
    day = date_value[8:10]

    if not all(
        part.isascii() and part.isdecimal()
        for part in (year, month, day)
    ):
        return False

    try:
        parsed_date = date(
            int(year),
            int(month),
            int(day),
        )
    except ValueError:
        return False

    return date(1800, 1, 1) <= parsed_date <= date.today()
