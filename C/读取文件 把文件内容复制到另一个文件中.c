#include "stdio.h"

// 读取文件 把文件内容复制到另一个文件中 
int main()
{ 
	FILE *in, *out;
	char ch;
	char infile[10], outfile[10];
	printf("Enter the infile name\n");
	scanf("%s",infile);
	printf("Enter the outfile name\n");
	scanf("%s", outfile);
	if ((in = fopen(infile, "r"))==NULL)
	{ 
	printf("can not open infile%s\n", infile);
	exit(0); 
	}
	if ((out = fopen(outfile, " w "))==NULL)
	{ 
	printf("can not open outfile%s\n", outfile);
	exit(0); 
	}
	while(fgetc(in) != EOF)
	fputc(in , out);
	fclose(in);
	fclose(out);
} 
