#include <stdio.h>
#include <string.h>
/*
	�ַ������� 
*/

// �Զ���strcpy
char *mycpy(char * dst,const char* src);

int main(int argc,char const *argv[]){
	
	char s1[]="abc";
	char s2[]="abc";
	
	strcpy(s2,s1);
	mycpy(s2,s1);
	return 0;
}

char *mycpy(char * dst,const char* src){
//	��¼����ָ����ʼλ�� 
	char* ret = dst;
	while(*src != '\0'){
		*dst = *src;
		dst++;
		src++;
	}
//	��Ŀ���ַ���������'\0 
	*dst='\0';
	return ret;
}

