from flask import Blueprint, request, jsonify, make_response
from dotenv import load_dotenv

import os
import requests

from app import db
from app.models.item import Item
# from app.models.board import Board


# added Bluerprint and one to many relationships between models

# example_bp = Blueprint('example_bp', __name__)
boards_bp = Blueprint("boards", __name__, url_prefix="/boards")
load_dotenv()

@boards_bp.route("", methods=["GET"])
def list_all_boards():
    boards_response = [board.as_dict() for board in Item.query.all()]
    return jsonify(boards_response)


# @boards_bp.route("", methods=["POST"])
# def create_board():
#     request_body = request.get_json()

#     if invalid_board_post_request_body(request_body):
#         return make_response({"details": "Missing required data"}, 400)

#     board = Board(title=request_body["title"], owner=request_body["owner"])

#     db.session.add(board)
#     db.session.commit()

#     return make_response({"id": board.board_id}, 201)


# def invalid_board_post_request_body(request_body):
#     if ("title" not in request_body or "owner" not in request_body):
#         return True
#     return False


# @boards_bp.route("/<int:board_id>", methods=["GET"])
# def get_board_by_id(board_id):
#     board = Board.query.get_or_404(board_id)
#     return jsonify(board.as_dict_with_cards())


# @boards_bp.route("/<int:board_id>", methods=["PUT"])
# def update_board(board_id):
#     board = Board.query.get_or_404(board_id)

#     request_body = request.get_json()
#     if invalid_board_post_request_body(request_body):
#         return make_response({"details": "Missing required data"}, 400)

#     board.title = request_body["title"]
#     board.owner = request_body["owner"]

#     db.session.add(board)
#     db.session.commit()

#     return make_response(board.as_dict(), 200)


# @boards_bp.route("/<int:board_id>", methods=["DELETE"])
# def delete_board(board_id):
#     board = Board.query.get_or_404(board_id)

#     db.session.delete(board)
#     db.session.commit()
#     return make_response(
#         jsonify(
#             details=f"board \"{board.title}\" successfully deleted", id=board.board_id),
#         200)


# # Handling CARDS


# @boards_bp.route("/<int:board_id>/cards", methods=["GET"])
# def get_rentals_by_board(board_id):
#     board = Board.query.get_or_404(board_id)

#     cards = [card.as_dict() for card in board.cards]

#     return make_response(jsonify(cards), 200)


# @boards_bp.route("/<int:board_id>/cards", methods=["POST"])
# def create_card(board_id):
#     request_body = request.get_json()
#     board = Board.query.get_or_404(board_id)

#     if invalid_card_post_request_body(request_body):
#         return make_response({"details": "Missing required data"}, 400)

#     card = Card(message=request_body["message"], board_id=board_id)

#     db.session.add(card)
#     db.session.commit()

#     send_slack_card_notification(card, board)

#     return make_response({"id": card.card_id}, 201)


# def invalid_card_post_request_body(request_body):
    
#     if ("message" not in request_body):
#         return True
#     return False


# @boards_bp.route("/increase_likes/<int:card_id>", methods=["POST"])
# def increase_likes(card_id):

#     card = Card.query.get_or_404(card_id)

#     card.likes_count += 1
#     db.session.add(card)
#     db.session.commit()

#     return make_response({"id": card.card_id}, 200)


# @boards_bp.route("/decrease_likes/<int:card_id>", methods=["POST"])
# def decrease_likes(card_id):

#     card = Card.query.get_or_404(card_id)

#     card.likes_count -= 1
#     db.session.add(card)
#     db.session.commit()

#     return make_response({"id": card.card_id}, 200)


# @boards_bp.route("/delete_card/<int:card_id>", methods=["DELETE"])
# def delete_card(card_id):
#     card = Card.query.get_or_404(card_id)

#     db.session.delete(card)
#     db.session.commit()
#     return make_response(
#         jsonify(
#             details=f"card \"{card.message}\" successfully deleted", id=card.card_id),
#         200)


# def send_slack_card_notification(card, board):
#     """
#     Sends a request to a slack bot to post the
#     to the ice-ice-baby channel
#     in the configured slack workspace
#     """
#     SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
#     text = f"📝 Someone just created a new card on the *<{board.title}>* board!! Take a look at http://ice-ice-inspo-board.herokuapp.com/ \n ```{card.message}``` \n "
#     url = f"https://slack.com/api/chat.postMessage?channel=ice-ice-baby&text={text}"

#     payload = ""

#     headers = {
#         'Authorization': f'Bearer {SLACK_BOT_TOKEN}'
#     }

#     response = requests.request("POST", url, headers=headers, data=payload)
#     return response