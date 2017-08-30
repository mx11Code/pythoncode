class Human:

    name = ""

    def introduce(self):
        print("My name is %s" % self.name)

    def run(self):
        pass

lc = Human()
lc.name = "luo chao"
lc.introduce()

pmx = Human()
pmx.name = "peng meng xiong"
pmx.introduce()
