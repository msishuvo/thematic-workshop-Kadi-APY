"""Part 4: automating a tensile test campaign (20 min).

The testing machine has written one result file per specimen into a folder.
Instead of uploading the files one by one and copying values into the
metadata by hand, a loop does this for every file.

Part A is a complete example: sample S01 is added to a collection and linked
to the machine record, and a loop evaluates every file. Part B is the
exercise: extend the loop so that it uploads everything to Kadi4Mat.

add_collection_link and link_record expect numeric IDs. If you only know the
identifier, get the record or collection with manager.record(identifier=...)
or manager.collection(identifier=...) and use its .id. On the command line,
identifiers can be used directly:
    kadi-apy records add-collection-link -R xy-sample-s01 -C xy-tensile-campaign-2026
    kadi-apy records add-record-link -R xy-sample-s01 -L xy-tensile-machine -n "tested with"

Run from the repository root:

    python exercises/03_test_campaign.py

Solution: exercises/solutions/03_test_campaign.py

Reference (https://kadi-apy.readthedocs.io/en/stable/usage/lib.html):
    KadiManager.collection      get or create a collection, parameters: see "Collection"
    Record.add_collection_link  add a record to a collection
    Record.link_record          link two records, e.g. sample and machine
Related: Record.remove_collection_link, Record.get_record_links,
Record.delete_record_link
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


manager = KadiManager()


# ---------------------------------------------------------------------------
# Part A: example
# ---------------------------------------------------------------------------

# Collection for the whole campaign (created if it does not exist yet).
collection = manager.collection(
    identifier=f"{PREFIX}-tensile-campaign-2026",
    title="Tensile test campaign 2026",
    create=True,
)

# The records from part 2, looked up by their identifiers
# (create=True only creates them if they do not exist yet).
sample = manager.record(identifier=f"{PREFIX}-sample-s01",
                        title="Steel sample S01", create=True)
machine = manager.record(identifier=f"{PREFIX}-tensile-machine",
                         title="Tensile testing machine", create=True)

# Add the sample to the collection and link it to the machine.
# Running link_record again tries to create the same link again.
print("Added to collection:", sample.add_collection_link(collection.id).ok)
print("Linked to machine:", sample.link_record(machine.id, name="tested with").ok)

# The indented block runs once for every CSV file in the folder.
for csv_file in sorted(DATA_FOLDER.glob("*.csv")):
    sample_id = csv_file.stem.split("_")[0]  # "S01_tensile" -> "S01"
    results = evaluate(csv_file)  # e.g. {"yield_strength": 364.1, ...}
    print(sample_id, results)


# ---------------------------------------------------------------------------
# Part B: exercise, upload all samples
# ---------------------------------------------------------------------------

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

    # TODO 4: add the record to the collection (collection from part A)

    # TODO 5: link the record to the machine (machine from part A, name
    #         "tested with"). S01 is already linked in part A, so skip it:
    #         if sample_id != "S01":

    print(sample_id, "uploaded")

print(f"Done. Open the collection '{collection.meta['title']}' in Kadi4Mat.")
