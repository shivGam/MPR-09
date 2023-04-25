class cll:
    class Node:
        def __init__(self, label=None, data=0):
            self.label = label #Stores memory Capacity
            self.data = data #Stores Process Size
            self.next = None #next pointer

    def __init__(self):
        self.head = None #head points to 1st node
        self.tail = None #tail points to last node

    def create_memory_blocks(self, block_sizes):
        for i in block_sizes:
            new_node = self.Node(label=str(i),data=0)
            if not self.head:
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head
            else:
                self.tail.next = new_node
                self.tail = new_node
                new_node.next = self.head

    def add_process_size(self, process):
        # temp=self.Node()
        temp = self.head
        for proc in process:
            while True:
                if temp.data == 0:
                    if proc <= int(temp.label):
                        temp.data = proc
                        # print(temp.data,temp.label)
                        # print()
                        break
                temp = temp.next
                if temp == self.head:
                    break
            temp = self.head
        
    def display(self,process):
        result = [[None, None] for i in range(len(process))]
        current=self.Node()
        current=self.head
        count=0
        if self.head is None:
            return
        else:
            for proc in process:
                result[count][0]=current.data
                result[count][1]=current.label
                # print(result)
                current = current.next
                count+=1
                if current == self.head:
                    break
        return result

class Main:
    process = []
    block_sizes = []
    #ans=[[]]
    # def defineValue(block_sizes_from_gui,process_from_gui):
    #     Main.process=process_from_gui
    #     Main.block_sizes=block_sizes_from_gui
    # n = 5
    # cl=cll()
    # print("Blocks",block_sizes)
    # print("Process",process)
    def defineValue(block_sizes_from_gui,process_from_gui):
        Main.process=process_from_gui
        Main.block_sizes=block_sizes_from_gui
    # print(block_sizes)
    # print(process)
    # cl.create_memory_blocks(block_sizes)
    # cl.add_process_size(process)
    # result2=cl.display(process)

    def allocation():
        cl=cll()
        cl.create_memory_blocks(Main.block_sizes)
        cl.add_process_size(Main.process)
        result2=cl.display(Main.process)
        return result2
