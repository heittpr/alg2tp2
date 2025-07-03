#ifndef KNAPSACK_H
#define KNAPSACK_H

#include <iostream>
#include <vector>

using ull = unsigned long long;
using ld = long double;

struct Item {
  ull value, weight; 
};

struct Instance {
  ull n, capacity;
  std::vector<Item> items;
};

class Solver {
  public:
    Solver(const Instance& i);
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

class FPTASSolver : public Solver {
  public:
    FPTASSolver(const Instance& i, ld e);
    ull solve() override;
  private:
    ld eps;
};


#endif
