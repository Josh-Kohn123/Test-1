import speech_recognition as sr 
import re
import os #Can remove if not working with OS

# Function to calculate average sentence length
def calculate_avg_sentence_length(text):
    # Split text into sentences using regular expression
    sentences = re.split(r'[.!?]', text)
    # Remove empty sentences
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    # Calculate total number of words and number of sentences
    total_words = sum(len(sentence.split()) for sentence in sentences)
    total_sentences = len(sentences)
    # Calculate average sentence length
    if total_sentences > 0:
        avg_sentence_length = total_words / total_sentences
    else:
        avg_sentence_length = 0
    return avg_sentence_length

# Function to transcribe audio using Google Speech Recognition
def transcribe_audio(audio_file):
    #import speech_recognition as sr 
    recognizer = sr.Recognizer()    
    with sr.WavFile(audio_file) as source:
        audio_data = recognizer.record(source)#, duration = 30, offset= 0)
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

#Example usage
if __name__ == "__main__":
    audio_file_path = "/Users/joshuakohn/Documents/GitHub/Test-1/Sample3.wav"  ##Insert Audio File Path as .wav
    transcribed_text = transcribe_audio(audio_file_path)
    print(transcribed_text)
    if transcribed_text:
        avg_sentence_length = calculate_avg_sentence_length(transcribed_text)
        print(f"Average sentence length: {avg_sentence_length} words per sentence")