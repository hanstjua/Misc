/////////////////////////////////////////////////////////////////////////////////

/* CE1007/CZ1007 Data Structures
Purpose: Implementing the required functions for Question 5 */
//////////////////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include "AS9_Q5.h" //Comment it and include library filewhen you work on code::blocks
////////////////////////////////// stack //////////////////////////////////////////

#ifndef _AS9_Q5_
#define _AS9_Q5_
typedef struct _listnode{
   char item;
   struct _listnode *next;
} ListNode;

typedef ListNode StackNode;

typedef struct _linkedlist{
   int size;
   ListNode *head;
} LinkedList;
typedef LinkedList Stack;
#endif

void push(Stack *sPtr, char item);
int pop(Stack *sPtr);
int peek(Stack s);
int isEmptyStack(Stack s);

void removeAllItemsFromStack(Stack *sPtr);

Stack* lineEditor(char* line);
int test_main(Stack* (*editor)(char*),void (*removeAllItemsFromStack)(Stack *));

int main()
{
    test_main(lineEditor,removeAllItemsFromStack);
    return 0;
}

void push(Stack *sPtr, char item)
{
	StackNode *newNode;
    newNode= malloc(sizeof(StackNode));
    newNode->item = item;
    newNode->next = sPtr->head;
    sPtr->head = newNode;
    sPtr->size++;
}

int pop(Stack *sPtr)
{
    if(sPtr==NULL || sPtr->head==NULL){
        return 0;
    }
    else{
       StackNode *temp = sPtr->head;
       sPtr->head = sPtr->head->next;
       free(temp);
       sPtr->size--;
       return 1;
    }
}

int isEmptyStack(Stack s)
{
     if(s.size==0) return 1;
     else return 0;
}

int peek(Stack s){
    return s.head->item;
}

void removeAllItemsFromStack(Stack *sPtr)
{
	while(pop(sPtr));
}

Stack* lineEditor(char* line){
    /* add your code here */
    Stack *exp = (Stack *)malloc(sizeof(Stack));
    Stack *reverse = (Stack *)malloc(sizeof(Stack));;
    
    char c;

    
    (exp)->size = 0;
    (exp)->head = NULL;
    reverse->size = 0;
    reverse->head = NULL;

    while(*line!='\0'){
        switch(*line){
            case '*':
                pop(exp);
                line++;
                break;
            case '^':
                if(isalpha(*(++line))){
                    push(exp, toupper(*line));
                    line++;
                }
                break;
            case '\\':
                push(exp, '\n');
                line++;
                break;
            case '#':
                while(!isEmptyStack(*exp) && peek(*exp)!='\n')pop(exp);
                line++;
                break;
            default:
                push(exp, *line++);
                break;
        }
    }
    while(!isEmptyStack(*exp)){
        push(reverse, peek(*exp));
        pop(exp);
    }
    
    return reverse;
}
