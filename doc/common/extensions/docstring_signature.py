"""Make explicit docstring signatures win over ``@overload`` signatures.

Workaround for https://github.com/sphinx-doc/sphinx/issues/10436: when a
function or method has overloads, autodoc unconditionally replaces the
signature(s) found in the docstring with the overload signatures. Classes
already behave correctly, so this only patches the function/method path. There
is no event hook for this in autodoc's new (Sphinx 9) pipeline, so
``_format_signatures`` is wrapped: when a docstring signature is present,
``autodoc_typehints`` is set to ``'none'`` for that single call, which
disables only the overload substitution branch.
"""

from sphinx.application import Sphinx
from sphinx.ext.autodoc._dynamic import _loader, _signatures
from sphinx.ext.autodoc._shared import _AutodocConfig

_orig_format_signatures = _signatures._format_signatures


def _format_signatures(**kwargs):
    config: _AutodocConfig = kwargs["config"]
    docstrings = kwargs.get("docstrings")
    options = kwargs["options"]
    props = kwargs["props"]

    if (
        kwargs.get("args") is None
        and docstrings
        and config.autodoc_docstring_signature
        and config.autodoc_typehints != "none"
        and props.obj_type in {"function", "method", "decorator"}
    ):
        # Probe on a copy: extraction strips signature lines from docstrings.
        docstring_signatures = _signatures._extract_signatures_from_docstrings(
            [list(lines) for lines in docstrings],
            props=props,
            tab_width=options._tab_width,
        )
        if docstring_signatures:
            values = {name: getattr(config, name) for name in _AutodocConfig.__slots__}
            values["autodoc_typehints"] = "none"
            kwargs["config"] = _AutodocConfig(**values)

    return _orig_format_signatures(**kwargs)


def setup(app: Sphinx):
    _signatures._format_signatures = _format_signatures
    _loader._format_signatures = _format_signatures

    return {"parallel_read_safe": True}
