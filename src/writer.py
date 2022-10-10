from java.nio.file import Paths
from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
from org.apache.lucene.store import SimpleFSDirectory

class Writer:
    def __init__(self):
        self.directory = None
        self.analyzer = None
        self.config = None
        self.writer = None
        return

    ##
    # Create an instance of IndexWriter
    ###
    def create(self, path):
        self.directory = SimpleFSDirectory(Paths.get(path))
        self.analyzer = LimitTokenCountAnalyzer(StandardAnalyzer(), 10000)
        self.config = IndexWriterConfig(self.analyzer)

        return IndexWriter(self.directory, self.config)