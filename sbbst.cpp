// C++ program to insert a node in AVL tree  
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
using namespace std; 
  
// An AVL tree node  
class Node {
    public: 
    int key;  
    Node *left;  
    Node *right;  
    int height;
};  

int height(Node *N) {
    if (N == NULL) {
        return 0;
    }
    return N->height;  
}  
  
int max(int a, int b) {
    return (a > b)? a : b;  
}  

Node* rightRotate(Node* y) {
    Node *x = y->left;  
    Node *T2 = x->right;  
    // Perform rotation  
    x->right = y;  
    y->left = T2;  
    // Update heights  
    y->height = max(height(y->left),height(y->right)) + 1;  
    x->height = max(height(x->left),height(x->right)) + 1;    
    // Return new root  
    return x;  
}  

Node* leftRotate(Node* x) {
    Node *y = x->right;  
    Node *T2 = y->left;    
    // Perform rotation  
    y->left = x;  
    x->right = T2;  
    // Update heights  
    x->height = max(height(x->left),height(x->right)) + 1;  
    y->height = max(height(y->left),height(y->right)) + 1;  
    // Return new root  
    return y;  
}  

int getBalance(Node *N) {
    if (N == NULL) { 
        return 0;
    }
    return height(N->left) - height(N->right);  
}

Node* newNode(int key) {
    Node* node = new Node(); 
    node->key = key;  
    node->left = NULL;  
    node->right = NULL;  
    node->height = 1;
    return(node);  
}

Node * minValueNode(Node* node) {
    Node* current = node;  
    while (current->left != NULL)  
        current = current->left;  
    return current;  
} 

Node* insert(Node* node, int key) {  
    if (node == NULL) {
        return(newNode(key));  
    }else if (key < node->key) {
        node->left = insert(node->left, key);  
    }else if (key > node->key) {
        node->right = insert(node->right, key);  
    }else {
        return node;  
    }

    node->height = 1 + max(height(node->left),height(node->right));  
    int balance = getBalance(node);  

    // Left Left Case  
    if (balance > 1 && key < node->left->key) {
        return rightRotate(node);  
    }// Right Right Case  
    if (balance < -1 && key > node->right->key) {
        return leftRotate(node);  
    }// Left Right Case  
    if (balance > 1 && key > node->left->key) {  
        node->left = leftRotate(node->left);  
        return rightRotate(node);  
    }// Right Left Case  
    if (balance < -1 && key < node->right->key){  
        node->right = rightRotate(node->right);  
        return leftRotate(node);  
    }  
    return node;  
} 

Node* deleteNode(Node* root, int key) {
    if (root == NULL) {
        return root;  
    }else if ( key < root->key ) {
        root->left = deleteNode(root->left, key);  
    }else if( key > root->key ) {
        root->right = deleteNode(root->right, key);  
    }else {
        if( (root->left == NULL) || (root->right == NULL) ) {  
            Node *temp = root->left ? root->left : root->right;  
            if (temp == NULL) {
                temp = root;  
                root = NULL;  
            }else { 
                *root = *temp;
            }
            free(temp);  
        }else {
            Node* temp = minValueNode(root->right);  
            root->key = temp->key;  
            root->right = deleteNode(root->right,temp->key);  
        }  
    }

    if (root == NULL) {
        return root;
    }
    root->height = 1 + max(height(root->left), height(root->right));  
    int balance = getBalance(root);  

    // Left Left Case  
    if (balance > 1 && getBalance(root->left) >= 0) {  
        return rightRotate(root);  
    }// Left Right Case  
    if (balance > 1 && getBalance(root->left) < 0) {
        root->left = leftRotate(root->left);  
        return rightRotate(root);  
    }// Right Right Case  
    if (balance < -1 && getBalance(root->right) <= 0) {
        return leftRotate(root);  
    }// Right Left Case  
    if (balance < -1 &&  getBalance(root->right) > 0) {
        root->right = rightRotate(root->right);  
        return leftRotate(root);  
    }
    return root;  
}

void preOrder(Node *root) {
    if(root != NULL){  
        cout << root->key << " ";  
        preOrder(root->left);  
        preOrder(root->right);  
    }
}  

void inOrder(Node *root) {
    if(root != NULL){
        inOrder(root->left);  
        cout << root->key << " ";
        inOrder(root->right);  
    }
}

int main() {  
    Node *head = NULL;  
    
    head = insert(head, 10);
    head = insert(head, 1);  
    head = insert(head, 2);
    head = insert(head, 7);  
    head = insert(head, 3);
    head = insert(head, 8);  
    head = insert(head, 4);  
    head = insert(head, 5);
    head = insert(head, 9); 
    head = insert(head, 6);  
    
    preOrder(head);
    cout << endl;
    inOrder(head);
    cout << endl << endl;

    /* The constructed AVL Tree would be  
             ______7____
            /           \  
          _4_           _9_
         /   \         /   \  
       _2_    5_      8    10
      /   \     \
      1   3      6
    */

    head = deleteNode(head, 5);
    head = deleteNode(head, 9); 
    head = deleteNode(head, 6);  

    preOrder(head);
    cout << endl;
    inOrder(head);
    cout << endl << endl;

    /* The constructed AVL Tree would be  
             _____7_____
            /           \  
          _2___        _10
         /     \      /  
        1      _4    8 
              /
             3
    */

    cin.get();
    return 0;  
}