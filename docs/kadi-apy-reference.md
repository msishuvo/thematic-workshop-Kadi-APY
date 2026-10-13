# kadi-apy Reference for the Workshop

This page lists the kadi-apy functions and commands used in the workshop,
together with related ones that are useful for similar tasks. All links point
to the official documentation of the stable release:
<https://kadi-apy.readthedocs.io/en/stable/>

## Using the documentation

The documentation has two main pages:

| Page | Content |
|---|---|
| [Usage > Library](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html) | All Python classes and functions |
| [Usage > CLI](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html) | All command line commands and their options |
| [Setup > Configuration](https://kadi-apy.readthedocs.io/en/stable/setup/configuration.html) | Host and access token, config file |

The Library page is organized by class. The ones used in the workshop are:

- `KadiManager`: the connection to Kadi4Mat and the starting point for everything else
  (`manager.record(...)`, `manager.collection(...)`, `manager.search`).
- `Record`: everything you can do with a record (metadata, files, tags, links).
  The parameters of `manager.record(...)` are described at the top of this section.
- `Collection`: the same for collections.
- `Search`: searching for records, collections and other resources.

A function entry shows the parameters and the return value, e.g.:

```
upload_file(file_path, file_name=None, file_description=None, force=False)
    Upload a file to a record.
    Parameters: file_path (str) - The path to the file (incl. name of the file).
                ...
    Returns:    The final response object of the upload process.
```

- Parameters without `=` are required, parameters with `=` are optional
  (the value after `=` is the default).
- Most functions return a response object: `response.ok` is `True` if the request
  was successful, `response.json()` returns the data sent back by Kadi4Mat.

The same information is available offline:

```python
from kadi_apy.lib.resources.records import Record
help(Record.upload_file)     # in Colab/Jupyter also: record.upload_file?
```

```bash
kadi-apy --help                  # all command groups
kadi-apy records --help          # all record commands
kadi-apy records add-files --help
```

More examples: <https://gitlab.com/iam-cms/kadi-apy/-/tree/master/examples>

## Python functions

Base URL of the links: <https://kadi-apy.readthedocs.io/en/stable/usage/lib.html>

### Used in the workshop

| Function | Purpose | Part |
|---|---|---|
| [`KadiManager()`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.core.KadiManager) | Connect to Kadi4Mat (reads the config file) | 0 |
| [`manager.record(...)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.core.KadiManager.record) | Get a record by `id` or `identifier`, or create it with `create=True`; parameters: see [`Record`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record) | 3, 4, 5 |
| [`record.add_metadata(metadata, force=False)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.add_metadata) | Add a list of metadata entries | 3, 4 |
| [`record.upload_file(file_path, force=False)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.upload_file) | Upload a file | 3, 4 |
| [`record.add_tag(tag)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.add_tag) | Add a tag | 3, 4 |
| [`record.get_metadatum(name)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.get_metadatum) | Read one metadata entry | 3 |
| [`manager.collection(...)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.core.KadiManager.collection) | Get or create a collection; parameters: see [`Collection`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.collections.Collection) | 4 |
| [`record.add_collection_link(collection_id)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.add_collection_link) | Add the record to a collection (collection ID) | 4 |
| [`record.link_record(record_to, name)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.link_record) | Link two records (ID of the target record, name of the link) | 4 |
| [`manager.search.search_resources(item, **params)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.search.Search.search_resources) | Search records, collections, ... | 5 |
| [`record.get_filelist()`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.get_filelist) | List the files of a record | 5 |
| [`record.download_file(file_id, file_path)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.download_file) | Download one file | 5 |

IDs and identifiers: functions that link resources, such as `add_collection_link`
and `link_record`, expect the numeric ID. If you only know the identifier, get the
resource first and use its `.id`:

```python
collection = manager.collection(identifier="jd-tensile-campaign-2026")
machine = manager.record(identifier="jd-tensile-machine")
record.add_collection_link(collection.id)
record.link_record(machine.id, name="tested with")
```

On the command line, identifiers can be used directly (see below).

### Related functions

| Function | Purpose |
|---|---|
| [`record.add_metadatum(metadatum, force=False)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.add_metadatum) | Add a single metadata entry |
| [`record.remove_metadatum(metadatum)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.remove_metadatum) | Remove a metadata entry |
| [`record.upload_string_to_file(string, file_name)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.upload_string_to_file) | Store text as a file, e.g. notes or a log |
| [`record.download_all_files(file_path)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.download_all_files) | Download all files as a ZIP archive |
| [`record.remove_tag(tag)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.remove_tag) | Remove a tag |
| [`record.edit(**kwargs)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.edit) | Change title, description, ... |
| [`record.remove_collection_link(collection_id)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.remove_collection_link) | Remove the record from a collection |
| [`record.get_record_links()`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.get_record_links) | List the links of a record |
| [`record.delete_record_link(record_link_id)`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.delete_record_link) | Delete a record link |
| [`record.export(path, export_type="json")`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.records.Record.export) | Export the record (json, pdf, qr, rdf, ro-crate) |
| [`collection.get_records()`](https://kadi-apy.readthedocs.io/en/stable/usage/lib.html#kadi_apy.lib.resources.collections.Collection.get_records) | List the records of a collection |

### Metadata entries

A metadata entry is a dictionary:

```python
{"key": "yield_strength", "type": "float", "value": 364.1, "unit": "MPa"}
```

| Python `type` | CLI `-t` | Example value |
|---|---|---|
| `str` | `string` (default) | `"S355 steel"` |
| `int` | `integer` | `3` |
| `float` | `float` | `364.1` |
| `bool` | `boolean` | `True` |

Units are only allowed for `int` and `float`.

## Command line

Base URL of the links: <https://kadi-apy.readthedocs.io/en/stable/usage/cli.html>

### Used in the workshop

| Command | Purpose | Part |
|---|---|---|
| [`kadi-apy config create`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-config-create) | Create an empty config file | 0 (local setup) |
| [`kadi-apy config set-host`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-config-set-host) | Set the Kadi4Mat address | 0 (local setup) |
| [`kadi-apy config set-pat`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-config-set-pat) | Set the access token | 0 (local setup) |
| [`kadi-apy records create`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-records-create) | Create a record (`-i` identifier, `-t` title) | 2 |
| [`kadi-apy records add-files`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-records-add-files) | Upload a file or folder (`-n`) | 2 |
| [`kadi-apy records add-metadatum`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-records-add-metadatum) | Add a metadata entry (`-m`, `-v`, `-t`, `-u`) | 2 |
| [`kadi-apy records add-tag`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-records-add-tag) | Add a tag (`-t`) | 2 |
| [`kadi-apy records show-info`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-records-show-info) | Show a record (`-m` metadata, `-l` files) | 2 |

All record commands select the record with `-R` (identifier) or `-r` (numeric ID).

### Links between resources

| Command | Purpose |
|---|---|
| [`kadi-apy records add-collection-link`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-records-add-collection-link) | Add a record to a collection (`-C` collection identifier or `-c` ID) |
| [`kadi-apy records add-record-link`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-records-add-record-link) | Link two records (`-L` identifier or `-l` ID of the target, `-n` name) |
| [`kadi-apy collections add-record-link`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-collections-add-record-link) | Add a record to a collection, starting from the collection |

```bash
kadi-apy records add-collection-link -R jd-sample-s01 -C jd-tensile-campaign-2026
kadi-apy records add-record-link -R jd-sample-s01 -L jd-tensile-machine -n "tested with"
```

### Related commands

| Command | Purpose |
|---|---|
| [`kadi-apy records add-metadata`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-records-add-metadata) | Add several metadata entries from a JSON string or file |
| [`kadi-apy records get-file`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-records-get-file) | Download files of a record |
| [`kadi-apy records get-records`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-records-get-records) | Search records (`-t` tag, `-q` query, ...) |
| [`kadi-apy records edit`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-records-edit) | Change title, description, visibility, ... |
| [`kadi-apy records export`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-records-export) | Export a record (json, pdf, qr, rdf, ro-crate) |
| [`kadi-apy collections create`](https://kadi-apy.readthedocs.io/en/stable/usage/cli.html#kadi-apy-collections-create) | Create a collection |
