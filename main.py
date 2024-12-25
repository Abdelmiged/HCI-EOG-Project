import matplotlib.pyplot as plt
import concatenate_signals
import preprocessing
import feature_extraction
import models
import pickle
from sklearn.model_selection import cross_val_score
# organize_dataset.organize_dataset()


labels = {
    0: 'up',
    1: 'down',
    2: 'left',
    3: 'right',
    4: 'blink'
}
def signals_testing(model, signal, labels):
    final_signal = preprocessing.concatenate_h_v(signal)
    bandpass_signal = preprocessing.butter_bandpass_filter(final_signal, low_cut_off=1, high_cut_off=30,
                                                                sampling_rate=176, order=2)
    resampled_signal = preprocessing.resampling(bandpass_signal, 50)
    features_test = feature_extraction.wavelet_features(resampled_signal, wavelet='db1', level=2)
    # if y_data is not None:
        # print(model.score(signal, y_data))
    return [labels[x] for x in model.predict(features_test)]

if __name__ == '__main__':

    up_signal = concatenate_signals.concatenate_folder_signals("Dataset/Train/up")
    down_signal = concatenate_signals.concatenate_folder_signals("Dataset/Train/down")
    left_signal = concatenate_signals.concatenate_folder_signals("Dataset/Train/left")
    right_signal = concatenate_signals.concatenate_folder_signals("Dataset/Train/right")
    blink_signal = concatenate_signals.concatenate_folder_signals("Dataset/Train/blink")

    fig = plt.figure()
    final_signal = concatenate_signals.concatenate_signals([up_signal, down_signal, left_signal, right_signal, blink_signal])
    fig.add_subplot()
    plt.plot([i for i in range(0, len(final_signal))], final_signal)
    plt.show()

    # Preprocessing
    signal = preprocessing.concatenate_h_v(final_signal)
    with open('preprocessing.txt', 'w') as file:
        for i in signal:
            file.write('%s\n' % i)
    fig.add_subplot()
    plt.plot([i for i in range(0, len(signal))], signal)
    plt.show()

    bandpass_signal = preprocessing.butter_bandpass_filter(signal)
    with open('butter_bandpass.txt', 'w') as file:
        for i in signal:
            file.write('%s\n' % i)
    fig.add_subplot()
    plt.plot([i for i in range(0, len(bandpass_signal))], bandpass_signal)
    plt.show()

    resampled_signal = preprocessing.resampling(bandpass_signal)
    with open('resampling.txt', 'w') as file:
        for i in signal:
            file.write('%s\n' % i)
    fig.add_subplot()
    plt.plot([i for i in range(0, len(resampled_signal))], resampled_signal)
    plt.show()

    # Feature Extraction
    features1 = feature_extraction.wavelet_features(resampled_signal)
    features2 = feature_extraction.raw_sample_features(resampled_signal)
    with open('features1.txt', 'w') as file:
        for i in signal:
            file.write('%s\n' % i)
    with open('features2.txt', 'w') as file:
        for i in signal:
            file.write('%s\n' % i)

    class_labels2 = models.get_labels(features2)
    class_labels1 = models.get_labels(features1)

    classifier1 = models.train_svm_model(features1, class_labels1)
    classifier2 = models.train_svm_model(features2, class_labels2)

    filename = 'classifier.sav'
    pickle.dump(classifier1, open(filename, 'wb'))


    print([labels[x] for x in classifier1.predict(features1)])
    print([labels[x] for x in classifier2.predict(features2)])

    print(classifier1.score(features1, class_labels1))
    print(classifier2.score(features2, class_labels2))

