class Sources:
    """
    """

    def __init__(self, id, name, description, url):
        """
        """
        self.id = id
        self.name = name
        self.description = description
        self.url = url


class Articles:
    """
    """

    def __init__(self, title, author, description, url, url_to_image, published_at):
        """
        """
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.url_to_image = url_to_image

        self.published_at = published_at


class Headlines:
    """

    """

    def __init__(self, title, url_to_image, url):
        self.title = title
        self.url_to_image = url_to_image
        self.url = url
