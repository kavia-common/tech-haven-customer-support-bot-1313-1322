from marshmallow import Schema, fields


class AskRequestSchema(Schema):
    """Schema for POST /api/ask request payload."""
    question = fields.String(required=True, description="Customer's question text.")


class AskResponseSchema(Schema):
    """Schema for POST /api/ask response payload."""
    matched = fields.Boolean(required=True, description="Whether a KB match was found.")
    id = fields.String(allow_none=True, description="Knowledge base entry id when matched.")
    title = fields.String(allow_none=True, description="Knowledge base entry title when matched.")
    answer = fields.String(required=True, description="Bot's answer or fallback guidance.")
    score = fields.Integer(required=True, description="Relevance score used for the match.")


class KbItemSchema(Schema):
    """Schema for a single knowledge base item."""
    id = fields.String(required=True)
    title = fields.String(required=True)
    keywords = fields.List(fields.String(), required=True)
    answer = fields.String(required=True)


class KbListResponseSchema(Schema):
    """Schema for GET /api/knowledge-base response payload."""
    items = fields.List(fields.Nested(KbItemSchema), required=True)
