int[] data;
int size;

boolean isKeyInList(int key) {
    int high = 0;
    int low = 0;
    while(getIntFromList(high) != 0) {
        low = high;
        high *= 2;
    }
    return binarySearch(low, high, key);
}

boolean binarySearch(int low, int high, int key) {
    while(low <= high) {
        int middle = (low + high) / 2;
        if(data[middle] == key) {
            return true;
        } else if(data[middle] > key) {
            high = middle - 1;
        } else {
            low = middle + 1;
        }
    }
    return false;
}
