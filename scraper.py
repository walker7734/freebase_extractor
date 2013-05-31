__author__ = 'bdwalker'
import sys

fb = None
relations = dict()


def openFreebaseDump(file):
    global fb
    try:
        fb = open(file, "r")

    except IOError as e:
        print e.message
        sys.exit(1)


def loadRelations(file):
    global relations
    try:
        relationFile = open(file, "r")

        for relation in relationFile.readlines():
            args = relation.split("\t")
            relations[args[0].strip("\n")] = [args[i].strip("\n") for i in range(1, len(args))]

        print relations

    except IOError as e:
        print e.message
        sys.exit(1)


def outputRelations(directory):
    fileOuts = dict()
    global relations, fb

    special = {"/common/topic/alias",
               "/organization/organization/date_founded",
               "/people/deceased_person/date_of_death",
               "/business/defunct_company/ceased_operations",
               "/people/person/date_of_birth",
               "/people/person/age",
               "/common/topic/official_website"
               }

    for key in relations.keys():
        output = open(directory + "/" + key.replace("/", "_") + ".txt", "w+")
        fileOuts[key] = output

    with open("/home/bdwalker/FreeBase/freebase.tsv") as fb:
        for line in fb:
            line = line.rstrip("\n")
            splitLine = line.split("\t")
            key = splitLine[1]
            if key in special and relations[key] == []:
                print key
                fileOuts[key].write(splitLine[0] + "\t" + splitLine[3] + "\t" + key + "\n")
            elif key in relations.keys() and relations[key] == []:
                print key
                fileOuts[key].write(splitLine[0] + "\t" + splitLine[2] + "\t" + key + "\n")

    for key, value in fileOuts:
        value.close()


if __name__ == "__main__":
    input_file = sys.argv[1]
    openFreebaseDump(input_file)
    loadRelations("./mappings.txt")
    outputRelations("/home/bdwalker/FreeBase/output")