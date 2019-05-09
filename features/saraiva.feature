Feature: Acessar site Saraiva e Pesquisar por Produto

    '''Funcionalidade de pesquisa no Site SAraiva '''

    Scenario: Entrar Site Saraiva e Pesquisar
    Given que estou na pagina inicial do Saraiva
    When pesquiso fone
    Then recebo resultado   
