CXX = g++
CXXFLAGS = -g -std=c++23 -O2 -Iinclude
CXXFLAGS += -Wall -Wshadow -Wconversion -Wextra -Wno-unused-result -Wno-sign-compare -Wno-char-subscripts
CXXFLAGS += -fsanitize=address,undefined -fno-omit-frame-pointer

SRC := $(wildcard src/*.cpp)
OBJ := $(SRC:src/%.cpp=obj/%.o)
HDR := $(wildcard include/*.hpp)

bin/tp2: $(OBJ) $(HDR) | bin
	$(CXX) $(CXXFLAGS) $(OBJ) -o bin/tp2

obj/%.o: src/%.cpp $(HDR) | obj
	$(CXX) $(CXXFLAGS) -c $< -o $@

bin:
	mkdir -p $@

obj:
	mkdir -p $@

clean:
	rm -rf bin obj
