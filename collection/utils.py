def get_id_from_bggurl(bggurl: str) -> int:
    """Gets the boardgamegeek id from the provided URL

    Arguments:
        bggurl {str} -- The boardgamegeek.com URL to the boardgame

    Returns:
        int -- The boardgamegeek ID
    """

    url_element_list = bggurl.split("/")
    return int(url_element_list[4])
