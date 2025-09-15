from flask_smorest import Blueprint
from flask.views import MethodView
from ..services.qa_service import find_best_answer, get_knowledge_base
from ..schemas.qa import AskRequestSchema, AskResponseSchema, KbListResponseSchema


blp = Blueprint(
    "Q&A",
    "qa",
    url_prefix="/api",
    description="Endpoints for Tech Haven customer support Q&A bot.",
)


@blp.route("/ask")
class AskQuestion(MethodView):
    """
    Handle customer questions and return the best answer.
    """

    @blp.arguments(AskRequestSchema, location="json")
    @blp.response(200, AskResponseSchema)
    def post(self, json_data):
        """
        Submit a customer question.

        Request JSON:
          - question: string (required)

        Returns 200 OK with:
          - matched: bool
          - id: string | null
          - title: string | null
          - answer: string
          - score: integer
        """
        question = json_data.get("question", "")
        result = find_best_answer(question)
        return result


@blp.route("/knowledge-base")
class KnowledgeBase(MethodView):
    """
    Expose the current static knowledge base for transparency/debugging.
    """

    @blp.response(200, KbListResponseSchema)
    def get(self):
        """
        Get the predefined knowledge base.
        Useful for frontend debugging or admin inspection.

        Returns 200 OK with:
          - items: array of KB entries
        """
        items = get_knowledge_base()
        return {"items": items}
