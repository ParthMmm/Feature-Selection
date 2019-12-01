import math
from random import random
from copy import deepcopy

def forward_selection(data_set,num_features,num_lines):

    current_set_of_features = []
    best_so_far_accuracy = 0
    copy_feature_set = []
    for i in range(num_features):
        feature_to_add_at_this_level = -1

        print("On level " + str(i) + " of search tree")
        for k in range(1, num_features + 1):
            if (k not in current_set_of_features):
                print("--Considering adding the ", k, " feature")
                copy_feature_set = deepcopy(current_set_of_features)
                if k >= 0:
                    copy_feature_set.append(k)
                accuracy = one_out_cross_validation(data_set, num_features, num_lines, copy_feature_set )
                #accuracy = rand_one_out()

                print("Using features ", copy_feature_set, " accuracy ", accuracy)
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy;
                    feature_to_add_at_this_level = k


        if feature_to_add_at_this_level >= 0:
            current_set_of_features.append(feature_to_add_at_this_level)
            print("On level ", i, " I added feature ",feature_to_add_at_this_level," to current set" )
        else:
            print("Accuracy decrease")
            break;

    print("Best set of features to use: ", current_set_of_features, " accuracy " , best_so_far_accuracy)
#
# def backward_elimination():
#
def nearest_neighbor(data_set, num_features, num_lines, copy_feature_set, one_out):

    #power(p1 -p2, 2)
    nn_dist = float('inf')
    nn = -1
    dist = 0


    for i in range(num_lines):
        if one_out == i:
            pass
        else:
            x = 0
            for j in range(len(copy_feature_set)):
                x += pow(data_set[i][copy_feature_set[j]] - data_set[one_out][copy_feature_set[j]],2)
            dist = math.sqrt(x)

            if dist < nn_dist:
                nn_dist = dist
                nn = i

    return nn

def rand_one_out():
    return random()

def one_out_cross_validation(data_set, num_features, num_lines, copy_feature_set):
    x = 0
    num_correct = 0
    for i in range(num_lines):
        x = i

        nn = nearest_neighbor(data_set, num_features, num_lines, copy_feature_set, x)

        if data_set[x][0] == data_set[nn][0]:
            num_correct += 1

    accuracy = (num_correct / num_lines) * 100
    return accuracy

#x = ((X-mean(x))/std(x))

def get_mean(data_set,num_features,num_lines):

    mean = []

    #get mean of each row into a list so mean[1] is mean of first line
    for i in range(1, num_features + 1):
            x = (sum(line[i] for line in data_set) / num_lines)
            mean.append(x)


    return mean

def get_std_dev(data_set, num_features, num_lines,mean):

    std_dev = []

    for i in range(1, num_features + 1): #mean[i-1] because num_features + 1
            x = (sum(pow((line[i] - mean[i-1]),2) for line in data_set )/ num_lines)
            std_dev.append(math.sqrt(x))

    return std_dev

def normalize(data, num_features, num_lines):

    #data = x-mean(x) / std(x)
    norm_data = []

    mean = get_mean(data, num_features, num_lines)
    std_dev = get_std_dev(data, num_features, num_lines, mean)


    for i in range(0, num_lines):
        for j in range(1, num_features + 1):
            data[i][j] = ((data[i][j] - mean[j-1]) / std_dev[j-1])

    return data


def custom_search(data_set, num_features, num_lines):



def main():
    print("Welcome to Parth Mangrola's Feature Selection Algorithm" + '\n')
    file_name = input("Type in the name of the file to test: ")



    data = open(file_name, "r")



    line = data.readline()
    num_features = len(line.split()) - 1 #num of features in a line
    print(num_features)

    data.seek(0,0)
    num_lines = len(data.readlines(  )) #num of lines/instancses
    print(num_lines)



    data.seek(0,0)
    data_set = [[] for i in range(num_lines)]


    for i in range(num_lines):
        data_set[i] = [float(j) for j in data.readline().split()]


    new_data = normalize(data_set,num_features,num_lines)
    #print(new_data)
    print("Type the number of the algorithm you want to run")
    algorithm_select = input("1) Forward Selection" + '\n'
                             "2) Backward Elimination" + '\n'
                             "3) Parth's Special Algorithm" + '\n')
    if algorithm_select == '1':
        forward_selection(new_data, num_features, num_lines)
    if algorithm_select == '2':
        pass
    if algorithm_select == '3':
        custom_search(new_data,num_features, num_lines)


    # The first column is the class, these values will always be either “1”s or “2”s.
    # The other columns contain the features, which are not normalized
    # 64 features, 2048 instances


main()
