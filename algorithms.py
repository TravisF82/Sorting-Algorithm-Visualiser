from bar import Bar

class Algorithm:
    def BubbleSort():
        total_swaps = 0
        compare = 0
        swaps = 1
        while swaps > 0:
            swaps = 0
            for i in range(len(Bar.bars) - 1):
                compare += 1
                yield i, compare, total_swaps
                if Bar.bars[i].val > Bar.bars[i + 1].val:
                    temp = Bar.bars[i]
                    Bar.bars[i] = Bar.bars[i + 1]
                    Bar.bars[i + 1] = temp
                    swaps += 1
                    total_swaps += 1

    """
    Time Complexity: O(n^2)
    """
    def SelectionSort():
        total_swaps = 0
        compare = 0
        n = len(Bar.bars)
        for i in range(n):
            current = Bar.bars[i]
            smallest = current
            smallestIndex = i
            for j in range(i, n):
                compare += 1
                yield j, compare, total_swaps
                if Bar.bars[j].val < Bar.bars[smallestIndex].val:
                    smallest = Bar.bars[j]
                    smallestIndex = j
                    total_swaps += 1

            Bar.bars[i] = smallest
            Bar.bars[smallestIndex] = current
            
    def InsertionSort(data: list[int]) -> list[int]:
        n = len(data)
        for i in range(n):
            ...

    def QuickSort():
        ...

    def HeapSort(data=None):
        middle = len(data) // 2
        half1, half2 = data[:middle], data[middle:]

    def MergeSort():
        pass

    algorithms = [BubbleSort, SelectionSort]