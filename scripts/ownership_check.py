

baskets = {
    6: {"owner_id": 25},
    7: {"owner_id": 26},
}


def get_basket(authenticated_user_id, basket_id):
    if authenticated_user_id is None:
        return 401, "Login required"

    basket = baskets.get(basket_id)
    if basket is None:
        return 404, "Basket not found"

    if basket["owner_id"] != authenticated_user_id:
        return 403, "Access denied"

    return 200, basket


# User identity must come from a verified server-side session.
for label, user_id, basket_id in [
    ("Own basket", 26, 7),
    ("Another user's basket", 26, 6),
    ("Not logged in", None, 7),
    ("Missing basket", 26, 99),
]:
    status, result = get_basket(user_id, basket_id)
    print(f"{label}: {status} - {result}")
