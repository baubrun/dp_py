from stripes import Stripes
from stripes_to_pal_adapter import StripesToPalAdapter


def adapter_main():
    stripes = Stripes()
    stripes.amount = 1000
    stripes._card_exp_month_day = "1231"
    stripes.card_exp_year = "21"
    stripes.card_cvv = 999
    stripes.card_number = 123456789
    stripes.customer_name = "Allain Toi"

    pal = StripesToPalAdapter(stripes)

    def check_adapter(pal):
        print(pal.total_amount)
        print(pal.cvv)
        print(pal.customer_card_number)
        print(pal.card_exp_month_date)
        print(pal.customer_card_name)

    check_adapter(pal)




if __name__ == "__main__":
    adapter_main()
