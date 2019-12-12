import math
import time
from copy import deepcopy


def forward_selection(data_set, num_features, num_lines):
    print("Beginning search")
    current_set_of_features = []
    best_so_far_accuracy = 0
    copy_feature_set = []
    for i in range(num_features):
        feature_to_add_at_this_level = -1

        print("On level " + str(i) + " of search tree")
        for k in range(1, num_features + 1):
            if (k not in current_set_of_features):
                copy_feature_set = deepcopy(current_set_of_features)
                if k >= 0:
                    copy_feature_set.append(k)
                accuracy = one_out_cross_validation(
                    data_set, num_features, num_lines, copy_feature_set)

                print("     Using feature(s):", copy_feature_set,
                      "accuracy is", str(round(accuracy, 2)), "%")
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = k

        if feature_to_add_at_this_level >= 0:
            current_set_of_features.append(feature_to_add_at_this_level)
            print("Feature set", feature_to_add_at_this_level,
                  "was best, accuracy is", str(round(best_so_far_accuracy, 2)), "%")

        else:
            print(
                "(Warning, Accuracy has decreased!")
            break

    print("Finished! Best set of features to use:", current_set_of_features,
          "with accuracy of", str(round(best_so_far_accuracy, 2)), "%")


def custom_forward_selection(data_set, num_features, num_lines):
    print("Beginning search")
    current_set_of_features = []
    best_so_far_accuracy = 0
    copy_feature_set = []
    num_mistakes = 0
    num_wrong = 0
    for i in range(num_features):
        feature_to_add_at_this_level = -1

        print("On level " + str(i) + " of search tree")
        for k in range(1, num_features + 1):
            if (k not in current_set_of_features):
                copy_feature_set = deepcopy(current_set_of_features)
                if k >= 0:
                    copy_feature_set.append(k)
                accuracy, num_wrong = custom_one_out_cross_validation(
                    data_set, num_features, num_lines, copy_feature_set, best_so_far_accuracy, num_mistakes)

                print("     Using feature(s):", copy_feature_set,
                      "accuracy is", str(round(accuracy, 2)), "%")

                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = k
                    num_mistakes = num_wrong

        if feature_to_add_at_this_level >= 0:
            current_set_of_features.append(feature_to_add_at_this_level)
            print("Feature set", feature_to_add_at_this_level,
                  "was best, accuracy is", str(round(best_so_far_accuracy, 2)), "%")

        else:
            print(
                "(Warning, Accuracy has decreased!")
            break

    print("Finished! Best set of features to use:", current_set_of_features,
          "with accuracy of", str(round(best_so_far_accuracy, 2)), "%")


def custom_one_out_cross_validation(data_set, num_features, num_lines, copy_feature_set, best_so_far, mistakes):
    x = 0
    num_correct = 0
    num_wrong = 0
    for i in range(num_lines):
        x = i

        nn = nearest_neighbor(data_set, num_features,
                              num_lines, copy_feature_set, x)

        if data_set[x][0] == data_set[nn][0]:
            num_correct += 1
        else:
            num_wrong += 1
        if mistakes != 0:
            if num_wrong > mistakes:
                return 0, 0
                break

    accuracy = (num_correct / num_lines) * 100
    return accuracy, num_wrong


def backward_elimination(data_set, num_features, num_lines, acc):
    print("Beginning search")

    current_set_of_features = []
    best_so_far_accuracy = acc
    copy_feature_set = []

    for elem in range(1, num_features + 1):
        current_set_of_features.append(elem)

    for i in range(num_features):
        feature_to_add_at_this_level = -1

        print("On level " + str(i) + " of search tree")
        for k in range(1, num_features + 1):
            if (k in current_set_of_features):
                copy_feature_set = deepcopy(current_set_of_features)
                if k >= 0:
                    copy_feature_set.remove(k)
                accuracy = one_out_cross_validation(
                    data_set, num_features, num_lines, copy_feature_set)

                print("     Using feature(s):", copy_feature_set,
                      "accuracy is", str(round(accuracy, 2)), "%")
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = k

        if feature_to_add_at_this_level >= 0:
            current_set_of_features.remove(feature_to_add_at_this_level)
            print("Feature set", feature_to_add_at_this_level,
                  "was best, accuracy is", str(round(best_so_far_accuracy, 2)), "%")

        else:
            print(
                "(Warning, Accuracy has decreased!")
            break

    print("Finished! Best set of features to use:", current_set_of_features,
          "with accuracy of", str(round(best_so_far_accuracy, 2)), "%")


