
import os

class AccountRulesPropertiesLoader:
    def __init__(self, config_dir="gdb/resources/config/rules"):
        self.config_dir = config_dir

    def load_properties(self, filepath):
        props = {}
        if not os.path.exists(filepath):
            return props
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, val = line.split('=', 1)
                    props[key.strip()] = val.strip()
        return props

    def load_all_rules(self):
        rules = {}
        if not os.path.exists(self.config_dir):
            return rules
            
        for filename in os.listdir(self.config_dir):
            if filename.endswith(".properties"):
                account_type = filename.split('.')[0].upper()
                rules[account_type] = self.load_properties(os.path.join(self.config_dir, filename))
        return rules
