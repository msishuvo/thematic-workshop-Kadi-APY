# Part 2: Command line interface (15 min)

Most actions in the Kadi4Mat web interface can also be done from the
terminal, which means they can be put in a script or run automatically on a
lab PC.

Replace `xy` with your own prefix (e.g. your initials) in all commands.
Identifiers must be unique in Kadi4Mat and may only contain lowercase
letters, digits, `-` and `_`. Run all commands from the root folder of this
repository.

## Example: record for sample S01

Create the record. `-i` is the identifier, `-t` the title:

```bash
kadi-apy records create -i xy-sample-s01 -t "Steel sample S01"
```

Upload the measurement file. `-R` selects the record by its identifier
(`-r` would select it by its numeric ID), `-n` is the file or folder:

```bash
kadi-apy records add-files -R xy-sample-s01 -n data/tensile_tests/S01_tensile.csv
```

Add metadata. Each entry has a name (`-m`), a value (`-v`), a type (`-t`,
default: string) and optionally a unit (`-u`):

```bash
kadi-apy records add-metadatum -R xy-sample-s01 -m material -v "S355 steel"
kadi-apy records add-metadatum -R xy-sample-s01 -m specimen_length -v 80 -t float -u mm
kadi-apy records add-metadatum -R xy-sample-s01 -m test_temperature -v 23 -t float -u degC
```

Add a tag and show the result (`-m` metadata, `-l` file list):

```bash
kadi-apy records add-tag -R xy-sample-s01 -t xy-tensile-tests
kadi-apy records show-info -R xy-sample-s01 -m -l
```

## Reference

Documentation of all commands: <https://kadi-apy.readthedocs.io/en/stable/usage/cli.html>

| Command | Purpose |
|---|---|
| `kadi-apy records create` | Create a record (or get it, if the identifier exists) |
| `kadi-apy records add-files` | Upload a file or all files of a folder |
| `kadi-apy records add-metadatum` | Add one metadata entry |
| `kadi-apy records add-tag` | Add a tag |
| `kadi-apy records show-info` | Show the record, its metadata (`-m`) and files (`-l`) |

Related commands: `records add-metadata` (several entries from a JSON file),
`records get-file` (download files), `records edit` (change title,
description, ...), `records delete`, `records get-records` (search).

`--help` after any command lists its options, e.g.
`kadi-apy records add-files --help`. `kadi-apy records --help` lists all
record commands.

## Exercise: record for the testing machine

Create a record for the tensile testing machine:

- identifier `xy-tensile-machine`, title "Tensile testing machine"
- metadata `max_force` = 100 (type float, unit kN)
- metadata `location` = "Lab 1" (text)
- show the record with its metadata

<details><summary>Show solution</summary>

```bash
kadi-apy records create -i xy-tensile-machine -t "Tensile testing machine"
kadi-apy records add-metadatum -R xy-tensile-machine -m max_force -v 100 -t float -u kN
kadi-apy records add-metadatum -R xy-tensile-machine -m location -v "Lab 1"
kadi-apy records show-info -R xy-tensile-machine -m
```

</details>
