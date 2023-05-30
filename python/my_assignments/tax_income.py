def compute_tax(status: str, tax_income: float):
    if tax_income < 1:
        return f"task income cannot be negative"
    if tax_income < 50000:
        return "Your task income cannot be "
    match (status):
        case "single":
            if (tax_income == 50000):
                tax_income - 8688
            elif (tax_income == 50050):
                tax_income - 8700
            elif (tax_income == 59950):
                tax_income - 11175
            else:
                tax_income - 11188

# ayinladesikiru@gmail.com
