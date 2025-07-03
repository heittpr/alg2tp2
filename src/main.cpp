#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define all(x) x.begin(), x.end()
using namespace std;
using ull = unsigned long long;

struct item {
  ull value, weight; 
};

ull N, W;
vector<item> items;

struct state {
  ull capacity, value, index, upper_bound;

  state(ull c, ull v, ull i) : capacity(c), value(v), index(i) {
    upper_bound = value + capacity*items[index].value / items[index].weight;
  };

  bool operator <(const state& other) const {
    return upper_bound > other.upper_bound;
  }
};

int main() {
  cin >> N >> W;
  items.resize(N);

  for (auto&[v, w] : items)
    cin >> v >> w;

  // compara as razões v/w sem usar floats
  // a.v/a.w > b.v/b.w <=> a.v*b.w > b.v*a.w
  sort(all(items), [](const item& a, const item& b) {
    return a.value*b.weight > b.value*a.weight;
  });

  ull ans = 0;
  
  priority_queue<state> q;
  q.push({W, 0, 0});

  while (!q.empty()) {
    state s = q.top(); q.pop();
      
    if (s.capacity == 0 || s.index == N-1) {
      ans = max(ans, s.value);
      continue;
    }

    auto [v, w] = items[s.index];
  
    if (s.capacity >= w) {
      state take = {s.capacity-w, s.value+v, s.index+1};
      if (take.upper_bound > ans) q.push(take);
    }

    state dont = {s.capacity, s.value, s.index+1};
    if (dont.upper_bound > ans) q.push(dont);
  }

  cout << ans << endl;
}
