import os
wynik_dzialania = ' '

@given(u'Jestem zalogowany na komputerze')
def step_impl(context):
    context.os=os
    #raise NotImplementedError(u'STEP: Given Jestem zalogowany na komputerze')


@when(u'Sprawdzam liczbe procesorow')
def step_impl(context):
    com="cat /proc/cpuinfo | grep process | wc -l"
    os=context.os
    wynik=os.popen(com).read().strip()
    context.wynik_dzialania=wynik
    #raise NotImplementedError(u'STEP: When Sprawdzam liczbe procesorow')


@then(u'Ilosc procesorow rowna 2')
def step_impl(context):
    print context.wynik_dzialania
    assert context.wynik_dzialania == '2'
    #raise NotImplementedError(u'STEP: Then Ilosc procesorow rowna 2')
