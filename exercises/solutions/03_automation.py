"""Part 4 (solution): automation."""

import sys
from pathlib import Path

from kadi_apy import KadiManager

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tensile import evaluate  # noqa: E402

PREFIX = "xy"
DATA_FOLDER = Path("data/tensile_tests")
TAG = f"{PREFIX}-tensile-tests"

UNITS = {
    "youngs_modulus": "GPa",
    "yield_strength": "MPa",
    "tensile_strength": "MPa",
    "elongation_at_break": "%",
}

manager = KadiManager()

# Part A: example
collection = manager.collection(
    identifier=f"{PREFIX}-tensile-tests-2026",
    title="Tensile tests 2026",
    create=True,
)
sample = manager.record(identifier=f"{PREFIX}-sample-s01",
                        title="Steel sample S01", create=True)
machine = manager.record(identifier=f"{PREFIX}-tensile-machine",
                         title="Tensile testing machine", create=True)
print("Added to collection:", sample.add_collection_link(collection.id).ok)
print("Linked to machine:", sample.link_record(machine.id, name="tested with").ok)

for csv_file in sorted(DATA_FOLDER.glob("*.csv")):
    sample_id = csv_file.stem.split("_")[0]
    print(sample_id, evaluate(csv_file))

# Part B: exercise, upload all samples

for csv_file in sorted(DATA_FOLDER.glob("*.csv")):
    sample_id = csv_file.stem.split("_")[0]

    record = manager.record(
        identifier=f"{PREFIX}-sample-{sample_id.lower()}",
        title=f"Steel sample {sample_id}",
        create=True,
    )

    results = evaluate(csv_file)
    metadata = [
        {"key": "material", "type": "str", "value": "S355 steel"},
        {"key": "test_standard", "type": "str", "value": "ISO 6892-1"},
    ]
    for key, value in results.items():
        metadata.append({"key": key, "type": "float", "value": value, "unit": UNITS[key]})

    record.add_metadata(metadata, force=True)
    record.upload_file(str(csv_file), force=True)
    record.add_tag(TAG)
    record.add_collection_link(collection.id)
    if sample_id != "S01":
        record.link_record(machine.id, name="tested with")

    print(sample_id, "uploaded")

print(f"Done. Open the collection '{collection.meta['title']}' in Kadi4Mat.")
