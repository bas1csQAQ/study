#include<stdio.h>
// 读取文件内容  并把大写字母改成小写字母输出 
int main(){
    FILE *fp;
    char ch;
   
    //如果文件不存在，给出提示并退出
    if( (fp=fopen("D:\\demo.txt","rt")) == NULL ){ // 给文件指针指向一个文件  
        puts("Fail to open file!"); // 如果路径有问题文件指针就是空的 
        exit(0); // 就强行终止程序 
    }
    //每次读取一个字节，直到读取完毕 
    while( (ch=fgetc(fp)) != EOF ){ // 文件指针读取到文件末尾之后 会返回 EOF end of file 
        if(ch >= 'A' && ch <= 'Z') 
        	ch +=32;
        putchar(ch);
    }
    putchar('\n');  //输出换行符
    fclose(fp);
    return 0;
}
