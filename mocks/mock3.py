# Question: 
# You are given an integer array target and an integer n.
# You have an empty stack with the two following operations:

# "Push": pushes an integer to the top of the stack.
# "Pop": removes the integer on the top of the stack.

# You also have a stream of the integers in the range [1, n].

# Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. You should follow the following rules:
# If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
# If the stack is not empty, pop the integer at the top of the stack.
# If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.
# Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them.
 
# Example 1:
# Input: target = [1,3], n = 3
# Output: ["Push","Push","Pop","Push"]
# Explanation: Initially the stack s is empty. The last element is the top of the stack.
# Read 1 from the stream and push it to the stack. s = [1].
# Read 2 from the stream and push it to the stack. s = [1,2].
# Pop the integer on the top of the stack. s = [1].
# Read 3 from the stream and push it to the stack. s = [1,3].


# 3 func - pop, push, main
# 1 func - 

#  stream arr - [1, n]
# stack - []  vs target - [1, 3]  : output - []
# check whether to push - 1. - len of stack < len of target 2. 
# check whether to pop -  when value in stack < val in target
# check logic complete - 1. len of target == len of stack && values in target == values in stack

def pushOrPop(target, n):
    stack_arr = []
    stream_arr = [i for i in range(1, n + 1)]
    print(stream_arr)
    output = []
    
    stack_len = len(stack_arr)
    target_len = len(target)
    
    
    # for i in range(0, target_len):
    #     if stack_len != target_len:
    #         stack_arr.append(stream_arr[i])
    #         output.append("push")
                
    # print(f'stack: {stack_arr}')
    # print(f'output: {output}')
        
    # # for i in range(0, stack_len-1):
    # if stack_arr != target:
    #         output.append("pop")
    #         val = stack_arr.pop()
    #         stack_arr.append(val + 1)
    #         output.append("push")
            
    # print(stack_arr)
    # # print(output)
    
    t_ind = 0
    
    for i in range(0, len(stream_arr)):
        # if stack_len != target_len:
        #     stack_arr.append(stream_arr[i])
        #     output.append("push")
        
        if t_ind < target_len:
            stack_arr.append(stream_arr[i])
            output.append("push")
            
            if stack_arr[-1] != target[t_ind]:
                stack_arr.pop()
                output.append("pop")
            else:
                t_ind += 1
        
        else:
            break
            
    print(stack_arr)
    print(output)
        
    return output
    
    # 1. check if the value added == value in the pos in the target array && len stack > len of target

target = [1,2]
n = 4
print(pushOrPop(target, n))
    
