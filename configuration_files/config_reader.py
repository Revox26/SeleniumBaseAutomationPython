import configparser

config = configparser.RawConfigParser()
config.read("..//configuration_files//config.ini")


class Readconfig:

    @staticmethod
    def get_qa_sl_url():
        qa_url = config.get("url", "qa_sl_url")
        return qa_url

    @staticmethod
    def get_v1_sl_url():
        v1_url = config.get("url", "v1_sl_url")
        return v1_url

    @staticmethod
    def get_v2_sl_url():
        v2_url = config.get("url", "v2_sl_url")
        return v2_url

    @staticmethod
    def get_v3_sl_url():
        v3_url = config.get("url", "v3_sl_url")
        return v3_url

    @staticmethod
    def get_v4_sl_url():
        v4_url = config.get("url", "v4_sl_url")
        return v4_url

    @staticmethod
    def get_replica_sl_url():
        replica_url = config.get("url", "replica_sl_url")
        return replica_url

    # CSL

    @staticmethod
    def get_qa_csl_url():
        csl_qa_url = config.get("url", "qa_csl_url")
        return csl_qa_url

    @staticmethod
    def get_v1_csl_url():
        v1_url = config.get("url", "v1_csl_url")
        return v1_url

    @staticmethod
    def get_v2_csl_url():
        v2_url = config.get("url", "v2_csl_url")
        return v2_url

    @staticmethod
    def get_v3_csl_url():
        v3_url = config.get("url", "v3_csl_url")
        return v3_url

    @staticmethod
    def get_v4_csl_url():
        v4_url = config.get("url", "v4_csl_url")
        return v4_url

    @staticmethod
    def get_replica_csl_url():
        replica_url = config.get("url", "replica_csl_url")
        return replica_url

    @staticmethod
    def get_echo_csl_url():
        echo_url = config.get("url", "echo_csl_url")
        return echo_url

    @staticmethod
    def get_echo_sl_url():
        echo_url = config.get("url", "echo_sl_url")
        return echo_url

    @staticmethod
    def get_it_dev_username():
        it_username = config.get("accounts", "it_dev_user_name")
        return it_username

    @staticmethod
    def get_george_user_name():
        it_username = config.get("accounts", "george_user_name")
        return it_username

    @staticmethod
    def get_admin_simon_user_name():
        it_username = config.get("accounts", "admin_simon_user_name")
        return it_username

    @staticmethod
    def get_intermediary_username():
        it_username = config.get("accounts", "intermediary_username")
        return it_username


    @staticmethod
    def get_password():
        password = config.get("accounts", "default_password")
        return password

    @staticmethod
    def get_director_password():
        director_password = config.get("accounts", "director_password")
        return director_password
