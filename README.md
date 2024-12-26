# ReplaceAppleMusic

A Python utility to replace source files of songs in Apple Music while preserving metadata like play count, favorite status, and playlist memberships.

## Features

- Preserves play count
- Maintains favorite status
- Keeps playlist memberships
- Automatically removes old track after replacement

## Requirements

- macOS
- Python 3.x
- Apple Music app

## Installation

You can install it directly from PyPI:
```bash
pip install replaceapplemusic
```

Or install from source:
1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Make sure Apple Music is running and you have the necessary permissions

## Usage

```bash
# Replace a song
ramusic /path/to/new/file.m4a

# Replace songs in a folder
ramusic /path/to/folder
```
