
class Slide:

    def __init__(self, image1, image2=None):
        if (image2==None and not image1.horizontal):
            raise Exception("You must provide 2 vertical images or 1 horizontal image")
        self.image1 = image1
        self.image2 = image2
        self.horizontal = image1.horizontal

    def get_tags(self):
        tags = self.image1._tags
        if not self.horizontal:
            tags = tags | self.image2._tags
        return tags

    def get_interest(self, other):
        common = self.get_tags() & other.get_tags()
        self_only  = self.get_tags()  ^ other.get_tags()
        other_only = other.get_tags() ^ self.get_tags()

        return min(len(common), len(self_only), len(other_only))









class Image:
    def __init__(self, img_id, horizontal, img_tags):
        self._tags = img_tags
        self._id = img_id
        self.horizontal = horizontal
