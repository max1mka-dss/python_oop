class Graph:
    LIMIT_Y=[0,10]
    def set_data(self,data):
        setattr(self,'data',data)
    def draw(self):
        #print(f'{self.data}')
        for i in range(len(self.data)):
            if self.data[i] >= self.LIMIT_Y[0] and self.data[i] <= self.LIMIT_Y[-1]:
                print (self.data[i],end = ' ')
graph_1 = Graph()

#print(type(graph_1))
graph_1.set_data([10,-5,100,20,0,80,45,2,5,7])
print(graph_1.data)
graph_1.draw()