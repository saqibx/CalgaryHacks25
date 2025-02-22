
import google.genai.types as types
from google import genai

import RentersMethods.Instructions
from config import Config
GEMINI_API_KEY = Config.GEMINI_KEY
client = genai.Client(api_key=GEMINI_API_KEY)
input = RentersMethods.Instructions.example_files


data_list = [
    {
        "text_input": input[0],
        "output": {
            "lease_terms": {
                "lease_term": "12-month fixed term, automatically renewing unless a 60-day written notice is provided.",
                "rent_payment": "$1,800 per month, due on the 1st. $75 late fee after the 5th.",
                "deposits": "Security deposit of $1,800 held in escrow, refunded within 14 days after move-out if no damages.",
                "rules": "Tenant responsible for all maintenance under $200. No unauthorized guests staying for more than 14 days.",
                "termination": "Early termination requires three months' rent as penalty unless a replacement tenant is found.",
                "additional_provisions": "Landlord reserves the right to install surveillance cameras in common areas."
            },
            "potential_issues": {
                "early_termination_penalty": "The penalty for early termination is excessive and may be unenforceable.",
                "guest_restrictions": "Restricting guest stays to 14 days may violate tenant privacy rights.",
                "maintenance_responsibility": "Tenant being responsible for all minor repairs can be unfair and costly.",
                "surveillance": "Surveillance cameras in common areas raise privacy concerns."
            },
            "recommendations": {
                "negotiation": "Tenant should negotiate the early termination penalty to be more reasonable.",
                "deposit_return": "Ensure security deposit return terms are clearly defined and comply with local laws.",
                "privacy_rights": "Verify if guest restrictions comply with provincial tenancy regulations.",
                "surveillance_laws": "Tenant should inquire whether surveillance is legally permissible in common areas."
            },
            "interaction_with_provincial_laws": {
                "deposit_refund_timeline": "Provincial laws may require the security deposit to be refunded within a set period, typically 10-30 days.",
                "tenant_repairs": "Some jurisdictions prohibit landlords from passing all minor maintenance costs to tenants.",
                "privacy_protection": "Laws may restrict the landlord’s ability to install surveillance cameras without tenant consent."
            },
            "remedies": {
                "challenging_unfair_clauses": "Tenant can challenge unreasonable lease clauses through the provincial tenancy board.",
                "deposit_disputes": "If the deposit is not refunded in compliance with the law, the tenant can file a formal complaint.",
                "privacy_rights_violation": "Tenant can seek legal action if the landlord's surveillance measures violate privacy laws."
            },
            "fairness_score": 3,
            "observations": "While the lease has some standard protections, certain clauses, particularly those regarding guest restrictions and surveillance, are concerning."
        }
    },
    {
        "text_input": input[1],
        "output": {
            "lease_terms": {
                "lease_term": "Month-to-month, renewing automatically unless terminated with 30 days' notice.",
                "rent_payment": "$1,600 per month. Late fee of $50 applies after the 3rd.",
                "deposits": "Non-refundable pet deposit of $500, security deposit of $1,600 refundable within 21 days.",
                "rules": "Quiet hours enforced from 10 PM to 6 AM. No short-term subleasing allowed.",
                "termination": "Landlord may terminate lease with 45 days' notice but requires 60 days from the tenant.",
                "additional_provisions": "Landlord may enter for inspections with 12-hour notice."
            },
            "potential_issues": {
                "termination_asymmetry": "Landlord requiring only 45 days' notice while tenant needs 60 days is unfair.",
                "late_fees": "The $50 late fee is high and may exceed provincial legal limits.",
                "non_refundable_pet_deposit": "Some provinces require pet deposits to be refundable.",
                "entry_notice": "12-hour entry notice is shorter than the standard 24 hours required by law."
            },
            "recommendations": {
                "lease_flexibility": "Negotiate equal notice periods for both landlord and tenant.",
                "late_fee_adjustment": "Ensure late fees do not exceed legal limits.",
                "deposit_terms": "Request clarification on whether pet deposits are refundable."
            },
            "interaction_with_provincial_laws": {
                "late_fee_regulations": "Check if local laws cap the maximum late fee landlords can charge.",
                "notice_periods": "Provincial tenancy laws often require equal termination notice for landlords and tenants.",
                "deposit_legislation": "Some provinces mandate pet deposits to be refundable."
            },
            "remedies": {
                "lease_dispute_resolution": "If unreasonable clauses remain, tenants can challenge them through provincial tenancy authorities.",
                "reporting_unfair_terms": "Tenants can file complaints if landlords impose illegal fees or notice periods."
            },
            "fairness_score": 5,
            "observations": "While the lease contains reasonable terms, the unequal notice periods and high late fees need revision."
        }
    },
    {
        "text_input": input[3],
        "output": {
            "lease_terms": {
                "lease_term": "Fixed 8-month lease, then converts to a month-to-month agreement.",
                "rent_payment": "$2,100 per month, paid via bank transfer or certified check.",
                "deposits": "Security deposit of $2,100, refundable within 15 days upon move-out.",
                "rules": "No unauthorized modifications. Tenant responsible for snow removal.",
                "termination": "Early termination requires 45 days' notice and forfeiture of the last month's rent.",
                "additional_provisions": "Lease renewal terms must be negotiated 30 days before expiration."
            },
            "potential_issues": {
                "early_termination": "Forfeiting the last month’s rent may be an unlawful penalty.",
                "payment_restrictions": "Limiting payment to bank transfers and certified checks may be inconvenient.",
                "tenant_responsibilities": "Snow removal should be clarified as either tenant or landlord responsibility."
            },
            "recommendations": {
                "legal_review": "Tenant should confirm that the lease aligns with provincial early termination laws.",
                "payment_options": "Negotiate additional payment methods such as e-transfers for convenience."
            },
            "interaction_with_provincial_laws": {
                "security_deposit_return": "Provincial regulations may require deposits to be refunded within a set timeframe.",
                "lease_extension_rules": "Some provinces require landlords to offer clear renewal terms before expiration."
            },
            "remedies": {
                "challenging_unlawful_penalties": "If required, the tenant can file a dispute over penalties for early termination.",
                "lease_modifications": "Request written confirmation if modifications to lease terms are agreed upon."
            },
            "fairness_score": 6,
            "observations": "Most clauses are standard, but the early termination penalty and limited payment options could be improved."
        }
    }
]



