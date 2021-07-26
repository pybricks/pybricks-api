from docutils import nodes
from docutils.parsers.rst import Directive


# Base feature set.
FEATURES_SMALL = set()

# Medium feature set.
FEATURES_MEDIUM = FEATURES_SMALL | {
    'pybricks-geometry',
    'pybricks-iodevices',
    'stm32-extra',
    'stm32-float',
}

# Large feature set.
FEATURES_LARGE = FEATURES_MEDIUM | set()

# Features per hub.
HUB_FEATURES = {
    'movehub': FEATURES_SMALL,
    'cityhub': FEATURES_MEDIUM,
    'technichub': FEATURES_MEDIUM,
    'primehub': FEATURES_LARGE,
    'inventorhub': FEATURES_LARGE,
}


class PybricksRequirementsDirective(Directive):

    required_arguments = 1
    optional_arguments = 10

    def run(self):
        # Get requirements from sphinx-directive.
        requirements = set(self.arguments)

        # Check compatibility for all hubs.
        compatible = {
            hub: requirements <= features
            for hub, features in HUB_FEATURES.items()
        }

        # Table cells with hub images.
        hub_cells = ["<th>{0}</th>".format(hub) for hub in compatible]

        # Table cells with checkmark or cross.
        compat_cells = [
            "<td>✔️</td>" if compat else "<td>❌</td>"
            for hub, compat in compatible.items()
        ]

        # Generate full table.
        html = """
        <table>
            <thead>
            <tr>
                {0}
            </tr>
            </thead>
            <tbody>
            <tr>
                {1}
            </tr>
            </tbody>
        </table>
        """.format("".join(hub_cells), "".join(compat_cells))

        # Return the node.
        node = nodes.raw('', html, format="html")
        return [node]


def setup(app):
    app.add_directive_to_domain(
        'py',
        'pybricks-requirements',
        PybricksRequirementsDirective
    )
