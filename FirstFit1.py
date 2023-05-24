# Python3 implementation of First-Fit algorithm
# Function to allocate memory to
# blocks as per First fit algorithm
def firstFit(blockSize, m, processSize, n):
    # Stores block id of the block allocated to a process
    allocation = [-1] * n
    # Create a flag list to track allocated blocks
    removeAllocated = [False] * m
    # Initially no block is assigned to any process
    # pick each process and find suitable blocks
    # according to its size and assign to it
    for i in range(n):
        for j in range(m):
            if not removeAllocated[j] and blockSize[j] >= processSize[i]:
                # Allocate block j to process i
                allocation[i] = j
                removeAllocated[j] = True
                # Reduce available memory in this block
                blockSize[j] = processSize[i]
                break
    print("Process No.   Process Size   Block no.")
    for i in range(n):
        print(" ", i + 1, "         ", processSize[i], "         ", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")
# Driver code
if __name__ == '__main__':
    blockSize = [100, 500, 200, 300, 600]
    processSize = [212, 417, 112, 426]
    m = len(blockSize)
    n = len(processSize)
    firstFit(blockSize, m, processSize, n)