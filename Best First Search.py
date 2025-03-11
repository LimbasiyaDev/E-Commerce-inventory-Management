#Best First Search
annual_demand = int(input("Enter the annual demand(D): "))
holding_cost = float(input("Enter the holding cost per unit(H): "))
ordering_cost = float(input("Enter the ordering cost per order(S): "))
intial_Q = int(input("Enter the intial order quantity(Q): "))
step_size = int(input("Enter the step size for optimization: "))

def total_cost(Q): # Added Q as an argument
  ordering_cost_part = (annual_demand/Q) * ordering_cost
  holding_cost_part = (Q/2) * holding_cost
  return ordering_cost_part + holding_cost_part

def best_first_search(intial_Q, step_size): # Added intial_Q and step_size as arguments
  current_Q = intial_Q
  current_cost = total_cost(current_Q)
  while True:
    neighbors = [current_Q + step_size, current_Q - step_size]
    costs = {Q: total_cost(Q) for Q in neighbors if Q > 0}
    best_Q = min(costs, key=costs.get)
    best_cost = costs[best_Q]
    if best_cost >= current_cost:
      break
    current_Q, current_cost = best_Q, best_cost
  return current_Q, current_cost

optimal_Q, optimal_cost = best_first_search(intial_Q, step_size)
print(f"Optimal order quantity: {optimal_Q}")
print(f"Optimal total cost: {optimal_cost:.2f}")