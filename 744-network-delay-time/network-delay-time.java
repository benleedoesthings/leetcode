class VertexDistance implements Comparable<VertexDistance> {
    public int vertex;
    public int distance;

    public VertexDistance(int vertex, int distance) {
        this.vertex = vertex;
        this.distance = distance;
    }

    @Override
    public int compareTo(VertexDistance o) {
        if (distance == o.distance) {
            return Integer.compare(vertex, o.vertex);
        }
        return Integer.compare(distance, o.distance);
    }

    @Override
    public String toString() {
        return "Pair with vertex " + vertex + " and distance " + distance;
    }
}

class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        HashMap<Integer, ArrayList<VertexDistance>> adj = new HashMap<>();
        for (int[] edge : times) {
            if (!adj.containsKey(edge[0])) {
                adj.put(edge[0], new ArrayList<>());
            }
            if (!adj.containsKey(edge[1])) {
                adj.put(edge[1], new ArrayList<>());
            }

            adj.get(edge[0]).add(new VertexDistance(edge[1], edge[2]));
        }

        PriorityQueue<VertexDistance> pq = new PriorityQueue<>();
        Map<Integer, Integer> distMap = new HashMap<>();
        pq.add(new VertexDistance(k, 0));

        int maxDist = 0;

        while (!pq.isEmpty() && distMap.size() < n) {
            VertexDistance curr = pq.remove();

            if (!distMap.containsKey(curr.vertex)) {
                distMap.put(curr.vertex, curr.distance);
                maxDist = Math.max(maxDist, curr.distance);

                for (VertexDistance neighbor : adj.get(curr.vertex)) {
                    if (!distMap.containsKey(neighbor.vertex)) {
                        pq.add(new VertexDistance(
                            neighbor.vertex, curr.distance + neighbor.distance
                        ));
                    }
                }
            }
        }

        if (maxDist == 0 || distMap.size() < n) {
            return -1;
        }

        return maxDist;
    }
}