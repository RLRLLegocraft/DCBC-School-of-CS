#include <stdlib.h>
#include <stdio.h>

#define MAX 100
void merge(int lo, int mid, int hi);
/*void mergeSort(int lo, int hi);*/

int arr[] = {2,3,8,4};

void mergeSort(int lo, int hi) {
  if (lo < hi) {
    int mid = hi+lo/2;
    mergeSort(lo, mid);
    mergeSort(mid+1, hi);
    /*merge(lo, mid, hi);*/
  }
}

/*
void merge(int lo, int mid, int hi) {
  int i=lo, j=mid, k=0, n;
  int helper[200];

  for (n=0; n<=hi; n++) {
      helper[n] = arr[n];
  }

  while (i<mid && j<=hi) {
    if (helper[i] < helper[j]) {
      arr[k] = helper[i];
      i++;
    } else {
      arr[k] = helper[j];
      j++;
    }
    k++;
  }

  while (i<mid) {
    arr[k] = helper[i];
    i++;
    k++;
  }

  while (j<=hi) {
    arr[k] = helper[j];
    j++;
    k++;
  }
}
*/

int main(void) {
  int i, n;
  n = sizeof(arr)/sizeof(int);

  printf("Before:\t");
  for (i=0; i<n; i++) {
    printf("%d ", arr[i]);
  }

  mergeSort(0, n-1);

  printf("After:\t");
  for (i=0; i<n; i++) {
    printf("%d ", arr[i]);
  }

  return 0;
}
