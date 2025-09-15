# PUBLIC_INTERFACE
def get_knowledge_base():
    """Return the predefined knowledge base for Tech Haven FAQs."""
    return [
        {
            "id": "store_hours",
            "title": "Store Hours",
            "keywords": [
                "hours",
                "open",
                "close",
                "closing",
                "opening",
                "time",
                "weekend",
                "weekday",
                "holiday",
                "when are you open",
                "store hours",
                "business hours"
            ],
            "answer": (
                "Tech Haven Store Hours:\n"
                "- Monday to Friday: 9:00 AM – 8:00 PM\n"
                "- Saturday: 10:00 AM – 6:00 PM\n"
                "- Sunday: 11:00 AM – 5:00 PM\n"
                "Holiday hours may vary; please check our website banner or call customer service."
            ),
        },
        {
            "id": "return_policy",
            "title": "Return Policy",
            "keywords": [
                "return",
                "refund",
                "exchange",
                "returns",
                "money back",
                "policy",
                "returning",
                "store credit",
            ],
            "answer": (
                "Tech Haven Return Policy:\n"
                "- Returns accepted within 30 days of purchase with receipt.\n"
                "- Items must be in original condition and packaging.\n"
                "- Opened software and downloadable products are not eligible for return.\n"
                "- Refunds are issued to the original method of payment.\n"
                "For online orders, start a return through your order history page."
            ),
        },
        {
            "id": "warranty",
            "title": "Product Warranties",
            "keywords": [
                "warranty",
                "warranties",
                "guarantee",
                "manufacturer",
                "coverage",
                "repair",
                "replacement",
                "defect",
                "faulty",
            ],
            "answer": (
                "Product Warranties at Tech Haven:\n"
                "- Most electronics include a 1-year limited manufacturer’s warranty.\n"
                "- Extended Protection Plans are available at checkout for select products.\n"
                "- To make a warranty claim, keep your receipt and contact the manufacturer or our support team for guidance."
            ),
        },
    ]


def _normalize(text: str) -> str:
    """Normalize text to lower case for simple keyword matching."""
    return (text or "").strip().lower()


def _score_match(question: str, kb_item: dict) -> int:
    """
    Score how well the question matches a knowledge base item.
    Simple heuristic: count keyword occurrences.
    """
    q = _normalize(question)
    score = 0
    for kw in kb_item.get("keywords", []):
        if _normalize(kw) in q:
            score += 2  # direct keyword phrase match
        else:
            # partial word token check
            tokens = _normalize(kw).split()
            if all(t in q for t in tokens):
                score += 1
    # Light boost if title words appear
    title_tokens = _normalize(kb_item.get("title", "")).split()
    if title_tokens and any(t in q for t in title_tokens):
        score += 1
    return score


# PUBLIC_INTERFACE
def find_best_answer(question: str) -> dict:
    """
    Find the best matching answer from the knowledge base.

    Returns:
        dict with fields:
        - matched: bool
        - id: knowledge id or None
        - title: title or None
        - answer: string (either matched answer or fallback)
        - score: integer score used for selection
    """
    if not question or not _normalize(question):
        return {
            "matched": False,
            "id": None,
            "title": None,
            "answer": "Please ask a question so I can help. For example: 'What are your store hours?'",
            "score": 0,
        }

    kb = get_knowledge_base()
    best = None
    best_score = -1

    for item in kb:
        score = _score_match(question, item)
        if score > best_score:
            best = item
            best_score = score

    # Threshold to consider it a match; tweakable
    threshold = 2
    if best and best_score >= threshold:
        return {
            "matched": True,
            "id": best["id"],
            "title": best["title"],
            "answer": best["answer"],
            "score": best_score,
        }

    # Fallback generic answer
    return {
        "matched": False,
        "id": None,
        "title": None,
        "answer": (
            "I’m not sure about that. I can help with our store hours, return policy, or product warranties. "
            "Try asking: 'What are your store hours?' or 'What is your return policy?'"
        ),
        "score": best_score if best_score > 0 else 0,
    }
