#include<stdio.h>
// 输入一行字符串 将小写字母转为大写字母 并写到demo.txt中 
int main(){
    FILE *fp; // 文件指针 
    char ch; // 每次读取的字符 

    //判断文件是否成功打开
    // 文件指针给的文件地址路径必须都是双斜杠 
    if( (fp=fopen("D:\\demo.txt","w+")) == NULL ){ // 给文件指针指定指向的文件 判断指针指向是否正确 
        puts("Fail to open file!"); // 如果文件指针是空  
        exit(0);   // 强行退出程序 
    }

    printf("Input a string:\n");
    //每次从键盘读取一个字符并写入文件
    while ( (ch=getchar()) != '\n' ){
    	if(ch >= 'a' && ch <= 'z') 
    		ch -= 32;
        fputc(ch,fp);
    }
    fclose(fp); // 关闭文件指针 
    return 0;
}
