import math

# def forward_selection():
#
# def backward_elimination():
#
# def nearest_neighbor():



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
    print(new_data)
    print("Type the number of the algorithm you want to run")
    algorithm_select = input("1) Forward Selection" + '\n'
                             "2) Backward Elimination" + '\n'
                             "3) Parth's Special Algorithm" + '\n')

    # The first column is the class, these values will always be either “1”s or “2”s.
    # The other columns contain the features, which are not normalized
    # 64 features, 2048 instances


main()
