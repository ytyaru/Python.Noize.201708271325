import pathlib
import Wave.Player
import Wave.Sampler
import Wave.WaveFile
import Wave.noise_generator
import Wave.NoiseMaker


hz = 44100
second = 5

p = Wave.Player.Player()
p.Open(rate=hz)

wf = Wave.WaveFile.WaveFile()
wf.BasePath = pathlib.PurePath(f'../res/noize/')
#nm = Wave.NoiseMaker.NoiseMaker()
for color in Wave.NoiseMaker.NoiseMaker._noise_colors:
#for color in nm._noise_generators.keys():
    print(color)
#    wav = Wave.Sampler.Sampler().Sampling(nm.Get(N=hz, color=color, state=None, a=1, sec=second))
    wav = Wave.Sampler.Sampler().Sampling(Wave.NoiseMaker.NoiseMaker.Get(N=hz, color=color, state=None, a=1, sec=second))
    p.Play(wav, rate=hz)
    wf.Write(wav, fs=hz, filename=color)

p.Close()

