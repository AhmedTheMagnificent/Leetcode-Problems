class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> anagramMap;
        for(string s : strs){
            string key = s;
            sort(key.begin(), key.end());
            anagramMap[key].push_back(s);
        }
        vector<vector<string>> result;
        for(auto &pair : anagramMap){
            result.push_back(pair.second);
        }
        return result;
    }
};