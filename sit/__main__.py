from sit.cli import sit


# TODO: move global variables to default argument values for click commands
CONFIG_PATH = "./.config"


def main():
    """Run 'sit' CLI command."""
    sit()


# Uncomment to debug
# if __name__ == "__main__":
#     main()
