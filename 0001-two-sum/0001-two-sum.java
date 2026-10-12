class Solution {
    public static int[] twoSum(int[] nums, int target) {
        // Create a HashMap to store the number and its index
        HashMap<Integer, Integer> numToIndex = new HashMap<>();
        
        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            // Calculate the complement
            int complement = target - nums[i];
            
            // Check if the complement exists in the HashMap
            if (numToIndex.containsKey(complement)) {
                // If it exists, return the indices
                return new int[] { numToIndex.get(complement), i };
            }
            
            // Otherwise, add the current number and its index to the HashMap
            numToIndex.put(nums[i], i);
        }
        
        // If no solution is found, return an empty array (though the problem guarantees one solution)
        return new int[0];
    }
}