# Leetcode 2105 - watering plants 11
# Alice and bob to water plans n. plants are in a row- [0, n-1]. ith plant is located at x = 1.
#  Each plant needs a specific amount of water.
# Alice and Bob water the plants in the following way:
#  Alice - left to right 0 to n-1
#  Bob - right to left   n-1 to 0
# takes same time to water each plant despite amount of water
# Alice/Bob muust water each plant if they have enough water else refill their can
# incase of tie, the one with more water waters the plant, if both have same water, Alice waters the plant

# Givem array plants[] where plants[i] is the amount of water the ith plant needs
# and integers capacityA and capacityB representing the number of water each watering can can hold

# return no. of times they have to refill to water all plants

def waterPlants(plants, capacityA, capacityB):
    n = len(plants)
    left = 0
    right = n-1
    # print("right", right)
    refills = 0
    waterA = capacityA
    waterB = capacityB
    while left <= right:
        if waterA < plants[left]:
            # print("waterA", waterA, plants[left])
            waterA = capacityA
            refills += 1
        if waterB < plants[right]:
            waterB = capacityB
            refills += 1
        waterA -= plants[left]
        waterB -= plants[right]
        left += 1
        right -= 1

    # if both are at the same plant
        if plants[left] == plants[right]:
            if waterA < plants[left]:
                waterA = capacityA
                refills += 1
            else:
                if waterB < plants[right]:
                    waterB = capacityB
                    refills += 1
            left += 1
            right -= 1
            print("left", left, "right", right, "refills", refills, "waterA", waterA, "waterB", waterB)
    
                
    return refills

plants = [1, 2, 4, 4, 5]        # [2, 2, 3, 3]
capacityA = 6
capacityB = 5
print(waterPlants(plants, capacityA, capacityB)) # 2

















