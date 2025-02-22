instructions = "Analyze the provided lease or rental contract thoroughly and generate a " \
               "detailed, expert breakdown that summarizes the key lease terms and rental" \
               " obligations while identifying any contradictions, red flags, unusual clauses," \
               " hidden fees, and signs of predatory behavior. Include clear recommendations" \
               " on what actions the lessee should or should not take based solely " \
               "on the clauses, evaluate how these terms interact with applicable provincial laws," \
               " and offer guidance on available remedies or recourse if issues arise." \
               " Conclude with a fairness score on a scale from 1 to 10 and give justification," \
               " and include any other relevant observations—all without any disclaimers, " \
               "introductory statements, or extraneous commentary. Please analyze the provided " \
               "rental agreement and return the output as a JSON object with the following keys: " \
               "lease_terms\, \potential_issues\, \ recommendations\, \interaction_with_provincial_laws\," \
               " \ remedies\, \ fairness_score\, \observations\. " \
               "Ensure the output is valid JSON and does not include any additional text."

example_files = [
    "LEASE AGREEMENT This lease agreement is made between Landlord and Tenant, for the rental property located at 123 Tenant St., City, Province."
    " Lease Term: 12-month fixed term, automatically renewing unless a 60-day written notice is provided. "
    "Rent Payment: $1,800 per month, due on the 1st of each month. A $75 late fee applies after the 5th. "
    "Security Deposit: $1,800 held in escrow, refunded within 14 days after move-out, minus damages. "
    "Rules & Responsibilities: Tenant responsible for all maintenance under $200. "
    "No unauthorized guests staying more than 14 days. Landlord reserves the right to install surveillance cameras in common areas. "
    "Termination: Early termination requires three months' rent as a penalty. Tenant must provide written notice before breaking the lease.",

    "LEASE AGREEMENT This agreement is made between Landlord and Tenant, for the property at 789 Lease Ave., City, Province. "
    "Lease Term: Month-to-month lease, 60-day notice required from either party for termination. "
    "Rent Payment: $1,900 per month. No grace period for late payments. Deposits: "
    "Non-refundable move-in fee: $300. Security deposit: $1,900 (refundable). Rules & Responsibilities: No overnight guests for more than two consecutive nights. "
    "Landlord may terminate the lease with 60 days' notice for any reason. Move-Out Conditions: Tenant must hire a professional cleaning service before moving out.",

    "LEASE AGREEMENT  This agreement is made between Landlord and Tenant, for the property at 789 Lease Ave., City, Province. "
    " Lease Term: Month-to-month lease, 60-day notice "
    "required from either party for termination.  Rent Payment: $1,900 per month. No grace period for late payments. "
    "Deposits:  Non-refundable move-in fee: $300.  Security deposit: $1,900 (refundable).  Rules & Responsibilities: "
    " No overnight guests for more than two consecutive nights.  Landlord may terminate the lease with 60 days' notice for any reason.  Move-Out Conditions:  Tenant must hire a professional cleaning service before moving out. ",

    "LEASE AGREEMENT This agreement is between Landlord and Tenant, for the property at 555 Landlord St., City, Province. "
    "Lease Term: Fixed 8-month lease, cannot be extended without landlord approval. Rent Payment: $2,100 per month, paid via cash only. "
    "Deposits: Security deposit: $2,100, refundable after a 60-day waiting period. Rules & Responsibilities: "
    "No visitors allowed past 10 PM. No pets permitted. Termination: Tenant must give 90 days’ notice for early termination. "
    "Landlord may increase rent every six months without notice",

    "LEASE AGREEMENT This lease is made between Landlord and Tenant, for the property at 321 NoFlex St., City, Province. "
    "Lease Term: Fixed-term 24-month lease, automatically renewing unless a 90-day notice is given. "
    "Rent Payment: $2,400 per month, due by the 5th. Late fee of $100 after the 7th. Deposits: "
    "Security deposit: $2,400, refundable within 30 days minus damages. Rules & Responsibilities: "
    "Tenant responsible for appliance maintenance. No smoking indoors. Termination: "
    "Early termination requires six months' rent as a penalty. Additional Provisions: Rent discount of $100/month for "
    "tenants paying six months upfront.",

    ""

]

