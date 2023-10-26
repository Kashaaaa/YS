import data
import configuration
import requests

#Шаг 1 создать заказ
def post_new_order(body):
    return requests.post(configuration.URL + configuration.POST_ORDER,
                         json=body,
                         headers=data.headers)

#Шаг 2 - сохранить трек
order_track = post_new_order(data.order_body).json()["track"]

#Шаг 3 найти заказ по треку
def get_order_by_track(track):
    return requests.get(configuration.URL + configuration.GET_ORDER_BY_TRACK,
                        params={"t": track})
