#include "knapsack.h"

#include <vector>

FPTASSolver::FPTASSolver(const Instance& i, ld e) : Solver(i), eps(e) {}

ull FPTASSolver::solve() {
  ull maxv = 0;
  for (auto[v, w] : inst.items)
    maxv = std::max(maxv, v); 
  ld u = (eps * maxv)/inst.n;
 
  ull sumv = 0;
  for (auto&[v, w] : inst.items)
    v /= u, sumv += v;

  const ull inf = inst.capacity+1;
  std::vector dp(inst.n+1, std::vector<ull>(sumv+1, 0));
  for (size_t j = 1; j <= sumv; j++) dp[0][j] = inf;
  for (size_t i = 0; i <= inst.n; i++) dp[i][0] = 0;

  for (size_t i = 1; i <= inst.n; i++)
    for (size_t j = 1; j <= sumv; j++) {
      auto[v, w] = inst.items[i-1]; // items é 0-indexado
      dp[i][j] = dp[i-1][j];
      if (v <= j) dp[i][j] = std::min(dp[i][j], dp[i-1][j-v]+w);
    }

  /*
   * TODO: calcular valor exato
   * Multiplicar a resposta final por u pode gerar imprecisão. talvez o ideal
   * seja guardar quais elementos foram escolhidos pela dp e reconstruir a
   * resposta com os valores originais.
   */
  for (size_t j = sumv; j != static_cast<ull>(-1); j--)
    if (dp[inst.n][j] <= inst.capacity)
      return j*u;
  return 0;
}
