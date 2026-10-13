"""Part 3: kadi-apy in Python (20 min).

Part A is a complete example (sample S02). Part B is the exercise: do the
same for sample S03 by filling in the lines marked TODO.

Run from the repository root:

    python exercises/02_first_script.py

Solution: exercises/solutions/02_first_script.py

Reference (https://kadi-apy.readthedocs.io/en/stable/usage/lib.html):
    KadiManager.record     get or create a record, parameters: see "Record"
    Record.add_metadata    add a list of metadata entries
    Record.upload_file     upload a file
    Record.add_tag         add a tag
    Record.get_metadatum   read one metadata entry
Related: Record.add_metadatum, Record.remove_metadatum,
Record.upload_string_to_file, Record.remove_tag, Record.edit
"""

from kadi_apy import KadiManager

# TODO: set your prefix (your initials, lowercase).
PREFIX = "xy"
CAMPAIGN_TAG = f"{PREFIX}-tensile-campaign"

# The connection to Kadi4Mat. It reads the host and token from the config
# file (kadi-apy config create / set-host / set-pat), so no token appears here.
manager = KadiManager()


# ---------------------------------------------------------------------------
# Part A: example, record for sample S02
# ---------------------------------------------------------------------------

# Get the record with this identifier, or create it if it does not exist yet.
# Running the script twice therefore does not create a duplicate.
record = manager.record(
    identifier=f"{PREFIX}-sample-s02",
    title="Steel sample S02",
    create=True,
)
print("Record:", record)

# Metadata is a list of dictionaries: key, type (str, int, float, bool),
# value and optionally unit. force=True overwrites existing entries.
metadata = [
    {"key": "material", "type": "str", "value": "S355 steel"},
    {"key": "specimen_length", "type": "float", "value": 80.0, "unit": "mm"},
    {"key": "test_temperature", "type": "float", "value": 23.0, "unit": "degC"},
]
record.add_metadata(metadata, force=True)

# Most functions return a response object; response.ok shows if it worked.
response = record.upload_file("data/tensile_tests/S02_tensile.csv", force=True)
print("Upload successful:", response.ok)

record.add_tag(CAMPAIGN_TAG)

# Read a value back from Kadi4Mat.
print(record.get_metadatum("specimen_length"))


# ---------------------------------------------------------------------------
# Part B: exercise, record for sample S03
# ---------------------------------------------------------------------------

# TODO 1: get or create the record f"{PREFIX}-sample-s03"
#         with the title "Steel sample S03"

# TODO 2: add the metadata material, specimen_length and test_temperature

# TODO 3: upload the file data/tensile_tests/S03_tensile.csv

# TODO 4: add the tag CAMPAIGN_TAG
