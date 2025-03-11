#hill Climb algorithm
annual_demand = int(input("Enter the annual demand(D): "))
holding_cost = float(input("Enter the holding cost per unit(H): "))
ordering_cost = float(input("Enter the ordering cost per order(S): "))
intial_Q = int(input("Enter the intial order quantity(Q): "))
step_size = int(input("Enter the step size for optimization: "))

def total_cost(Q): # Added Q as an argument
  ordering_cost_part = (annual_demand/Q) * ordering_cost
  holding_cost_part = (Q/2) * holding_cost
  return ordering_cost_part + holding_cost_part

def hill_climb(intial_Q, step_size): # Added intial_Q and step_size as arguments
  currunt_Q = intial_Q
  currunt_cost = total_cost(currunt_Q)

  while True:
    #Evaluate neighbour
    next_Q_up = currunt_Q + step_size
    next_Q_down = currunt_Q - step_size

    next_cost_up = total_cost(next_Q_up)
    next_cost_down = total_cost(next_Q_down)

    # cheak if neighbour have lower cost
    if next_cost_up < currunt_cost:
      currunt_Q, currunt_cost = next_Q_up, next_cost_up
    elif next_cost_down < currunt_cost:
      currunt_Q, currunt_cost = next_Q_down, next_cost_down
    else:
      # No improvement terminate
      break
  return currunt_Q, currunt_cost

optimal_Q, optimal_cost = hill_climb(intial_Q,step_size)
print(f"Optimal order quantity: {optimal_Q}")
print(f"Optimal total cost: {optimal_cost:.2f}")