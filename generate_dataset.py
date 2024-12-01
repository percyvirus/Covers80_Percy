import os
import json
import subprocess
import tempfile
from pydub import AudioSegment
from collections import defaultdict

# Directory containing the audio files
directory = 'coversongs/wav_16k'  # Replace with the path to the audio files

# Path to the list1.list file
list1_path = 'coversongs/list1.list'

# Base path for the "wav" key in the JSON output
base_path = 'data/covers80_percy/wav_16k/'

# Counter for the "perf" key
perf_counter = 0

# Dictionaries to track indices and version counts
work_indices = {}
work_version_count = defaultdict(int)

# List to store the records
records = []

# Read the list1.list file
with open(list1_path, 'r', encoding='utf-8') as f:
    list1_performances = f.read().splitlines()

# Group songs by folder
list1_dict = defaultdict(list)
for line in list1_performances:
    folder, original_performance_name = line.split('/', 1)  # Split folder and song name
    list1_dict[folder].append(original_performance_name)

# Process folder by folder
for folder, original_performances in list1_dict.items():
    # Get all MP3 files in the folder
    folder_path = os.path.join(directory, folder)
    try:
        all_mp3_files = [
            f[:-4] for f in os.listdir(folder_path)
            if f.lower().endswith('.mp3')
        ]
    except FileNotFoundError:
        print(f"Folder not found: {folder_path}")
        continue

    # Include MP3 files not listed in list1.list
    cover_performances = set(all_mp3_files) - set(original_performances)
    all_work_performances = original_performances + list(cover_performances)

    for performance_name in all_work_performances:
        # Generate the full path to the MP3 file
        file_path = os.path.join(folder_path, performance_name + '.mp3')

        # Process the audio file
        try:
            audio = AudioSegment.from_file(file_path)
            duration_seconds = round(audio.duration_seconds, 3)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            continue

        # Get the work name based on the song's folder
        work = folder

        # Assign a unique index to each "work" if not present
        if work not in work_indices:
            work_indices[work] = len(work_indices)
        work_index = work_indices[work]

        # Get the current version number
        version_number = work_version_count[work]

        # Generate the JSON record
        record = {
            "perf": f"cover80_percy_{perf_counter:08d}_{work_index}_{version_number}",
            "wav": os.path.join(base_path, performance_name + '.wav'),
            "dur_s": duration_seconds,
            "work": work,
            "version": performance_name + '.mp3'
        }
        records.append(record)

        # Increment the counters
        perf_counter += 1
        work_version_count[work] += 1

# Save the records to a file
output_file = 'dataset.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    for record in records:
        f.write(json.dumps(record) + '\n')

print(f"JSON records saved to '{output_file}'.")
