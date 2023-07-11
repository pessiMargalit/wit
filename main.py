import sys
import wit


class WitInterface:
    @staticmethod
    def handle_commands(command, args):
        match command:
            case "init":
                wit.Wit.init()
            case "add":
                wit.Wit.add(args)
            case "commit":
                wit.Wit.commit(args)


if __name__ == "__main__":
    # TODO: handle edge cases
    command = sys.argv[1]
    args = sys.argv[2:]
    WitInterface.handle_commands(command, args)