training_dataset = types.TuningDataset(
examples = [
    types.TuningExample(
        text_input=input[0],
        output={
            "lease_terms": {
                "lease_term": "12-month fixed term, automatically renewing unless a 60-day written notice is provided.",
                "rent_payment": "$1,800 per month, due on the 1st. $75 late fee after the 5th.",
                "deposits": "Security deposit of $1,800 held in escrow, refunded within 14 days after move-out if no damages.",
                "rules": "Tenant responsible for all maintenance under $200. No unauthorized guests staying for more than 14 days.",
                "termination": "Early termination requires three months' rent as penalty unless a replacement tenant is found.",
                "additional_provisions": "Landlord reserves the right to install surveillance cameras in common areas."
            },
            "potential_issues": {
                "early_termination_penalty": "The penalty for early termination is excessive and may be unenforceable.",
                "guest_restrictions": "Restricting guest stays to 14 days may violate tenant privacy rights.",
                "maintenance_responsibility": "Tenant being responsible for all minor repairs can be unfair and costly.",
                "surveillance": "Surveillance cameras in common areas raise privacy concerns."
            },
            "recommendations": {
                "negotiation": "Tenant should negotiate the early termination penalty to be more reasonable.",
                "deposit_return": "Ensure security deposit return terms are clearly defined and comply with local laws.",
                "privacy_rights": "Verify if guest restrictions comply with provincial tenancy regulations.",
                "surveillance_laws": "Tenant should inquire whether surveillance is legally permissible in common areas."
            },
            "interaction_with_provincial_laws": {
                "deposit_refund_timeline": "Provincial laws may require the security deposit to be refunded within a set period, typically 10-30 days.",
                "tenant_repairs": "Some jurisdictions prohibit landlords from passing all minor maintenance costs to tenants.",
                "privacy_protection": "Laws may restrict the landlord’s ability to install surveillance cameras without tenant consent."
            },
            "remedies": {
                "challenging_unfair_clauses": "Tenant can challenge unreasonable lease clauses through the provincial tenancy board.",
                "deposit_disputes": "If the deposit is not refunded in compliance with the law, the tenant can file a formal complaint.",
                "privacy_rights_violation": "Tenant can seek legal action if the landlord's surveillance measures violate privacy laws."
            },
            "fairness_score": 3,
            "observations": "While the lease has some standard protections, certain clauses, particularly those regarding guest restrictions and surveillance, are concerning."
        }
    ),

    types.TuningExample(
        text_input=input[1],
        output={
            "lease_terms": {
                "lease_term": "Month-to-month, renewing automatically unless terminated with 30 days' notice.",
                "rent_payment": "$1,600 per month. Late fee of $50 applies after the 3rd.",
                "deposits": "Non-refundable pet deposit of $500, security deposit of $1,600 refundable within 21 days.",
                "rules": "Quiet hours enforced from 10 PM to 6 AM. No short-term subleasing allowed.",
                "termination": "Landlord may terminate lease with 45 days' notice but requires 60 days from the tenant.",
                "additional_provisions": "Landlord may enter for inspections with 12-hour notice."
            },
            "potential_issues": {
                "termination_asymmetry": "Landlord requiring only 45 days' notice while tenant needs 60 days is unfair.",
                "late_fees": "The $50 late fee is high and may exceed provincial legal limits.",
                "non_refundable_pet_deposit": "Some provinces require pet deposits to be refundable.",
                "entry_notice": "12-hour entry notice is shorter than the standard 24 hours required by law."
            },
            "recommendations": {
                "lease_flexibility": "Negotiate equal notice periods for both landlord and tenant.",
                "late_fee_adjustment": "Ensure late fees do not exceed legal limits.",
                "deposit_terms": "Request clarification on whether pet deposits are refundable."
            },
            "interaction_with_provincial_laws": {
                "late_fee_regulations": "Check if local laws cap the maximum late fee landlords can charge.",
                "notice_periods": "Provincial tenancy laws often require equal termination notice for landlords and tenants.",
                "deposit_legislation": "Some provinces mandate pet deposits to be refundable."
            },
            "remedies": {
                "lease_dispute_resolution": "If unreasonable clauses remain, tenants can challenge them through provincial tenancy authorities.",
                "reporting_unfair_terms": "Tenants can file complaints if landlords impose illegal fees or notice periods."
            },
            "fairness_score": 5,
            "observations": "While the lease contains reasonable terms, the unequal notice periods and high late fees need revision."
        }
    ),

    types.TuningExample(
        text_input=input[3],
        output={
            "lease_terms": {
                "lease_term": "Fixed 8-month lease, then converts to a month-to-month agreement.",
                "rent_payment": "$2,100 per month, paid via bank transfer or certified check.",
                "deposits": "Security deposit of $2,100, refundable within 15 days upon move-out.",
                "rules": "No unauthorized modifications. Tenant responsible for snow removal.",
                "termination": "Early termination requires 45 days' notice and forfeiture of the last month's rent.",
                "additional_provisions": "Lease renewal terms must be negotiated 30 days before expiration."
            },
            "potential_issues": {
                "early_termination": "Forfeiting the last month’s rent may be an unlawful penalty.",
                "payment_restrictions": "Limiting payment to bank transfers and certified checks may be inconvenient.",
                "tenant_responsibilities": "Snow removal should be clarified as either tenant or landlord responsibility."
            },
            "recommendations": {
                "legal_review": "Tenant should confirm that the lease aligns with provincial early termination laws.",
                "payment_options": "Negotiate additional payment methods such as e-transfers for convenience."
            },
            "interaction_with_provincial_laws": {
                "security_deposit_return": "Provincial regulations may require deposits to be refunded within a set timeframe.",
                "lease_extension_rules": "Some provinces require landlords to offer clear renewal terms before expiration."
            },
            "remedies": {
                "challenging_unlawful_penalties": "If required, the tenant can file a dispute over penalties for early termination.",
                "lease_modifications": "Request written confirmation if modifications to lease terms are agreed upon."
            },
            "fairness_score": 6,
            "observations": "Most clauses are standard, but the early termination penalty and limited payment options could be improved."
        }
    ),
types.TuningExample(
        text_input=input[4],
        output={
            "lease_terms": {
                "lease_term": "24-month lease, automatically renewing unless a 90-day notice is given.",
                "rent_payment": "$2,400 per month, due by the 5th. Late fee of $100 after the 7th.",
                "deposits": "Security deposit of $2,400, refundable within 30 days, minus damages.",
                "rules": "Tenant responsible for appliance maintenance. No smoking indoors.",
                "termination": "Early termination requires six months' rent as a penalty.",
                "additional_provisions": "Rent discount of $100/month for tenants paying 6 months upfront."
            },
            "potential_issues": {
                "early_termination_penalty": "Requiring six months' rent for early termination is likely excessive.",
                "appliance_maintenance": "Responsibility for appliance maintenance should belong to the landlord.",
                "late_fee_amount": "A $100 late fee after 7 days may violate provincial limits."
            },
            "recommendations": {
                "negotiate_termination": "Request a more reasonable lease-breaking penalty.",
                "clarify_appliance_maintenance": "Ensure the lease specifies that landlords maintain major appliances.",
                "review_late_fees": "Verify if provincial regulations cap late fees."
            },
            "interaction_with_provincial_laws": {
                "lease_renewal": "Some provinces require landlords to provide lease renewal options in writing.",
                "late_fee_limits": "Provincial law may prohibit excessive late fees."
            },
            "remedies": {
                "dispute_excessive_fees": "File a complaint with the tenancy board if late fees exceed legal limits."
            },
            "fairness_score": 4,
            "observations": "While rent discounts are a good incentive, the lease has overly strict penalties and questionable clauses."
        }
    ),

    # 5
    types.TuningExample(
        text_input=input[3],
        output={
            "lease_terms": {
                "lease_term": "Month-to-month lease, 60-day notice required from either party for termination.",
                "rent_payment": "$1,900 per month. No grace period for late payments.",
                "deposits": "Non-refundable move-in fee of $300, security deposit of $1,900 refundable.",
                "rules": "No overnight guests for more than two consecutive nights.",
                "termination": "Landlord can terminate for ‘any reason’ with 60 days’ notice.",
                "additional_provisions": "Tenant required to provide professional cleaning service before move-out."
            },
            "potential_issues": {
                "termination_rights": "Landlord terminating without cause may be problematic.",
                "overnight_guest_restrictions": "Limiting guests to two nights may infringe on tenant rights.",
                "cleaning_requirement": "Forcing professional cleaning could be an unfair expense."
            },
            "recommendations": {
                "modify_guest_policy": "Ensure guest policies do not unreasonably restrict tenants.",
                "challenge_cleaning_fee": "Negotiate the removal of mandatory professional cleaning."
            },
            "interaction_with_provincial_laws": {
                "tenant_protection": "Landlord termination policies may require valid reasoning in some provinces."
            },
            "remedies": {
                "file_a_dispute": "If unfairly evicted, the tenant can file a dispute with the tenancy board."
            },
            "fairness_score": 5,
            "observations": "Guest restrictions and cleaning fees make this lease less tenant-friendly."
        }
    ),

    # 6
    types.TuningExample(
        text_input=input[2],
        output={
            "lease_terms": {
                "lease_term": "One-year lease with an automatic 10% rent increase on renewal.",
                "rent_payment": "$2,700 per month. Must be paid in cryptocurrency.",
                "deposits": "Security deposit of $2,700, refundable with proof of no damage.",
                "rules": "Tenant must allow landlord quarterly inspections.",
                "termination": "Lease cannot be terminated early except in emergencies.",
                "additional_provisions": "Landlord provides free internet and cleaning once a month."
            },
            "potential_issues": {
                "rent_increase": "Automatic 10% rent increases are excessive.",
                "crypto_only_payment": "Requiring payment in cryptocurrency limits tenant options.",
                "inspection_frequency": "Quarterly inspections may violate tenant privacy."
            },
            "recommendations": {
                "adjust_rent_increases": "Negotiate a rent increase cap in line with local laws.",
                "request_payment_flexibility": "Ask for additional payment options beyond cryptocurrency."
            },
            "interaction_with_provincial_laws": {
                "rent_control": "Some provinces require rent increases to be justified."
            },
            "remedies": {
                "file_a_complaint": "If excessive rent hikes occur, file a dispute with the rental authority."
            },
            "fairness_score": 3,
            "observations": "The lease offers benefits but is highly restrictive in terms of rent increases and payment methods."
        }
    ),

    # 7-15 (More Unique Cases Covering Various Lease Scenarios)

    types.TuningExample(
        text_input="input_data",
        output={
            "lease_terms": {
                "lease_term": "Fixed-term 8-month lease, cannot be extended without landlord approval.",
                "rent_payment": "$2,100 per month, paid via cash only.",
                "deposits": "Security deposit of $2,100, refundable after a 60-day waiting period.",
                "rules": "No visitors allowed past 10 PM. No pet ownership permitted.",
                "termination": "Tenant must give 90 days’ notice for early termination.",
                "additional_provisions": "Landlord can increase rent every six months without notice."
            },
            "potential_issues": {
                "visitor_policy": "Restricting visitors past 10 PM may violate tenant rights.",
                "cash-only_payment": "Forcing cash payments could be problematic for record-keeping.",
                "rent_increases": "Unnotified rent increases are likely illegal."
            },
            "recommendations": {
                "request_digital_payments": "Ensure there is a paper trail for rent payments.",
                "challenge_rent_hikes": "Ask for a defined schedule of rent increases."
            },
            "interaction_with_provincial_laws": {
                "tenant_protection": "In most provinces, rent increases require advance notice."
            },
            "remedies": {
                "report_illegal_increases": "If rent increases without notice, file a legal complaint."
            },
            "fairness_score": 2,
            "observations": "Landlord retains too much power; tenant protections are weak."
        }
    )



]

)
tuning_job = client.tunings.tune(
    base_model='models/gemini-2.0-flash',
    training_dataset=data_list,
    config=types.CreateTuningJobConfig(
        epoch_count= 5,
        batch_size=4,
        learning_rate=0.001,
        tuned_model_display_name="test tuned model"
    )
)

sample = RentersMethods.Instructions.sample_contract
response = client.models.generate_content(
    model=tuning_job.tuned_model.model,
    contents=sample,
)

print(response.text)

