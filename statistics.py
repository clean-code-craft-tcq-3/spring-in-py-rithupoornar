
def calculateStats(numbers):
  computedNumbers = {}
  try:
    computedNumbers["avg"] = sum(numbers)/len(numbers)
    computedNumbers["max"] = max(numbers)
    computedNumbers["min"] = min(numbers)
  except Exception as e:
    computedNumbers["avg"] = float('nan')
    computedNumbers["max"] = float('nan')
    computedNumbers["min"] = float('nan')

  return computedNumbers
