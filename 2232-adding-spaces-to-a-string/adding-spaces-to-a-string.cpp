class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string newstr = "";
        int j = 0;
        for(auto i : spaces){
            newstr += s.substr(j, i - j) + " ";
            j = i;
        }
        newstr += s.substr(j);
        return newstr;
    }
};