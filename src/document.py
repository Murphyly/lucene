from org.apache.lucene.document import Document as LuceneDocument, Field, StringField, TextField


class Document:
    def __init__(self):
        return

    ##
    # Create an instance of a new document
    ###
    def create(self, id, title, artist, lyrics):
        indexDocument = LuceneDocument()
        indexDocument.add(Field("id", str(id), StringField.TYPE_STORED))
        indexDocument.add(Field("title", str(title), TextField.TYPE_STORED))
        indexDocument.add(Field("keywords", self.__keywords(
            id, title), TextField.TYPE_NOT_STORED))
        return indexDocument

    ##
    # Generates a keywords according to document attributes
    ###
    def __keywords(self, id, title):
        keyword = str(id) + " " + str(title)
        return keyword
