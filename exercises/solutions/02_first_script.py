"""Part 3 (solution): kadi-apy in Python."""

from kadi_apy import KadiManager

PREFIX = "xy"
CAMPAIGN_TAG = f"{PREFIX}-tensile-campaign"

manager = KadiManager()

METADATA = [
    {"key": "material", "type": "str", "value": "S355 steel"},
    {"key": "specimen_length", "type": "float", "value": 80.0, "unit": "mm"},
    {"key": "test_temperature", "type": "float", "value": 23.0, "unit": "degC"},
]

# Part A: example, record for sample S02
record = manager.record(
    identifier=f"{PREFIX}-sample-s02",
    title="Steel sample S02",
    create=True,
)
print("Record:", record)
record.add_metadata(METADATA, force=True)
response = record.upload_file("data/tensile_tests/S02_tensile.csv", force=True)
print("Upload successful:", response.ok)
record.add_tag(CAMPAIGN_TAG)
print(record.get_metadatum("specimen_length"))

# Part B: exercise, record for sample S03
record = manager.record(
    identifier=f"{PREFIX}-sample-s03",
    title="Steel sample S03",
    create=True,
)
record.add_metadata(METADATA, force=True)
record.upload_file("data/tensile_tests/S03_tensile.csv", force=True)
record.add_tag(CAMPAIGN_TAG)
print("Done. Check the record in Kadi4Mat:", record)
