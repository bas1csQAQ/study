#include <stdio.h>

int main() {
	int a[4][4], b[4][4], i, j;
	for(i = 0 ; i < 4; i++) {
		for(j = 0 ; j < 4 ; i++) {
			// 向 数组 a 中正常赋值 
			scanf("%d", &a[i][j]);
			// 将数组逆时针旋转 90° 之后的值赋值到 b 
			/*
				见分析图 
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
