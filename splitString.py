def split_string(s):
    """
     Return total number of ways to split the given string into three non-overlapping
     substrings having the same number of As.
    """

    len_of_string = len(s)

    total_num_zeroes = 0 #initialize sum of zeroes

    #compute the sum of zeroes
    for i in range(len_of_string):
        if s[i] == '0':
            total_num_zeroes += 1

    #1st edge case
    #sum of zeros is not divisible by 3
    #Return zero
    if total_num_zeroes % 3 != 0:
        return 0

    #2nd edge case
    #sum of zeros  is 0
    #Return zero
    if total_num_zeroes == 0:
        return 0
    

    #initialize sum of zeroes in each string part
    sum_of_zeroes_in_str_part = total_num_zeroes // 3

    #initialize ways to cut string
    first_cut,second_cut = 0,0

    #initialize count
    zero_count = 0

    #loop from the start
    for i in range(len_of_string):

        #increment count if element is '0'
        if s[i] == '0':
            zero_count += 1

        
        if (zero_count == sum_of_zeroes_in_str_part):
            first_cut += 1

        elif (zero_count == 2 * sum_of_zeroes_in_str_part):
            second_cut += 1

    return first_cut * second_cut

#driver code
print(split_string('01010'))

