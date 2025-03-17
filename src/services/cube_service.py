class CubeService:
    def __init__(self):
        pass
    def run_test(self) -> tuple[str,str]:
        gap = 0
        for i in range(5):
            gap += 1  # Increment gap by 1 in each iteration
        print(gap)
        return ("feng", {"testing message"})
    
