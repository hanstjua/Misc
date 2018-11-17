//CE1007/CZ1007 Data Structures
// Week 13 Lab Tutorial - Binary Search Tree
// Question 1

#include <stdio.h>
#include <stdlib.h>

#define MAXSPACE 8

typedef struct _btnode{
    int item;
    struct _btnode *left;
    struct _btnode *right;
} BTNode;

void insertBTNode(BTNode** cur, int item);
void printBTNode(BTNode *root, int space);
void deleteTree(BTNode *root);

int main()
{
    BTNode* root=NULL;
    int item;

    printf("Enter a list of numbers for a Binary Tree, terminated by any non-digit character: \n");
    while(scanf("%d",&item))
        insertBTNode(&root, item);
    scanf("%*s");

    printf("The Binary Search Tree:\n");
    printBTNode(root,0);

    deleteTree(root);
    root=NULL;
    return 0;
}

void printBTNode(BTNode *root,int space){
    // Base case
    if (root == NULL)
        return;
    // Increase distance between levels
    space += MAXSPACE;

    // "Reversed" inorder tree traversal
    printBTNode(root->right, space);

    printf("\n");
    for (int i = MAXSPACE; i < space; i++)
        printf(" ");
    printf("%d\n", root->item);

    printBTNode(root->left, space);
}

void deleteTree(BTNode *root){
    BTNode* temp;
    if(root !=NULL)
    {
        temp = root->right;
        deleteTree(root->left);
        free(root);
        deleteTree(temp);
    }
}

void insertBTNode(BTNode** cur, int item){
   /* Write your program code here */
  //printf("entering insertBTNode\n");
  BTNode *temp = *cur;
  BTNode *node = (BTNode*)malloc(sizeof(BTNode));
  node->item = item;
  node->right = node->left = NULL;

  if(*cur==NULL){
    *cur = node;
    return;
  }

  while(temp!=NULL){
    if(temp->item > item){
      if(temp->left==NULL)break;
      else temp = temp->left;
    }
    else if(temp->item < item){
      if(temp->right==NULL)break;
      else temp = temp->right;
    }
    else {
      printf("Duplicated item: %d\n", temp->item);
      return;
    }
  }

  if(temp->item>item)temp->left = node;
  else temp->right = node;
}
