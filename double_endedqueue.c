#include <stdio.h>
#define MAX 50

typedef struct {
    int arr[MAX];
    int front;
    int rear;
    int size;
} Deque;

void initDeque(Deque *dq) {
    dq->front = -1;
    dq->rear = 0;
    dq->size = 0;
}

// a. Front insertion
void insertFront(Deque *dq, int key) {
    if (dq->size == MAX) {
        printf("Deque Overflow\n");
        return;
    }
    if (dq->front == -1) {
        dq->front = 0;
        dq->rear = 0;
    } else if (dq->front == 0) {
        dq->front = MAX - 1;
    } else {
        dq->front = dq->front - 1;
    }
    dq->arr[dq->front] = key;
    dq->size++;
    printf("Inserted %d at Front\n", key);
}

// b. Rear insertion
void insertRear(Deque *dq, int key) {
    if (dq->size == MAX) {
        printf("Deque Overflow\n");
        return;
    }
    if (dq->front == -1) {
        dq->front = 0;
        dq->rear = 0;
    } else if (dq->rear == MAX - 1) {
        dq->rear = 0;
    } else {
        dq->rear = dq->rear + 1;
    }
    dq->arr[dq->rear] = key;
    dq->size++;
    printf("Inserted %d at Rear\n", key);
}

// c. Front deletion
void deleteFront(Deque *dq) {
    if (dq->size == 0) {
        printf("Deque Underflow\n");
        return;
    }
    printf("Deleted %d from Front\n", dq->arr[dq->front]);
    if (dq->front == dq->rear) {
        dq->front = -1;
        dq->rear = -1;
    } else if (dq->front == MAX - 1) {
        dq->front = 0;
    } else {
        dq->front = dq->front + 1;
    }
    dq->size--;
}

// d. Rear deletion
void deleteRear(Deque *dq) {
    if (dq->size == 0) {
        printf("Deque Underflow\n");
        return;
    }
    printf("Deleted %d from Rear\n", dq->arr[dq->rear]);
    if (dq->front == dq->rear) {
        dq->front = -1;
        dq->rear = -1;
    } else if (dq->rear == 0) {
        dq->rear = MAX - 1;
    } else {
        dq->rear = dq->rear - 1;
    }
    dq->size--;
}

int main() {
    Deque dq;
    initDeque(&dq);

    insertRear(&dq, 34);
    insertRear(&dq, 22);
    insertFront(&dq, 7);
    
    deleteFront(&dq);
    deleteRear(&dq);

    return 0;
}
