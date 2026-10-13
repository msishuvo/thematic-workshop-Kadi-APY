"""Exercise 3 (solution): batch-upload a whole tensile test campaign.

Run from the repository root:

    python exercises/solutions/03_batch_upload.py
"""

import sys
from pathlib import Path

from kadi_apy import KadiManager

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tensile import evaluate  # noqa: E402

PREFIX = "xy"
DATA_FOLDER = Path("data/tensile_tests")
CAMPAIGN_TAG = f"{PREFIX}-tensile-campaign"

UNITS = {
    "youngs_modulus": "GPa",
    "yield_strength": "MPa",
    "tensile_strength": "MPa",
    "elongation_at_break": "%",
}

manager = KadiManager()

# One collection for the whole test campaign.
collection = manager.collection(
    identifier=f"{PREFIX}-tensile-campaign-2026",
    title="Tensile test campaign 2026",
    create=True,
)

for csv_file in sorted(DATA_FOLDER.glob("*.csv")):
    sample_id = csv_file.stem.split("_")[0]  # "S01_tensile" -> "S01"
    print(f"Processing {csv_file.name} ...")

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
    record.add_tag(CAMPAIGN_TAG)
    record.add_collection_link(collection.id)

    print(f"  -> {record}  {results}")

print(f"Done. Open the collection '{collection.meta['title']}' in Kadi4Mat.")

# Stretch goal: link every sample to a record describing the test machine.
# machine = manager.record(identifier=f"{PREFIX}-tensile-machine",
#                          title="Tensile testing machine", create=True)
# record.link_record(machine.id, name="tested with")
