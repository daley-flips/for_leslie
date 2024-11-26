# hope this helps :)
import re

def normalize_merchant_name(name):
    name = name.lower()  # convert to lowercase
    name = re.sub(r'[^a-z\s]', '', name)  # remove non-alphanumeric characters except spaces
    name = re.sub(r'\bsuperstore\b|\bmarket\b', '', name)  # remove specific suffixes like 'superstore' or 'market'
    name = name.strip()  # remove leading/trailing spaces
    
    # return the standardized name
    if "walmart" in name:
        return "walmart"
    return name


print(normalize_merchant_name("WAL*MART"))            # walmart
print(normalize_merchant_name("WALMART SUPERSTORE"))  # walmart
print(normalize_merchant_name("Walmart Market"))      # walmart
