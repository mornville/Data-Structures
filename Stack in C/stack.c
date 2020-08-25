#include<stdlib.h>
#include<stdio.h>

int MAX_SIZE = 10;
int stack[10];
int top = -1;

int isEmpty()
{
    if(top == -1){
        return 1;
    }
    else{
        return 0;
    }
}

int isFull()
{
    if(top == MAX_SIZE)
        return 1;
    else
        return 0;
}

int peek() {
   return stack[top];
}


void push(int element){
    if(!isFull()){
        top = top +1;
        stack[top] = element;
    }
    else
    {
        printf("STACK IS FULL\n");
    }
    
}

int pop(){
    if(!isEmpty()){
        return stack[top--];
    }
    else
    {
        printf("STACK IS EMPTY");
        return -1;
    }
    
}


void display()
{
    int i;
	
	if(top==-1)
	{
		printf("\nStack is empty!!");
	}
	else
	{
		for(i=top;i>=0;--i)
			printf("%d\n",stack[i]);
	}
}

int main(){
// push items on to the stack 
   push(3);
   push(5);
   push(9);
   push(1);
   push(12);
   push(15);

   printf("-----------------------\nElement at top of the stack: %d\n" ,peek());
   printf("-----------------------\nStack Elements(Top to Bottom): \n");
   display();
   printf("-----------------------\nPopped Element : %d \n", pop());

   printf("Stack full: %s\n" , isFull()?"true":"false");
   printf("Stack empty: %s\n" , isEmpty()?"true":"false");
   
   return 0;
}