#include <stdio.h>

int main() {
	int a[4][4], b[4][4], i, j;
	for(i = 0 ; i < 4; i++) {
		for(j = 0 ; j < 4 ; i++) {
			// �� ���� a ��������ֵ 
			scanf("%d", &a[i][j]);
			// ��������ʱ����ת 90�� ֮���ֵ��ֵ�� b 
			/*
				������ͼ 
			*/ 
			b[3 - j][i] = a[i][j];
		}
	}
	printf("%\n");
	for(i = 0 ; i < 4; i++) {
		for(j = 0 ; j < 4 ; i++) {
			printf("%-5d", b[i][j]);
		}
		printf("%\n");
	}
	
} 
