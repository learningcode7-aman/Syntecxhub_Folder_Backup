# Folder Backup / Sync Tool

Python-based folder backup and synchronization tool with timestamped backups, ZIP compression, logging, dry-run support, and automated backup rotation using CLI arguments.

## Features

* Backup folders to another location
* Timestamped backup creation
* Optional ZIP compression
* Dry-run mode
* Automatic old backup rotation
* Logging support
* Command-line interface using argparse

## Usage

### Basic Backup

```bash
python folder_backup.py --source "SOURCE_PATH" --destination "DESTINATION_PATH"
```

### Dry Run

```bash
python folder_backup.py --source "SOURCE_PATH" --destination "DESTINATION_PATH" --dry-run
```

### ZIP Backup

```bash
python folder_backup.py --source "SOURCE_PATH" --destination "DESTINATION_PATH" --zip
```

### Keep Only 2 Backups

```bash
python folder_backup.py --source "SOURCE_PATH" --destination "DESTINATION_PATH" --keep 2
```

## Example

```bash
python folder_backup.py --source "C:\Users\HP1\Desktop\source_files" --destination "C:\Users\HP1\Desktop\backups" --zip --keep 3
```

## Technologies Used

* Python
* os
* shutil
* argparse
* logging
* zipfile

## Author

Aman Shaik
