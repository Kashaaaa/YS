import sender_stand_request
#Шашков Кирилл 9 когорта финальный проект
#Шаг 4 проверяем, что код ответа = 200 (осталось впечатление, что можно обойтись без деф_позитив_ассёрта, но подумал, что это начало для будущих автотестов, может быть будет верным оставить его.)
def possitive_assert(track):
    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200;

def test_get_order_by_track():
    possitive_assert(sender_stand_request.order_track)