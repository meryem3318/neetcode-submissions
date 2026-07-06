class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        list_cars = list(zip(position, speed))
        list_cars.sort()
        stack = []

        for p, s in list_cars[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)




        