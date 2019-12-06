

database ={
    "A":[
            {
            'url': 'www',
            'qm_db_url': 'data-test.hzed.net',
            'qm_db_uname': 'u_ddqb_test1',
            'qm_db_pwd': 'gb2a6e9m7dm',
            'qm_db_name': 'ddqb_test1'
            }
        ],

    "B": [
        {
            'url': 'www2',
            'qm_db_url': 'data-test.hzed.net',
            'qm_db_uname': 'u_ddqb_test2',
            'qm_db_pwd': '4b2g6e7h7dX',
            'qm_db_name': 'ddqb_test2'
        }
    ],

    "C": [
        {
            'url':'www3',
            'qm_db_url': 'data-test.hzed.net',
            'qm_db_uname': 'u_ddqb_test3',
            'qm_db_pwd': 'db2gpe65mdr',
            'qm_db_name': 'ddqb_test3'
        }
    ],

    "chanel_A": [
        {
            'chanel_db_url': 'data-dev.hzed.net',
            'chanel_db_uname': 'u_channeldb_test',
            'chanel_db_pwd': 'gb2ak9m7f6y',
            'chanel_db_name': 'channeldb_test'
        }
    ],

    "chanel_B": [
        {
            'chanel_db_url': 'data-dev.hzed.net',
            'chanel_db_uname': 'chaneldb_api',
            'chanel_db_pwd': 'NVBgrSkFr3',
            'chanel_db_name': 'chaneldb_api'
        }
    ]
}


sqls = {
    '查询用户信息':'''SELECT id from t_qm_app_user_accunt_info t WHERE t.mobile ='{mobile}'; ''',
    '更新渠道user表用户类型':'''
                update t_user set customer_classify='CC02' WHERE mobile='{mobile}';''',

    '更新渠道t_loan_apply表': '''
                UPDATE t_loan_apply 
                SET push_status = 2,
                order_status = 5,
                audit_time = '{Time}',
                withdraw_status = 1,
                withdraw_time = '{Time}',
                audit_conclusion = '[SZ02]',
                score = 0,
                audit_amount = '15000'
                WHERE
                    mobile = '{mobile}';''',
    '更新全民库订单表': '''
                UPDATE t_qm_app_order 
                SET order_status = '{status}',
                approval_amount = 15000,
                approval_time = '{Time}',
                confirm_time = '{Time}' 
                WHERE
                    user_id = '{userid}';
              ''',

    '查询全民订单号': '''
                SELECT order_no from t_qm_app_order WHERE user_id='{userid}';
              '''


}

database1 ={
    "chanel_A": [
        {
            'chanel_db_url': 'data-dev.hzed.net',
            'chanel_db_uname': 'u_channeldb_test',
            'chanel_db_pwd': 'gb2ak9m7f6y',
            'chanel_db_name': 'channeldb_test'
        }
    ],

    "chanel_B": [
        {
            'chanel_db_url': 'data-dev.hzed.net',
            'chanel_db_uname': 'chaneldb_api',
            'chanel_db_pwd': 'NVBgrSkFr3',
            'chanel_db_name': 'chaneldb_api'
        }
    ],

    "A":[
            {
            'url': 'fenqiyi01',
            'qm_db_url': 'data-test.hzed.net',
            'qm_db_uname': 'u_fqy_test1',
            'qm_db_pwd': 's32a7e9mr6m',
            'qm_db_name': 'fqy_test1'
            }
        ],

    "B": [
        {
            'url': 'fenqiyi02',
            'qm_db_url': 'data-test.hzed.net',
            'qm_db_uname': 'u_fqy_test2',
            'qm_db_pwd': 'gb2a6ehqnhm',
            'qm_db_name': 'fqy_test2'
        }
    ],

    "C": [
        {
            'url':'fenqiyi03',
            'qm_db_url': 'data-test.hzed.net',
            'qm_db_uname': 'u_fqy_test3',
            'qm_db_pwd': '1dcarv9m7mn',
            'qm_db_name': 'fqy_test3'
        }
    ]
}


sqls1 = {
    '查询用户信息':'''SELECT id from t_qm_app_user_account_info t WHERE t.mobile ='{mobile}'; ''',
    '更新渠道user表用户类型':'''
                update t_user set customer_classify='CC02' WHERE mobile='{mobile}';''',

    '更新渠道t_loan_apply表': '''
                UPDATE t_loan_apply
                SET push_status = 2,
                order_status = 5,
                audit_time = '{Time}',
                withdraw_status = 1,
                withdraw_time = '{Time}',
                audit_conclusion = '[SZ02]',
                score = 0,
                audit_amount = '15000'
                WHERE
                    mobile = '{mobile}';''',
    '更新全民库订单表': '''
                UPDATE t_qm_app_order
                SET order_status = '{status}',
                approval_amount = 15000,
                approval_time = '{Time}',
                confirm_time = '{Time}'
                WHERE
                    user_id = '{userid}';
              ''',

    '查询全民订单号': '''
                SELECT order_no from t_qm_app_order WHERE user_id='{userid}';
              '''


}