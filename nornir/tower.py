from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

nr.config.runner.options["num_workers"]