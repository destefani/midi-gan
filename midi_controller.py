from pygame import midi
import numpy as np

midi.init()

# Start device
default_id = midi.get_default_input_id()
device = midi.get_device_info(default_id)

if device is not None:
    print(midi.get_device_info(default_id))
    midi_input = midi.Input(device_id=default_id)
else:
    print("No MIDI input device detected")
    exit()

# Get signal
try:
    while True:
        if midi_input.poll():
            print(midi_input.read(num_events=16))
except KeyboardInterrupt as e:
    print("\nExiting...")
    midi_input.close()
    exit()
