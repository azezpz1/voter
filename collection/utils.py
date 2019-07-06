from boardgamegeek import BGGClient


def get_id_from_bggurl(bggurl: str) -> int:
    """Gets the boardgamegeek id from the provided URL

    Arguments:
        bggurl {str} -- The boardgamegeek.com URL to the boardgame

    Returns:
        int -- The boardgamegeek ID
    """

    url_element_list = bggurl.split("/")
    return int(url_element_list[4])


def get_boardgame_obj_from_bgg(bggid: str):
    """Gets a board game object from boardgamegeek.com for the boardgame of the provided ID

    Arguments:
        bggid {str} -- The boardgamegeek.com ID for the boardgame

    Returns:
        boardgamegeek.api.game -- A boardgame object with boardgame data
    """

    client = BGGClient()
    return client.game(game_id=bggid)
