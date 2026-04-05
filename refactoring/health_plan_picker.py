def determine_insurance_plan():
    print("Welcome to the Insurance Plan Selector!")

    # Collect user inputs
    age             = int(input("Enter your age: "))
    income          = float(input("Enter your annual income: "))
    marital_status  = input("Are you single or married? (Enter 'single' or 'married'): ").lower()
    has_children    = input("Do you have children? (yes/no): ").lower()
    health_level    = input("Do you visit the doctor a lot or have any chronic illness? (yes/no): ").lower()

    # Plan details dictionary
    plans = {
        "High-Deductible A": {
            "deductible": "3500/person, 7500/family",
            "coverage":   "80% after deductible",
            "cost":       "1100/month individual, 2300/month family",
        },
        "High-Deductible B": {
            "deductible": "4500/person, 9500/family",
            "coverage":   "80% after deductible",
            "cost":       "800/month individual, 1800/month family",
        },
        "Regular Plan A": {
            "deductible": "1500/person, 3500/family",
            "coverage":   "80% after deductible",
            "cost":       "2800/month individual, 3800/month family",
        },
        "Regular Plan B": {
            "deductible": "1500/person, 3500/family",
            "coverage":   "90% after deductible",
            "cost":       "3500/month individual, 4800/month family",
        },
        "Low Income Plan": {
            "deductible": "No deductible",
            "coverage":   "90% coverage",
            "cost":       "1000/month individual, 2000/month family",
        },
    }

    if age <= 18:
        print("Sorry, you do not qualify for any plans.")
        return

    # Determine context flags used for all branching decisions below
    is_family    = (marital_status == "married" and has_children == "yes")
    is_high_need = (health_level == "yes")
    is_low_income = income < (65000 if is_family else 35000)
    is_high_income = income > 50000

    # --- Low income: always recommend Low Income Plan first ---
    if is_low_income:
        primary = "Low Income Plan"
        alternate = "Regular Plan A" if is_high_need else ("High-Deductible A" if is_family else "High-Deductible B")

    # --- Higher income, low health needs: high-deductible plans ---
    elif not is_high_need:
        if is_high_income:
            primary   = "High-Deductible A" if is_family else "High-Deductible B"
            alternate = "High-Deductible B" if is_family else "High-Deductible A"
        else:
            primary   = "High-Deductible B" if is_family else "High-Deductible A"
            alternate = "Regular Plan A"

    # --- Higher income, high health needs: full-coverage plans ---
    else:
        if is_high_income:
            primary   = "Regular Plan A"
            alternate = "Regular Plan B"
        else:
            primary   = "Regular Plan B"
            alternate = "High-Deductible A" if not is_family else "Regular Plan A"

    # Display results
    size_label = "Family" if is_family else "Individual"
    print(f"\nRecommended Plan: {primary} ({size_label})")
    print_plan_details(primary, plans)
    print(f"\nAlternate Plan: {alternate} ({size_label})")
    print_plan_details(alternate, plans)


def print_plan_details(plan_name, plans):
    """Print the deductible, coverage, and cost for the given plan."""
    print(f"\nPlan: {plan_name}")
    print(f"  Deductible: {plans[plan_name]['deductible']}")
    print(f"  Coverage:   {plans[plan_name]['coverage']}")
    print(f"  Cost:       {plans[plan_name]['cost']}")


determine_insurance_plan()
