#include <iostream>
#include "knapsack.h"

int main(int argc, char** argv) {
  if (argc < 2) {
    std::cout << "Modo de uso: " << std::endl;
    std::cout << argv[0] << " <solver> [opções]" << std::endl;
    std::cout << std::endl;
    std::cout << "Solvers:" << std::endl;
    std::cout << "  bnb           Branch and Bound." << std::endl;
    std::cout << "  fptas <eps>   Full Polynomial-Time Approximation Scheme." << std::endl;
    std::cout << "  greedy        Guloso 2-aproximado." << std::endl;
    std::cout << std::endl;
    std::cout << "Opções:" << std::endl;
    std::cout << "  eps           Precisão para o FPTAS (0 < eps <= 1)." << std::endl;
    return 1;
  }

  std::string solver = argv[1];
  if (solver != "bnb" && solver != "fptas" && solver != "greedy") {
    std::cout << "Solver inválido: " << argv[1] << "!" << std::endl;
    std::cout << "As opções válidas são: bnb, fptas e greedy." << std::endl;
    return 1;
  }

  Instance inst;
  std::cin >> inst.n >> inst.capacity;
  inst.items.resize(inst.n);
  for (auto&[v, w] : inst.items)
    std::cin >> v >> w;

  Solver* s = nullptr;
  if (solver == "bnb") {
    s = new BnBSolver(inst);
  } else if (solver == "fptas") {
    if (argc < 3) {
      std::cout << "Especifique um valor para eps!" << std::endl;
      return 1;
    }
    long double eps = std::stold(argv[2]);
    s = new FPTASSolver(inst, eps);
  } else {
    s = new GreedySolver(inst);
  }

  std::cout << s->solve() << std::endl;
  delete s;
}
