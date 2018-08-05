#include <stdlib.h>
#include <stdio.h>

#define MAX 100
int arr[] = {2,3,8,4};

int main(void) {

  int i, j, key, n;
  n = sizeof(arr)/sizeof(int);

  for (i=1; i<n; i++) {
    key = arr[i];
    j=i-1;
    while (key < arr[j] && j>=0) {
      arr[j+1] = arr[j];
      j--;
    }
    arr[j+1] = key;
  }

  for (i=0; i<n; i++) {
    printf("%d  ", arr[i]);
  }

  return 0;
}
