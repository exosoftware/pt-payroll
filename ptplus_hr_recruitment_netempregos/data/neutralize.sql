-- Drop the Net-Empregos credentials so that a restored production database
-- can never publish or delete job offers on the live platform.
UPDATE res_company
   SET l10n_pt_netempregos_api_key = NULL;
