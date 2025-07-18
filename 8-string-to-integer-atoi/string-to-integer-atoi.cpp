class Solution {
public:
    int myAtoi(string s) {
        int i = 0, n = s.size();
        while(i < n && s[i] == ' ') i++;
        int sign = 1;
        if(s[i] == '+' && i < n) i++;
        else if(s[i] == '-' && i < n){
            sign = -1;
            i++;
        }
        int num = 0;
        while(i < n && isdigit(s[i])){
            int digit = s[i] - '0';
            if(num > (INT_MAX - digit) / 10){
                return sign == 1 ? INT_MAX : INT_MIN;
            }
            num = 10 * num + digit;
            i++;
        }
        return num * sign;
    }
};