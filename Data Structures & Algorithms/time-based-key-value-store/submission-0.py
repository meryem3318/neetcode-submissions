class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp, value)]
        else:
            self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # 1. If the key doesn't exist at all, return an empty string
        if key not in self.store:
            return ""
        
        values = self.store[key]
        low = 0
        high = len(values) - 1
        res = ""  # Default fallback if no valid timestamp is found
        
        # 2. Binary search for the largest timestamp <= target timestamp
        while low <= high:
            mid = (low + high) // 2
            mid_timestamp = values[mid][0]
            mid_value = values[mid][1]
            
            if mid_timestamp <= timestamp:
                # This is a valid candidate! Save it and try to find a closer (larger) one.
                res = mid_value
                low = mid + 1
            else:
                # This timestamp is too far in the future, search the left side
                high = mid - 1
                
        return res
