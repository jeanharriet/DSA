#include <iostream>
using namespace std;

#define SIZE 10   

class Queue {
private:
    int arr[SIZE];
    int front;
    int rear;

public:
    Queue() {
        front = -1;
        rear  = -1;
    }

    bool isFull() {
        return (rear == SIZE - 1);
    }

    bool isEmpty() {
        return (front == -1 || front > rear);
    }

    // ENQUEUER: insert element at the rear
    void enqueue(int value) {
        if (isFull()) {
            cout << "Queue Overflow! Cannot insert " << value << endl;
            return;
        }
        if (front == -1)        // first element being inserted
            front = 0;
        rear++;
        arr[rear] = value;
        cout << value << " enqueued into the queue." << endl;
    }

    // DEQUEUER: remove element from the front
    void dequeue() {
        if (isEmpty()) {
            cout << "Queue Underflow! Cannot dequeue from an empty queue." << endl;
            return;
        }
        cout << arr[front] << " dequeued from the queue." << endl;
        front++;
        if (front > rear) {     // queue became empty, reset
            front = -1;
            rear  = -1;
        }
    }

    // Display all elements
    void display() {
        if (isEmpty()) {
            cout << "Queue is empty." << endl;
            return;
        }
        cout << "Queue elements: ";
        for (int i = front; i <= rear; i++)
            cout << arr[i] << " ";
        cout << endl;
    }
};

int main() {
    Queue q;
    int choice, value;

    do {
        cout << "\n===== QUEUE list =====" << endl;
        cout << "1. Enqueue" << endl;
        cout << "2. Dequeue" << endl;
        cout << "3. Display" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter value to enqueue: ";
                cin >> value;
                q.enqueue(value);
                break;
            case 2:
                q.dequeue();
                break;
            case 3:
                q.display();
                break;
            case 4:
                cout << "Exiting program..." << endl;
                break;
            default:
                cout << "Invalid choice! Try again." << endl;
        }
    } while (choice != 4);

    return 0;
}