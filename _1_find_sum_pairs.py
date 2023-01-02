class Array:
    def __init__(self,size):
        self.size = size
        self.data = []
        self.length = 0

    def display(self):
        if self.length <= self.size:
            print(self.data)
    
    def add(self, element):
        if self.length < self.size:
            self.data.append(element)
            self.length += 1
        else:
            print("Array is full!")
            
    def sum(self,no):
        for i in range(len(self.data)):
            for j in range(i,len(self.data)):
                if self.data[i]+self.data[j] == no and i !=j:
                    print(self.data[i],self.data[j])
                    

size = int(input("Enter the size of Array: "))
array = Array(size)
for i in range(size):
    ele = int(input(f"Enter the {i+1} element: "))
    array.add(ele)
array.display()
no = int(input("Enter the number to find sum pairs: "))
array.sum(no)