from org.apache.lucene.store import SimpleFSDirectory
import lucene
import document
import searcher
import writer
import time
import os

INDEXES_DIRECTORY = 'indexes'


class Main:
    def __init__(self):
        lucene.initVM()
        os.system('reset')

    def run(self):
        print("|================================================|")
        print("| Selecione uma ação: ")
        print("|-------------------------------------------------|")
        print("| ➕ (i) Insira um novo registro no Lucene")
        print("| ➕ (a) Insira o autor do título")
        print("| 🔍 (s) Busque por um termo nos registros do Lucene")
        print("| 🚪 (e) Sair do programa")
        print("|=================================================|")
        while(True):
            command = input("| O que você quer fazer? ")

            if (command == 'i'):
                print("|-------------------------------------------------|")
                title = input("| ➕ Adicionar um Titulo: ")
                self.__index(title)
                print("|-------------------------------------------------|")
                print("|  ✅ Registro adiocionado com sucesso!")
                print("|-------------------------------------------------|")
            if (command == 'a'):
                print("|-------------------------------------------------|")
                artist= input("| ➕ Adicionar autor do título: ")
                self.__index(artist)
                print("|-------------------------------------------------|")
                print("|  ✅ Registro adiocionado com sucesso!")
                print("|-------------------------------------------------|")
            if (command == 's'):
                print("|-------------------------------------------------|")
                query = input("| 🔍 Quais termos, você quer buscar: ")
                self.__search(query)
            elif (command == 'e'):
                print("| 🚪 Ok. Até logo!")
                break
        return

    def __index(self, title):
        indexWriter = writer.Writer().create(INDEXES_DIRECTORY)
        indexWriter.addDocument(
            document.Document().create(int(time.time()), title, artist)
        )
        indexWriter.commit()
        indexWriter.close()
        return

    def __search(self, query):
        indexSearcher = searcher.Searcher().create(INDEXES_DIRECTORY)
        indexQuery = searcher.Searcher().query(query)
        indexDocuments = indexSearcher.search(indexQuery, 50).scoreDocs

        if (len(indexDocuments) == 0):
            print("| ❌ Não há registros com esses termos: '" + query + "'.")
            return

        print("|=================================================|")
        print("| ✅ Sua busca retornou ", str(
            len(indexDocuments)), "resultados")
        print("|=================================================|")
        for i, indexDocument in enumerate(indexDocuments):
            fields = indexSearcher.doc(indexDocument.doc).getFields()

            print("[" + str(i + 1) + "]",
                  "[Ranking: " + str(indexDocument.score) + "]")
            for field in fields:
                if (field.name() != 'id'):
                    print("|", field.name() + ":\t", field.stringValue())
                else:
                    print("|", field.name() + ":\t\t", field.stringValue())

            print("|-------------------------------------------------|")
        return


main = Main()
main.run()
