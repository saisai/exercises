from django.forms import NumberInput, Select, TextInput
from django.test import TestCase

from django_filters.widgets import (
        BaseCSVWidget,
        BooleanWidget,
        CSVWidget,
        LinkWidget,
        LookupChoiceWidget,
        QueryArrayWidget,
        RangeWidget,
        SuffixedMultiWidget,
        )

def show_dir(o):
    for obj in [f for f in dir(o) if not f.startswith('_')]:
        print(obj, "=>", getattr(o, obj))

class LookupTypeWidgetTests(TestCase):
    def test_widget_requires_field(self):
        with self.assertRaises(TypeError):
            LookupChoiceWidget()

    def test_widget_render(self):
        widgets = [TextInput(), Select(choices=(("a", "a"), ("b", "b")))]
        w = LookupChoiceWidget(widgets)
        #show_dir(w)
        print(w.render("price", ""))
        print(w.render("price", None))
        self.assertHTMLEqual(
            w.render("price", ""),
            """
            <input name="price" type="text" />
            <select name="price_lookup">
                <option value="a">a</option>
                <option value="b">b</option>
            </select>""",
        )

        self.assertHTMLEqual(
            w.render("price", None),
            """
            <input name="price" type="text" />
            <select name="price_lookup">
                <option value="a">a</option>
                <option value="b">b</option>
            </select>""",
        )

        self.assertHTMLEqual(
            w.render("price", ["2", "a"]),
            """
            <input name="price" type="text" value="2" />
            <select name="price_lookup">
                <option selected="selected" value="a">a</option>
                <option value="b">b</option>
            </select>""",
        )
