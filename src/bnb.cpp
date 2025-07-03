#include "knapsack.h"

#include <algorithm>
#include <queue>

struct BnBSolver::State {
  ull capacity, value, idx, upper_bound = 0;

  bool operator <(const State& other) const {
    return upper_bound > other.upper_bound;
  }
};

ull BnBSolver::solve() {
  /*
   * Compara as razões v/w sem usar floats:
   * a.v/a.w > b.v/b.w <=> a.v*b.w > b.v*a.w
   */
  std::sort(inst.items.begin(), inst.items.end(), [](const Item& a, const Item& b) {
    return a.value*b.weight > b.value*a.weight;
  });

  ull ans = 0;
  
  std::priority_queue<State> q;
  
  /*
   * Calcula a cota superior de um estado e adiciona ele somente se essa cota
   * é >= a resposta atual. É difícil mover essa lógica para dentro de State
   * porque calcular a cota superior depende de inst.items.
   */
  auto add = [&](State s) -> void { 
    if (s.idx < inst.n) {
      auto[v, w] = inst.items[s.idx];
      s.upper_bound = s.value + s.capacity*v/w;
    } else {
      s.upper_bound = s.value;
    }
    if (s.upper_bound > ans) q.push(s);
  };
  
  add({inst.capacity, 0, 0});
  while (!q.empty()) {
    State s = q.top(); q.pop();
    if (s.capacity == 0 || s.idx == inst.n) {
      ans = std::max(ans, s.value);
      continue;
    }

    auto [v, w] = inst.items[s.idx];
    if (s.capacity >= w) add({s.capacity-w, s.value+v, s.idx+1});
    add({s.capacity, s.value, s.idx+1});
  }

  return ans;
}
