import moviepy.editor as mp
import os
from moviepy.audio.io.AudioFileClip import AudioFileClip

def normalize_audio(input_file, output_file, target_dBFS=-20):
    audio_clip = AudioFileClip(input_file)
    audio_normalized = audio_clip.fx(mp.audio.fx.all.normalize_audio, target_dBFS=target_dBFS)
    audio_normalized.write_audiofile(output_file)


def main():
    input_file = input("Enter the path of the video file: ")
    target_dBFS_str = input("Enter the target loudness in dBFS (default is -20): ")
    target_dBFS = float(target_dBFS_str) if target_dBFS_str else -20
    input_dir, filename = os.path.split(input_file)
    output_file = os.path.join(input_dir, "normalized_" + filename)
    if filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mov") or filename.endswith(".mkv"):
        normalize_audio(input_file, output_file, target_dBFS=target_dBFS)

if __name__ == "__main__":
    main()
#for this code to work, you have to install 'moviepy' from the command prompt
