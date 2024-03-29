# Heapsort
def heapity(A, n, i):
    l = 2*i+1
    r = 2*i+2

    # Find largest
    if l < n and A[i] < A[l]:
        largest = l
    else:
        largest = i
    if r < n and A[largest] < A[r]:
        largest = r
 
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapity(A, n, largest)

def buildMaxHeap(A):
    for i in range(len(A)//2-1,-1,-1):
        heapity(A, len(A), i)
 
def heapSort(A):
    buildMaxHeap(A)
    for i in range(len(A)-1,0,-1):
        A[i], A[0] = A[0], A[i]
        heapity(A, i, 0)

# Read file and save numbers to variable
text_file = open("dane.txt", "r")
lines = text_file.read().split('\n')
text_file.close()
for i in range(0, len(lines)):
    lines[i] = int(lines[i])

# Sort
heapSort(lines)