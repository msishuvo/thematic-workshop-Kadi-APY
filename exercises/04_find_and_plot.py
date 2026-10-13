"""Exercise 4: find your records, download the data and plot it (10 min).

Search the records by tag, print a table of the metadata, download the
CSV files and plot all curves in one figure.

Fill in the TODOs, then run from the repository root:

    python exercises/04_find_and_plot.py

Solution: exercises/solutions/04_find_and_plot.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
from kadi_apy import KadiManager

from tensile import read_curve  # helper in exercises/tensile.py

# TODO 1: set your prefix.
PREFIX = "xy"
CAMPAIGN_TAG = f"{PREFIX}-tensile-campaign"
DOWNLOAD_FOLDER = Path("downloads")
DOWNLOAD_FOLDER.mkdir(exist_ok=True)

manager = KadiManager()

# Search all records that carry our tag.
response = manager.search.search_resources("record", tag=[CAMPAIGN_TAG], per_page=100)
found = response.json()["items"]
print(f"Found {len(found)} records with tag '{CAMPAIGN_TAG}'\n")

print(f"{'Record':<30} {'Yield [MPa]':>12} {'UTS [MPa]':>10}")
for item in found:
    record = manager.record(id=item["id"])

    # Turn the metadata list into a simple {key: value} dictionary.
    extras = {e["key"]: e.get("value") for e in record.meta["extras"]}

    # TODO 2: also print the "elongation_at_break" column (and add a header).
    print(
        f"{record.meta['title']:<30} "
        f"{extras.get('yield_strength', '-'):>12} "
        f"{extras.get('tensile_strength', '-'):>10}"
    )

    # Download every CSV file of the record and plot it.
    for file_info in record.get_filelist().json()["items"]:
        if not file_info["name"].endswith(".csv"):
            continue
        local_path = DOWNLOAD_FOLDER / file_info["name"]
        record.download_file(file_info["id"], str(local_path))
        strain, stress = read_curve(local_path)
        plt.plot(strain, stress, label=record.meta["title"])

# TODO 3: label the axes: "Strain [%]" and "Stress [MPa]"
#         Hint: plt.xlabel(...) and plt.ylabel(...)

plt.title("Tensile test campaign")
plt.legend()
plt.savefig("tensile_campaign.png", dpi=150)
print("\nPlot saved to tensile_campaign.png")
plt.show()

# Optional: upload the plot back to Kadi4Mat, e.g. into the collection's records
# or a new "campaign summary" record, so the figure lives next to the data.
