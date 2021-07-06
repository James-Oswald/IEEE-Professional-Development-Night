//https://leetcode.com/problems/string-to-integer-atoi

#include<sstream>
#include<string>

class Solution{
public:
    std::stringstream ss;
    int myAtoi(std::string str){
        int rv;
        str.append("t");
        ss<<str;
        ss>>rv;
        return rv;
    }
};