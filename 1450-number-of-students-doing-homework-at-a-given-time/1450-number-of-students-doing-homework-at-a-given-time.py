class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        count = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                count += 1
        return count
  