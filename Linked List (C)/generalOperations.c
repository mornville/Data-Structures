#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<stdbool.h>

struct node{
    int data;
    struct node *next;
};

struct node *head = NULL;
struct node * current = NULL;

//display list
void printList(){
    struct node *ptr = head;
    printf('\n');

    while(ptr!=NULL){
        printf("%d, %d", ptr->data);
        ptr = ptr->next;
    }
}