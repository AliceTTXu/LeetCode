public class Solution {
    public double[] calcEquation(String[][] equations, double[] values, String[][] queries) {

        // Builds the map
        Map<String, Map<String, Double>> graph = new HashMap<>();
        int n = equations.length;
        for (int i = 0; i < n; i++) {
            addEdge(graph, equations[i][0], equations[i][1], values[i]);
            addEdge(graph, equations[i][1], equations[i][0], 1 / values[i]);
        }

        // Finds the answer
        int m = queries.length;
        double[] answer = new double[m];
        for (int i = 0 ; i < m; i++) {
            answer[i] = getValue(graph, queries[i][0], queries[i][1]);
        }

        // Ends
        return answer;

    }

    private void addEdge(Map<String, Map<String, Double>> graph, String startNode, String endNode, Double value) {
        if (!graph.containsKey(startNode)) {
            graph.put(startNode, new HashMap<String, Double>());
        }
        if (!graph.get(startNode).containsKey(endNode)) {
            graph.get(startNode).put(endNode, value);
        }
    }

    private double getValue(Map<String, Map<String, Double>> graph, String startNode, String endNode) {
        // If we don't have information regarding to the start or the end node, return -1
        if (!graph.containsKey(startNode) || !graph.containsKey(endNode)) {
            return -1;
        }

        // Prepares for BFS
        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        Map<String, Double> values = new HashMap<>();

        queue.offer(startNode);
        visited.add(startNode);
        values.put(startNode, 1d);

        // Starts the BFS
        while (!queue.isEmpty()) {
            String currentNode = queue.poll();
            for (String nextNode : graph.get(currentNode).keySet()) {
                double value = graph.get(currentNode).get(nextNode);
                values.put(nextNode, values.get(currentNode) * value);

                if (nextNode.equals(endNode)) {
                    return values.get(nextNode);
                } else if (!visited.contains(nextNode)) {
                    queue.offer(nextNode);
                    visited.add(nextNode);
                }

            }
        }

        return -1;

    }

}
