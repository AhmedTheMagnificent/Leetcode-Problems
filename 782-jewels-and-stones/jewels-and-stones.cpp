class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int cost = 0;
        map<char, int> stoneMap;
        for(auto stone : stones){
            stoneMap[stone]++;
        }
        for(auto jewel : jewels){
            cost += stoneMap[jewel];
        }
        return cost;
    }
};