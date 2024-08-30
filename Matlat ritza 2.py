class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def is_empty(self):
        return self.top is None

    def peek(self):         # peek() returns the top element
        if self.is_empty():
            return None
        return self.top.data

def find_visible_buildings(heights): # time complexity: O(n)
    n = len(heights)
    result = [0] * n
    stack = Stack()

    for i in range(n): 
        while not stack.is_empty() and heights[stack.peek()] < heights[i]: 
            stack.pop()            

        if not stack.is_empty():
            result[i] = stack.peek() + 1 #taller building
        else:
            result[i] = 0 #sea

        stack.push(i)

    return result

def main():

    heights = []
    print("Enter the heights of 30 buildings:")
    for i in range(30):
        height = int(input(f"Enter height for building {i + 1}: "))
        heights.append(height)

    # Find visible buildings
    visible = find_visible_buildings(heights)

    # Print the results
    print("\nVisible buildings or sea from each building:")
    for i in range(30):
        if visible[i] == 0:
            print(f"From building {i + 1}: Sea")
        else:
            print(f"From building {i + 1}: Building {visible[i]}")

if __name__ == "__main__":
    main()
