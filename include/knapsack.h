#ifndef KNAPSACK_H
#define KNAPSACK_H

#include <iostream>
#include <vector>
using ull = unsigned long long;

struct Item {
  ull value, weight; 
};

struct Instance {
  ull n, capacity;
  std::vector<Item> items;
};

class Solver {
  public:
    Solver(const Instance& i) : inst(i) {};
    virtual ull solve() = 0;
  protected:
    Instance inst;
};

class BnBSolver : public Solver {
  public:
    using Solver::Solver;
    ull solve() override;
  private:
    struct State;
};


#endif
