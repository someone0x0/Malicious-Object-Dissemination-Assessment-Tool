import json
import yara
import hashlib

def hash_rule(hash_value):
    yara_rule = f'''
import "hash"

rule DetectDLL {{
    
    condition:
       hash.sha1(0, filesize) == "{hash_value}"
}}
'''
    return yara_rule


# Function to use YARA rule
def match_hash(hash_value):
    yara_rule = hash_rule(hash_value)
    rules = yara.compile(source=yara_rule)
    matches = rules.match(data=hash_value)
    if len(matches) > 0:
        return "match"
    else:
        return "No-match"

def main():
    # JSON data for testing add you key and value here 
    json_data = '''
    {
        "hash": "7805455ad9e3d1b8e0d65a1aaf10974532377ce7537489a74ed140cbe27a0067",
        "key2": null,
        "key3": "value3"
    }
    '''
    # dont change this line !
    data = json.loads(json_data)
    # add you function here like this call it and save the out put in result var
    if data["hash"] is not None:
        result = match_hash(data["hash"])
        print(result)
    # ex for add new if
    if data["key2"] is not None:
        print("key2 is set")

# Entry point of the script
if __name__ == "__main__":
    main()
