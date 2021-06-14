import java.util.Arrays;

class Solution {
    public int twoSumLessThanK(int[] nums, int k) {
        Arrays.sort(nums);
        int pointer1 = 0;
        int pointer2 = nums.length - 1;
        int ans = -1;
        while (pointer1 < pointer2) {
            int sum = nums[pointer1] + nums[pointer2];
            if (sum < k) {
                if (sum > ans) {
                    ans = sum;
                }
                pointer1++;
            } else {
                pointer2--;
            }
        }
        return ans;

    }
}