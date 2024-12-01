### README for `cover80_percy` Package

This is a dataset and code based on the **covers80** dataset, with several modifications and additions.

---

### Overview:
The `covers80_percy/` directory contains an extended version of the **covers80** dataset. In this version:
- Additional cover songs have been added to ensure most original songs have at least five cover versions. Some songs may have fewer covers (3-4) due to availability.
- Corrections were made to the `list1.list` and `list2.list` files to ensure consistency: `list1.list` contains only original songs, and `list2.list` contains only cover songs.

---

### File Structure:
The `coversongs/` directory contains the audio files and related metadata for the dataset. However, this directory is **not included** in the GitHub repository due to file size limitations. To access the dataset, you can download it from the following Google Drive link:

[Download coversongs from Google Drive](<ENLACE_DE_GOOGLE_DRIVE>)

Once you have downloaded and extracted the `coversongs` folder, you can use the following directory structure:

- **`coversongs/covers32k/`**:  
  The original MP3 files, including the original songs from **covers80** and the additional covers I added. These files are encoded at different sampling rates.

- **`coversongs/mp3_16k/`**:  
  MP3 files converted from the `covers32k` directory. These files are resampled to 16kHz and converted to mono using the provided `convert_mp3_to_mp3_mono.sh` Bash script.

- **`coversongs/wav_16k/`**:  
  WAV files converted from the `covers32k` directory. These files are resampled to 16kHz and converted to mono using the provided `convert_mp3_to_wav_mono.sh` Bash script.  
  This is the main directory used for training and testing the **CoverHunterMPS** system.

- **`coversongs/list1.list`**:  
  A file containing paths to the original songs.  

- **`coversongs/list2.list`**:  
  A file containing paths to the cover songs.

- **`generate_dataset.py`**:  
  A Python script that processes the audio files in `coversongs/wav_16k/` and generates a `dataset.txt` file, formatted for use with **CoverHunterMPS**.

---

### Scripts for Audio Preprocessing:
Two Bash scripts were used for preprocessing the audio files:

1. **Convert MP3 to MP3 (Mono, 16kHz):**
   - Converts files in `covers32k` to mono MP3s at 16kHz.  
   - Outputs are stored in `coversongs/mp3_16k/`.

2. **Convert MP3 to WAV (Mono, 16kHz):**
   - Converts files in `covers32k` to WAV format, resampled to 16kHz and converted to mono.  
   - Outputs are stored in `coversongs/wav_16k/`.

---

### `generate_dataset.py` Script:
This script processes the WAV files in the `coversongs/wav_16k/` directory and generates a `dataset.txt` file, which is a JSON-formatted dataset for the **CoverHunterMPS** system. Key features:
- Extracts audio duration and creates unique identifiers for each file.
- Groups files by original song (work) and version (original or cover).
- Outputs a JSON record for each file containing:
  - `perf`: Unique identifier for the performance.
  - `wav`: Path to the WAV file.
  - `dur_s`: Duration of the audio file (in seconds).
  - `work`: Name of the original song (work).
  - `version`: Label indicating whether it’s an original or a cover version.

---

### Updates:
- Additional cover versions were added to expand the dataset, prioritizing achieving five covers per original song where possible.
- Corrected the `list1.list` and `list2.list` files for consistency.
- Processed the original MP3s to create two new sets of files:
  - Mono MP3s at 16kHz (`mp3_16k`).
  - Mono WAVs at 16kHz (`wav_16k`), used for training.

---

### Contact:
If you have any problems, questions, or suggestions, feel free to reach out.

**Percy Wilberth Bonett Mendoza**  
📧 *percy96bm@gmail.com*  
📅 *2024-12-01*

---

### Additional Note:
Remember that you need to download the `coversongs` folder from the Google Drive link before you can use the scripts and process the data correctly.
