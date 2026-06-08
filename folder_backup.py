import os
import sys
import shutil
import logging
import argparse
from datetime import datetime
from zipfile import ZipFile, ZIP_DEFLATED

logging.basicConfig(filename = 'backup.log', level=logging.INFO, format='%(asctime)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

parser = argparse.ArgumentParser(description= "Folder Backup / Sync Tool")

parser.add_argument("--source", required=True, help = "Source folder path")
parser.add_argument("--destination", required=True, help = "Destination folder path")
parser.add_argument("--dry-run", action='store_true', help = "Perform a dry run without making changes")
parser.add_argument("--zip", action='store_true', help = "Compress backup into zip file")
parser.add_argument("--keep", type=int, default=3, help = "Number of backups to keep")

args = parser.parse_args()

source = args.source
destination = args.destination
dry_run = args.dry_run
zip_backup = args.zip
keep_limit = args.keep

if not os.path.isdir(source):
    print(f"Error: {source} is not a valid directory.")
    sys.exit(1)

if not os.path.isdir(destination):
    print(f"Error: {destination} is not a valid directory.")
    sys.exit(1)


timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder_name = f"backup_{timestamp}"
backup_path = os.path.join(destination, backup_folder_name)

if dry_run:
    print("\n[DRY RUN]")
    print(f"Would back up {source} to {backup_path}")

else:
    try:
        shutil.copytree(source, backup_path)
        print(f"Backup successfully created at {backup_path}")
        logging.info(f"Backup created at {backup_path}")
        
        if zip_backup:
            zip_name = backup_path + ".zip"
            with ZipFile(zip_name, 'w', ZIP_DEFLATED) as zipf:
                for foldername, subfolders, filenames in os.walk(backup_path):
                    for file in filenames:
                        file_path = os.path.join(foldername, file)
                        arcname = os.path.relpath(file_path, backup_path)
                        zipf.write(file_path, arcname)
            print(f"\nZIP Backup created: {zip_name}")
            logging.info(f"ZIP created: {zip_name}")
        
        backups = sorted([folder for folder in os.listdir(destination)
                          if folder.startswith("backup_")])
        while len(backups) > keep_limit:
            oldest = backups.pop(0)
            oldest_path = os.path.join(destination, oldest)
            if os.path.isdir(oldest_path):
                shutil.rmtree(oldest_path)
                print(f"Deleted old backup: {oldest}")
                logging.info(f"Deleted old backup: {oldest_path}")
            elif os.path.isfile(oldest_path):
                os.remove(oldest_path)
                logging.info(f"Deleted old backup: {oldest_path}")

    except Exception as e:
        logging.error(f"Error: {e}")
        print(f"An error occurred: {e}")