#include <iostream>
using namespace std;

class Stack {
    private:
        int *stack;
        int top;
        int capacity;

    public:
        // Constructor to initialize stack
        Stack(int size) {
            stack = new int[size];
            top = -1;
            capacity = size;
        }

        // Destructor to free memory
        ~Stack() {
            delete[] stack;
        }

        // Method to add an element to the stack
        void push(int value) {
            if (top >= capacity - 1) {
                cout << "Stack Overflow! Cannot add " << value << " to the stack." << endl;
                return;
            }
            stack[++top] = value;
        }

        // Method to display stack elements
        void displayStack() {
            if (top == -1) {
                cout << "Stack is empty." << endl;
                return;
            }
            cout << "Stack elements: ";
            for (int i = 0; i <= top; i++) {
                cout << stack[i] << " ";
            }
            cout << endl;
        }
};

int main() {
    // Create a stack with a capacity of 5 elements
    Stack s(5);

    // Push elements onto the stack
    s.push(10);
    s.push(20);
    s.push(30);
    s.displayStack();  // Display stack elements

    // Attempt to push more elements than stack capacity
    s.push(40);
    s.push(50);
    s.push(60);  // This should cause a stack overflow

    s.displayStack();  // Display final stack elements

    return 0;
}