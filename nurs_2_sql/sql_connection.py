from .config_parser import ConfigParser


def config_2_con_string(path, config_id="DEFAULT"):
    parser = ConfigParser()
    parser.read(path)

    con_template = "{dialect}://{username}:{password}@{host}:{port}"

    config = parser[config_id]

    con_string = con_template.format(**config)
    option_string = ""
    if "driver" in config:
        option_string += f"driver={config['driver']}"

    if option_string:
        con_string += "?"
        con_string += option_string

    return con_string
