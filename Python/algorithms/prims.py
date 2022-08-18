import heapq
###https://www.youtube.com/watch?v=5ZYBFcPSvvE
mst = []
used_vertices = set()
with open("prims_data.txt") as f:
     num_vertices = int(f.readline())
     edges = [[] for _ in range(num_vertices)]
     for line in f.readlines():
         edge = tuple(map(int, line.split(" ")))
         if edge[0] == edge[1]: continue
         heapq.heappush(edges[edge[0]],(edge[2],edge[1]))
         heapq.heappush(edges[edge[1]], (edge[2],edge[0]))
cost,dest = 0,1
while len(used_vertices) < num_vertices:
    vertex_with_smallest_edge = 0
    for vertex in used_vertices:
        while len(edges[vertex]) > 0 and edges[vertex][0][dest] in used_vertices:
            heapq.heappop(edges[vertex])
        if len(edges[vertex]) == 0: continue
        if len(edges[vertex_with_smallest_edge]) == 0 or edges[vertex_with_smallest_edge][0][cost]:
            vertex_with_smallest_edge = vertex
    edge = heapq.heappop(edges[vertex_with_smallest_edge])
    mst.append((vertex_with_smallest_edge,edge[dest],edge[cost]))
    used_vertices.add(vertex_with_smallest_edge)
    used_vertices.add(edge[dest])
print(mst)