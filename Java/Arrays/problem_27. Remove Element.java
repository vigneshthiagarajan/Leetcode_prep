class Solution {
    public int removeElement(int[] nums, int val) {
        int pointer1  = 0;
        for(int pointer2 = 0; pointer2 < nums.length; pointer2++){
            if(nums[pointer2] != val){
                nums[pointer1] = nums[pointer2];
                pointer1++;
            }
        }
        return pointer1;
    }
}