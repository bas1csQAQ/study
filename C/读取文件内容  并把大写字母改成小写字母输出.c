#include<stdio.h>
// ��ȡ�ļ�����  ���Ѵ�д��ĸ�ĳ�Сд��ĸ��� 
int main(){
    FILE *fp;
    char ch;
   
    //����ļ������ڣ�������ʾ���˳�
    if( (fp=fopen("D:\\demo.txt","rt")) == NULL ){ // ���ļ�ָ��ָ��һ���ļ�  
        puts("Fail to open file!"); // ���·���������ļ�ָ����ǿյ� 
        exit(0); // ��ǿ����ֹ���� 
    }
    //ÿ�ζ�ȡһ���ֽڣ�ֱ����ȡ��� 
    while( (ch=fgetc(fp)) != EOF ){ // �ļ�ָ���ȡ���ļ�ĩβ֮�� �᷵�� EOF end of file 
        if(ch >= 'A' && ch <= 'Z') 
        	ch +=32;
        putchar(ch);
    }
    putchar('\n');  //������з�
    fclose(fp);
    return 0;
}
