# Test all the endpoints, print out examples, and update schema files

import os
from os import environ
import sys
import urllib3
import re
import json
import getpass

# Change directory to directory of this file
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Add this version of the API to the start of the path
sys.path.insert(0, os.path.abspath("../.."))
from church_of_jesus_christ_api import ChurchOfJesusChristAPI

urllib3.disable_warnings()

username = (
    environ["CHURCH_USERNAME"] if "CHURCH_USERNAME" in environ else input("username: ")
)
password = (
    environ["CHURCH_PASSWORD"]
    if "CHURCH_PASSWORD" in environ
    else getpass.getpass("password: ")
)

api = ChurchOfJesusChristAPI(username, password)


def convert_JSON_to_simple_example(json_node, converter_func):
    type_node = type(json_node)
    if type_node == dict:
        ret_node = type_node()
        for key, value in json_node.items():
            ret_node[key] = convert_JSON_to_simple_example(value, converter_func)
    elif type_node == list and len(json_node) > 0:
        ret_node = type_node()
        ret_node.append(convert_JSON_to_simple_example(json_node[0], converter_func))
    else:
        ret_node = converter_func(json_node)
    return ret_node


# Test all getters
failed_methods = set()
if not os.path.exists("JSON_schemas"):
    os.makedirs("JSON_schemas")

actual_example = convert_JSON_to_simple_example(api.user_details, lambda leaf: leaf)
schema_example = convert_JSON_to_simple_example(
    api.user_details, lambda leaf: type(leaf).__name__
)

print(json.dumps(actual_example, indent=2, sort_keys=True))
open(f"JSON_schemas/user_details-schema.md", "w").write(
    "\n".join(
        line.replace('"', "")
        for line in json.dumps(schema_example, indent=2, sort_keys=True).split("\n")
    )
)

for attr in sorted(dir(api)):
    if re.search("^get_", attr):
        print(f"Simple example for return value of {attr}")
        try:
            ret_val = getattr(api, attr)()
            actual_example = convert_JSON_to_simple_example(ret_val, lambda leaf: leaf)
            schema_example = convert_JSON_to_simple_example(
                ret_val, lambda leaf: type(leaf).__name__
            )

            assert("accessDenied" not in schema_example or schema_example["accessDenied"] == False)

            print(json.dumps(actual_example, indent=2, sort_keys=True))

            open(f"JSON_schemas/{attr}-schema.md", "w").write(
                "\n".join(
                    line.replace('"', "")
                    for line in json.dumps(
                        schema_example, indent=2, sort_keys=True
                    ).split("\n")
                )
            )

        except KeyboardInterrupt:
            raise
        except:
            failed_methods.add(attr)

if len(failed_methods) > 0:
    print("The following getters failed:")
    print(failed_methods)
