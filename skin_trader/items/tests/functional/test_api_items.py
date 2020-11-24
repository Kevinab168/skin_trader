from skin_trader.items.models import Item


def test_create_item(db, api_client, item_factory):
    item = item_factory.create()
    retrieved_item = Item.objects.first()
    response = api_client.get(f'http://localhost8000/api/items/{item.id}/')
    assert response.status_code == 200
    data = response.json()
    assert data.get('name') == retrieved_item.name
    assert data.get('label') == retrieved_item.label
    assert data.get('description') == retrieved_item.description
    assert data.get('price') == retrieved_item.price
    assert data.get('game') == retrieved_item.game
    assert data.get('id_number') == retrieved_item.id_number
