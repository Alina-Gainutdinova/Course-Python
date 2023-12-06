class Image:
    def __init__(self, resolution, title, extension) -> None:
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self):
        self.resolution = "1920x1080"


my_img1 = Image("2650x1650", "python", "png")
print(my_img1.resolution)
my_img1.resize()
print(my_img1.resolution)
