class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
        int ret = 0;
        for (int num : nums) {
            if (!hashMap.containsKey(num)) {
                hashMap.put(num, 1);
            } else {
                hashMap.put(num, hashMap.get(num) + 1);
            }
            if (hashMap.get(num) > nums.length / 2) {
                ret = num;
                break;
            }
        }

        return ret;
    }
}