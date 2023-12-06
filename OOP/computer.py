class Computer:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Бренд компьютера: {self.brand}")
        print(f"Модель компьютера: {self.model}")


comp_1 = Computer("HP", "Pavilion Gaming GT 5")
comp_1.display_info()
