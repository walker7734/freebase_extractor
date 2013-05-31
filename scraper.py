__author__ = 'bdwalker'
import sys

fb = None
relations = dict()


def openFreebaseDump(file):
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


if __name__ == "__main__":
    input_file = sys.argv[1]
    openFreebaseDump(input_file)
    loadRelations("./mappings.txt")