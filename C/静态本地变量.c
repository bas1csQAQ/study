#include <stdio.h>
#include <stdbool.h>

     
void f()
{
	static int i=1;
	printf("i=%d\n",i);
	i+=2;
	printf("i+2=%d\n\n",i);
}

int main(int argc, char const *argv[])
{
	f();
	f();
	f();
}
