import glob
import extract_signals

def concatenate_folder_signals(folder_path, vertical_text=None, horizontal_text=None):
    if vertical_text and horizontal_text:
        concatenated_signal = []
        horizontal_signal_values = extract_signals.extract_signal_values(horizontal_text)
        vertical_signal_values = extract_signals.extract_signal_values(vertical_text)
        concatenated_signal.append(vertical_signal_values)
        concatenated_signal.append(horizontal_signal_values)
        return concatenated_signal

    concatenated_signal = []
    signals_paths = glob.glob(folder_path + "/*")
    for signal_path in signals_paths:
        signal_values = extract_signals.extract_signal_values(signal_path)
        concatenated_signal.append(signal_values)
    return concatenated_signal


def concatenate_signals(signals_list):
    signal = []
    for signal_list in signals_list:
        for signal_value in signal_list:
            signal.append(signal_value)
    return signal