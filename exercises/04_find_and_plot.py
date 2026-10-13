"""Part 5: search, download and plot (10 min).

Part A is a complete example: search the records by tag and print a table of
their metadata. Part B is the exercise: download the CSV files and plot all
curves in one figure.

Run from the repository root:

    python exercises/04_find_and_plot.py

Solution: exercises/solutions/04_find_and_plot.py

Reference (https://kadi-apy.readthedocs.io/en/stable/usage/lib.html):
    Search.search_resources  search records, collections, ...
    Record.get_filelist      list the files of a record
    Record.download_file     download one file
Related: Record.download_all_files, Record.export
The search options (tag, q, collection, ...) are the same as for the command
`kadi-apy records get-records --help`.
"""

from pathlib import Path

import matplotlib.pyplot as plt
from kadi_apy import KadiManager

from tensile import read_curve  # in exercises/tensile.py

# TODO: set your prefix.
PREFIX = "xy"
CAMPAIGN_TAG = f"{PREFIX}-tensile-campaign"
DOWNLOAD_FOLDER = Path("downloads")
DOWNLOAD_FOLDER.mkdir(exist_ok=True)

manager = KadiManager()


# ---------------------------------------------------------------------------
# Part A: example, search by tag
# ---------------------------------------------------------------------------

# search_resources returns a response object; .json()["items"] contains the
# records that were found, as dictionaries.
response = manager.search.search_resources("record", tag=[CAMPAIGN_TAG], per_page=100)
found = response.json()["items"]
print(f"Found {len(found)} records with tag '{CAMPAIGN_TAG}'\n")

print(f"{'Record':<30} {'Yield [MPa]':>12} {'UTS [MPa]':>10}")
for item in found:
    record = manager.record(id=item["id"])
    # Turn the metadata list into a simple {key: value} dictionary.
    extras = {e["key"]: e.get("value") for e in record.meta["extras"]}
    print(
        f"{record.meta['title']:<30} "
        f"{extras.get('yield_strength', '-'):>12} "
        f"{extras.get('tensile_strength', '-'):>10}"
    )


# ---------------------------------------------------------------------------
# Part B: exercise, download and plot
# ---------------------------------------------------------------------------

for item in found:
    record = manager.record(id=item["id"])
    for file_info in record.get_filelist().json()["items"]:
        if not file_info["name"].endswith(".csv"):
            continue
        local_path = DOWNLOAD_FOLDER / file_info["name"]

        # TODO 1: download the file to local_path (file ID: file_info["id"],
        #         download_file expects a string: str(local_path))

        strain, stress = read_curve(local_path)
        plt.plot(strain, stress, label=record.meta["title"])

# TODO 2: label the axes "Strain [%]" and "Stress [MPa]"
#         Hint: plt.xlabel(...) and plt.ylabel(...)

plt.title("Tensile test campaign")
plt.legend()
plt.savefig("tensile_campaign.png", dpi=150)
print("\nPlot saved to tensile_campaign.png")
plt.show()
