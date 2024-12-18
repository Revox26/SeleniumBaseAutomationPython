import configparser

config = configparser.RawConfigParser()
config.read("..//configuration_files//config.ini")


class ReadBusinessCentreConfig:

    # SL URL
    @staticmethod
    def get_bc_staging():
        delta_url = config.get("url", "bc_staging_link")
        return delta_url
