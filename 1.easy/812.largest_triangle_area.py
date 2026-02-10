class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        # Calculate area for every combination of 3 points
        # O(n^3)
        largest_area = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    pi = points[i]
                    pj = points[j]
                    pk = points[k]
                    area = 0.5 * abs(pi[0] * (pj[1] - pk[1]) + pj[0] * (pk[1] - pi[1]) + pk[0] * (pi[1] - pj[1]))
                    largest_area = max(largest_area, area)

        return largest_area