def nearest_neighbor(data_set, num_features, num_lines, copy_feature_set, one_out):

    #power(p1 -p2, 2)
    nn_dist_best_so_far = float('inf')
    nn_best_so_far_loc = -1
    dist = 0

    for i in range(num_lines):
        if one_out == i:
            pass
        else:
            x = 0
            for j in range(len(copy_feature_set)):
                x += pow(data_set[i][copy_feature_set[j]] -
                         data_set[one_out][copy_feature_set[j]], 2)
            dist = math.sqrt(x)

            if dist < nn_dist_best_so_far:
                nn_dist_best_so_far = dist
                nn_best_so_far_loc = i

    return nn_best_so_far_loc


def one_out_cross_validation(data_set, num_features, num_lines, copy_feature_set):
    x = 0
    num_correct = 0
    for i in range(num_lines):
        x = i

        nn = nearest_neighbor(data_set, num_features,
                              num_lines, copy_feature_set, x)

        if data_set[x][0] == data_set[nn][0]:
            num_correct += 1

    accuracy = (num_correct / num_lines) * 100
    return accuracy

#x = ((X-mean(x))/std(x))


def get_mean(data_set, num_features, num_lines):

    mean = []

    # get mean of each row into a list so mean[1] is mean of first line
    for i in range(1, num_features + 1):
        x = (sum(line[i] for line in data_set) / num_lines)
        mean.append(x)

    return mean


def get_std_dev(data_set, num_features, num_lines, mean):

    std_dev = []

    for i in range(1, num_features + 1):  # mean[i-1] because num_features + 1
        x = (sum(pow((line[i] - mean[i - 1]), 2)
                 for line in data_set) / num_lines)
        std_dev.append(math.sqrt(x))

    return std_dev


def normalize(data, num_features, num_lines):

    #data = x-mean(x) / std(x)
    norm_data = []

    mean = get_mean(data, num_features, num_lines)
    std_dev = get_std_dev(data, num_features, num_lines, mean)

    for i in range(0, num_lines):
        for j in range(1, num_features + 1):
            data[i][j] = ((data[i][j] - mean[j - 1]) / std_dev[j - 1])

    return data


def main():
    print("Welcome to Parth Mangrola's Feature Selection Algorithm" + '\n')
    file_name = input("Type in the name of the file to test: ")

    data = open(file_name, "r")

    line = data.readline()
    num_features = len(line.split()) - 1  # num of features in a line

    data.seek(0, 0)
    num_lines = len(data.readlines())  # num of lines/instancses

    data.seek(0, 0)
    data_set = [[] for i in range(num_lines)]

    print("This dataset has", num_features,
          "features (not including class attribute), with", num_lines, "instances." + "\n")

    for i in range(num_lines):
        data_set[i] = [float(j) for j in data.readline().split()]

    print("Normalizing data . . ." + "\n")

    new_data = normalize(data_set, num_features, num_lines)
    copy_feature_set = []
    for elem in range(1, num_features + 1):
        copy_feature_set.append(elem)

    acc = one_out_cross_validation(
        data_set, num_features, num_lines, copy_feature_set)
    print("Running nearest neighbor with all", num_features,
          "features, using \"leaving-one-out\" evaluation, I get an accuracy of", str(round(acc, 2)), "%" + "\n")
    print("Type the number of the algorithm you want to run")
    algorithm_select = input("1) Forward Selection" + '\n'
                             "2) Backward Elimination" + '\n'
                             "3) Parth's Special Algorithm" + '\n')

    if algorithm_select == '1':
        start = time.time()
        forward_selection(new_data, num_features, num_lines)
        end = time.time()
    if algorithm_select == '2':
        start = time.time()
        backward_elimination(new_data, num_features, num_lines, acc)
        end = time.time()
    if algorithm_select == '3':
        start = time.time()
        custom_forward_selection(new_data, num_features, num_lines)
        end = time.time()
    print("Time elapsed: ", end - start)

    # The first column is the class, these values will always be either “1”s or “2”s.
    # The other columns contain the features, which are not normalized
    # 64 features, 2048 instances


main()
