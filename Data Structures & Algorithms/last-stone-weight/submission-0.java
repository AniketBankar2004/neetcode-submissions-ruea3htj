class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxheap = new PriorityQueue<>(Collections.reverseOrder());

        int  len = stones.length;

        for(int i = 0;i<len;i++){
            maxheap.add(stones[i]);
        }

        while(!maxheap.isEmpty()){
            if(maxheap.size()==1){
                return maxheap.poll();
            }

            int stone1 = maxheap.poll();
            int stone2 = maxheap.poll();

            maxheap.add(Math.abs(stone1-stone2));
        }

        return 0;


    }
}
