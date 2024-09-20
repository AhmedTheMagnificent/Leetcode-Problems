class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int length = matrix.size();
        for(int i = 0; i < length; i++){
            for(int j = i; j < length; j++){
                if(i == j){
                    continue;
                }
                else{
                    swap(matrix[i][j], matrix[j][i]);
                }
            }
        }
        for(int i = 0; i < length; i++){
            for(int j = 0; j < length/2; j++){
                swap(matrix[i][j], matrix[i][length - j - 1]);
            }
        }
        
    }
    void swap(int &x, int &y){
        int temp = x;
        x = y;
        y = temp;
    }
};