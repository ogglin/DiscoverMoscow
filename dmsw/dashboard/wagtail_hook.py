"""Richtext hooks."""
import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from django.utils.html import format_html
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineStyleElementHandler
)
from wagtail.core import hooks


@hooks.register("register_rich_text_features")
def register_code_styling(features):
    """Add the <code> to the richtext editor and page."""

    # Step 1
    feature_name = "code"
    type_ = "CODE"
    tag = "code"

    # Step 2
    control = {
        "type": type_,
        "label": "</>",
        "description": "Code"
    }

    # Step 3
    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    # Step 4
    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {"style_map": {type_: {"element": tag}}}
    }

    # Step 5
    features.register_converter_rule("contentstate", feature_name, db_conversion)

    # Step 6. This is optional
    # This will register this feature with all richtext editors by default
    features.default_features.append(feature_name)


@hooks.register("register_rich_text_features")
def register_centertext_feature(features):
    """Creates centered text in our richtext editor and page."""

    # Step 1
    feature_name = "center"
    type_ = "CENTERTEXT"
    tag = "span"

    # Step 2
    control = {
        "type": type_,
        "label": "Center",
        "description": "Center Text",
        "style": {
            "display": "span",
            "text-align": "center",
        },
    }

    # Step 3
    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    # Step 4
    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {
            "style_map": {
                type_: {
                    "element": tag,
                    "props": {
                        "class": "d-block text-center"
                    }
                }
            }
        }
    }

    # Step 5
    features.register_converter_rule("contentstate", feature_name, db_conversion)

    # Step 6, This is optional.
    features.default_features.append(feature_name)


@hooks.register("register_rich_text_features")
def register_gap_feature(features):
    """Creates gap in our richtext editor and page."""

    # Step 1
    feature_name = "gap"
    type_ = "HR"
    tag = "gap"

    # Step 2
    control = {
        "type": type_,
        "label": "Gap",
        "description": "Интервал",
        "style": {
            "display": "block",
            "padding": "20px"
        },
    }

    # Step 3
    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    # Step 4
    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {
            "style_map": {
                type_: {
                    "element": tag,
                    "props": {
                        "class": "gap"
                    }
                }
            }
        }
    }

    # Step 5
    features.register_converter_rule("contentstate", feature_name, db_conversion)

    # Step 6, This is optional.
    features.default_features.append(feature_name)


@hooks.register('insert_global_admin_js')
def global_admin_js():
    return format_html(
        '<script src="/static/js/dashbord.js"></script>',
    )


@hooks.register('construct_settings_menu')
def hide_settings_menu_items(request, menu_items):
    if request.user.username == 'admin':
        menu_items[:] = [item for item in menu_items]
    else:
        menu_items[:] = [item for item in menu_items if item.name != 'languages']


@hooks.register('construct_main_menu')
def hide_main_menu_items(request, menu_items):
    # for item in menu_items:
    #     print(item, item.name)
    if request.user.username == 'admin':
        menu_items[:] = [item for item in menu_items]
    else:
        menu_items[:] = [item for item in menu_items if item.name != 'explorer' and item.name != 'reports']
