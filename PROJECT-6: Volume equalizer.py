"""
make a Python program that will take any kind of format of video file from the user(there should be an option where after running the program, it will ask the user to input a directory name of a video
file) and creates a duplicate file where it'll balance its sound to an average disiable where if the sound of a particular part of the video is low it'll raise the sound level and also if the sound is
high from the average level it'll pitch it down. the should be able to set the average level of sound and if he doesn't, there will also be a default value. You need to install moviepy for this from command 
prompt to run this program.
"""
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
