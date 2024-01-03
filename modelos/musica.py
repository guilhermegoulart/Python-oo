class Musica:
    musicas = []
  
    def __init__(self, nome='', artista='', duracao=0): 
      self.nome = ''
      self.artista = ''
      self.duracao = int
      Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
      
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')
            
musica_favorita = Musica(nome='Broken Vessels', artista='Hillsong United', duracao=5)
