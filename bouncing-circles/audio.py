import pygame
import numpy as np
import config
from typing import List
import mido
import sys


class AudioManager:
    def __init__(self, melodyFile: str) -> None:
        self.melodyFile: str = melodyFile
        pygame.mixer.init()
        self.melodySounds: List[pygame.mixer.Sound] = []
        self.currentNoteIndex: int = 0
        self.loadMidiMelody()
        self.generateMelodySounds()

    def generateMelodySounds(self) -> None:
        for midiNote in self.midiNotes:
            frequency: float = self.midiToFreq(midiNote)
            t: np.ndarray = np.linspace(
                0, config.NOTE_DURATION, int(config.SAMPLE_RATE * config.NOTE_DURATION), False)

            # Use a more musical waveform (sine wave with harmonics)
            wave: np.ndarray = (np.sin(2 * np.pi * frequency * t) +
                                0.3 * np.sin(4 * np.pi * frequency * t) +
                                0.1 * np.sin(6 * np.pi * frequency * t))

            # Better envelope (ADSR-like)
            attack_samples = int(0.05 * config.SAMPLE_RATE)  # 50ms attack
            decay_samples = int(0.1 * config.SAMPLE_RATE)    # 100ms decay
            total_samples = len(wave)

            envelope = np.ones(total_samples)
            # Attack phase
            if attack_samples > 0:
                envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
            # Decay phase
            if decay_samples > 0 and attack_samples + decay_samples < total_samples:
                envelope[attack_samples:attack_samples +
                         decay_samples] = np.linspace(1, 0.7, decay_samples)
            # Release phase (last 30% of note)
            release_start = int(0.7 * total_samples)
            envelope[release_start:] = np.linspace(
                0.7, 0, total_samples - release_start)

            wave *= envelope
            # Reduced volume and clipping
            wave = np.clip(wave * 16383, -32767, 32767).astype(np.int16)
            stereoWave: np.ndarray = np.column_stack((wave, wave))
            sound: pygame.mixer.Sound = pygame.sndarray.make_sound(stereoWave)
            self.melodySounds.append(sound)

    def loadMidiMelody(self) -> None:
        try:
            mid: mido.MidiFile = mido.MidiFile(self.melodyFile)
            self.midiNotes: List[int] = []

            print(f"MIDI file info: {len(mid.tracks)} tracks")

            # Process all tracks and collect notes with timing
            notes_with_time = []
            current_time = 0

            for i, track in enumerate(mid.tracks):
                print(f"Track {i}: {len(track)} messages")
                track_time = 0

                for msg in track:
                    track_time += msg.time

                    if msg.type == 'note_on' and msg.velocity > 0:
                        notes_with_time.append((track_time, msg.note))
                        print(f"Note: {msg.note} (time: {track_time})")
                    elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                        # You might want to handle note_off events if needed
                        pass

            # Sort by time and extract just the notes
            notes_with_time.sort(key=lambda x: x[0])
            self.midiNotes = [note for time, note in notes_with_time]

            # Remove consecutive duplicates (but keep non-consecutive repeats)
            if self.midiNotes:
                filtered_notes = [self.midiNotes[0]]
                for note in self.midiNotes[1:]:
                    if note != filtered_notes[-1]:
                        filtered_notes.append(note)
                self.midiNotes = filtered_notes

            print(f"Final melody: {self.midiNotes}")

        except Exception as e:
            print(f"Error loading MIDI: {e}")
            self.midiNotes = config.MELODY_NOTES

    def getNextSound(self) -> pygame.mixer.Sound:
        if not self.melodySounds:
            return None
        sound = self.melodySounds[self.currentNoteIndex]
        self.currentNoteIndex = (
            self.currentNoteIndex + 1) % len(self.melodySounds)
        return sound

    def midiToFreq(self, midiNote: int) -> float:
        return 440.0 * (2.0 ** ((midiNote - 69) / 12.0))


def main():
    if len(sys.argv) != 2:
        print("Usage: python audio.py <midi_file>")
        sys.exit(1)

    audioManager = AudioManager(sys.argv[1])
    print(f"Playing {len(audioManager.midiNotes)} notes...")

    for i, note in enumerate(audioManager.midiNotes):
        print(
            f"Playing note {i+1}/{len(audioManager.midiNotes)}: MIDI {note} ({audioManager.midiToFreq(note):.1f} Hz)")
        sound = audioManager.getNextSound()
        if sound:
            sound.play()
            # Convert to milliseconds
            pygame.time.delay(int(config.NOTE_DURATION * 1000))
        else:
            print("No sound generated")


if __name__ == "__main__":
    main()
