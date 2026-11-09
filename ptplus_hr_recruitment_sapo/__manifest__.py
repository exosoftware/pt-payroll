##############################################################################
#
#    Copyright (C) 2016 Exo Software, Lda. (<https://exosoftware.pt>)
#
##############################################################################
# pylint: disable=license-allowed, manifest-required-author
{
    "name": "Portugal - SAPO Emprego Job Board",
    "summary": "Publish your job offers on the SAPO Emprego platform",
    "version": "19.0.1.0.0",
    "license": "OPL-1",
    "author": "Exo Software",
    "website": "https://github.com/exosoftware/portugal-payroll",
    "category": "Human Resources/Recruitment/Integration",
    "depends": ["hr_recruitment_integration_base"],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/ir_cron_data.xml",
        "data/hr_recruitment_platform_data.xml",
        "views/ptplus_sapo_code_views.xml",
        "views/hr_contract_type_views.xml",
        "views/hr_recruitment_degree_views.xml",
        "views/hr_job_post_views.xml",
        "views/res_config_settings_views.xml",
        "wizard/hr_recruitment_post_views.xml",
    ],
    "installable": True,
    "application": False,
}
