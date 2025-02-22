#alias(takma ad) takma ad  verme işlemi o dosyaya özeldir başka bir dosyada başka bir ad verilebilir ve burada verilen takma ad diğer dosyada tanınmaz aynı vermedikçe.

from matematik import topla as toplamaIslemi #sadece toplama işlemini aldırdık
from day2 import sayHello
from video3 import Human
# import matematik as m  => burada artık bu iki dosyayı bağladık.matematikteki alanları çağırabiliriz.
#built-in modules
import random
#package

print (toplamaIslemi(10,20))

print(random.randint(0,100))

human1 = Human("Mirza")
human1.talk("Merhaba")

#chromeDriver = webdriver.Chorme() dışardan paket alma
#packages