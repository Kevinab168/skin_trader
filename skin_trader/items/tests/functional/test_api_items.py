from skin_trader.items.models import Item


def test_get_item(db, api_client, item_factory):
    item = item_factory.create()
    response = api_client.get(f'http://localhost:8000/api/items/{item.id}/')
    assert response.status_code == 200
    assert Item.objects.filter(name=item.name).exists()


def test_create_item(db, api_client, item_factory):
    name = 'TEST-NAME'
    label = 'TEST-LABEL'
    description = 'TEST-DESCR'
    game = 'TEST-GAME'
    id_number = '123'
    price = '1'
    response = api_client.post(
        'http://localhost:8000/api/items/',
        {
            'name': name,
            'label': label,
            'description': description,
            'game': game,
            'id_number': id_number,
            'price': price,
        },
        format='json',
    )
    assert response.status_code == 201
    retrieved_item = Item.objects.filter(name=name)[0]
    assert retrieved_item.label == label
    assert retrieved_item.description == description


def test_update_item(db, api_client, item_factory):
    item = item_factory.create()
    updated_name = 'TEST'
    updated_label = 'TEST'
    response = api_client.put(
        f'http://localhost:8000/api/items/{item.id}/',
        {
            'name': updated_name,
            'label': updated_label,
            'description': item.description,
            'price': item.price,
            'game': item.game,
            'id_number': item.id_number,
        },
        format='json',
    )
    assert response.status_code == 200
    assert Item.objects.filter(name=updated_name).exists()


def test_delete_item(db, api_client, item_factory):
    item = item_factory.create()
    response = api_client.delete(f'http://localhost:8000/api/items/{item.id}/')
    assert response.status_code == 204
    assert not Item.objects.first()
