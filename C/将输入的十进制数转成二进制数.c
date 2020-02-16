
// 将输入的十进制数转成二进制数 
#include<stdio.h>
int dtob(int n,int *p)
{  int m,i=0;
          do
          {  m=n%2;
               p[i]=m   ; 
             n=n/2;
             i++;
          }while(n!=0);
          return i;
}
main()
{  int n,j,a[20];
          printf("Input the umber: \n");
          scanf("%d",&n);
          j=dtob(n,a);
          for(;j>0;j--)
             printf("%d",  a[j-1] );  
}


