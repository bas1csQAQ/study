#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
	字符串函数 
*/

int main(int argc,char const *argv[]){
	
	char s[]="hello";
	char* p=strchr(s,'l');
	printf("p=%s\n",p); // llo
	
//	查找第二个l  因为p第一个字符就是l 所以要从 p+1的位置开始查找l 
	p=strchr(p+1,'l');
	printf("p=%s\n",p); 
	
//	将查找到的字符串复制到 新的字符串中
	char* t = (char*)malloc(strlen(p)+1); 
	strcpy(t,p);
	printf("t=%s\n",t);
	free(t);
	
//	需要找到的l之前的  将查找到的l的位置的字符改为'\0'  字符串会判断结束 所以就得到了l之前的字符串 
//	char c=*p; 将p的值保存一下  以便之后恢复字符串用 
	*p='\0'; 
	char* t2 = (char*)malloc(strlen(s)+1); 
	strcpy(t,s);
	printf("t2=%s\n",t2);
	free(t);
}



