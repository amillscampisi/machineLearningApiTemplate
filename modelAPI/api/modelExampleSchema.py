from marshmallow import Schema, fields, validates_schema, ValidationError
from marshmallow.validate import Range


class RequestInputSchema(Schema):
    """
    This validation schema is based off a made up housing example.

    In this example you can supply a bedroom and bathroom count and the
    list start and end dates and get an estimation of the homes value.

    This validation schema also demonstrates custom validation functions.
    """
    bedrooms = fields.Float(required=True, validate=Range(min=0, max=10, max_inclusive=True))
    bathrooms = fields.Float(required=True)
    list_start_date = fields.Date(required=True)
    list_end_date = fields.Date(required=True)

    @validates_schema
    def validate_start_end_dates(self, data, **kwargs):
        if not data["list_end_date"] is None:
            if data["list_start_date"] >= data["list_end_date"]:
                raise ValidationError("Properties must start listing before they can end")
