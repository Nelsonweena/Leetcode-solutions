class Solution {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] sorted = sorting(nums1, nums2);
        int len = sorted.length;
        double median;

        if (len % 2 == 1) {
            median = sorted[len / 2];
        } else {
            int mlen = len / 2;
            median = (sorted[mlen] + sorted[mlen - 1]) / 2.0;
        }

        return median;
    }

    public static int[] sorting(int[] arr1, int[] arr2) {
        int len1 = arr1.length;
        int len2 = arr2.length;
        int lentot = len1 + len2;
        int[] newarr = new int[lentot];

        for (int i = 0; i < len1; i++) {
            newarr[i] = arr1[i];
        }

        for (int i = 0; i < len2; i++) {
            newarr[len1 + i] = arr2[i];
        }

        Arrays.sort(newarr); // Simplified sorting

        return newarr;
    }
}