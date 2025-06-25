class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        for(auto i : s){
            if(i == '{' || i == '[' || i == '('){
                stack.push(i);    
            }
            else{
                if(stack.empty()) return false;
                if(i == '}' && stack.top() != '{') return false;
                if(i == ']' && stack.top() != '[') return false;
                if(i == ')' && stack.top() != '(') return false;
                stack.pop();
            }
            
        }
        return stack.empty();
    }
};