#include <stdio.h> 

int main(){
//	���׻���Ӣ��
//  ��֪Ӣ�Ƴ��ȵ�Ӣ��foot �� Ӣ���inchֵ ��ô��Ӧ������(foot+inch/12)*0.3048 ��ô�����û����������� ��Ӧ��Ӣ�Ƶĳ���Ӣ�ߺ�Ӣ���Ƕ����� 1Ӣ��=12Ӣ��

int cm = 0;
scanf("%d", &cm);

int foot = cm/30.48; //  
int inch = ((cm/30.48)-foot)*12;

printf("%d %d0",foot,inch);
}
