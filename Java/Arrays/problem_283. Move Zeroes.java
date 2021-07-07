class Solution {
    public void moveZeroes(int[] nums) {
        int pointer1 = 0;
        int count_zeroes = 0;
        for (int pointer2 = 0; pointer2 < nums.length; pointer2++) {
            if (nums[pointer2] != 0) {
                nums[pointer1++] = nums[pointer2];
            }
            if (nums[pointer2] == 0) {
                count_zeroes++;
            }
        }
        for (int i = nums.length - count_zeroes; i < nums.length; i++) {
            nums[i] = 0;
        }

    }
}