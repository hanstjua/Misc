#include <stdio.h>

typedef struct _node{
  int item;
  struct _node *left;
  struct _node *right;
}BTNode;

void insertNode(BTNode **root, int item){
  
  if((*root)==NULL){
    *root  = malloc(sizeof(BTNode));
    (*root)->left = (*root)->right = NULL;
    (*root)->item = item;
    return;
  }
  
  if((*root)->item > item){
    insertNode(&(*root)->left, item);
  }
  else if((*root)->item < item){
    insertNode(&(*root)->right, item);
  }
  else printf("Number already exist!\n");
}

void printBST(BTNode *root){
  if(root==NULL)return;

  printBST(root->left);
  printBST(root->right);
  printf("%d ", root->item);
}

void rotateNodeCW(BTNode **root, int item){
  BTNode *node = malloc(sizeof(BTNode));

  if(*root==NULL){
    printf("Empty tree\n");
    return;
  }

  if((*root)->left!=NULL && (*root)->left->item == item){
    node = (*root)->left;
    if(node->left->right==NULL)node->left->right = malloc(sizeof(BTNode));
    node->left->right = node;
    (*root)->left = node->left;
    node->left = NULL;
    return;
  }
  else if((*root)->right!=NULL && (*root)->right->item == item){
    node = (*root)->right;
    node->left->right = node;
    (*root)->right = node->left;
    node->left = NULL;
    return;
  }

  printf("entering left\n");

  if((*root)->left!=NULL)rotateNodeCW(&(*root)->left, item);
  printf("entering right\n");
  if((*root)->right!=NULL)rotateNodeCW(&(*root)->right, item);
  printf("exiting\n");
}

int main(void) {
  int i;
  BTNode *bt = NULL;

  printf("Enter numbers end with char\n");

  while(scanf("%d ",&i)){
    insertNode(&bt, i);
  }

  printf("Post-order traversal:\n");
  printBST(bt);
  printf("\n");

  scanf("%*c");

  printf("Node to rotate about\n");
  scanf("%d", &i);
  rotateNodeCW(&bt, i);

  printBST(bt);

  return 0;
}
