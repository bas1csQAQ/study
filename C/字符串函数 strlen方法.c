#include <stdio.h>
#include <string.h>
/*
	字符串变函数 
*/

// 手动定义 strlen方法
size_t mylen(const char*s); 

int main(int argc,char const *argv[]){
	char line[]="Hello";
	printf("strlen=%lu\n",strlen(line)); // strlen 会返回字符串长度 不保罗字符串结尾的'\0' 
	printf("sizeof=%lu\n",sizeof(line)); // sizeof会返回所占据的字节数 包括字符串结尾的'\0' 
	
	printf("mylen=%lu\n", mylen(line));
	return 0;
}
size_t mylen(const char *s){
	// 定义字符串长度 
	int cnt=0;
	// 当指针指向的值不为'\0'的时候 就跳出循环 返回字符串长度 
	while(*s!='\0'){
		// 长度++ 
		cnt++;
		// 指针移动到下一个地方 
		s++;
	}
	return cnt;
}
