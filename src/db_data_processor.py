from data_processor_interface import AbstractDataProcessor



"""
WITH oe AS (
    SELECT
        MAX(t1.bk_data_stor_instn_id) bk_data_stor_instn_id,
        dsi.bk_test_cyc_cd bk_test_cyc_cd,
        scn.bk_macro_scn_skey bk_macro_scn_skey,
        nvl(scn.bk_descn,'') bk_macro_scn_cd,
        nvl(snstv.bk_snstv_skey, '') bk_snstv_skey,
        nvl(snstv.bk_nm, '') bk_snstv,
        ts.bk_as_of_dt bk_as_of_dt
    FROM
        bkxcrp1.bk_car_macro_econ_var_tm_sers t1
    JOIN bk_data_stor_instn dsi ON t1.bk_data_stor_instn_id = dsi.bk_data_stor_instn_id
        AND t1.bk_test_cyc_cd = dsi.bk_test_cyc_cd
    JOIN bk_test_cyc ON t1.bk_test_cyc_cd = bk_test_cyc.bk_test_cyc_cd
    LEFT JOIN bk_snstv snstv ON dsi.bk_snstv_skey = snstv.bk_snstv_skey
    LEFT JOIN bk_macro_scn scn ON dsi.bk_macro_scn_skey = scn.bk_macro_scn_skey
    JOIN bk_nsf_ncm_mwf_map map ON t1.bk_data_stor_instn_id = map.bk_data_stor_instn_id
    WHERE
        map.bk_nsf_overall_stat = 'COMPLETED'
        AND dsi.bk_snstv_skey IS NULL
        AND dsi.bk_test_cyc_cd = '{testcycle}'
    GROUP BY
        dsi.bk_test_cyc_cd,
        snstv.bk_nm,
        scn.bk_macro_scn_skey,
        scn.bk_descn,
        snstv.bk_snstv_skey,
        ts.bk_as_of_dt
    ORDER BY
        ts.bk_as_of_dt
)

SELECT
    mac.ec_bk_test_cyc "TEST CYCLE",
    oe.bk_ccar_scn_cd AS "SCENARIO",
    to_char(ec_bk_as_of_dt, 'MM/DD/YYYY') AS "AS OF DATE",
    CONCAT('Q', : 1 + ROW_NUMBER() OVER(
        PARTITION BY oe.bk_test_cyc, mac.ec_bk_var_nm, oe.bk_data_stor_instn_id
        ORDER BY
            mac.ec_bk_as_of_dt
    )) AS QUARTER,
    AS RATING,

    mac.ec_bk_var_nm AS "NAME",
    mac.ec_bk_var_no AS "VARIABLE NUMBER",
    mac.ec_bk_input_val AS "INPUT VALUE"

FROM
    bkxcrp1.bk_car_macro_econ_var_tm_sers mac_ec,
    oe
WHERE
    mac.ec_bk_data_stor_instn_id = oe.bk_data_stor_instn_id
    AND mac.ec_bk_freq = 'Q'
    AND mac.ec_bk_var_no IN (var_list)
    AND mac.ec_bk_as_of_dt BETWEEN oe.bk_as_of_dt AND add_months(oe.bk_as_of_dt, ('num_q' * 3 + 1))
ORDER BY
    mac.ec_bk_test_cyc,
    mac.ec_bk_var_no,
    mac.ec_bk_as_of_dt
"""

class DBDataProcessor(AbstractDataProcessor):
    # Specyficzna logika dla procesora danych DB
    ...
