# File Synchronization Script

The File Synchronization Script is a Python script that continuously synchronizes files and directories between a source folder and a replica folder. It ensures that both folders stay up to date with the latest changes and additions. This script can be useful for backup, mirroring, or keeping two directories in sync.

## How it Works

1. The script monitors the contents of the `source_folder` and `replica_folder`.

2. Any new files or directories created in the `source_folder` are automatically copied to the `replica_folder`.

3. If a file or directory is deleted in the `source_folder`, it will also be removed from the `replica_folder` to maintain synchronization.

4. The script runs continuously, checking for changes at regular intervals.

## Usage

1. Create a `source_folder` and a `replica_folder` in the same directory as the script.

2. Run the script, and it will start monitoring and synchronizing the folders.

3. Any changes made in the `source_folder` will be reflected in the `replica_folder`, and vice versa.

## Customization

- You can customize the synchronization interval by adjusting the `time.sleep()` duration in the script.

- Feel free to modify the source and replica folder paths to match your directory locations.

## Dependencies

This script does not require any external libraries or dependencies. It utilizes built-in Python modules.
