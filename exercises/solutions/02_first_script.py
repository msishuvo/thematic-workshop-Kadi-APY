"""Exercise 2 (solution): your first kadi-apy script."""

from kadi_apy import KadiManager

PREFIX = "xy"

manager = KadiManager()

record = manager.record(
    identifier=f"{PREFIX}-sample-s02",
    title="Steel sample S02",
    create=True,
)
print("Working on:", record)

metadata = [
    {"key": "material", "type": "str", "value": "S355 steel"},
    {"key": "specimen_length", "type": "float", "value": 80.0, "unit": "mm"},
    {"key": "test_temperature", "type": "float", "value": 23.0, "unit": "degC"},
]
record.add_metadata(metadata, force=True)

record.upload_file("data/tensile_tests/S02_tensile.csv", force=True)

record.add_tag(f"{PREFIX}-tensile-campaign")

print("Done! Now open the record in Kadi4Mat in your browser:", record)
