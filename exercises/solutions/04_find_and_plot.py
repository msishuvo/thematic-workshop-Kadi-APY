"""Part 5 (solution): search, download and plot."""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from kadi_apy import KadiManager

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tensile import read_curve  # noqa: E402

PREFIX = "xy"
TAG = f"{PREFIX}-tensile-tests"
DOWNLOAD_FOLDER = Path("downloads")
DOWNLOAD_FOLDER.mkdir(exist_ok=True)

manager = KadiManager()

# Part A: example, search by tag and plot metadata
response = manager.search.search_resources("record", tag=[TAG], per_page=100)
found = response.json()["items"]
print(f"Found {len(found)} records with tag '{TAG}'\n")

print(f"{'Record':<30} {'Yield [MPa]':>12} {'UTS [MPa]':>10}")
for item in found:
    record = manager.record(id=item["id"])
    extras = {e["key"]: e.get("value") for e in record.meta["extras"]}
    print(
        f"{record.meta['title']:<30} "
        f"{extras.get('yield_strength', '-'):>12} "
        f"{extras.get('tensile_strength', '-'):>10}"
    )


# The metadata can be plotted directly, without downloading any files.
# get_metadatum returns one entry (key, type, value, unit) or None.
names, yield_strength, tensile_strength = [], [], []
for item in found:
    record = manager.record(id=item["id"])
    ys = record.get_metadatum("yield_strength")
    ts = record.get_metadatum("tensile_strength")
    if ys and ts:  # only records that have both values
        names.append(record.meta["title"])
        yield_strength.append(ys["value"])
        tensile_strength.append(ts["value"])

x = range(len(names))
plt.bar([i - 0.2 for i in x], yield_strength, width=0.4, label="Yield strength")
plt.bar([i + 0.2 for i in x], tensile_strength, width=0.4, label="Tensile strength")
plt.xticks(list(x), names)
plt.ylabel("Strength [MPa]")
plt.title("Metadata from Kadi4Mat")
plt.margins(y=0.2)  # space above the bars for the legend
plt.legend(ncol=2)
plt.savefig("metadata.png", dpi=150)
print("\nPlot saved to metadata.png")
plt.show()

# Part B: exercise, download and plot the measured data
plt.figure()
for item in found:
    record = manager.record(id=item["id"])
    for file_info in record.get_filelist().json()["items"]:
        if not file_info["name"].endswith(".csv"):
            continue
        local_path = DOWNLOAD_FOLDER / file_info["name"]
        record.download_file(file_info["id"], str(local_path))
        strain, stress = read_curve(local_path)
        plt.plot(strain, stress, label=record.meta["title"])

plt.xlabel("Strain [%]")
plt.ylabel("Stress [MPa]")
plt.title("Tensile tests")
plt.legend()
plt.savefig("tensile_tests.png", dpi=150)
print("\nPlot saved to tensile_tests.png")
plt.show()
