# Digram de classes

classDiagram
    class Usuario {
        +int id
        +string nome
        +string email
        +string senha
        +string contato
        +string dataNascimento
        +string bio
        +date dataCadastro
        +boolean ativo
        +criarEvento()
        +pesquisarEvento()
        +favoritarEvento()
        +confirmarPresenca()
    }

    class Conexao{
        +int id
        +int emissorConvite
        +int recepitorConvite
        +int evento
        +boolean aceite
        +aceitarConvite()
    }

    class Evento {
        +int id
        +string nome
        +string descricao
        +string tipoDeEvento
        +string statusDoEvento
        +date dataInicio
        +date dataFim
        +int usuarioId
        +int localizacaoId
        +criarEvento()
        +convidarParticipante()
    }

    class Localizacao {
        +int id
        +string nome
        +string endereco
        +string cidade
        +string estado
        +string pais
        +string geolocalizacao
        +adicionarLocalizacao()
    }

    Usuario "1" -- "*" Evento : cria
    Evento "1" -- "1" Localizacao : ocorre em
