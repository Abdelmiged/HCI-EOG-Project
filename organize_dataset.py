import glob
import shutil

dataset = glob.glob("./3-class/*")

test_signals_count = [8, 8, 8, 8, 8]

dest_path = "./Dataset"

def organize_dataset():
    for signal_text in dataset:
        if signal_text.find("yukari") != -1:
            shutil.move(signal_text, dest_path + "/Up")
        elif signal_text.find("asagi") != -1:
            shutil.move(signal_text, dest_path + "/Down")
        elif signal_text.find("sag") != -1:
            shutil.move(signal_text, dest_path + "/right")
        elif signal_text.find("sol") != -1:
            shutil.move(signal_text, dest_path + "/left")
        elif signal_text.find("kirp") != -1:
            shutil.move(signal_text, dest_path + "/blink")
