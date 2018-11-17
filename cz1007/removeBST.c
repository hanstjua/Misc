//CE1007/CZ1007 Data Structures
// Week 13 Lab Tutorial - Binary Search Tree
// Question 4

#include <stdio.h>
#include <stdlib.h>

#define MAXSPACE 8

typedef struct _btnode{
    int item;
    struct _btnode *left;
    struct _btnode *right;
} BTNode;

BTNode* insertBSTNode(BTNode* cur, int item);
void printBTNode(BTNode *root, int space);
void deleteTree(BTNode *root);
int removeBSTNode(BTNode **nodePtr, int item);

int getReplacement(BTNode **node){
  int temp;

  if((*node)->right == NULL && (*node)->left == NULL){
    temp = (*node)->item;
    (*node) = NULL;
    return temp;
  }

  if((*node)->left != NULL)return getReplacement(&(*node)->left);

  if((*node)->left==NULL && (*node)->right!=NULL){
    temp = (*node)->item;
    *node = (*node)->right;
    return temp;
  }
}

int main()
{
    BTNode* root=NULL;
    int item;

    printf("Enter a list of numbers for a Binary Tree, terminated by any non-digit character: \n");
    while(scanf("%d",&item))
        root = insertBSTNode(root, item);
    scanf("%*s");

    printf("The Binary Search Tree:\n");
    printBTNode(root,0);

    printf("Enter an integer to be removed from the tree:\n");
    scanf("%d",&item);

    if(removeBSTNode(&root,item))
       printf("%d was removed\n",item);

    else
       printf("%d is not in the tree.\n",item);

    printf("The Binary Search Tree:\n");
    printBTNode(root,0);

    deleteTree(root);
    root=NULL;
    return 0;
}

BTNode* insertBSTNode(BTNode* cur, int item){
    if (cur == NULL){
        BTNode* node = (BTNode*) malloc(sizeof(BTNode));
    	node->item = item;
    	node->left = node->right = NULL;
    	return node;
	}
    if (item < cur->item)
        cur->left  = insertBSTNode (cur->left, item);
    else if (item > cur->item)
        cur->right = insertBSTNode (cur->right, item);
    else
        printf("Duplicated Item: %d\n",item);

    return cur;
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

int removeBSTNode(BTNode **nodePtr, int item){
/* Write your program code here. */
  BTNode *temp = *nodePtr;

  if(*nodePtr==NULL)return 0;

  if(temp==NULL)return 0;

  if(temp->item > item)removeBSTNode(&(temp->left), item);
  else if(temp->item < item)removeBSTNode(&(temp->right), item);
  else{
    (*nodePtr)->item = getReplacement(&(*nodePtr)->right);
    return 1;
  }
}
