"""Part 4: batch upload of a tensile test campaign (20 min).

The testing machine has written one result file per specimen into a folder.
Instead of uploading the files one by one and copying values into the
metadata by hand, a loop does this for every file.

Part A is a complete example: a loop that evaluates every file. Part B is
the exercise: extend the loop so that it uploads everything to Kadi4Mat.

Run from the repository root:

    python exercises/03_batch_upload.py

Solution: exercises/solutions/03_batch_upload.py

Reference (https://kadi-apy.readthedocs.io/en/stable/usage/lib.html):
    KadiManager.collection      get or create a collection, parameters: see "Collection"
    Record.add_collection_link  add a record to a collection
    Record.link_record          link two records, e.g. sample and machine
Related: Record.remove_collection_link, Record.get_record_links
"""

from pathlib import Path

from kadi_apy import KadiManager

from tensile import evaluate  # in exercises/tensile.py

# TODO: set your prefix.
PREFIX = "xy"
DATA_FOLDER = Path("data/tensile_tests")
CAMPAIGN_TAG = f"{PREFIX}-tensile-campaign"

UNITS = {
    "youngs_modulus": "GPa",
    "yield_strength": "MPa",
    "tensile_strength": "MPa",
    "elongation_at_break": "%",
}


# ---------------------------------------------------------------------------
# Part A: example, evaluate all files in the folder
# ---------------------------------------------------------------------------

# The indented block runs once for every CSV file in the folder.
for csv_file in sorted(DATA_FOLDER.glob("*.csv")):
    sample_id = csv_file.stem.split("_")[0]  # "S01_tensile" -> "S01"
    results = evaluate(csv_file)  # e.g. {"yield_strength": 364.1, ...}
    print(sample_id, results)


# ---------------------------------------------------------------------------
# Part B: exercise, upload all samples
# ---------------------------------------------------------------------------

manager = KadiManager()

# One collection for the whole test campaign.
collection = manager.collection(
    identifier=f"{PREFIX}-tensile-campaign-2026",
    title="Tensile test campaign 2026",
    create=True,
)

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

    # TODO 1: add the metadata to the record (use force=True)

    # TODO 2: upload the CSV file (upload_file expects a string: str(csv_file))

    # TODO 3: add the tag CAMPAIGN_TAG

    # TODO 4: add the record to the collection (use collection.id)

    print(sample_id, "uploaded")

print(f"Done. Open the collection '{collection.meta['title']}' in Kadi4Mat.")

# Optional: link every sample to the machine record from part 2, e.g.
#   machine = manager.record(identifier=f"{PREFIX}-tensile-machine")
#   record.link_record(machine.id, name="tested with")
# Each call adds a new link, so do this only once per sample.
