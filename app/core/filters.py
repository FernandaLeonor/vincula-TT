from django_filters import filters, filterset


class BaseFilterSet(filterset.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Applying a common class to various filter types
        for field_name, field in self.filters.items():
            widget_class = field.field.widget
            existing_classes = widget_class.attrs.get("class", "")
            additional_classes = "input-field col s12"
            if additional_classes not in existing_classes:
                widget_class.attrs[
                    "class"
                ] = f"{existing_classes} {additional_classes}".strip()