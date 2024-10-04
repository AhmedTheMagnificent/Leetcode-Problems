class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        sort(skill.begin(), skill.end());
        long long chem = 0;
        int length = skill.size();
        int teamSum = skill[0] + skill[length - 1];
        for(int i = 0; i < length/2; i++){
            if(skill[i] + skill[length - i - 1] == teamSum){
                chem += skill[length - i - 1] * skill[i] ;
            }
            else{
                return -1;
            }
        }
        return chem;
    }
};