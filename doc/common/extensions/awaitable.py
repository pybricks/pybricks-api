"""Show ``await`` in front of multitasking functions and methods.

The Pybricks API returns awaitable objects when a run loop is active but
blocks otherwise. Such functions are annotated with ``MaybeAwaitable*``
return types. This extension:

* makes autodoc treat functions/methods returning ``MaybeAwaitable*`` as
  async (there is no public hook for this, so ``is_async`` is patched);
* renders the signature prefix as ``await`` (linked to the multitasking
  section in tools) instead of ``async``, which better matches how users
  call these functions.
"""

from collections.abc import Sequence

from docutils import nodes
from sphinx.addnodes import desc_sig_keyword
from sphinx.application import Sphinx
from sphinx.domains.python import PyFunction, PyMethod, type_to_xref
from sphinx.ext.autodoc._property_types import _FunctionDefProperties


def _is_async(self: _FunctionDefProperties) -> bool:
    if "async" in self.properties:
        return True

    try:
        return_type = self._obj.__annotations__["return"]
    except (AttributeError, KeyError):
        return False

    return "MaybeAwaitable" in str(return_type)


class _AwaitPrefixMixin:
    """Replaces the ``async`` keyword prefix with a linked ``await``."""

    def get_signature_prefix(self, sig: str) -> Sequence[nodes.Node]:
        prefix = []
        for node in super().get_signature_prefix(sig):
            if isinstance(node, desc_sig_keyword) and node.astext() == "async":
                node = type_to_xref("await", self.env, suppress_prefix=True)
            prefix.append(node)
        return prefix


class PybricksPyFunction(_AwaitPrefixMixin, PyFunction):
    pass


class PybricksPyMethod(_AwaitPrefixMixin, PyMethod):
    pass


def setup(app: Sphinx):
    _FunctionDefProperties.is_async = property(_is_async)

    app.add_directive_to_domain("py", "function", PybricksPyFunction, override=True)
    app.add_directive_to_domain("py", "method", PybricksPyMethod, override=True)

    return {"parallel_read_safe": True}
