import os
import sys


def generate_playlist_m3u(directory):
    try:
        files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    except FileNotFoundError:
        print(f"The directory '{directory}' was not found.")
        return
    except PermissionError:
        print(f"You don't have permissions to access the directory '{directory}'.")
        return

    video_files = [file for file in files if file.lower().endswith((".mp4", ".mkv", ".avi", ".mov"))]

    playlist_path = os.path.join(directory, 'playlist.m3u')
    with open(playlist_path, 'w') as playlist_file:
        for file in video_files:
            playlist_file.write(file + '\n')

    print(f"Playlist generated successfully: {playlist_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_playlist.py /path/to/directory")
    else:
        target_directory = sys.argv[1]
        generate_playlist_m3u(target_directory)
