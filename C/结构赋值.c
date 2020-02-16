#include <stdio.h>
#include <stdbool.h>

struct point{
	int x;
	int y;
};

struct point getStruct(void);
void output(struct point p);


struct point* getStruct2(struct point*p);
void print(const struct point *p);

int main(int argc, const char * argv[]) {
	
	
struct point y = {0, 0}; 
    
//    y = getStruct();  
//    output(y);      
//    
    getStruct2(&y);
    print(getStruct2(&y));
    output(*getStruct2(&y));
  	*getStruct2(&y) = (struct point){1,2};
    return 0;
}


struct point getStruct(void)
{
    struct point p; //本地变量
    scanf("%d", &p.x);  //4
    scanf("%d", &p.y);  //5
    printf("%d, %d\n", p.x, p.y);   //4, 5
    return p;
}
void output(struct point p)
{
    printf("%d, %d\n", p.x, p.y);     //0, 0
}

struct point* getStruct2(struct point* p){
//	箭头表达式 
	scanf("%d", &p->x);  //4
    scanf("%d", &p->y);  //5
    printf("%d, %d\n", p->x, p->y);   //4, 5
    return p;
}

void print(const struct point *p){
	printf("%d, %d\n",p->x,p->y);
}


