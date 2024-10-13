class RandomizedSet {
public:
    RandomizedSet() {

    }
    
    bool insert(int val) {
        if(index.find(val) != index.end()){
            return false;
        }
        arr.push_back(val);
        index.insert({val, arr.size() - 1});
        return true;
    }
    
    bool remove(int val) {
        if (index.find(val) == index.end()) {
            return false;  // Value doesn't exist
        }
        // Get index of the value to be removed
        int i = index[val];
        int lastElement = arr.back();  // Get the last element in the array
        
        // Move last element to the position of the element to be removed
        arr[i] = lastElement;
        index[lastElement] = i;  // Update the index map with new position of last element
        
        // Remove the last element from the array and the map
        arr.pop_back();
        index.erase(val);
        
        return true;
    }
    
    int getRandom() {
        int random = rand() % arr.size();
        return arr[random];
    }

private:
        unordered_map<int, int> index;
        vector<int> arr;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */