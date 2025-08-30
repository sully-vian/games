import mido
import numpy as np
import pygame
import sys

def midi_to_sounds(midi_filename, sample_rate=44100):
    """
    Convert a MIDI file into a list of pygame.mixer.Sound objects.
    Each note_on/note_off pair becomes one Sound.
    """
    # Initialize pygame mixer
    if not pygame.mixer.get_init():
        pygame.mixer.init(frequency=sample_rate, size=-16, channels=1)

    mid = mido.MidiFile(midi_filename)
    sounds = []

    current_time = 0
    note_start_times = {}

    for msg in mid:
        current_time += msg.time
        if msg.type == 'note_on' and msg.velocity > 0:
            # store note start time
            note_start_times[msg.note] = current_time
        elif msg.type in ('note_off', 'note_on') and msg.note in note_start_times:
            # calculate duration
            start_time = note_start_times.pop(msg.note)
            duration = current_time - start_time

            if duration > 0:
                # generate waveform for this note
                freq = 440.0 * (2 ** ((msg.note - 69) / 12.0))  # MIDI note -> Hz
                t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
                waveform = (0.5 * np.sin(2 * np.pi * freq * t)).astype(np.float32)

                # Convert to bytes for pygame
                sound = pygame.mixer.Sound(buffer=(waveform * 32767).astype(np.int16).tobytes())
                sounds.append(sound)

    return sounds

pygame.init()
sounds = midi_to_sounds(sys.argv[1])

# Play all sounds one after the other
for s in sounds:
    s.play()
    pygame.time.wait(int(s.get_length() * 1000))
