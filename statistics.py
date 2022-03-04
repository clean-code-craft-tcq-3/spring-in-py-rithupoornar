
def calculateStats(numbers):
  computedNumbers = {}
  computedNumbers["avg"] = sum(numbers)/len(numbers)
  computedNumbers["maxNum"] = max(numbers)
  computedNumbers["minNum"] = min(numbers)
  return computedNumbers
