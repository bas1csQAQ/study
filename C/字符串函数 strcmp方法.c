#include <stdio.h>
#include <string.h>
/*
	字符串函数 
*/

// 自定义strcmp
int mycmp(const char *s1,const char *s2);

int main(int argc,char const *argv[]){
	char s1[]="abc";
	char s2[]="abc";
	char s3[]="bbc";
	char s4[]="Abc";
	printf("%d\n",strcmp(s1,s2));
	printf("%d\n",strcmp(s1,s3));
	printf("%d\n",strcmp(s1,s4));
	printf("-------------------------\n");
//	实际上比较的是相同位数的askii码 
	
	printf("%d\n",mycmp(s1,s2));
	printf("%d\n",mycmp(s1,s3));
	printf("%d\n",mycmp(s1,s4));
	
	return 0;
}

int mycmp(const char *s1,const char *s2){
	int ret;
	while(*s1 == *s2 && *s1!='\0'){
		s1++;
		s2++;
	}
	if((*s1-*s2)==0){
		ret = 0;
	}else if((*s1-*s2)>0){
		ret = 1;
	}else{
		ret = -1;
	}
	return ret;
}

