#include <iostream>
#include "knapsack.h"

int main() {
  Instance inst;

  std::cin >> inst.n >> inst.capacity;
  inst.items.resize(inst.n);
  for (auto&[v, w] : inst.items)
    std::cin >> v >> w;

  BnBSolver s(inst);
  std::cout << s.solve() << std::endl;
}
