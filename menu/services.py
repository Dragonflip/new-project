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

def create_or_update_ingredientes(ingredientes_data):

    ingredientes = []
    for ingrediente_data in ingredientes_data:
        ingrediente_instance = Ingredientes.objects.filter(
            nome=ingrediente_data.get('nome')
        ).first()

        if ingrediente_instance:
            ingrediente_instance = update_ingrediente(ingrediente_data, ingrediente_instance)
            ingredientes.append(ingrediente_instance)
        else:
            ingrediente_instance = create_ingrediente(ingrediente_data)
            ingredientes.append(ingrediente_instance)

    return ingredientes

def create_media(media):
    instance = ItemMedia.objects.create(
        title=media.get('title'),
        imagem=media.get('imagem')
    )
    return instance

def update_media(data, instance):
    instance.title = data.get('title')
    instance.imagem = data.get('imagem')
    instance.save()

    return instance

def create_or_update_media(media_data):
    media_instance = ItemMedia.objects.filter(
        title=media_data.get('title')
    ).first()

    if media_instance:
        media_instance = update_media(media_data, media_instance)
    else:
        media_instance = create_media(media_data)

    return media_instance

def create_item(item):

    media_instance = None
    if item.get('media'):
        media_data = item.pop('media')
        media_instance = create_or_update_media(media_data)

    ingredientes = None
    if item.get('ingredientes'):
        ingredientes_data = item.pop('ingredientes')
        ingredientes = create_or_update_ingredientes(ingredientes_data)

    item_instance = Item.objects.create(
        **item
    )

    if ingredientes:
        item_instance.ingredientes.set(ingredientes)
    
    if media_instance:
        item_instance.media = media_instance

    item_instance.save()

    return item_instance

def update_item(data, item):

    if data.get('media'):
        media_data = data.pop('media')
        media_instance = create_or_update_media(media_data)
        item.media = media_instance

    if data.get('ingredientes'):
        ingredientes_data = data.pop('ingredientes')
        ingredientes = create_or_update_ingredientes(ingredientes_data)
        item.ingredientes.set(ingredientes)

    item.nome = data.get('nome') or item.nome
    item.descricao = data.get('descricao') or item.descricao
    item.preco = data.get('preco') or item.preco
    item.tempo_preparacao = data.get('tempo_preparacao') or item.tempo_preparacao
    item.porcao = data.get('porcao') or item.porcao
    item.alcoolico = data.get('alcoolico') or item.alcoolico

    item.save()

    return item
