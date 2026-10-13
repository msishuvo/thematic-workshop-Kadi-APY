"""Exercise 2: your first kadi-apy script (20 min, code-along).

Goal: create a record for sample S02, give it metadata and upload its file.

Fill in the lines marked TODO, then run from the repository root:

    python exercises/02_first_script.py

Solution: exercises/solutions/02_first_script.py
"""

from kadi_apy import KadiManager

# TODO 1: set your prefix (your initials, lowercase).
PREFIX = "xy"

# The manager is "your login". It reads the host and token you saved with
# `kadi-apy config create`, so no password or token appears in this script.
manager = KadiManager()

# Get the record with this identifier, or create it if it doesn't exist yet.
# Running the script twice therefore does NOT create a duplicate.
record = manager.record(
    identifier=f"{PREFIX}-sample-s02",
    title="Steel sample S02",
    create=True,
)
print("Working on:", record)

# Metadata ("extras") is a list of small dictionaries.
# Each one has: key (name), type, value and optionally a unit.
metadata = [
    {"key": "material", "type": "str", "value": "S355 steel"},
    {"key": "specimen_length", "type": "float", "value": 80.0, "unit": "mm"},
    # TODO 2: add a metadatum "test_temperature" of 23.0 degC
    #         (copy the line above and change it)
]
record.add_metadata(metadata, force=True)

# TODO 3: upload the file data/tensile_tests/S02_tensile.csv to the record.
#         Hint: record.upload_file("path/to/file", force=True)

# Tags make records easy to find later.
record.add_tag(f"{PREFIX}-tensile-campaign")

print("Done. Check the record in Kadi4Mat:", record)
