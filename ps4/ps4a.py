# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx
word_list = []
def get_permutations(s):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    #>>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.

    if len(word_list) == 0:
        word_list.append(sequence[-1])
        return get_permutations(sequence[:-1])
    elif len(word_list) != 0:
        for word in word_list:
            for i in range(len(word) + 1):
                word
    '''
    #I found three ways to solve this problem. However I found third one the most easiest to understand and apply.

    ### 1st solution

    #if(len(s)==1):
    #    return [s]
    #result=[]
    #for i,v in enumerate(s):
    #    for p in get_permutations(s[:i] + s[i+1:]):
    #        result.append(v+p)
    #    #result += [v+p for p in get_permutations(s[:i]+s[i+1:])]
    #return result

    ### 2nd solution

    #if len(s)<=1:
    #    yield s
    #else:
    #    for p in get_permutations(s[1:]):
    #        for i in range(len(s)):
    #            yield p[:i]+s[0:1]+p[i:]

    ### 3rd solution

    emp_list = []
    if len(s)<=1:
        return s
    else:
        for p in get_permutations(s[1:]):
            for i in range(len(s)):
                emp_list.append(p[:i]+s[0:1]+p[i:])
        return emp_list




if __name__ == '__main__':
    #EXAMPLE 1
    example_input = 'aeiou'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', (get_permutations(example_input)))

    #EXAMPLE 2
    print('\n')
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', (get_permutations(example_input)))

    #EXAMPLE 3
    print('\n')
    example_input = 'def'
    print('Input:', example_input)
    print('Expected Output:', ['def', 'dfe', 'fed', 'fde', 'efd', 'edf'])
    print('Actual Output:', (get_permutations(example_input)))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)




