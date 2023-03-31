def selection_sort(my_list):

    for i in range(len(my_list)):
        min_index = i
        
        for j in range(i, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        
        temp = my_list[i]
        my_list[i] = my_list[min_index]
        my_list[min_index] = temp

    return my_list


"""_summary_


iter 1 ext
    my_list = [6,2,8,9,0,3]
    i = 0
    min_index = 4
        
        iter 1 int
        j = 0
        6 menor que 6?
        
        iter 2  int
        j = 1
        2 es menor que 6?

        iter 3 int
        j = 2
        es 8 menos que 2?

        iter 4 int
        j = 3
        es 9 menor que 2?

        iter 5 int
        j = 4
        es 0 menor que 2?

        iter 6 int
        j = 5
        es 3 menor que 0
    temp = 6
    list = [0,2,8,9,0,3]
    list = [0,2,8,9,6,3]






"""

if "__main__" == __name__:
    my_list = [6,2,8,9,0,3,6,10,1,5,4]
    sorted_list = selection_sort(my_list)
    assert sorted_list == [0,1,2,3,4,5,6,6,8,9,10]

    my_list = [1,0]
    sorted_list = selection_sort(my_list)
    assert sorted_list == [0,1]

    my_list = [4,3,2,1]
    sorted_list = selection_sort(my_list)
    assert sorted_list == [1,2,3,4]

        