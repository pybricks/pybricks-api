from os import path, makedirs

from docutils import nodes
from docutils.parsers.rst import Directive

from sphinx.util.osutil import copyfile

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

        # Copy required resources to static
        # CC BY-SA 4.0 via https://stackoverflow.com/a/63728208
        env = self.state.document.settings.env

        destdir = path.join(env.app.builder.outdir, '_images')
        if not path.exists(destdir):
            makedirs(destdir)

        for hub in HUB_FEATURES:
            for compat in ("true", "false"):
                uri = 'compat_{0}_{1}_label.png'.format(hub, compat)
                src_uri = path.join(env.app.builder.srcdir, 'images', uri)
                build_uri = path.join(env.app.builder.outdir, '_images', uri)
                copyfile(src_uri, build_uri)

        # Get requirements from sphinx-directive.
        requirements = set(self.arguments)

        # Cell with image of a hub.
        hub_cell = """
        <th><div class="align-default">
        <img alt="" src="../_images/compat_{0}_{1}_label.png">
        </div></th>
        """

        # Table row with hub images.
        compat_row = "".join([
            hub_cell.format(hub, "true" if requirements <= features else "false")
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
                </tbody>
            </table>
        </div>
        """.format(compat_row)

        # Return the node.
        node = nodes.raw('', html, format="html")
        return [node]


def setup(app):
    app.add_directive_to_domain(
        'py',
        'pybricks-requirements',
        PybricksRequirementsDirective
    )
