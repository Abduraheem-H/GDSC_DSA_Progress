
class KthLargest {
public:
    KthLargest(int k, vector<int>& nums) : k(k) {
        
        for (int num : nums) {
            add(num);
        }
    }
    
    int add(int val) {
       
        if (minHeap.size() < k) {
            minHeap.push(val);
        } else if (val > minHeap.top()) {
           
            minHeap.pop();
            minHeap.push(val);
        }
        
        
        return minHeap.top();
    }

private:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;
};
