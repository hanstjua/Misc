import simpleaudio as sa
import numpy as np
import math
import matplotlib.pyplot as plt

#### generate audio data

sample_rate = 44100
T = 1.25

# sound envelope: env_<comp> = (<duration> , <amplitude>)
env_a = (0.05, 1.0)
env_d = (0.1, 0.15)
env_s = (0.1, env_d[1])
env_r = (round(T - env_a[0] - env_d[0] - env_s[0], 2), 0)

adsr_t = [env_a[0], env_d[0], env_s[0], env_r[0]]
adsr_a = [env_a[1], env_d[1], env_s[1], env_r[1]]

adsr = [
    np.linspace(0, adsr_a[0], adsr_t[0] * sample_rate, False),
    np.linspace(adsr_a[0], adsr_a[1], adsr_t[1] * sample_rate, False),
    np.linspace(adsr_a[1], adsr_a[2], adsr_t[2] * sample_rate, False),
    np.linspace(adsr_a[2], adsr_a[3], adsr_t[3] * sample_rate, False)
]

adsr = np.hstack(adsr)

a_freq = 440

t = np.linspace(0, T, T * sample_rate, False)

a_notes = np.sin(2 * np.pi * a_freq*0.5 * t) * 0.170
a_notes += np.cos(2 * np.pi * a_freq*1 * t) * 0.985
a_notes += np.sin(2 * np.pi * a_freq*1.5 * t) * 0.185
a_notes += np.sin(2 * np.pi * a_freq*2 * t) * 0.110
a_notes += np.cos(2 * np.pi * a_freq*2.5 * t) * 0.260
a_notes += np.sin(2 * np.pi * a_freq*3 * t) * 0.095
a_notes += np.sin(2 * np.pi * a_freq*3.5 * t) * 0.080

plt.plot(a_notes[:400])

plt.show()

audio  = 2**15 / np.max(abs(a_notes)) * (a_notes * adsr)

plt.plot(audio)

# plt.show()

audio = np.hstack([audio,audio,audio])
audio  = audio.astype(np.int16)

# play the sound

playback = sa.play_buffer(audio, 1, 2, sample_rate)

playback.wait_done()
