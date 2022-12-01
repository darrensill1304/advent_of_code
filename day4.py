import re


class Height:
    def __init__(self, value, units):
        self.value = value
        self.units = units


class IdDocument:
    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None

    def parse_input(self, data):
        if 'byr:' in data:
            self.byr = re.search('byr:([\S]*)', data).group(1)
        if 'iyr' in data:
            self.iyr = re.search('iyr:([\S]*)', data).group(1)
        if 'eyr' in data:
            self.eyr = re.search('eyr:([\S]*)', data).group(1)
        if 'hgt' in data:
            match = re.search('hgt:([0-9]*)([a-z]*)', data)
            self.hgt = Height(match.group(1), match.group(2))
        if 'hcl' in data:
            self.hcl = re.search('hcl:([\S]*)', data).group(1)
        if 'ecl' in data:
            self.ecl = re.search('ecl:([\S]*)', data).group(1)
        if 'pid' in data:
            self.pid = re.search('pid:([\S]*)', data).group(1)
        if 'cid' in data:
            self.cid = re.search('cid:([\S]*)', data).group(1)

    def byr_valid(self):
        if self.byr is None:
            return False
        if len(self.byr) != 4 or not self.byr.isdigit():
            return False
        return 1920 <= int(self.byr) <= 2002

    def iyr_valid(self):
        if self.iyr is None:
            return False
        if len(self.iyr) != 4 or not self.iyr.isdigit():
            return False
        return 2010 <= int(self.iyr) <= 2020

    def eyr_valid(self):
        if self.eyr is None:
            return False
        if len(self.eyr) != 4 or not self.eyr.isdigit():
            return False
        return 2020 <= int(self.eyr) <= 2030

    def hgt_valid(self):
        if self.hgt is None:
            return False

        if self.hgt.units == 'cm':
            return 150 <= int(self.hgt.value) <= 193
        if self.hgt.units == 'in':
            return 59 <= int(self.hgt.value) <= 76
        return False

    def hcl_valid(self):
        if self.hcl is None:
            return False
        if len(self.hcl) != 7:
            return False
        return re.match('#[a-fA-F0-9]{6}', self.hcl)

    def ecl_valid(self):
        if self.ecl is None:
            return False

        return self.ecl == 'amb' or \
               self.ecl == 'blu' or \
               self.ecl == 'gry' or \
               self.ecl == 'brn' or \
               self.ecl == 'grn' or \
               self.ecl == 'hzl' or \
               self.ecl == 'oth'

    def pid_valid(self):
        if self.pid is None:
            return False
        if len(self.pid) != 9:
            return False
        return re.match('[0-9]{9}', self.pid)

    def is_valid(self):
        return \
            self.byr_valid() and \
            self.iyr_valid() and \
            self.eyr_valid() and \
            self.hgt_valid() and \
            self.hcl_valid() and \
            self.ecl_valid() and \
            self.pid_valid()


valid_count = 0
id_str = ""
with open("day4-input.txt") as file:
    for line in file:
        if line == "\n":  # Blank line denotes end of document
            id_doc = IdDocument()
            id_doc.parse_input(id_str)
            if id_doc.is_valid():
                valid_count += 1
            id_str = ""
        else:
            id_str += line.rstrip() + " "

print("Number of Valid IDs: {}".format(valid_count))
