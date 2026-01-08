#Restaurant 

class Restaurant:
    rname = 'Bhagyashree Hotel'
    menu = {
        'Cold Coffee': 50,
        'Poha': 30,
        'Dosa': 50,
        'Idli': 50,
        'Pithal Bhakri': 80,
        'Vadapav': 20,
        'Misal pav': 80,
        'Thalipith': 60,
        'NilangaRice': 10,
        }
    def __init__(self, cn, cph, nitems = 0, total = 0):
        import random
        self.cname = cn
        self.cphno = cph
        self.bill_no = random.randint(100, 999)
        self.no_items = nitems
        self.bill_amt = total
        
    @classmethod
    def disp_menu(cls):
        for i,j in cls.menu.items():
            print(f"Dish: {i} \t Price: {j}")


    @staticmethod
    def add(a, b, c):
        return a + (b * c)

    @staticmethod
    def add_items(a, b):
        return a + b
    
    def order(self, dish, qty):
        self.bill_amt = self.add(self.bill_amt, self.menu[dish], qty)
        self.no_items = self.add_items(self.no_items, qty)

    def display_bill(self):
        print(self.cname, self.cphno, self.bill_no, self.no_items, self.bill_amt)
        
    @staticmethod
    def sub(a, b, c):
        return a - (b * c)

    @staticmethod
    def remove_items(s, b):
        return s - b

    def cancel_order(self, dish, qty = 1):
        self.bill_amt = self.sub(self.bill_amt, self.menu[dish], qty)
        self.no_items = self.remove_items(self.no_items, qty)

Restaurant.disp_menu()

cust1 = Restaurant('Anjali', 9171424841)
cust2 = Restaurant('Dolly', 7499695694)
print()
cust1.display_bill()
cust1.order('Misal pav', 3)
cust1.order('Vadapav', 2)
print()
cust1.display_bill()
print()
cust2.display_bill()
cust2.order('Poha', 5)
cust2.order('Vadapav', 5)
cust2.display_bill()
print()
cust1.cancel_order('Misal pav', 1)
cust1.display_bill()

