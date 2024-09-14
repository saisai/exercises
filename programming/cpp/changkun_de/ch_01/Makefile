C = gcc
CXX = g++

SOURCE_C = foo.c
OBJECTS_C = foo.o

SOURCE_CXX = 001.cpp

TARGET = 1.1
#LDFLAGS_COMMON = -std=c++2a

all:
	$(C) -c $(SOURCE_C)
	$(CXX) $(SOURCE_CXX) $(OBJECTS_C) $(LDFLAGS_COMMON) -o $(TARGET)

clean:
	rm -rf *.o $(TARGET)
