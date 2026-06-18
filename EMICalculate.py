def calculate_standard_emi(principal, annual_rate, tenure_years):
    """Calculates standard EMI for a lump sum loan."""
    monthly_rate = (annual_rate / 12) / 100
    months = tenure_years * 12
    
    # Formula: [P x r x (1+r)^n] / [(1+r)^n - 1]
    emi = (principal * monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return emi

def education_loan_menu():
    print("\n--- Education Loan Setup ---")
    college_duration = float(input("Enter college duration (in years): "))
    annual_fees = float(input("Enter the annual fees of your college (₹/$): "))
    annual_rate = float(input("Enter the annual interest rate (%): "))
    repayment_duration = float(input("Enter duration to pay back all fees (in years): "))
    
    # Calculate total principal based on annual fees over college duration
    total_principal = annual_fees * college_duration
    
    # Calculate EMI using our standard formula logic applied to the total fee pool
    emi = calculate_standard_emi(total_principal, annual_rate, repayment_duration)
    
    print("\n" + "="*40)
    print(f"Total College Fees (Principal): {total_principal:,.2f}")
    print(f"Your Monthly EMI will be:       {emi:,.2f}")
    print("="*40)

def personal_loan_menu():
    print("\n--- Personal Loan Setup ---")
    principal = float(input("Enter required loan amount (₹/$): "))
    annual_rate = float(input("Enter annual interest rate (%): "))
    tenure_years = float(input("Enter repayment tenure (in years): "))
    
    emi = calculate_standard_emi(principal, annual_rate, tenure_years)
    
    print("\n" + "="*40)
    print(f"Your Monthly EMI will be: {emi:,.2f}")
    print("="*40)

def main():
    while True:
        print("\n===== MULTI-LOAN EMI CALCULATOR =====")
        print("1. Personal Loan")
        print("2. Education Loan")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            personal_loan_menu()
        elif choice == '2':
            education_loan_menu()
        elif choice == '3':
            print("Thank you for using the EMI Calculator! Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()