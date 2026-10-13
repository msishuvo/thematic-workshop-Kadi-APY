"""Exercise 3: batch-upload a whole tensile test campaign (20 min).

The testing machine has written one result file per specimen into a
folder. Instead of uploading them one by one and copying numbers into
metadata fields by hand, this script does it for every file in the folder:

  1. create (or reuse) one record per sample
  2. evaluate the curve (yield strength etc.) -> store as metadata with units
  3. upload the raw CSV file
  4. tag the record and add it to a collection for the campaign

Fill in the TODOs, then run from the repository root:

    python exercises/03_batch_upload.py

Solution: exercises/solutions/03_batch_upload.py
"""

from pathlib import Path

from kadi_apy import KadiManager

from tensile import evaluate  # helper in exercises/tensile.py

# TODO 1: set your prefix.
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

# Run the indented block once for every CSV file in the folder.
for csv_file in sorted(DATA_FOLDER.glob("*.csv")):
    sample_id = csv_file.stem.split("_")[0]  # "S01_tensile" -> "S01"
    print(f"Processing {csv_file.name} ...")

    # TODO 2: get or create the record for this sample.
    #   identifier: f"{PREFIX}-sample-{sample_id.lower()}"
    #   title:      f"Steel sample {sample_id}"
    #   (see exercise 2)
    record = ...

    # Evaluate the curve: returns e.g. {"yield_strength": 364.1, ...}
    results = evaluate(csv_file)

    metadata = [
        {"key": "material", "type": "str", "value": "S355 steel"},
        {"key": "test_standard", "type": "str", "value": "ISO 6892-1"},
    ]
    for key, value in results.items():
        metadata.append({"key": key, "type": "float", "value": value, "unit": UNITS[key]})

    # TODO 3: add the metadata list to the record (use force=True).

    # TODO 4: upload the CSV file. Note: upload_file wants a string,
    #         so use str(csv_file).

    # TODO 5: add the tag CAMPAIGN_TAG to the record.

    # Put the record into the campaign collection.
    record.add_collection_link(collection.id)

    print(f"  -> {record}  {results}")

print(f"Done. Open the collection '{collection.meta['title']}' in Kadi4Mat.")

# Optional: create one record for the tensile testing machine and link
# every sample to it, e.g. record.link_record(machine.id, name="tested with")
