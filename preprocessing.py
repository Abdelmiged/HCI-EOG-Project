from scipy import signal
from scipy.signal import butter,filtfilt
import statistics

def butter_bandpass_filter(input_signals,low_cut_off=1,high_cut_off=30,sampling_rate=176,order=2):
    nyq_rate = 0.5 * sampling_rate
    f_low=low_cut_off/nyq_rate
    f_high=high_cut_off/nyq_rate
    filtered = []
    for signal in input_signals:
        Numerator,denominator = butter(order, [f_low,f_high], btype='band', output='ba', analog=False, fs=None)
        filtered.append(filtfilt(Numerator,denominator,signal))
    return filtered

def resampling(Signals, SamplingRate=50):
    resampled_signals = []
    for Signal in Signals:
        resampled_signals.append(signal.resample(Signal,SamplingRate))
    return resampled_signals

def DC_component(Signals,Mode):
    DC_Signals = []
    for Signal in Signals:
        Mean = statistics.mean(Signal)
        Mean = Mean * Mode
        DC_Signals.append([(Signal[i] + Mean) for i in range (len(Signal))])
    return DC_Signals

def concatenate_h_v(signal):
    final_signal = []
    for i in range(0, len(signal), 2):
        final_signal.append(signal[i] + signal[i + 1])
    return final_signal