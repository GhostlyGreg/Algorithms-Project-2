import time
import random

def mergeSort( A ):
    if( len( A ) > 1 ):
        midPoint = len(A)//2
        leftArray = A[:midPoint] 
        rightArray = A[midPoint:]

        mergeSort( leftArray )
        mergeSort( rightArray )

        x = 0
        y = 0
        z = 0
        while( x < len(leftArray) and y < len(rightArray) ):
            if( leftArray[x] < rightArray[y] ):
                A[z] = leftArray[x]
                x = x + 1
            else:
                A[z] = rightArray[y]
                y = y + 1
            z = z + 1

        while x < len(leftArray):
            A[z] = leftArray[x]
            x = x + 1
            z = z + 1

        while y < len(rightArray):
            A[z] = rightArray[y]
            y = y + 1
            z = z + 1

def heapSort( A ):
  length = len( A ) - 1
  leastParent = length // 2
  for i in range ( leastParent, -1, -1 ):
    siftDown( A, i, length )
 
  # flatten heap into sorted array
  for i in range( length, 0, -1 ):
    if A[0] > A[i]:
      swap( A, 0, i )
      siftDown( A, 0, i - 1 )
 
 
def siftDown( A, first, last ):
  largest = 2 * first + 1
  while largest <= last:
    if ( largest < last ) and ( A[largest] < A[largest + 1] ):
      largest += 1
      
    if A[largest] > A[first]:
      swap( A, largest, first )
      first = largest;
      largest = 2 * first + 1
      
    else:
      return 
 
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

def countingSort( A, maxValue ):
    counter = [0] * ( maxValue + 1 )
    for i in A:
      counter[i] += 1
      
    ndx = 0;
    for i in range( len( counter ) ):
      while 0 < counter[i]:
        A[ndx] = i
        ndx += 1
        counter[i] -= 1

# Merge Sort 
f = open( "merge_sort_data2.txt", "w" )
for X in range( 1, 100000):

    SAMPLE = [random.randint(1,1000) for _ in range(X)]
     
    start = time.clock() 
    mergeSort( SAMPLE )
    duration = time.clock() - start
    f.write( str(duration) )
    f.write( "\n" )   
f.close()

# Heap Sort 
f = open( "heap_sort_data2.txt", "w" )
for X in range( 1, 70000):

    SAMPLE2 = [random.randint(1,1000) for _ in range(X)]
     
    start = time.clock() 
    heapSort( SAMPLE2 )
    duration = time.clock() - start
    f.write( str(duration) )
    f.write( "\n" )   
f.close()

# Counting Sort 
f = open( "counting_sort_data2.txt", "w" )
for X in range( 1, 70000):

    SAMPLE3 = [random.randint(1,1000) for _ in range(X)]
     
    start = time.clock() 
    mergeSort( SAMPLE3 )
    duration = time.clock() - start
    f.write( str(duration) )
    f.write( "\n" )   
f.close()




