CXX = g++
CXXFLAGS = -Wall -g

main: main.o algorithm.o sort_util.o
	$(CXX) $(CXXFLAGS) -o main main.o algorithm.o sort_util.o

main.o: main.cpp algorithm.cpp sort_util.cpp
	$(CXX) $(CXXFLAGS) -c main.cpp

algorithm.o: algorithm.h

sort_util.o: sort_util.h

clean:
	rm main *.o


