
graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['C', 'D'],
        'F': ['D']
        }
print(graph.keys())
print(graph['E'])

# input一个graph和起始点s
def BFS(graph, s):
	#创建队列
    queue = []
    #将起始点s放入队列，假设起始点为‘A’
    queue.append(s)
	#set():创建一个无序不重复元素集，可进行关系测试，删除重		复数据,还可以计算交集、差集、并集
    seen = set()
    #'A'我们已经见过，放入seen
    seen.add(s)
    #当队列不是空的时候
    while len(queue) > 0:
    	#将队列的第一个元素读出来，即‘A’
        vertex = queue.pop(0)
     #graph['A']就是A的相邻点：['B','C'],将其储存到nodes
        nodes = graph[vertex]
        #遍历nodes中的元素，即['B','C']
        for w in nodes:
    		#如果w没见过
            if w not in seen:
                queue.append(w)
                #加入seen表示w我们看见过了
                seen.add(w)
        print(vertex)

#"DFS的方法就是将BFS中的队列改成栈即可"
def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex)

print("BFS--")
BFS(graph, 'A')
print("DFS--")
DFS(graph, 'A')



