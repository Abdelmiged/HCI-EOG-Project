import pickle
import concatenate_signals
from main import signals_testing, labels

blinkH = 'Dataset/Train/blink/kirp1h.txt'
blinkV = 'Dataset/Train/blink/kirp1v.txt'
upH = 'Dataset/Train/Up/yukari1h.txt'
upV = 'Dataset/Train/Up/yukari1v.txt'
downH = 'Dataset/Train/Down/asagi1h.txt'
downV = 'Dataset/Train/Down/asagi1v.txt'
leftH = 'Dataset/Train/Left/sol1h.txt'
leftV = 'Dataset/Train/Left/sol1v.txt'
rightH = 'Dataset/Train/Right/sag1h.txt'
rightV = 'Dataset/Train/Right/sag1v.txt'

def up():
    return concatenate_signals.concatenate_folder_signals('',
                                                                  upH,
                                                                  upV)

def down():
    return concatenate_signals.concatenate_folder_signals('',
                                                          downH,
                                                          downV)

def left():
    return concatenate_signals.concatenate_folder_signals('',
                                                                    leftH,
                                                                    leftV)

def right():
    return concatenate_signals.concatenate_folder_signals('',
                                                          rightH,
                                                          rightV)

def blink():
    return concatenate_signals.concatenate_folder_signals('',
                                                          blinkH,
                                                          blinkV)

def TestCase1():
    svm = pickle.load(open('classifier.sav', 'rb'))
    signals = []
    # 9
    signals.extend(down())
    signals.extend(left())
    signals.extend(blink())
    # +
    signals.extend(up())
    signals.extend(up())
    signals.extend(blink())
    # 4
    signals.extend(right())
    signals.extend(blink())
    dirs = signals_testing(svm, signals, labels)
    return dirs