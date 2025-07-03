#include <iostream>
#include "knapsack.h"

int main() {
  Instance inst;

  std::cin >> inst.n >> inst.capacity;
  inst.items.resize(inst.n);
  for (auto&[v, w] : inst.items)
    std::cin >> v >> w;

  FPTASSolver s(inst, 0.01);
  std::cout << s.solve() << std::endl;
}
