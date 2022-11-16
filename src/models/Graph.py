class Graph:
    def __init__(self, filename):
        self.nodes = []
        self.load_file(filename)

    def load_file(self, filename):
        with open(filename, 'r') as file:
            file.readline()
            buf = file.readline().split()
            for i in range(len(buf)):
                self.nodes.append([])
            buf = file.readline()
            while buf != "}":
                tmp = buf.split("-")
                n1 = int(tmp[0][1:])
                n2 = int(tmp[1][1:])
                self.nodes[n1-1].append(n2)
                self.nodes[n2-1].append(n1)
                buf = file.readline()
            file.close()
    def __str__(self):
        buf = "["
        for node in self.nodes:
            buf += f" {node},"
        buf += "]"
        return buf
