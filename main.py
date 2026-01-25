import dataGenerator
from graph import Graph
    
def main():
    graph = Graph(1920, 1080)
    dataGenerator.DataGenerator.GenerateDataSet(100)
    graph.Run()

if __name__ == "__main__":
    main()