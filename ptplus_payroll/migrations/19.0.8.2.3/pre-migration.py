def migrate(cr, version):
    """
    This pre-migration script is designed to change the type of
    the code field in the hr_professional_category_pt table.
    """

    cr.execute(
        """
        ALTER TABLE hr_professional_category_pt
        ALTER COLUMN code
        TYPE varchar
        USING code::varchar;
    """
    )
