scent_costs = [1000,704,405]
paraffin_cost = 60
def cost(scent,percent):
    sc = percent*scent_costs[scent]
    total_cost = (((100-percent)*paraffin_cost) + sc) / 100
    return(total_cost)
print(cost(int(input("Scent?")),int(input("Percentage?"))))
