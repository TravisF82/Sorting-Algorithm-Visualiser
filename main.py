import dataGenerator
import algorithms
from graph import Graph
    

def main():
    graph = Graph(1280, 720, algorithms.SelectionSort)
    dataGenerator.DataGenerator.GenerateDataSet(50)
    graph.Run()

if __name__ == "__main__":
    main()