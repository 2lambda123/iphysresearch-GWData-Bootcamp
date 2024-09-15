class Solution:
    """ """
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """

        :param arr: List[int]:

        """
        return next(
            (
                i
                for i in range(len(arr) - 1, -1, -1)
                if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]
            ),
            -1,
        )
