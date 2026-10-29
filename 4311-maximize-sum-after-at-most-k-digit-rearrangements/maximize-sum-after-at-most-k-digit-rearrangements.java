class Solution {
    public long maximizeSum(int[] nums, int k) {
        int n = nums.length;
        long sum = 0;
        int[] gains = new int[n];

        for (int i = 0; i < n; i++) {
            int maxNum = rearrange(nums[i]);

            sum += nums[i];
            gains[i] = maxNum - nums[i];
        }

        Arrays.sort(gains);

        for (int i = n - 1; i >= n - k; i--) {
            sum += gains[i];
        }

        return sum;
    }

    private int rearrange(int num) {
        int[] digits = new int[10];
        int count = 0;

        while (num > 0) {
            digits[count++] = num % 10;
            num /= 10;
        }

        Arrays.sort(digits, 0, count);

        int res = 0;
        for (int i = count - 1; i >= 0; i--) {
            res = res * 10 + digits[i];
        }

        return res;
    }
}