# C++
# std::vector<int> myVector;
# myVector.push_back(10);
# myVector.push_back(20);

# Python equivalent: List
my_list = []
my_list.append(10)
my_list.append(20)
print(my_list)  # Output: [10, 20]

# C++
# std::stack<int> myStack;
# myStack.push(10);
# int topElement = myStack.top();

# Python equivalent: List (using append and pop)
my_stack = []
my_stack.append(10)
top_element = my_stack[-1]
print(top_element)  # Output: 10

# C++
# std::queue<int> myQueue;
# myQueue.push(10);
# int frontElement = myQueue.front();

# Python equivalent: Queue from the queue module
from queue import Queue
my_queue = Queue()
my_queue.put(10)
front_element = my_queue.queue[0]
print(front_element)  # Output: 10

# C++
# std::priority_queue<int> myPriorityQueue;
# myPriorityQueue.push(10);
# int topElement = myPriorityQueue.top();

# Python equivalent: PriorityQueue from queue module
from queue import PriorityQueue
my_priority_queue = PriorityQueue()
my_priority_queue.put(10)
top_element = my_priority_queue.queue[0]
print(top_element)  # Output: 10


# C++
# std::unordered_set<int> mySet;
# mySet.insert(10);
# mySet.insert(20);

# Python equivalent: Set
my_set = set()
my_set.add(10)
my_set.add(20)
print(my_set)  # Output: {10, 20}

# C++
# std::unordered_map<string, int> myMap;
# myMap["key1"] = 10;
# myMap["key2"] = 20;

# Python equivalent: Dictionary
my_dict = {}
my_dict["key1"] = 10
my_dict["key2"] = 20
print(my_dict)  # Output: {'key1': 10, 'key2': 20}
