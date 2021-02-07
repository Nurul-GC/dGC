"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys


def reprodutor():
    print("""
    [*] REPRODUZINDO UM ARQUIVO DE AUDIO (.wav) [*]
-------------------------------------------------------
""")
    CHUNK = 1024

    wf = wave.open("sound/Franco.wav", 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


if __name__ == '__main__':
    reprodutor()
