department=[
    {"name":"chile","hours":40},
    {"name":"peru","hours":50},
    {"name":"colombia","hours":30}
]

standard_rate=25
total_company_payout=0
for employee in department:
    payout=employee["hours"]*standard_rate
    print(f"{employee['name']} | Weekely payout: ${payout}")
    total_company_payout+=payout
    
print(f"Total company payout: ${total_company_payout}")