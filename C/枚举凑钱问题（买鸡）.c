#include <stdio.h>

int main(){
//	可以使 1角 2角 5角的凑够 10块 以下的钱数

	int x ;// 总钱数
	int one,two,five;// 每一种钱的数量 
	
//	scanf("%d",x);
	x=3;
	int exit = 0;
	for(one = 0;one<x*10;one++){
		for(two = 0;two <x*10/2;two++){// 总钱数(块)*10 得到 总共的钱数(角) / 每种钱的 面值 = 没种钱的数量 
			for(five = 0;five<x*10/5;five++){
				if(one*1+two*2+five*5 == x*10){
					printf("%d张1角的和%d张2角的和%d张5角的可以组成 %d 块钱\n",one,two,five,x);
//					goto out; 
					exit =1;
					break;
				}
				if(exit)break;
			}
			if(exit)break;
		}
	}
	
//	一般不建议使用 goto 因为太方便了 可以随便goto 会把代码结构弄得很乱  跳出多重循环一般使用 接力 break；
//out :
	return 0; 
	 
} 
