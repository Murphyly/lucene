from java.nio.file import Paths
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.queryparser.classic import QueryParser

class Searcher:
    def __init__(self):
        self.directory = None
        return
    
    ##
    # Create an instance of IndexSearcher
    ###
    def create(self, path):
        self.directory = DirectoryReader.open(SimpleFSDirectory(Paths.get(path)))

        return IndexSearcher(self.directory)

    ##
    # Generate parsed query
    ###
    def query(self, arguments):
        analyzer = StandardAnalyzer()
        parser = QueryParser("keywords", analyzer)
        parser.setDefaultOperator(QueryParser.Operator.OR)

        return parser.parse(arguments)