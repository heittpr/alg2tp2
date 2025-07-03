#include "knapsack.h"

/*
 * Compara as razões v/w sem usar floats:
 * a.v/a.w > b.v/b.w <=> a.v*b.w > b.v*a.w
 */
bool Item::operator <(const Item& other) const {
  return value*other.weight > other.value*weight;
}

Solver::Solver(const Instance& i) : inst(i) {}
