class Solution {
public:
    string frequencySort(string s) {
        map<char, int> dict;
        for(auto i : s){
            dict[i]++;
        }
        vector<pair<char, int>> freqVec(dict.begin(), dict.end());
        sort(freqVec.begin(), freqVec.end(), [](auto &a, auto &b){
            return a.second > b.second;
        });
        string ret = "";
        for(auto &p : freqVec){
            ret += string(p.second, p.first);
        }
        return ret;

    }
};