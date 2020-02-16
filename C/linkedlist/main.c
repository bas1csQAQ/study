#include <stdio.h>
#include <stdlib.h>
#include "node.h"

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
Node* add(Node** node ,int number);
int main(int argc, char *argv[]) {
	
	Node* head = NULL;
	int number;
	do{
		scanf("%d",&number);
		if(number != -1){
			head = add(&head,number); 
		}
	}while(number!=-1);
	return 0;
}

Node* add(Node** pHead ,int number){
	Node *p=(Node*)malloc(sizeof(Node));
	p->next=NULL;
	p->value=number;
	
	
	Node* last = *pHead;
	if(last){
		while(last->next ){
			last=last->next;
		}
		last->next=p;
	}else{
		pHead=p;
	}
	return pHead;
}
