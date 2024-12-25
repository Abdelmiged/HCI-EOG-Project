import re

regex = "\d+"

def extract_signal_values(signal_text_path):
    signal_text = open(signal_text_path, 'r')
    signal_text = signal_text.readlines()
    signal_values = []
    for item in signal_text:
        signal_values.append(int(re.findall(regex, item)[0]))
    # print(signal_values)
    return signal_values