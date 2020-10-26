import plistlib
import yaml


def parse_plist(plist_file):
    with open(plist_file, 'rb') as fp:
        orig = plistlib.load(fp)

    return orig


def write_yaml(yml_file, orig):

    new = {'name': 'expanso-latex', 'parent': 'default', 'matches': []}

    new['matches'] = [{'trigger': entry['shortcut'] + "\\",
                       'replace': entry['phrase']} for entry in orig]

    with open(yml_file, 'w') as fp:
        yaml.dump(new, fp)


if __name__ == "__main__":
    plist_file = './original/LaTeX Subsitutions.plist'
    yml_file = './espanso-latex/0.1.0/package.yml'

    orig = parse_plist(plist_file)
    write_yaml(yml_file, orig)
