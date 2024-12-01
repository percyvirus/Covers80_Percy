#!/bin/bash

# Root directory where the mp3 files are located
SOURCE_DIRECTORY='./coversongs/covers32k'
DEST_DIRECTORY='./coversongs/wav_16k'

# File to store failed conversions
LOG_FILE="conversion_errors.log"

# Clear the log file before starting
> "$LOG_FILE"

# Create the destination directory if it doesn't exist
mkdir -p "$DEST_DIRECTORY"

# Traverse through the directories and subdirectories to find mp3 files
find "$SOURCE_DIRECTORY" -type f -name "*.mp3" | while read -r file; do
    # Get the relative path of the mp3 file from the source directory
    relative_path="${file#$SOURCE_DIRECTORY/}"
    
    # Create the corresponding directory structure in the destination directory
    output_dir="$DEST_DIRECTORY/$(dirname "$relative_path")"
    mkdir -p "$output_dir"
    
    # Set the output file path in the new directory (change extension to .wav)
    output_file="$output_dir/$(basename "${file%.mp3}.wav")"

    # Convert the mp3 file to wav (mono and 16kHz) using SoX
    sox "$file" -r 16000 -c 1 "$output_file"

    # Check if the conversion was successful
    if [ $? -eq 0 ]; then
        echo "Converted: $file -> $output_file"
    else
        # Log the failed conversion
        echo "Error converting: $file" >> "$LOG_FILE"
        echo "Failed to convert: $file"
        # Remove the partially converted file if it exists
        [ -e "$output_file" ] && rm "$output_file"
    fi
done

# Show the errors in the log file (if any)
if [ -s "$LOG_FILE" ]; then
    echo "The following files could not be converted:"
    cat "$LOG_FILE"
else
    echo "All files were converted successfully."
fi
