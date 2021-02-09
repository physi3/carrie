"""
Holds Porcupine class
"""

import struct
from threading import Thread

import pvporcupine
import pyaudio

class Porcupine(Thread):
    "Runs run_func on hearing keyword"

    def __init__(self, keyword, sensitivity, run_func, input_device_index = None):
        super().__init__()

        self.run_func = run_func
        self.keyword = keyword
        self.sensitivity = sensitivity
        self.input_device_index = input_device_index

    def run(self):
        porcupine = py_audio_instance = audio_stream = None
        try:
            porcupine = pvporcupine.create(
                keyword_paths = [pvporcupine.KEYWORD_PATHS[self.keyword]],
                sensitivities = [self.sensitivity])
            py_audio_instance = pyaudio.PyAudio()
            audio_stream = py_audio_instance.open(
                rate = porcupine.sample_rate,
                channels = 1,
                format = pyaudio.paInt16,
                input = True,
                frames_per_buffer = porcupine.frame_length,
                input_device_index = self.input_device_index)

            print("Listening.. ")

            while True:
                audio_frame = audio_stream.read(porcupine.frame_length)
                pcm = struct.unpack_from("h" * porcupine.frame_length, audio_frame)
                if porcupine.process(pcm) >= 0:
                    print("Detecting")
                    self.run_func()

        except KeyboardInterrupt:
            print("Stopping ...")

        finally:
            if porcupine is not None:
                porcupine.delete()
            if audio_stream is not None:
                audio_stream.close()
            if py_audio_instance is not None:
                py_audio_instance.terminate()
