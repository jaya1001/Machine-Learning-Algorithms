import random
import math
from csv import reader


# Load a CSV File
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row: continue
            dataset.append(row)
    return dataset


def str_column_to_flt(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())


dataset = load_csv("iris_dataset")



window_size = 5
train_ratio = 0.8
test_ratio = 0.2
features = 3

mu = random.uniform(0,1)


def inputs(i):

    mean = 0
    variance = 0
    actual = 0
    pattern = list()
    for j in range(i, i + window_size):
        mean += dataset[j]
        actual = dataset[j]

    mean = mean / window_size

    for j in range(i, i + window_size):
        variance += (dataset[j] - mean) * (dataset[j] - mean)

    variance = variance / window_size

    pattern.append(actual)
    pattern.append(mean)
    pattern.append(variance)

    return pattern



def LSM():
    iterate = len(dataset)-window_size+1
    train_len = int(train_ratio*iterate)
    test_len = int(test_ratio*iterate)
    count = 0
    error_list = list()
    weights = [0]*features
    error = -1
    while True:
        for i in range(0, train_len):
            pattern = inputs(i)

            predicted_value = 0
            for k in range(0, features):
                predicted_value += weights[k]*pattern[k]

            actual_output = dataset[i+window_size+1]

            error = predicted_value - actual_output
            error_list.append(error)

            for i in range(0, features):
                weights[i] = weights[i]+2*mu*pattern[i]*error
            count += 1
        if len(error_list)>1 and error_list[len(error_list)-2] == error or count == 100:
            break

    output_error = list()

    for i in range(train_len+1, len(dataset)):
        patterns = inputs(i)

        predicted_value = 0
        for k in range(0, features):
            predicted_value += weights[k] * patterns[k]

        actual_output = dataset[i + window_size + 1]

        error = predicted_value - actual_output
        output_error.append(error)

    mean_error = 0
    for i in range(0, len(output_error)):
        mean_error += output_error[i]

    mean_error = mean_error/len(error_list)
    return mean_error




def lsmExpansion():




def lsmBatchProcess():
    iterate = len(dataset) - window_size + 1
    train_len = int(train_ratio * iterate)
    test_len = int(test_ratio * iterate)
    count = 0
    error_list = list()
    final_weights = [0] * features
    weights = [0] * features
    error = -1

    while True:

        for i in range(0, train_len):
            pattern = inputs(i)

            predicted_value = 0
            for k in range(0, features):
                predicted_value += weights[k] * pattern[k]

            actual_output = dataset[i + window_size + 1]

            error = predicted_value - actual_output
            error_list.append(error)

            for p in range(0, features):
                x = weights[p]
                weights[p] = weights[p] + 2 * mu * pattern[p] * error
                final_weights[p] += x-weights[p]

            count += 1
        if len(error_list) > 1 and error_list[len(error_list) - 2] == error or count == 100:
            break


    output_error = list()

    for j in range(0, features):
        final_weights[j] = final_weights[j]/train_len

    for i in range(train_len + 1, len(dataset)):
        patterns = inputs(i)

        predicted_value = 0
        for k in range(0, features):
            predicted_value += final_weights[k] * patterns[k]

        actual_output = dataset[i + window_size + 1]

        error = predicted_value - actual_output
        output_error.append(error)

    mean_error = 0
    for i in range(0, len(output_error)):
        mean_error += output_error[i]

    mean_error = mean_error / len(error_list)
    return mean_error


