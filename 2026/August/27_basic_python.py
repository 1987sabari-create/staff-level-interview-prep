class BasicPython:
  def __init__(self):
    return None

if __name__ == "__main__":
  # here exploring array
  array = []
  array.append(1);
  val = array.pop()
  print(array)

  # here exploring queue
  queue = deque()
  queue.append(1)
  queue.append(2)
  queue.append(3)
  queue.append(4)

  print(queue.popleft())
  print(queue.pop())

  # if any question come related to alphabets - use ord and chr 
  print(ord('a'))
  

  
