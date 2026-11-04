def migrate(cr, version):
    """
    Create the column of the Social Security leave option before the module
    loads, so the ORM does not compute it on the existing time off types: that
    would refuse the types without "Ignore Public Holidays". The end-migration
    sets both options.
    """
    cr.execute(
        "ALTER TABLE hr_leave_type "
        "ADD COLUMN IF NOT EXISTS l10n_pt_social_security_leave BOOLEAN"
    )
