from menu.models import Ingredientes, Item, ItemMedia


def create_ingrediente(ingrediente):
    instance = Ingredientes.objects.create(
        nome=ingrediente.get('nome'),
        gordura=ingrediente.get('gordura'),
        proteina=ingrediente.get('proteina'),
        carboidrato=ingrediente.get('carboidrato'),
        vegetal=ingrediente.get('vegetal'),
    )

    return instance

def update_ingrediente(data, instance):
    instance.nome = data.get('nome')
    instance.proteina = data.get('proteina')
    instance.gordura = data.get('gordura')
    instance.carboidrato = data.get('carboidrato')
    instance.vegetal = data.get('vegetal')
    instance.save()

    return instance

def create_item(item):

    media = None
    if item.get('media'):
        media = item.pop('media')

    ingredientes_data = []
    if item.get('ingredientes'):
        ingredientes = item.pop('ingredientes')

    item_instance = Item.objects.create(
        **item
    )

    ingredientes = []
    for ingrediente in ingredientes_data:
        instance = Ingredientes.objects.create(
            **ingrediente
        )
        ingredientes.append(instance)

    if media:
        instance = ItemMedia.objects.create(
            title=item.get('nome'),
            imagem=media
        )
        item_instance.media = instance

    item_instance.ingredientes.set(ingredientes)
    item_instance.save()

    return item_instance

def update_item(data, item):

    media = None
    if data.get('media'):
        media = item.pop('media')

    ingredientes_data = []
    if data.get('ingredientes'):
        ingredientes = item.pop('ingredientes')

    item.nome = data.get('nome')
    item.descricao = data.get('descricao') 
    item.preco = data.get('preco')
    item.tempo_preparacao = data.get('tempo_preparacao')
    item.porcao = data.get('porcao')
    item.alcoolico = data.get('alcoolido')

    ingredientes = []
    for ingrediente in ingredientes_data:
        ingrediente_instance = Ingredientes.objects.get(
            nome=ingrediente.nome
        )
        ingredientes.append(ingrediente_instance)
        item.ingredientes = ingredientes

    if media:
        media_instance = ItemMedia.objects.get(
            title=media.title
        )
        item.media=media_instance
    item.save()
