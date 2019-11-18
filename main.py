
# def forward_selection():
#
# def backward_elimination():
#
# def nearest_neighbor():


def main():
    print("Welcome to Parth Mangrola's Feature Selection Algorithm"+ '\n')
    file_name = input("Type in the name of the file to test: ")

    data = open(file_name,"r")

    count = len(data.readlines(  ))
    # data.seek(0,0)
    # line = data.readline()
    # parts = line.split()
    # print(parts)
    print(count)

    total_numbers = 0
    for i in range(count):
        data.seek(i,0)
        line = data.readline()
        parts = line.split()
        print(parts)
        total_numbers += len(parts)
        print(total_numbers)
    #
    # print(total_numbers)


    print("Type the number of the algorithm you want to run")
    algorithm_select = input("1) Forward Selection" + '\n'
                             "2) Backward Elimination" + '\n'
                             "3) Parth's Special Algorithm" + '\n')


    #The first column is the class, these values will always be either “1”s or “2”s.
    #The other columns contain the features, which are not normalized




main()
