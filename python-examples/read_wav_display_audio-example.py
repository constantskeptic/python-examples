# read and display wav audio file example
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# globals
fullfilepath = '/Users/mbpjc/projects/digiclean2/noise-files/naylor_noisy.wav'
resultpath = '/Users/mbpjc/projects/digiclean2/output/'
# read audio samples
input_data = read("/Users.wav")
audio = input_data[1]

plt.plot(audio)

# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title
plt.title("Sample Wav")
# display the plot
plt.show()
