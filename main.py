from file_reader import *
import bridge, sys, os

def print_help():
    print(f"Usage: {sys.argv[0]} [folder_path]")
    print("If folder_path is not provided, will use current directory")
    sys.exit(0)

def process_folder(folder_path):
    songs = get_songs_in_folder(folder_path)
    for song in songs:
        track = bridge.get_song_info(song.meta.title, song.meta.artist, song.meta.album)
        print(f"Song info: {track}")
        bridge.replace_song(song, track)

def main():
    if len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']: print_help()
    
    folder_path = sys.argv[1] if len(sys.argv) == 2 else os.getcwd()
    process_folder(folder_path)


if __name__ == "__main__":
    main()