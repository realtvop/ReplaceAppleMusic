import bridge, sys, os, file_reader

def print_help():
    print("ReplaceAppleMusic")
    print(f"Usage: ramusic [path]")
    print("path can be either a folder or a file")
    sys.exit(0)

def process_folder(folder_path, folder=True):
    songs = file_reader.get_songs_in_folder(os.path.abspath(folder_path)) if folder else [ file_reader.process_file(os.path.abspath(folder_path)) ]
    for song in songs:
        track = bridge.get_song_info(song.meta.title, song.meta.artist, song.meta.album)
        print(f"Song info: {track}")
        bridge.replace_song(song, track)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']: print_help()
    
    path = sys.argv[1] if len(sys.argv) == 2 else os.getcwd()
    process_folder(path, folder=os.path.isdir(path))


if __name__ == "__main__":
    main()