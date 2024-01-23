queue=[None]*10
frontPointer=0
rearPointer=-1
queueFull=10
currentSize=0

def enQueue(item):
  global currentSize,rearPointer,queueFull
  if currentSize<queueFull: # if queue is not full
      if rearPointer<len(queue)-1:
        rearPointer=rearPointer+1
      else:
        rearPointer=0
      currentSize=currentSize+1
      queue[rearPointer]=item
  else:
      print("Queue is full")

def deQueue():
  global currentSize,frontPointer,rearPointer,item
  if currentSize==0:
    print("Queue is empty")
  else:
    item = queue[frontPointer]
    if frontPointer==len(queue)-1: #if front pointer is at the final index in the array
      frontPointer=0
    else:
      frontPointer=frontPointer+1
  currentSize=currentSize-1
    
      

for i in range(0,10):
    enQueue(i)

print(queue)
deQueue()
enQueue(10)
print('\n',queue)
