class Solution{
    public String longestPalindrome(String s) {
        char[] str = s.toCharArray();
        int n = str.length;
        int [][]dp = new int[n][n];
        int start = 0 ;
        for(int i=0;i<n;i++){
            dp[i][i] = 1;
        }

        int maxLength = 1;

        for(int j=0;j<n-1;j++){
            if(str[j]==str[j+1]){
                dp[j][j+1] =1;
                maxLength = 2;
                start = j;
            }
        }

        
        for(int length =3;length<=n;length++){
            for(int i = 0;i < (n-length)+1 ;i++){
                int j = i + length -1 ;

                if(str[i]==str[j] && dp[i+1][j-1] == 1){
                    dp[i][j] =1;
                    maxLength = length;
                    start = i;
                }
            }
        }

       
        return s.substring(start,start + maxLength);
     
        
    }
}
