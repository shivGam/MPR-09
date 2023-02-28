class cll:
    class Node:
        def _init_(self, label=None, data=0):
            self.label = label
            self.data = data
            self.next = None

    def _init_(self):
        self.head = None
        self.tail = None

    def create_memory_blocks(self, block_sizes):
        for i in block_sizes:
            new_node = self.Node(label=str(i))
            if not self.head:
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head
            else:
                self.tail.next = new_node
                self.tail = new_node
                new_node.next = self.head

    def add_process_size(self, process):
        temp = self.head
        ct = ""
        for proc in process:
            while True:
                if temp.data == 0:
                    if proc <= int(temp.label):
                        temp.data = proc
                        ct += f"                                                {proc}                       {temp.label}\n"
                        break
                temp = temp.next
                if temp == self.head:
                    break
            temp = self.head
        return ct

class Main:
    process = [12,45,11,1,10]
    block_size = [10,20,30,50,60]
    n = count = 0
    count2 = 0
    ans = ""
    ch = ""

    def set_n(self, x):
        Main.n = x

    def get_n(self):
        return Main.n

    def blocksz(self, a):
        Main.block_size[Main.count] = a
        Main.count += 1

    def processz(self, b):
        Main.process[Main.count2] = b
        Main.count2 += 1

    def print_blocks(self):
        for i in range(Main.n):
            Main.ch += f" {Main.block_size[i]},"
        return Main.ch

    def allot(self):
        cl = cll()
        cl.create_memory_blocks(Main.block_size)
        Main.ans = cl.add_process_size(Main.process)
        return Main.ans

    # n = 5
    # cl=cll()
    # print("Blocks",block_size)
    # print("Process",process)
    # cl.create_memory_blocks(block_size)
    # ss=cl.add_process_size(process)
    # print(ss)