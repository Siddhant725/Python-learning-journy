department=[
    {"name":"alex","hours":40,"rate":20},
    {"name":"sam","hours":50,"rate":22},
    {"name":"sara","hours":35,"rate":25}
]

total_company_cost=0

for employee in department:
    if employee["hours"]>40:
        pay=employee["hours"]*employee["rate"]*1.5
    else:
        pay=employee["hours"]*employee["rate"]
    total_company_cost+=pay
    print(f"{employee['name']} earned ${pay:.2f}")

print(f"Total company cost: ${total_company_cost:.2f}")