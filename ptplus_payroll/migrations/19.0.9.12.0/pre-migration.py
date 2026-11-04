CONTRACT_REASON_CODES = {
    "a_e_a": "AEAT",
    "a_s": "ATSA",
    "c_t_s_d": "CTSD",
    "e_d_o_p": "EOPA",
    "e_t_o": "EXTO",
    "i_d_f_d_e": "IFEE",
    "l_n_a_d_i": "LNAT",
    "s_t_c_a_j": "STAJ",
    "s_t_a_t_i": "STAT",
    "s_t_c_l": "STLR",
    "s_t_t_c": "STTC",
    "o_m": "ESTA",
    "v_p_t_d": "VAPT",
    "n_i_m": "NIMO",
    "n_i_p": "NIPA",
    "r_p_t": "RAPT",
    "s_d_t_t_a": "STPS",
    "s_d_t_t_t": "STTT",
}

PROVISION_OF_WORK_CODES = {"on-site": "P", "remote": "T", "mixed": "A"}


def migrate(cr, version):
    """
    The contract reason and the provision of work now store the Social
    Security codes, so that the hiring communication (QLF-O1051) sends the
    fields as they are stored. Convert the values already saved with the old
    keys.
    """

    for column, codes in (
        ("l10n_pt_contract_reason", CONTRACT_REASON_CODES),
        ("l10n_pt_provision_of_work", PROVISION_OF_WORK_CODES),
    ):
        for old_value, ss_code in codes.items():
            cr.execute(
                f"""
                UPDATE hr_version
                SET {column} = %s
                WHERE {column} = %s;
            """,  # pylint: disable=sql-injection
                (ss_code, old_value),
            )
