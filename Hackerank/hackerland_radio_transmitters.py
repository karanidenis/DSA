# Hackerland is a one-dimensional city with houses aligned at integral locations along a road. The Mayor wants to install radio transmitters on the roofs of the city's houses. Each transmitter has a fixed range meaning it can transmit a signal to all houses within that number of units distance away.

# Given a map of Hackerland and the transmission range, determine the minimum number of transmitters so that every house is within range of at least one transmitter. Each transmitter must be installed on top of an existing house.

# 8 2
# 7 2 4 6 5 9 12 11 
# output = 3

def hackerlandRadioTransmitters(x, k):
    # Sort the house positions
    x.sort()
    print(f"Sorted houses: {x}")
    
    n = len(x)
    count = 0  # Number of transmitters used
    
    i = 0
    while i < n:
        # Find the farthest house within the range to place the transmitter
        transmitter = x[i] + k
        print(f"Placing transmitter covering from {x[i]} to {transmitter}")

        # Move i to the farthest house that can host the transmitter
        while i < n and x[i] <= transmitter:
            i += 1

        # Place the transmitter at the farthest point within the range
        transmitter_position = x[i - 1]
        print(f"Transmitter placed at house {transmitter_position}")

        # Move i to the first house not covered by the current transmitter
        transmitter_range_end = transmitter_position + k
        print(f"Transmitter covers up to {transmitter_range_end}")

        while i < n and x[i] <= transmitter_range_end:
            print(f"House {x[i]} covered")
            i += 1

        count += 1
        print(f"Remaining houses: {x[i:]}")
    
    print(f"Total transmitters needed: {count}")
    return count

# Test the function
x = [7, 2, 4, 6, 5, 9, 12, 11]
k = 2
print(hackerlandRadioTransmitters(x, k))
