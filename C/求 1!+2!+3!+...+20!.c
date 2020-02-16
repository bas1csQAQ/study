#include "stdio.h"
#include "string.h"
#include "math.h"

// Çó 1!+2!+3!+...+20! 

int f(int n) {
	if(n == 1)
		return 1;
	return f(n-1)*n;
}
int main()
{ 
int i,sum=0; 
for(i=1;i<21;i++){
	sum += f(i);
} 
printf("%d",sum);

return 0;

}


