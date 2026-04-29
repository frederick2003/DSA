import java.util.ArrayList;
class MinStack {
    private ArrayList<Integer> stack;
    private ArrayList<Integer> minimumStack;
    private int currentStackSize;
    private int currentMinStackSize;

    public MinStack() {
        stack = new ArrayList<>();
        minimumStack = new ArrayList<>();
        currentStackSize = 0;
        currentMinStackSize = 0;
    }
    
    public void push(int val) {
        // Check if the element is the min element in the current stack.
        if(stack.size() == 0 || val <= minimumStack.get(currentMinStackSize - 1)){
            minimumStack.add(val);
            currentMinStackSize++;
        }

        // Add the element to the stack.
        stack.add(val);
        currentStackSize++;
    }
    
    public void pop() {
        // Remove element from the stack.
        int removedElement = stack.remove(currentStackSize - 1);
        currentStackSize--;

        // If the removed element is the current min, remove it from the mimimum stack.
        if(removedElement == minimumStack.get(currentMinStackSize - 1)){
            minimumStack.remove(currentMinStackSize - 1);
            currentMinStackSize--;
        }
    }
    
    public int top() {
        return stack.get(currentStackSize - 1);
    }
    
    public int getMin() {
        return minimumStack.get(currentMinStackSize - 1);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */