class Solution {

    public int find(int x , int[]parent){
        if (parent[x] == x){
            return x;
        }
        else{
            return find(parent[x],parent);
        }
    }

    public void union(int a,int b,int[] parent){
        int parentA = find(a,parent);
        int parentB = find(b,parent);

        if(parentA!=parentB){
            parent[parentA] = parentB;
        }
    }

    public int countComponents(int n, int[][] edges) {
        int[] parent = new int[n];

        for(int i=0;i<n;i++){
            parent[i] = i;
        }

        for(int[]edge :edges){
            union(edge[0],edge[1],parent);
        }
        int count = 0;

        for(int i = 0;i<n;i++){
            if (parent[i]==i){
                count ++;
            }
        }

        return count;
    }


}
