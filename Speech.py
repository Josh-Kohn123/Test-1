import os
from pyAudioAnalysis import audioSegmentation
import wave

##Teacher Speaking Time
def get_speaker_duration(audio_file, speaker_name):
    # Load audio file
    audio = wave.open(audio_file, "rb")

    # Extract speaker segments
    speaker_segments = audioSegmentation.speaker_diarization(audio_file,0)

    # Calculate duration for the predefined speaker
    predefined_speaker_duration = sum(seg[1] - seg[0] for seg, speaker in zip(speaker_segments, speaker_segments[1:]) if speaker == speaker_name)

    # Calculate total duration
    total_duration = audio.getnframes() / float(audio.getframerate())

    # Close audio file
    audio.close()

    return predefined_speaker_duration, total_duration - predefined_speaker_duration

# Example usage
audio_file_path = "/Users/joshuakohn/Documents/GitHub/Test-1/Sample3.wav"  # Replace with your audio file path
predefined_speaker = "Predefined Speaker"  # Replace with the name of the predefined speaker
predefined_duration, other_duration = get_speaker_duration(audio_file_path, predefined_speaker)

print(f"Duration of {predefined_speaker}: {predefined_duration} seconds")
print(f"Duration of other speakers: {other_duration} seconds")
