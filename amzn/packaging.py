def maxNumPackages(cost):

    package_cost_count = {}

    for c in cost:

        if c not in package_cost_count:
            package_cost_count[c] = 0
        
        package_cost_count[c] += 1
        
    package_costs = list(package_cost_count.keys())
    for i in range(len(package_costs)):
        c1 = package_cost_count[i]

        package_cost_count[2*c1] = package_cost_count[c1] // 2

        for j in range(i + 1, len(package_costs)):

            c2 = package_costs[j]
            if c1+c2 not in package_cost_count:
                package_cost_count[c1+c2] = 0
            package_cost_count[c1+c2] += min(package_cost_count[c1], package_cost_count[c2])
    
    print(package_cost_count)
    return max(package_cost_count.values())


print(maxNumPackages([4, 5, 10, 3, 1, 2, 2, 2, 3]))

