#include <stdio.h>
#include <string.h>
/*
	�ַ����亯�� 
*/

// �ֶ����� strlen����
size_t mylen(const char*s); 

int main(int argc,char const *argv[]){
	char line[]="Hello";
	printf("strlen=%lu\n",strlen(line)); // strlen �᷵���ַ������� �������ַ�����β��'\0' 
	printf("sizeof=%lu\n",sizeof(line)); // sizeof�᷵����ռ�ݵ��ֽ��� �����ַ�����β��'\0' 
	
	printf("mylen=%lu\n", mylen(line));
	return 0;
}
size_t mylen(const char *s){
	// �����ַ������� 
	int cnt=0;
	// ��ָ��ָ���ֵ��Ϊ'\0'��ʱ�� ������ѭ�� �����ַ������� 
	while(*s!='\0'){
		// ����++ 
		cnt++;
		// ָ���ƶ�����һ���ط� 
		s++;
	}
	return cnt;
}
