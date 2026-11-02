-- Drop the SAPO Emprego credentials so that a restored production database
-- can never publish, change or pause job offers on the live platform.
UPDATE res_company
   SET l10n_pt_sapo_api_token = NULL,
       l10n_pt_sapo_environment = 'sandbox';
