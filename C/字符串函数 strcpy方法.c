#include <stdio.h>
#include <string.h>
/*
	字符串函数 
*/

// 自定义strcpy
char *mycpy(char * dst,const char* src);

int main(int argc,char const *argv[]){
	
	char s1[]="abc";
	char s2[]="abc";
	
	strcpy(s2,s1);
	mycpy(s2,s1);
	return 0;
}

char *mycpy(char * dst,const char* src){
//	记录返回指针起始位置 
	char* ret = dst;
	while(*src != '\0'){
		*dst = *src;
		dst++;
		src++;
	}
//	将目标字符串最后加上'\0 
	*dst='\0';
	return ret;
}

