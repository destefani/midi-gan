from pygame import midi
import numpy as np


def normalize(input):
    pass


def main():
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
                message = midi_input.read(num_events=16)[0][0][2]
                # print(midi_input.read(num_events=16)[0][0][2]) # [[[status, data1, data2, data3], timestamp], ...]
                z = message / 127
                print(z)

    except KeyboardInterrupt as e:
        print("\nExiting...")
        midi_input.close()
        exit()


if __name__ == "__main__":
    main()
