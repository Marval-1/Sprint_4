from pages.scooter_main_page import LocatorScooterMainPage


class UserData:
    Ivan = ['Иван', 'Петров', 'Ленина, 90', 'Лубянка', '899977776655']
    Nina = ['Нина', 'Бронникова', 'Ленина, 54', 'Университет', '898856782324']


class Urls:
    def __init__(self):
        self.yandex_url = 'https://dzen.ru/?yredirect=true'


class SectionQuestions:
    data = [
        [LocatorScooterMainPage.question_price, LocatorScooterMainPage.dropdown_price,
         'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
        [LocatorScooterMainPage.question_several, LocatorScooterMainPage.dropdown_several,
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
         'можете просто сделать несколько заказов — один за другим.'],
        [LocatorScooterMainPage.question_rental_time, LocatorScooterMainPage.dropdown_rental_time,
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
         'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
         'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
        [LocatorScooterMainPage.question_rented_today, LocatorScooterMainPage.dropdown_rented_today,
         'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
        [LocatorScooterMainPage.question_extend_the_order, LocatorScooterMainPage.dropdown_extend_the_order,
         'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        [LocatorScooterMainPage.question_charger, LocatorScooterMainPage.dropdown_charger,
         'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — '
         'даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
        [LocatorScooterMainPage.question_cancel_the_order, LocatorScooterMainPage.dropdown_cancel_the_order,
         'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        [LocatorScooterMainPage.question_beyond_the_MKAD, LocatorScooterMainPage.dropdown_beyond_the_MKAD,
         'Да, обязательно. Всем самокатов! И Москве, и Московской области.']

    ]
