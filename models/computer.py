class Computer:
    def __init__(
        self,
        name,
        brand,
        price,
        color,
        memory,
        storage,
        processor,
        category,
        description,
        image_url,
        stock,
    ):
        self.name = name
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory
        self.storage = storage
        self.processor = processor
        self.category = category
        self.description = description
        self.image_url = image_url
        self.stock = stock

    def __str__(self):
        return f"Computer: {self.name}, {self.brand}, {self.price}, {self.color}, {self.memory}, {self.storage}, {self.processor}, {self.category}, {self.description}, {self.image_url}, {self.stock}"

    def toDBCollection(self):
        return {
            "name": self.name,
            "brand": self.brand,
            "price": self.price,
            "color": self.color,
            "memory": self.memory,
            "storage": self.storage,
            "processor": self.processor,
            "category": self.category,
            "description": self.description,
            "image_url": self.image_url,
            "stock": self.stock,
        }