sample_contract = "This Residential Tenancy Agreement is made and entered into on June 1, 2025," \
                  " between John Peterson (the “Landlord”), residing at 4578 Maple Drive, Calgary," \
                  " Alberta, T2A 1R6, and Sarah Thompson (the “Tenant”), for the rental property" \
                  " located at Unit 203, 150 Evergreen Crescent SW, Edmonton, Alberta, T5J 4B1. " \
                  "The rental unit includes appliances such as a refrigerator, stove/oven, " \
                  "dishwasher, microwave, washer, and dryer. The Landlord shall provide water and " \
                  "heating, while the Tenant is responsible for electricity, internet, cable TV, and " \
                  "gas. The lease shall commence on June 1, 2025, and terminate on May 31, 2026, after " \
                  "which it will automatically convert to a month-to-month tenancy unless a 60-day" \
                  " written notice is provided by either party. The monthly rent is $1,850, payable" \
                  " on the 1st of each month, with acceptable payment methods including e-transfer " \
                  "to payments@maplerentals.ca, direct deposit, or certified cheque. A $50 late fee" \
                  " applies if rent is not received by the 5th of the month, with an additional $10 " \
                  "per day until paid in full. The Tenant must provide a security deposit of $1,850" \
                  " before moving in, which will be held in a trust account as per the Alberta " \
                  "Residential Tenancies Act and returned within 10 days after move-out, provided " \
                  "there are no damages or outstanding charges. The property is to be used exclusively" \
                  " for residential purposes, and only Sarah Thompson and Maxwell Thompson" \
                  " (Tenant’s minor child, Age: 8) are permitted to reside in the unit. " \
                  "Subletting or allowing additional occupants requires written approval" \
                  " from the Landlord. The Tenant is responsible for maintaining the unit in a " \
                  "clean and habitable condition, replacing lightbulbs, batteries in smoke detectors," \
                  " and furnace filters as needed, and promptly reporting necessary repairs. " \
                  "The following activities are strictly prohibited: smoking " \
                  "(including cannabis and vaping), illegal drug use, excessive noise," \
                  " unauthorized pets, and business operations without permission. " \
                  "The Landlord may enter the premises in emergency situations " \
                  "without notice or for non-emergency repairs and inspections " \
                  "with at least 24 hours’ written notice and must conduct visits between " \
                  "8:00 AM and 8:00 PM. Pets are permitted only under specific conditions;" \
                  " the Tenant is allowed one cat or one small dog (under 30 lbs.) and " \
                  "must pay a refundable pet deposit of $300. All pets must be kept inside the" \
                  " unit or on a leash outdoors, and excessive noise or damage caused by pets may" \
                  " result in fines. The Tenant is responsible for any damage beyond normal wear and " \
                  "tear, including holes in walls, excessive stains, broken appliances, or carpet" \
                  " damage, while the Landlord is responsible for major appliance repairs and " \
                  "structural maintenance. The Tenant must provide 60 days' written notice before" \
                  " vacating, while the Landlord must provide 90 days' notice for eviction without " \
                  "cause. If the Tenant terminates early, they must pay two months' rent as an early " \
                  "termination fee unless a replacement tenant is found. If the Tenant abandons the " \
                  "unit, the Landlord may seize any personal belongings left behind after 30 days and " \
                  "pursue legal action for unpaid rent and damages. This Agreement is governed by the " \
                  "Alberta Residential Tenancies Act, and any unenforceable provisions shall not " \
                  "affect the validity of the remaining terms. The Agreement constitutes the entire " \
                  "understanding between the Landlord and Tenant. Both parties must sign and date " \
                  "the Agreement for it to be legally binding. John Peterson (Landlord) and Sarah " \
                  "Thompson (Tenant) sign this agreement on June 1, 2025."


