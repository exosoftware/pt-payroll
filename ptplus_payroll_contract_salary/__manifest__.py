##############################################################################
#
#    Copyright (C) 2026 Exo Software, Lda. (<https://exosoftware.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author

{
    "name": "Portugal - Payroll Salary Configurator",
    "license": "OPL-1",
    "author": "Exo Software",
    "website": "https://github.com/exosoftware/portugal-payroll",
    "category": "Localization",
    "version": "19.0.1.1.0",
    "summary": "Portuguese fiscal profile used by the salary configurator previews",
    "depends": [
        "ptplus_payroll",
        "hr_contract_salary_payroll",
    ],
    "data": [
        "data/hr_contract_salary_personal_info_data.xml",
        "data/hr_contract_salary_resume_data.xml",
        "views/hr_contract_template_views.xml",
    ],
    "auto_install": True,
    "installable": True,
}
