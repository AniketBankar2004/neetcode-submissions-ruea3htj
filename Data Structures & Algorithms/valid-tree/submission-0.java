class Solution {

    Set<Integer>visited = new HashSet<>();
    List<List<Integer>> adj = new ArrayList<>();
    
    public boolean dfs(int i, int prev){
        if(visited.contains(i)){
            return false;
        }

        visited.add(i);

        for(int nei :adj.get(i)){
            if(nei == prev){
                continue;
            }

            if(!dfs(nei,i)){
                return false;
            }
        }
        return true;
    }

    public boolean validTree(int n, int[][] edges) {
        
        for(int i = 0;i<n;i++){
            adj.add(new ArrayList<>());
        }

        for(int[] edge : edges){
            int u = edge[0];
            int v = edge[1];

            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        return dfs(0,-1) && visited.size()==n;
    }
}
