#include<stdio.h>
// ����һ���ַ��� ��Сд��ĸתΪ��д��ĸ ��д��demo.txt�� 
int main(){
    FILE *fp; // �ļ�ָ�� 
    char ch; // ÿ�ζ�ȡ���ַ� 

    //�ж��ļ��Ƿ�ɹ���
    // �ļ�ָ������ļ���ַ·�����붼��˫б�� 
    if( (fp=fopen("D:\\demo.txt","w+")) == NULL ){ // ���ļ�ָ��ָ��ָ����ļ� �ж�ָ��ָ���Ƿ���ȷ 
        puts("Fail to open file!"); // ����ļ�ָ���ǿ�  
        exit(0);   // ǿ���˳����� 
    }

    printf("Input a string:\n");
    //ÿ�δӼ��̶�ȡһ���ַ���д���ļ�
    while ( (ch=getchar()) != '\n' ){
    	if(ch >= 'a' && ch <= 'z') 
    		ch -= 32;
        fputc(ch,fp);
    }
    fclose(fp); // �ر��ļ�ָ�� 
    return 0;
}
