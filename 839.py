from typing import List

class Solution:
  def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    stack = []
    sorted_speed_position = list(zip(position, speed))
    # reverse sorting, so that it is easier to say which car bumps to the one in front of it
    sorted_speed_position.sort(key=lambda x:x[0], reverse=True)
    times_to_target = [(target - sorted_speed_position[i][0]) / sorted_speed_position[i][1] for i in range(len(sorted_speed_position))]
    for car in times_to_target:
      if len(stack) != 0:
        if stack[-1] >= car:
          # car bumps on the one in front of it
          continue
      stack.append(car)
    return len(stack)

solution = Solution()
result = solution.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])
print(result)