"""Exercise 4 (solution): find your records, download the data and plot it.

Run from the repository root:

    python exercises/solutions/04_find_and_plot.py
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from kadi_apy import KadiManager

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tensile import read_curve  # noqa: E402

PREFIX = "xy"
CAMPAIGN_TAG = f"{PREFIX}-tensile-campaign"
DOWNLOAD_FOLDER = Path("downloads")
DOWNLOAD_FOLDER.mkdir(exist_ok=True)

manager = KadiManager()

# Search all records with our tag.
response = manager.search.search_resources("record", tag=[CAMPAIGN_TAG], per_page=100)
found = response.json()["items"]
print(f"Found {len(found)} records with tag '{CAMPAIGN_TAG}'\n")

print(f"{'Record':<30} {'Yield [MPa]':>12} {'UTS [MPa]':>10}")
for item in found:
    record = manager.record(id=item["id"])
    extras = {e["key"]: e.get("value") for e in record.meta["extras"]}
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

plt.xlabel("Strain [%]")
plt.ylabel("Stress [MPa]")
plt.title("Tensile test campaign")
plt.legend()
plt.savefig("tensile_campaign.png", dpi=150)
print("\nPlot saved to tensile_campaign.png")
plt.show()
