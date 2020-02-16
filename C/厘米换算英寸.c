#include <stdio.h> 

int main(){
//	厘米换算英寸
//  已知英制长度的英尺foot 和 英寸的inch值 那么对应的米是(foot+inch/12)*0.3048 那么现在用户输入厘米数 对应的英制的长度英尺和英寸是多少呢 1英尺=12英寸

int cm = 0;
scanf("%d", &cm);

int foot = cm/30.48; //  
int inch = ((cm/30.48)-foot)*12;

printf("%d %d0",foot,inch);
}
