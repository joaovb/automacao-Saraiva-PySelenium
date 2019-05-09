@given(u'que estou na pagina inicial do Saraiva')
def step_impl(context):
    context.page.abrir_sitesaraiva()


@when(u'pesquiso fone')
def step_impl(context):
    context.page.realiza_pesquisa()


@then(u'recebo resultado')
def step_impl(context):
    context.page.exibe_resultado()