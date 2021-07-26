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

        # Cell with image of a hub.
        hub_cell = """
        <th><div class="align-default">
        <img alt="" src="../_images/{0}.png">
        </div></th>
        """

        # Table row with hub images.
        hub_row = "".join([hub_cell.format(hub) for hub in HUB_FEATURES])

        # Cell with checkmark or cross.
        compat_cell = """<td><div style="text-align: center;">{0}</div></td>"""

        # Table row with checkmark or cross.
        compat_row = "".join([
            compat_cell.format("✔️" if requirements <= features else "❌")
            for hub, features in HUB_FEATURES.items()
        ])

        # Generate full table.
        html = """
        <div class="wy-table-responsive">
            <table class="docutils align-default">
                <tbody>
                    <tr>
                        {0}
                    </tr>
                    <tr>
                        {1}
                    <tr/>
                </tbody>
            </table>
        </div>
        """.format(hub_row, compat_row)

        # Return the node.
        node = nodes.raw('', html, format="html")
        return [node]


def setup(app):
    app.add_directive_to_domain(
        'py',
        'pybricks-requirements',
        PybricksRequirementsDirective
    )
