# "add <product_id> <quantity>": Add the specified quantity of the product to the inventory.
# "remove <product_id> <quantity>": Remove the specified quantity of the product from the inventory. If there isn’t enough quantity available, remove as much as possible.
# "check <product_id>": Return the current quantity of the product in the inventory.
# Design and implement a function that processes a list of these operations and returns the results of all "check" operations.
# Example 1:
# Input:

# operations = [
#     "add P1 10", 
#     "add P2 5", 
#     "remove P1 3", 
#     "check P1", 
#     "check P2", 
#     "remove P2 10", 
#     "check P2"
# ]

# Output:
# [7, 5, 0]


# inventory - dict - product_id: quantity
# add - quantity - Pr_id
# sub - quantity - pr_id
# return - quantity - pr_id
# list 

def manageInventory(operations):
    """
    take a list of ops
    add - add quanity
    remove - subtract quantity
    check - return quantity
    """
    # inv = {product_id: quantity}
    inv = {}
    product_id = ''
    for op in operations:
        # "add P1 10", 
        op_list = op.split()
        
        # print(op_list)
        func = op_list[0]
        product_id = op_list[1]
        # quantity = op_list[2]
        
        values_returned = []
        
        # inv[product_id] = inv.get()
        
        # check for id in inventory
        # check for arithmetic
        
        if product_id in inv.keys():
        
            # print("key exists checking for function")
            # check func
            # add 
            if func == "add":
                print("adding")
                # inv.get(inv[product_id],0)
                # inv[product_id] = inv.get(inv[product_id], 0) + quantity
                # print(inv)
                
                inv[product_id] += int(op_list[2])
                print(inv)
            
            # subtract
            if func == "remove":
                print("subtracting")
                inv[product_id] -= int(op_list[2])
                print(inv)
                
            # check
            if func == "check":
                print("checking")
                values_returned.append(inv[product_id])
            print(values_returned)
        else:
            print("key does not exist, added")
            inv[product_id] = int(op_list[2])
         
        # return values_returned
        
 
operations = [
    "add P1 10", 
    "add P2 5", 
    "add P1 3", 
    "remove P1 3", 
    "check P1", 
    "check P2", 
    # "remove P2 10", 
    # "check P2"
]        
print(manageInventory(operations))