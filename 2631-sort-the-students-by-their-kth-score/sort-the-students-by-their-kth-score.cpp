class Solution {
public:
    vector<vector<int>> sortTheStudents(vector<vector<int>>& score, int k) {
        vector<int> temp;
        for(int i = 0; i < score.size(); i++){
            int maxIndex = i;
            for(int j = i + 1; j < score.size(); j++){
                if(score[maxIndex][k] < score[j][k]){
                    maxIndex = j;
                }
            }
            temp = score[maxIndex];
            score[maxIndex] = score[i];
            score[i] = temp;
        }
        return score;
    }
};