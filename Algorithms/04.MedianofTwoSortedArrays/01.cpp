class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int totalSize = nums1.size() + nums2.size();
        int targetPoint = totalSize / 2;
        double medianPoint1, medianPoint2;
        int i = 1;
        vector<int>::const_iterator iItr = nums1.cbegin();
        vector<int>::const_iterator jItr = nums2.cbegin();
        while (iItr < nums1.cend() || jItr < nums2.cend()) {
            int temp;
            if (iItr == nums1.cend()) {
                temp = *jItr;
                jItr++;
            } else if (jItr == nums2.cend()) {
                temp = *iItr;
                iItr++;
            } else if (*iItr > *jItr) {
                temp = *jItr;
                jItr++;
            } else {
                temp = *iItr;
                iItr++;
            }
            if (i == targetPoint) {
                medianPoint1 = temp;
            } else if (i == targetPoint + 1) {
                medianPoint2 = temp;
                break;
            }
            i++;
        }
        return totalSize % 2 ? medianPoint2 : (medianPoint1 + medianPoint2)/2;
    }
};