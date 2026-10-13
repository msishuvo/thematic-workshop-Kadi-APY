# Exercise 1: Command line interface (15 min)

Most actions in the Kadi4Mat web interface can also be done from the
terminal, which means they can be put in a script or run automatically on a
lab PC.

Replace `xy` with your own prefix (e.g. your initials) in all commands.
Identifiers must be unique in Kadi4Mat and may only contain lowercase
letters, digits, `-` and `_`.

Run all commands from the root folder of this repository.

## 1. Create a record for a sample

```bash
kadi-apy records create -i xy-sample-s01 -t "Steel sample S01"
```

The record is now visible in Kadi4Mat.

## 2. Upload a measurement file

```bash
kadi-apy records add-files -R xy-sample-s01 -n data/tensile_tests/S01_tensile.csv
```

`-R` selects the record by its identifier; `-r` would select it by its
numeric ID. `-n` also accepts a whole folder.

## 3. Add metadata

Metadata entries have a name, a value, a type and optionally a unit:

```bash
kadi-apy records add-metadatum -R xy-sample-s01 -m material -v "S355 steel"
kadi-apy records add-metadatum -R xy-sample-s01 -m specimen_length -v 80 -t float -u mm
kadi-apy records add-metadatum -R xy-sample-s01 -m test_temperature -v 23 -t float -u degC
```

## 4. Add a tag

```bash
kadi-apy records add-tag -R xy-sample-s01 -t xy-tensile-campaign
```

## 5. Show the record

```bash
kadi-apy records show-info -R xy-sample-s01 -m -l
```

`-m` shows metadata, `-l` shows the file list.

## 6. Search by tag

```bash
kadi-apy records get-records -t xy-tensile-campaign
```

## Further steps

- Run `kadi-apy records --help` to see everything the CLI can do.
- Upload the same file again, first without and then with `-f`.
