#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
	�ַ������� 
*/

int main(int argc,char const *argv[]){
	
	char s[]="hello";
	char* p=strchr(s,'l');
	printf("p=%s\n",p); // llo
	
//	���ҵڶ���l  ��Ϊp��һ���ַ�����l ����Ҫ�� p+1��λ�ÿ�ʼ����l 
	p=strchr(p+1,'l');
	printf("p=%s\n",p); 
	
//	�����ҵ����ַ������Ƶ� �µ��ַ�����
	char* t = (char*)malloc(strlen(p)+1); 
	strcpy(t,p);
	printf("t=%s\n",t);
	free(t);
	
//	��Ҫ�ҵ���l֮ǰ��  �����ҵ���l��λ�õ��ַ���Ϊ'\0'  �ַ������жϽ��� ���Ծ͵õ���l֮ǰ���ַ��� 
//	char c=*p; ��p��ֵ����һ��  �Ա�֮��ָ��ַ����� 
	*p='\0'; 
	char* t2 = (char*)malloc(strlen(s)+1); 
	strcpy(t,s);
	printf("t2=%s\n",t2);
	free(t);
}



