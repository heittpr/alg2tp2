#include "knapsack.h"

#include <algorithm>
#include <vector>

ull GreedySolver::solve() {
  std::vector<Item> items;
  for (auto[v, w] : inst.items)
    if (w <= inst.capacity) items.push_back({v, w});
  std::sort(items.begin(), items.end());

  ull n = items.size(), capacity = inst.capacity, ans = 0;
  size_t i;
  for (i = 0; i < n; i++) {
    auto[v, w] = items[i];
    if (w <= capacity) capacity -= w, ans += v;
    else break;
  }
  
  if (i == n) return ans;
  return std::max(ans, items[i].value);
}
