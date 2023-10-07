from pydub import AudioSegment, playback
import numpy as np

def change_pitch(sound, semitones):
    semitone_ratio = 2 ** (semitones / 12.0)
    
    # Pitch shift using interpolation
    samples = np.array(sound.get_array_of_samples())
    pitch_shifted_samples = np.interp(
        np.arange(0, len(samples), semitone_ratio),
        np.arange(0, len(samples)), samples).astype(np.int16)
    
    # Create a new sound with the same parameters
    new_sound = AudioSegment(
        pitch_shifted_samples.tobytes(),
        frame_rate=sound.frame_rate,
        sample_width=sound.sample_width,
        channels=sound.channels
    )
    
    return new_sound

def main():
    # Load the audio file
    audio_file = "C:/Users/Gerric Villanueva/Documents/Voice_test/Gerric/Gerric_add.wav"
    sound = AudioSegment.from_file(audio_file)

    # Parameters for pitch adjustment (adjust as needed)
    semitones_shift = -1  # Adjusted for making the pitch higher (like a kid's voice)

    # Apply pitch shift
    high_pitch_sound = change_pitch(sound, semitones_shift)
    
    # Play the modified sound with the same speed
    #playback.play(high_pitch_sound)

    # Export the modified sound to a new file
    output_file = "C:/Users/Gerric Villanueva/Documents/Voice_test/Gerric/Add.wav"
    high_pitch_sound.export(output_file, format="wav")

if __name__ == "__main__":
    main()
