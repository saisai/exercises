

class FindMedianSortedArrays {
    
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {

        int m = nums1.length;
        int n = nums2.length;

        if (m > n) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int total = m + n;
        int half = (total + 1) / 2;

        int left = 0;
        int right = m;

        double result = 0.0;

        while(left <= right) {

            int i = left + (right - left) / 2;
            int j = half - i;

            // get the four points around possible median
            int left1 = ( i > 0) ? nums1[i - 1] : Integer.MIN_VALUE;
            int right1 = (i < m) ? nums1[i] : Integer.MAX_VALUE;
            int left2 = ( j > 0) ? nums2[j- 1] : Integer.MIN_VALUE;
            int right2 = ( j < n) ? nums2[j] : Integer.MAX_VALUE;

            // partition is correct
            if(left1 <= right2 && left2 <= right) {
                // even
                if(total % 2 == 0) {
                    result = (Math.max(left1, left2) + Math.min(right1, right2)) / 2.0;
                } else {
                    //odd
                    result = Math.max(left1, left2);
                }
                break;
            }
            // partition is wrong (update left/right pointers)
            else if (left1 > right2) {
                right = i - 1;
            } else {
                left = i + 1;
            }

        }
        return result;
    }

    public static void main(String[] args) {

        int[] nums1 = {1,3};
        int[] nums2 = {2};
        // FindMedianSortedArrays obj = new findMedianSortedArrays()
        double result = findMedianSortedArrays(nums2, nums2);

        System.out.println(result);

    }
}
