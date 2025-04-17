from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        寻找两个正序数组的中位数
        时间复杂度：O(log(m+n))
        空间复杂度：O(1)
        
        Args:
            nums1: 第一个有序数组
            nums2: 第二个有序数组
            
        Returns:
            两个数组合并后的中位数
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            # 在 nums1 中找到合适的分割点
            partition1 = (left + right) // 2
            # 在 nums2 中找到对应的分割点
            partition2 = (m + n + 1) // 2 - partition1
            
            # 获取分割点左右的值
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # 检查是否找到了正确的分割点
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # 如果总长度为奇数
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)
                # 如果总长度为偶数
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            # 调整搜索范围
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1

# 这是一个测试编辑
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    nums1 = [1, 3]
    nums2 = [2]
    print(f"测试用例1: nums1 = {nums1}, nums2 = {nums2}")
    print(f"中位数: {solution.findMedianSortedArrays(nums1, nums2)}")  # 应输出 2.0
    
    # 测试用例2
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(f"\n测试用例2: nums1 = {nums1}, nums2 = {nums2}")
    print(f"中位数: {solution.findMedianSortedArrays(nums1, nums2)}")  # 应输出 2.5 