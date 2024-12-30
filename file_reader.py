from mutagen.mp4 import MP4
from types import SimpleNamespace
import os

def read_m4a_metadata(file_path):
    try:
        audio = MP4(file_path)
        return SimpleNamespace(
            title=audio.get('\xa9nam', [os.path.splitext(os.path.basename(file_path))[0]])[0],
            artist=audio.get('\xa9ART', [None])[0],
            album=audio.get('\xa9alb', [None])[0],
        )
    except Exception as e:
        return f"Error reading metadata: {str(e)}"

def process_folder(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith('.m4a'):
            full_path = os.path.join(folder_path, file)
            yield full_path

def process_file(file_path):
    metadata = read_m4a_metadata(file_path)
    print(f"\nProcessing: {file_path}")
    # print(f"Metadata: {metadata}")
    return SimpleNamespace(
        meta=metadata,
        path=file_path,
    )

def get_songs_in_folder(folder_path):
    for file_path in process_folder(folder_path):
        yield process_file(file_path)
