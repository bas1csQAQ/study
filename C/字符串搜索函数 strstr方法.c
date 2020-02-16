#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
	字符串函数 
*/

int main(int argc,char const *argv[]){
	char s[]="abcdefg";
	char s2[]="def";
	char* p =strstr(s,s2);
	printf("%s\n",p); 
//	strcasestr 不区分大小写 
//	char s3[]="DEF";
//	char* p2=strcasestr(s,s3);
//	printf("%s\n",p2); 

}



